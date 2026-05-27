# repo.radeon.com/rocm/yum/rpm/: why not HTTPS or at least sign the RPMs

> **Issue #807**
> **状态**: closed
> **创建时间**: 2019-05-31T12:06:09Z
> **更新时间**: 2024-03-22T02:45:58Z
> **关闭时间**: 2024-03-22T02:45:58Z
> **作者**: drwetter
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/807

## 描述


?


---

## 评论 (4 条)

### 评论 #1 — drwetter (2019-06-04T11:43:51Z)

or at least please sign http://repo.radeon.com/rocm/yum/rpm/repodata/repomd.xml (signature in http://repo.radeon.com/rocm/yum/rpm/repodata/repomd.xml.asc) -- best with a signed/known key.


---

### 评论 #2 — drwetter (2019-08-04T17:56:44Z)

Anybody out there?

Also the RPMs are not signed. In total this seems to be a software distribution transport mechanism from the 2000 era, latest.

---

### 评论 #3 — nartmada (2024-02-09T15:06:38Z)

Hi @drwetter, apologies for the lack of response.  We have confirmed RPM files are signed.

# First, Download and Import the GPG key
wget https://repo.radeon.com/rocm/rocm.gpg.key
sudo rpm --import rocm.gpg.key
```
```
# Then, Download the RPM files
wget -r -l1 -np "https://repo.radeon.com/rocm/yum/rpm/" -A ".rpm"
```
```
# Finally, Verify the signatures
cd repo.radeon.com/rocm/yum/rpm
rpm -K *.rpm
```
```
# Sample of output
rocprofiler-2.0.60000.60000-91.el7.x86_64.rpm: digests signatures OK
rocprofiler6.0.0-2.0.60000.60000-91.el7.x86_64.rpm: digests signatures OK
rocprofiler-devel-2.0.60000.60000-91.el7.x86_64.rpm: digests signatures OK
rocprofiler-devel6.0.0-2.0.60000.60000-91.el7.x86_64.rpm: digests signatures OK
rocprofiler-docs-2.0.60000.60000-91.el7.x86_64.rpm: digests signatures OK
rocprofiler-docs6.0.0-2.0.60000.60000-91.el7.x86_64.rpm: digests signatures OK
rocprofiler-plugins-2.0.60000.60000-91.el7.x86_64.rpm: digests signatures OK
rocprofiler-plugins6.0.0-2.0.60000.60000-91.el7.x86_64.rpm: digests signatures OK
rocrand-2.10.17.60000-91.el7.x86_64.rpm: digests signatures OK
rocrand6.0.0-2.10.17.60000-91.el7.x86_64.rpm: digests signatures OK
rocrand-devel-2.10.17.60000-91.el7.x86_64.rpm: digests signatures OK
rocrand-devel6.0.0-2.10.17.60000-91.el7.x86_64.rpm: digests signatures OK
```


---

### 评论 #4 — nartmada (2024-03-22T02:45:58Z)

Closing the ticket as we have confirmed RPM files are signed.

---
