from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Any

from .config import deep_merge
from .config import load_component_env_index


def normalize_profiles(entrypoint: dict[str, Any]) -> list[str]:
    profiles = entrypoint.get("env_profiles")
    if isinstance(profiles, list):
        return [str(profile) for profile in profiles]
    profile = entrypoint.get("env_profile")
    if profile:
        return [str(profile)]
    return ["test_runner"]


def resolve_entrypoint(index: dict[str, Any], component: str, test_type: str) -> dict[str, Any]:
    defaults = index.get("defaults", {})
    component_cfg = index.get("components", {}).get(component, {})
    mode_override = index.get("mode_overrides", {}).get(test_type, {}).get(component, {})

    entrypoint = deep_merge(defaults, component_cfg)
    entrypoint = deep_merge(entrypoint, mode_override)
    entrypoint["component"] = component
    entrypoint["test_type"] = test_type
    entrypoint["env_profiles"] = normalize_profiles(entrypoint)

    if entrypoint.get("entrypoint_type") == "test_runner":
        entrypoint["test_component"] = entrypoint.get("test_component") or component
    return entrypoint


def profile_chain(
    index: dict[str, Any],
    profile_name: str,
    visiting: set[str] | None = None,
) -> list[dict[str, Any]]:
    profiles = index.get("env_profiles", {})
    if visiting is None:
        visiting = set()
    if profile_name in visiting:
        raise SystemExit(f"env_profiles 存在循环继承: {profile_name}")
    profile = profiles.get(profile_name)
    if not isinstance(profile, dict):
        raise SystemExit(f"未知 env_profile: {profile_name}")

    visiting.add(profile_name)
    chain: list[dict[str, Any]] = []
    for inherited in profile.get("inherits", []):
        chain.extend(profile_chain(index, str(inherited), visiting))
    visiting.remove(profile_name)
    chain.append(profile)
    return chain


def expand_template(value: str, context: dict[str, str]) -> str:
    result = value
    for key, replacement in context.items():
        result = result.replace("{" + key + "}", replacement)
    return result


def prepend_env_value(env: dict[str, str], key: str, values: list[str]) -> None:
    existing = env.get(key, "")
    clean_values = [value for value in values if value]
    if existing:
        clean_values.append(existing)
    seen: set[str] = set()
    deduped: list[str] = []
    for value in clean_values:
        if value in seen:
            continue
        seen.add(value)
        deduped.append(value)
    env[key] = ":".join(deduped)


def default_sudo_askpass_path() -> str:
    return str(Path.home() / ".therock" / "sudo-askpass.sh")


def default_sudo_agent_socket() -> str:
    return str(Path.home() / ".therock" / "sudo-agent.sock")


def configure_sudo_askpass_env(state: dict[str, Any], env: dict[str, str]) -> None:
    """Inject askpass settings and a sudo shim without storing passwords."""
    if state["meta"].get("sudo_policy") != "askpass":
        return

    askpass = (
        state["meta"].get("sudo_askpass")
        or os.environ.get("THEROCK_SUDO_ASKPASS")
        or os.environ.get("SUDO_ASKPASS")
        or default_sudo_askpass_path()
    )
    socket_path = (
        state["meta"].get("sudo_agent_socket")
        or os.environ.get("THEROCK_SUDO_AGENT_SOCKET")
        or default_sudo_agent_socket()
    )
    real_sudo = shutil.which("sudo") or "/usr/bin/sudo"
    shim_dir = Path(state["meta"]["output_dir"]) / "sudo_askpass_bin"
    shim_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    shim_path = shim_dir / "sudo"
    shim_path.write_text(
        "#!/usr/bin/env bash\n"
        "set -euo pipefail\n"
        f"exec {real_sudo!r} -A \"$@\"\n",
        encoding="utf-8",
    )
    shim_path.chmod(0o700)

    env["SUDO_ASKPASS"] = str(Path(str(askpass)).expanduser())
    env["THEROCK_SUDO_AGENT_SOCKET"] = str(Path(str(socket_path)).expanduser())
    prepend_env_value(env, "PATH", [str(shim_dir)])


def task_context(state: dict[str, Any], task: dict[str, Any], entrypoint: dict[str, Any]) -> dict[str, str]:
    meta = state["meta"]
    return {
        "component": task["component"],
        "test_component": str(entrypoint.get("test_component") or task["component"]),
        "test_type": task["test_type"],
        "script": str(entrypoint.get("script", "")),
        "build_root": meta["build_root"],
        "rocm_dist": meta["rocm_dist"],
        "therock_bin_dir": str(Path(meta["rocm_dist"]) / "bin"),
        "amdgpu_families": meta["amdgpu_families"],
        "amdgpu_targets": meta.get("amdgpu_targets", meta["amdgpu_families"]),
    }


def build_task_env(
    state: dict[str, Any],
    task: dict[str, Any],
    entrypoint: dict[str, Any],
) -> tuple[dict[str, str], dict[str, Any]]:
    index = state.get("_component_env_index") or load_component_env_index(Path(state["meta"]["component_env_index"]))
    env = os.environ.copy()
    context = task_context(state, task, entrypoint)
    profile_names = normalize_profiles(entrypoint)
    preflight_modules: list[str] = []
    requires_sudo_policy = False

    for profile_name in profile_names:
        for profile in profile_chain(index, profile_name):
            for key, value in profile.get("required", {}).items():
                env[str(key)] = expand_template(str(value), context)
            for key, values in profile.get("prepend", {}).items():
                prepend_env_value(
                    env,
                    str(key),
                    [expand_template(str(value), context) for value in values],
                )
            for module in profile.get("preflight_python_modules", []):
                if str(module) not in preflight_modules:
                    preflight_modules.append(str(module))
            if profile.get("requires_sudo_policy"):
                requires_sudo_policy = True

    configure_sudo_askpass_env(state, env)

    for required in entrypoint.get("requires", []):
        module_name = {
            "pytest-xdist": "xdist",
            "OUTPUT_ARTIFACTS_DIR": "",
        }.get(str(required), str(required))
        if module_name and module_name not in env and module_name not in preflight_modules:
            preflight_modules.append(module_name)

    metadata = {
        "entrypoint_type": entrypoint.get("entrypoint_type"),
        "script": entrypoint.get("script") or "test_runner.py",
        "test_component": entrypoint.get("test_component"),
        "env_profiles": profile_names,
        "known_issue_category": entrypoint.get("known_issue_category"),
        "retry_policy": entrypoint.get("retry_policy"),
        "gpu_hang_risk": bool(entrypoint.get("gpu_hang_risk", task.get("gpu_hang_risk", False))),
        "timeout_hint_seconds": entrypoint.get("timeout_hint_seconds"),
        "preflight_python_modules": preflight_modules,
        "requires_sudo_policy": requires_sudo_policy,
    }
    return env, metadata
