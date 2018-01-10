## Set up firewall rules 

Actions:
- Set up firewall rules

### Variables

Mandatory:
- firewall_linux_ports: list of all ports to open in the format port/protocol or port-range/protocol

### Compatibility version: 2.3.0

### Example Playbook

Define firewall rules 

```
- hosts: test
  remote_user: root
  roles:
    - { role: firewall_linux, firewall_linux_ports: ['443/tcp', '80/tcp'] }
```

Define firewall rules using ranges 

```
- hosts: test
  remote_user: root
  roles:
    - { role: firewall_linux, firewall_linux_ports: ['443-445/tcp', '53/udp'] }
```
