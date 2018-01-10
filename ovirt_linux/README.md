## Ovirt linux role

Deploy linux machine using cloud-init

Actions:
- Deploy linux machine using a Template
- Configure the machine using cloud init	


## Requirements (on the ansible host that executes module)

- python >= 2.7
- ovirt-engine-sdk-python >= 4.0.0


### Compatibility version: 2.3.0

### Variables:

Mandatory
- ovirt_linux_ovirt_username: "ovirt administrator"
- ovirt_linux_ovirt_password: "ovirt password"
- ovirt_linux_ovirt_url: "ovirt API url"
- ovirt_linux_root_password: "linux root password"
- ovirt_linux_dns_servers: "list of dns servers"
- ovirt_linux_dns_search: "search domain"
- ovirt_linux_nic_netmask: "netmask"
- ovirt_linux_nic_gateway: "ip address of the gateway"
- ovirt_linux_network_profile: "network profile"
- ovirt_linux_vmname: "virtual machine name"
- ovirt_linux_cluster: "Cluster name"
- ovirt_linux_template: "Template name"
- ovirt_linux_memory: "Memory in GiB"
- ovirt_linux_cpu_cores: "Cpus cores"
- ovirt_linux_nic_address: "nic ip address"
- ovirt_linux_ssh_ansible_key: "ssh key of your ansible box in order to be managed"

Optional (Create the vm with additional disk) 
- ovirt_linux_disksize: "disk size of the data disk GiB"
- ovirt_linux_datastore: "datastore to use for the data disk"


### Example Playbook

1) Define the hosts file "playbookname/hosts"
```
[ovirt_engine]
localhost ansible_connection=local ansible_user=root
```

2) Define shared variables used by all linux vms "playbookname/group_vars/all"
```
ovirt_linux_ovirt_username: admin@internal
ovirt_linux_ovirt_password: ******
ovirt_linux_ovirt_url: https://ovirt/ovirt-engine/api
ovirt_linux_root_password: ******
ovirt_linux_ssh_ansible_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDwhnjN5EwOIsSQjuf2...
```

Encrypt the vars file
```
ansible-vault encrypt "playbookname/group_vars/all"  --vault-password-file /home/ansible/.vaultpass
```

3) Define the playbook "playbookname/site.yaml"
```
- hosts: ovirt_engine
  vars:
    ovirt_linux_dns_servers: 10.10.14.91 10.13.36.12
    ovirt_linux_dns_search: domain.com
    ovirt_linux_nic_netmask: 255.255.255.0
    ovirt_linux_nic_gateway: 10.11.10.1
    ovirt_linux_network_profile: ovirtmgmt
    ovirt_linux_cluster: Default
    ovirt_linux_template: Centos7-Prod
    ovirt_linux_memory: 2GiB
    ovirt_linux_cpu_cores: 2
  roles:
    - { role: ovirt_linux, ovirt_linux_vmname: testlinux, ovirt_linux_nic_address: 10.11.10.200 }
```

4) The playbook can be run providing the password (stored in pwsafe)
```
ansible-playbook -i hosts site.yaml --vault-password-file /home/ansible/.vaultpass
```
