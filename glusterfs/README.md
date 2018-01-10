## Glusterfs role
Creating glusterfs storage clusters, bricks and volumes. This covers replicated nodes only.

### Actions:
- installing glusterfs repo if 'glusterfs_install' variable is defined
- installing glusterfs packages if 'glusterfs_install' variable is defined
- enabling glusterfs
- including vars
- probing peer
- crteating volume
- creating uid
- creating gid
- enabling shard
- tuning for performance
- activating volume

### Compatibility version: 2.2.1

### Variables:
Mandatory
- glusterfs_first (True/False only one node can act as first)
- glusterfs_vars (a file which contains the rest of variables)

Optional
- glusterfs_install (includes glusterfs version to be installed and it is a number without dot between version and subversion, for
instance 38 which means version 3.8)

Optional vars file
- glusterfs_peers (a list of peers)
- glusterfs_volume (volume name)
- glusterfs_replica (a number of bricks to be replicated)
- glusterfs_hosts (a one line list of hosts and brick paths, for instance host1:/path/brick host2:/path/brick)
- glusterfs_uid (uid definition for access control list)
- glusterfs_gid (gid definition for access control list)
- glusterfs_shard (True/False to enable shard translator)
- glusterfs_block (block size consists a number and unit if shard translator is enabled, for instance 512MB)
- glusterfs_performance (True/False to enable performance for a hypervisors purpose)
- glusterfs_activate (True/False to activate volume)
