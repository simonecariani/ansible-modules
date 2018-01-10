## Lvol role
Creating a logical volume and putting XFS on the top.

### Actions:
- creating VG if it does not exist. A 'lvol_pv' variable is a must in this case
- creating LV
- creating XFS

### Compatibility version: 2.2.1

### Variables:
Mandatory
- lvol_vg (volume group name)
- lvol_lv (logical volume name)
- lvol_size (the size of the logical volume, according to lvcreate(8) --size, by default in megabytes or optionally with one of [bBsSkKmMgGtTpPeE] units; or according to lvcreate(8) --extents as a percentage of [VG|PVS|FREE]; Float values must begin with a digit)

Optional
- lvol_pv (only if VG does not exist and it must to be created)
