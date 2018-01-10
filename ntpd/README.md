## Install Network Time Protocol "NTP"

Action:
- Install NTP daemon and configure the ntp servers.

### Variables

Mandatory:
- ntp_servers: List of ntp servers.

### Compatibility version: 2.3.0

### Example Playbook
Use the role under playbookname/site.yaml
```
- hosts: hosts
  vars:
    ntp_servers:
      - 10.10.13.123
      - 10.13.36.9
  remote_user: root
  roles:
    - { role: ntpd }
```
