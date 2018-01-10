## Limits role
Setting limits

### Actions:
- Setting limits

### Compatibility version: 2.3

### Variables:
Mandatory
- limits_user (a username, @groupname, wildcard, uid/gid range)
- limits_item (core, data, fsize, memlock, nofile, rss, stack, cpu, nproc, as, maxlogins, maxsyslogins, priority, locks, sigpending, msgqueue, nice, rtprio, chroot)
- limits_type (hard, soft or - for both)
- limits_value (value to set)
- limits_file (absolute path to limits file)
