## VmWare windows role

Deploy windows machine on VmWare

Actions:
- Deploy windows machine using a Template


## Requirements (on the ansible host that executes module)

- python >= 2.7
- ovirt-engine-sdk-python >= 4.0.0
- PyVmomi

### Compatibility version: 2.3.0

### Variables:

Mandatory
- vmware_windows_vcenter_hostname: "Vcenter address"
- vmware_windows_vcenter_username: "VmWare Administrator"
- vmware_windows_vcenter_password: "VmWare password"
- vmware_windows_datacenter: "Datacenter"
- vmware_windows_cluster: "Cluster"
- vmware_windows_hostname: "Vm name"
- vmware_windows_template: "Template name"
- vmware_windows_disk_size: "Disk size in GB"
- vmware_windows_datastore: "Datastore name"
- vmware_windows_memory: "Memory in MB"
- vmware_windows_vcpus: "Cpus cores"
- vmware_windows_network: "network name" (default is "VM Network")
- vmware_windows_ip: "nic ip address"
- vmware_windows_netmask: "netmask"
- vmware_windows_gateway: "gateway ip"
- vmware_windows_dns_servers: "list of dns servers"
- vmware_windows_admin_password: "Administrator password"
- vmware_windows_domain: "domain name"


Optional 
- resource_pool: "Resource Pool"
- folder: "Folder name"

### Example Playbook

1) Define the hosts file "playbookname/hosts"
```
[vmware_engine]
localhost ansible_connection=local ansible_user=root
```

2) Define shared variables used by all windows vms "playbookname/group_vars/all"
```
vmware_windows_vcenter_hostname: Vcenter-IP
vmware_windows_vcenter_username: administrator@vsphere.local
vmware_windows_vcenter_password: ****
vmware_windows_admin_password: ****
```

Encrypt the vars file
```
ansible-vault encrypt "playbookname/group_vars/all"  --vault-password-file /home/ansible/.vaultpass
```

3) Define the playbook "playbookname/site.yaml"
```
- hosts: vmware_engine
  vars:
    vmware_windows_datacenter: Datacenter
    vmware_windows_cluster: Cluster
    vmware_windows_template: win2012
    vmware_windows_disk_size: 40
    vmware_windows_datastore: nfs1
    vmware_windows_memory: 1024
    vmware_windows_vcpus: 1
    vmware_windows_network: "VM Network"
    vmware_windows_netmask: 255.255.255.224
    vmware_windows_gateway: 10.10.30.65
    vmware_windows_dns_servers:
      - 10.10.14.91
      - 10.13.36.12
    vmware_windows_domain: vsphere.local
  roles:
    - { role: vmware_windows, vmware_windows_hostname: testwindows, vmware_windows_ip: 10.10.30.71 }
```

4) The playbook can be run providing the password (stored in pwsafe)
```
ansible-playbook -i hosts site.yaml --vault-password-file /home/ansible/.vaultpass
```

