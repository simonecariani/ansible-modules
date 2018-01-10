## Install Splunkforwarder on Linux

Install Splunkforwarder on Linux

Actions:
- Install Splunkforwarder on Linux and add monitor files


### Compatibility version: 2.3.0

### Variables

Optional for Splunkforwarder
- splunkforwarder_linux_inputs_monitor: is the list of path/index to use in the forwarder

### Example Playbook
Install splunk forwarder

```
- hosts: linux
  remote_user: root
  roles:
    - { role: splunkforwarder_linux }

```
Install splunk forwarder and add monitors
```
- hosts: linux
  vars:
    splunkforwarder_linux_inputs_monitor:
      - path: /var/log/messages
        index: platform_dev
      - path: /var/log/secure
        index: platform_dev
  remote_user: root
  roles:
    - { role: splunkforwarder_linux }
```
