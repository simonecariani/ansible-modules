## Install Cassandra Cluster

Install Cassandra cluster in a cluster of 3+ nodes.

### Variables

Mandatory:
- cassandra_cluster_name: Cassandra cluster name


Optional (if not set the default values are taken):
- cassandra_datadir: Cassandra datadir (Default is /var/lib/cassandra)


### Compatibility version: 2.3.0

### Example Playbook

1) Define the host group in "playbookname/hosts" (the group name MUST have the same name of the cassandra_cluster_name)
```
[cassandra_cluster_rms]
ip_address_cassandra1
ip_address_cassandra2
ip_address_cassandra3
```

2) Use the role under playbookname/site.yaml
```
- hosts: cassandra_cluster_rms
  remote_user: root
  roles:
    - { role: cassandra, cassandra_cluster_name: cassandra_cluster_rms }
```
