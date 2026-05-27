# rocm-smi --setfan X != pwm1 value

> **Issue #243**
> **状态**: closed
> **创建时间**: 2017-11-04T19:05:40Z
> **更新时间**: 2018-06-03T15:14:10Z
> **关闭时间**: 2018-06-03T15:14:10Z
> **作者**: rhlug
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/243

## 描述

Can someone explain to me why --setfan and pwm1 value differ.
```
# cat /sys/class/drm/card0/device/hwmon/hwmon0/pwm1
168
# rocm-smi -d 0 --setfan 170
# cat /sys/class/drm/card0/device/hwmon/hwmon0/pwm1
181
# rocm-smi -d 0 --setfan 175
# cat /sys/class/drm/card0/device/hwmon/hwmon0/pwm1
188
# rocm-smi -d 0 --setfan 180
# cat /sys/class/drm/card0/device/hwmon/hwmon0/pwm1
193
```


---

## 评论 (2 条)

### 评论 #1 — rhlug (2018-01-31T22:47:29Z)

Can someone please explain this setfan logic to me?

```
# for x in `seq 100 255` ; do  echo $x > pwm1;  P=`cat pwm1`;  D=$(expr $P - $x);  echo “Set $x Got $P diff $D” ; sleep 1; done
“Set 100 Got 142 diff 42”
“Set 101 Got 122 diff 21”
“Set 102 Got 119 diff 17”
“Set 103 Got 124 diff 21”
“Set 104 Got 124 diff 20”
“Set 105 Got 124 diff 19”
“Set 106 Got 127 diff 21”
“Set 107 Got 127 diff 20”
“Set 108 Got 127 diff 19”
“Set 109 Got 127 diff 18”
“Set 110 Got 127 diff 17”
“Set 111 Got 132 diff 21”
“Set 112 Got 132 diff 20”
“Set 113 Got 132 diff 19”
“Set 114 Got 132 diff 18”
“Set 115 Got 135 diff 20”
“Set 116 Got 137 diff 21”
“Set 117 Got 135 diff 18”
“Set 118 Got 135 diff 17”
“Set 119 Got 140 diff 21”
“Set 120 Got 140 diff 20”
“Set 121 Got 142 diff 21”
“Set 122 Got 142 diff 20”
“Set 123 Got 142 diff 19”
“Set 124 Got 145 diff 21”
“Set 125 Got 145 diff 20”
“Set 126 Got 147 diff 21”
“Set 127 Got 147 diff 20”
“Set 128 Got 147 diff 19”
“Set 129 Got 150 diff 21”
“Set 130 Got 150 diff 20”
“Set 131 Got 150 diff 19”
“Set 132 Got 150 diff 18”
“Set 133 Got 150 diff 17”
“Set 134 Got 155 diff 21”
“Set 135 Got 155 diff 20”
“Set 136 Got 155 diff 19”
“Set 137 Got 158 diff 21”
“Set 138 Got 158 diff 20”
“Set 139 Got 158 diff 19”
“Set 140 Got 158 diff 18”
“Set 141 Got 158 diff 17”
“Set 142 Got 163 diff 21”
“Set 143 Got 163 diff 20”
“Set 144 Got 163 diff 19”
“Set 145 Got 163 diff 18”
“Set 146 Got 163 diff 17”
“Set 147 Got 165 diff 18”
“Set 148 Got 165 diff 17”
“Set 149 Got 168 diff 19”
“Set 150 Got 168 diff 18”
“Set 151 Got 168 diff 17”
“Set 152 Got 170 diff 18”
“Set 153 Got 170 diff 17”
“Set 154 Got 175 diff 21”
“Set 155 Got 175 diff 20”
“Set 156 Got 175 diff 19”
“Set 157 Got 175 diff 18”
“Set 158 Got 175 diff 17”
“Set 159 Got 175 diff 16”
“Set 160 Got 178 diff 18”
“Set 161 Got 178 diff 17”
“Set 162 Got 181 diff 19”
“Set 163 Got 181 diff 18”
“Set 164 Got 181 diff 17”
“Set 165 Got 183 diff 18”
“Set 166 Got 183 diff 17”
“Set 167 Got 183 diff 16”
“Set 168 Got 183 diff 15”
“Set 169 Got 183 diff 14”
“Set 170 Got 188 diff 18”
“Set 171 Got 188 diff 17”
“Set 172 Got 188 diff 16”
“Set 173 Got 188 diff 15”
^C

```

---

### 评论 #2 — rhlug (2018-01-31T22:54:16Z)

This is polaris... why is vega so different above


```
# for x in `seq 100 255` ; do  echo $x > pwm1;  P=`cat pwm1`;  D=$(expr $P - $x);  echo “Set $x Got $P diff $D” ; sleep 1; done
“Set 100 Got 96 diff -4”
“Set 101 Got 96 diff -5”
“Set 102 Got 102 diff 0”
“Set 103 Got 102 diff -1”
“Set 104 Got 102 diff -2”
“Set 105 Got 102 diff -3”
“Set 106 Got 102 diff -4”
“Set 107 Got 102 diff -5”
“Set 108 Got 104 diff -4”
“Set 109 Got 104 diff -5”
“Set 110 Got 107 diff -3”
“Set 111 Got 107 diff -4”
“Set 112 Got 107 diff -5”
“Set 113 Got 109 diff -4”
“Set 114 Got 109 diff -5”
“Set 115 Got 112 diff -3”
“Set 116 Got 112 diff -4”
“Set 117 Got 112 diff -5”
“Set 118 Got 114 diff -4”
“Set 119 Got 114 diff -5”
“Set 120 Got 117 diff -3”
“Set 121 Got 117 diff -4”
“Set 122 Got 117 diff -5”
“Set 123 Got 119 diff -4”
“Set 124 Got 119 diff -5”
“Set 125 Got 122 diff -3”
“Set 126 Got 122 diff -4”
“Set 127 Got 122 diff -5”
“Set 128 Got 124 diff -4”
“Set 129 Got 124 diff -5”
“Set 130 Got 124 diff -6”
“Set 131 Got 127 diff -4”
“Set 132 Got 127 diff -5”
“Set 133 Got 130 diff -3”
“Set 134 Got 130 diff -4”
“Set 135 Got 130 diff -5”
“Set 136 Got 132 diff -4”
“Set 137 Got 132 diff -5”
“Set 138 Got 135 diff -3”
“Set 139 Got 135 diff -4”
“Set 140 Got 135 diff -5”
“Set 141 Got 137 diff -4”
“Set 142 Got 137 diff -5”
“Set 143 Got 140 diff -3”
“Set 144 Got 140 diff -4”
“Set 145 Got 140 diff -5”
“Set 146 Got 142 diff -4”
“Set 147 Got 142 diff -5”
“Set 148 Got 145 diff -3”
“Set 149 Got 145 diff -4”
“Set 150 Got 145 diff -5”
“Set 151 Got 147 diff -4”
^C

```

---
