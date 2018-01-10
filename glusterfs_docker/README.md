## Install Gluster

Install Glusterfs in a cluster of 3+ nodes.

### Variables

Mandatory:
- glusterfs_cluster_name: Gluster cluster name
- glusterfs_docker_brick_volume: Block volume or logical volume used as brick in gluster
- glusterfs_docker_brick_volume_mount: Mount point of gluster brick
- glusterfs_docker_swarm_volume_mount: Mount point for swarm volumes
- glusterfs_docker_gluster_replica: Name of the gluster replica

Optional:
- glusterfs_install: Gluster version to install (by default takes the os default gluster version)

### Compatibility version: 2.3.0

### Example Playbook

1) Define the host group in "playbookname/hosts" (the group name MUST have the same name of the glusterfs_cluster_name)
```
[rms-docker]
ip_address_docker1
ip_address_docker2
ip_address_docker3
```

2) Use the role under playbookname/site.yaml
```
# Install and configure Glusterfs
- hosts: rms-docker
  remote_user: root
  vars:
    glusterfs_install: 312
    glusterfs_docker_brick_volume: /dev/mapper/centos-glusterfs
    glusterfs_docker_brick_volume_mount: /gluster/data
    glusterfs_docker_swarm_volume_mount: /swarm/volumes
    glusterfs_docker_gluster_replica: swarm-vols
  roles:
    - { role: glusterfs_docker, glusterfs_cluster_name: rms-docker  }
```
