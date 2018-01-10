## Install Mongodb and configure replicaset

Install Mongodb

Actions:
- Install Mongodb and configure replicaset

### Variables

Mandatory:
- mongod_admin_password: Mongodb administrator password
- mongod_key: Replica authentication key
- mongod_replicaset: Mongodb replica name


Optional (if not set the default values are taken):
- mongod_version: Version of Mongodb to install (Default is 3.4)
- mongod_port: Mongodb Port (default is 27017)
- mongod_dbpath: Mongodb database path (Default is /var/lib/mongo)


### Compatibility version: 2.3.0

### Example Playbook
Install Mongod and configure replicaset

1) Define the host group in "playbookname/hosts" (the group name MUST have the same name of the replicaset name)
```
[replicaset1]
ip_address_mongo1
ip_address_mongo2
ip_address_mongo3
```

2) Define the following variables under the encrypted file "playbookname/group_vars/all"
```
# Mongod auth
mongod_admin_password: test
mongod_key: |
  GmzJTeDVGVNXGR37V/sJebZ8sLws0aZtKgYxubcpijhkWSm4YV8tj1yszM9hFitC
  y9bvAvzsypkDX2HF7Jrs15FSffOYwFFh3Hfhl+9+kNUue6HFYoayOu/HENw7iVGu
  h4E0aDSKwdESHQDUApBpFylt0w4RVLBGL+X9JyqVXDUecaqGjtG2coS4rd1Vby/x
  s5ywG4ioc3XUqhTyIjz5aqflpHZJqETV5/lYCIE8hjJzTuu4
```

3) Use the role under playbookname/site.yaml
```
- hosts: replicaset1
  remote_user: root
  roles:
    - { role: mongod, mongod_replicaset: replicaset1 }
```
