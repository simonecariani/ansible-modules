## Ovirt windows role

Deploy windows machine using sysprep

Actions:
- Deploy windows machine using a Template
- Configure the machine using sysprep


## Requirements (on the ansible host that executes module)

- python >= 2.7
- ovirt-engine-sdk-python >= 4.0.0


### Compatibility version: 2.3.0


### Variables:

Mandatory
- ovirt_windows_ovirt_username: "ovirt administrator"
- ovirt_windows_ovirt_password: "ovirt password"
- ovirt_windows_ovirt_url: "ovirt API url"
- ovirt_windows_admin_password: "administrator password"
- ovirt_windows_dns_servers: "list of dns servers"
- ovirt_windows_dns_search: "search domain"
- ovirt_windows_nic_netmask: "netmask"
- ovirt_windows_nic_gateway: "ip address of the gateway"
- ovirt_windows_network_profile: "network profile"
- ovirt_windows_vmname: "virtual machine name"
- ovirt_windows_cluster: "Cluster name"
- ovirt_windows_template: "Template name"
- ovirt_windows_memory: "Memory in GiB"
- ovirt_windows_cpu_cores: "Cpus cores"
- ovirt_windows_nic_address: "nic ip address"


Optional (Create the vm with additional disk) 
- ovirt_windows_disksize: "disk size of the data disk in GiB"
- ovirt_windows_datastore: "datastore to use for the data disk"


### Example Playbook

1) Define the hosts file "playbookname/hosts"
```
[ovirt_engine]
localhost ansible_connection=local ansible_user=root
```

2) Define shared variables used by all windows vms "playbookname/group_vars/all"
```
ovirt_windows_ovirt_username: admin@internal
ovirt_windows_ovirt_password: ******
ovirt_windows_ovirt_url: https://ovirt/ovirt-engine/api
ovirt_windows_admin_password: ******
```

Encrypt the vars file
```
ansible-vault encrypt "playbookname/group_vars/all" --vault-password-file /home/ansible/.vaultpass
```

3) Define the playbook "playbookname/site.yaml"
```
- hosts: ovirt_engine
  vars:
    ovirt_windows_dns_servers: 10.10.14.91 10.13.36.12
    ovirt_windows_dns_search: domain.com
    ovirt_windows_nic_netmask: 24
    ovirt_windows_nic_gateway: 10.11.10.1
    ovirt_windows_network_profile: ovirtmgmt
    ovirt_windows_cluster: Default
    ovirt_windows_template: Windows2012_R2-Prod
    ovirt_windows_memory: 2GiB
    ovirt_windows_cpu_cores: 2
  roles:
    - { role: ovirt_windows, ovirt_windows_vmname: testwindows, ovirt_windows_nic_address: 10.11.10.201 }
```

4) The playbook can be run providing the password (stored in pwsafe)
```
ansible-playbook -i hosts site.yaml --vault-password-file /home/ansible/.vaultpass
```
