## Prep role
Preparing OS for deployment purpose via ansible. This role must be run as a first.

### Actions:
- Installing all Critical and Security packages update

### Compatibility version: 2.3

### Example playbook


Define the following variables under playbookname/group_vars/windows
```
# Windows ansible credentials
ansible_user: Administrator
ansible_password: "Windows Admin password"
ansible_port: 5986
ansible_connection: winrm
ansible_winrm_server_cert_validation: ignore
```

Use the role under playbookname/site.yaml
```
- hosts: windows
  roles:
    - { role: windows_prep }
```

