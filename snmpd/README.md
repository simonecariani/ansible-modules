## Install SNMPD

Action:
- Install SNMP daemon and configure it.

### Variables

Mandatory:
- snmpd_community: snmp community.

### Compatibility version: 2.3.0

### Example Playbook
Use the role under playbookname/site.yaml
```
- hosts: hosts
  vars:
    snmpd_community: public
  remote_user: root
  roles:
    - { role: snmpd }
```
