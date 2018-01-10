## Install Splunkforwarder on Windows

Install Splunkforwarder on Windows

Actions:
- Install Splunkforwarder on Windows and add monitor files


### Compatibility version: 2.3.0

### Variables

Mandatory for ansible integration

- ansible_user: "Windows Administrator user"
- ansible_password: "Windows Administrator password"
- ansible_port: 5986
- ansible_connection: winrm
- ansible_winrm_server_cert_validation: ignore


Optional for Splunkforwarder
- splunkforwarder_windows_inputs_monitor: is the list of path/index to use in the forwarder


### Example Playbook

Define the following variables under playbookname/group_vars/windows
```
# Windows ansible credentials
ansible_user: Administrator
ansible_password: "Windows Admin password"
ansible_port: 5986
ansible_connection: winrm
ansible_winrm_server_cert_validation: ignore
```


Install splunk forwarder

```
- hosts: windows
  roles:
    - { role: splunkforwarder_windows }

```
Install splunk forwarder and add monitors
```
- hosts: windows
  vars:
    splunkforwarder_windows_inputs_monitor:
      - path: C:\logs.txt
        index: platform_dev
      - path: C:\logs2.txt 
        index: platform_dev
  roles:
    - { role: splunkforwarder_windows }
```
