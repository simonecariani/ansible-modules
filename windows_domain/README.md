## Join Windows machine to Domain 

Join the Windows machine to Domain 

Actions:
- Join Windows machine to Domain


### Compatibility version: 2.3.0

### Variables

Mandatory for ansible integration

- ansible_user: "Windows Administrator user"
- ansible_password: "Windows Administrator password"
- ansible_port: 5986
- ansible_connection: winrm
- ansible_winrm_server_cert_validation: ignore


Mandatory for joining the windows machine to the domain

- windows_domain_name: "Domain Name"
- windows_domain_admin_user: "Domain Administrator user in the form username@domain"
- windows_domain_admin_password: "Domain Administrator password"
- windows_domain_join: "Boolean True/False"


### Example playbook


Define the following variables under playbookname/group_vars/windows
```
# Windows ansible credentials
ansible_user: Administrator
ansible_password: "Windows Admin password"
ansible_port: 5986
ansible_connection: winrm
ansible_winrm_server_cert_validation: ignore

# Domain admin credentials
windows_domain_name: "domain.example"
windows_domain_admin_user: "domain_administrator@domain.example"
windows_domain_admin_password: "domain_administrator_password"
```

Use the role under playbookname/site.yaml
```
- hosts: windows
  roles:
    - { role: windows_domain, windows_domain_join: True }
```
