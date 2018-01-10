## VmWare linux role

Deploy linux machine on VmWare

Actions:
- Deploy linux machine using a Template


## Requirements (on the ansible host that executes module)

- python >= 2.7
- ovirt-engine-sdk-python >= 4.0.0
- PyVmomi

### Compatibility version: 2.3.0

### Variables:

Mandatory
- vmware_linux_vcenter_hostname: "Vcenter address"
- vmware_linux_vcenter_username: "VmWare Administrator"
- vmware_linux_vcenter_password: "VmWare password"
- vmware_linux_datacenter: "Datacenter"
- vmware_linux_cluster: "Cluster"
- vmware_linux_hostname: "Vm name"
- vmware_linux_template: "Template name"
- vmware_linux_disk_size: "Disk size in GB"
- vmware_linux_datastore: "Datastore name"
- vmware_linux_memory: "Memory in MB"
- vmware_linux_vcpus: "Cpus cores"
- vmware_linux_network: "network name" (default is "VM Network")
- vmware_linux_ip: "nic ip address"
- vmware_linux_netmask: "netmask"
- vmware_linux_gateway: "gateway ip"
- vmware_linux_dns_servers: "list of dns servers"
- vmware_linux_domain: "domain name"


Optional 
- resource_pool: "Resource Pool"
- folder: "Folder name"

### Example Playbook

1) Define the hosts file "playbookname/hosts"
```
[vmware_engine]
localhost ansible_connection=local ansible_user=root
```

2) Define shared variables used by all linux vms "playbookname/group_vars/all"
```
vmware_linux_vcenter_hostname: Vcenter-IP
vmware_linux_vcenter_username: administrator@vsphere.local
vmware_linux_vcenter_password: ****
```

Encrypt the vars file
```
ansible-vault encrypt "playbookname/group_vars/all"  --vault-password-file /home/ansible/.vaultpass
```

3) Define the playbook "playbookname/site.yaml"
```
- hosts: vmware_engine
  vars:
    vmware_linux_datacenter: Datacenter
    vmware_linux_cluster: Cluster
    vmware_linux_template: centos7
    vmware_linux_disk_size: 10
    vmware_linux_datastore: nfs1
    vmware_linux_memory: 1024
    vmware_linux_vcpus: 1
    vmware_linux_network: "VM Network"
    vmware_linux_netmask: 255.255.255.224
    vmware_linux_gateway: 10.10.30.65
    vmware_linux_dns_servers:
      - 10.10.14.91
      - 10.13.36.12
    vmware_linux_domain: vsphere.local
  roles:
    - { role: vmware_linux, vmware_linux_hostname: testlinux, vmware_linux_ip: 10.10.30.71 }
```

4) The playbook can be run providing the password (stored in pwsafe)
```
ansible-playbook -i hosts site.yaml --vault-password-file /home/ansible/.vaultpass
```

