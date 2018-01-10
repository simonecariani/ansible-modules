## Zabbix role
Deploying zabbix agent

### Actions:
- Installing zabbix repository
- Installing zabbix-agent
- Setting source IP if 'zabbix_ip' variable is defined
- Setting listen IP if 'zabbix_ip' variable is defined
- Setting server IP
- Setting server active IP
- Setting hostname
- Starting agent

### Compatibility version: 2.3

### Variables:
Optional
- zabbix_ip (source IP on which zabbix agent is listening and which is used for outgoing connections)
