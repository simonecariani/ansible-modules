## Lvg role
Creating and/or extend a volume group .

### Actions:
- create/exented a VG using the provided PV devices

### Compatibility version: 2.2.1

### Variables:
Mandatory
- lvg_vg (volume group name)
- lvg_pv (PV devices used in this VG "comma separated")

### Example
```
roles:
  - { role: lvg, lvg_vg: centos, lvg_pv: "/dev/vda3,/dev/vdb" }
```
