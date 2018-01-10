## Deploy octopus agent

Deploy octopus tentacle agent on Windows machines 

Actions:
- Deploy octopus agent 


### Compatibility version: 2.3.0

### Variables

Mandatory for ansible integration

- ansible_user: "Windows Administrator user"
- ansible_password: "Windows Administrator password"
- ansible_port: 5986
- ansible_connection: winrm
- ansible_winrm_server_cert_validation: ignore


Mandatory for Octopus cofigurations

- octopus_tentacle_version: "Version of the Octopus tentacles agent"
- octopus_tentacle_thumbprint: "Octoupus server thumbprint" 
- octopus_tentacle_port: "Octopus agent port (defaul is 10933)"
- octopus_tentacle_apikey: "Octopus apikey"
- octopus_tentacle_server: "URL of the Octopus deploy server"
- octopus_tentacle_role: "Role"
- octopus_tentacle_environment: "Environment"


### Example playbook


Define the following variables under playbookname/group_vars/windows
```
# Windows ansible credentials
ansible_user: Administrator
ansible_password: "Windows Admin password"
ansible_port: 5986
ansible_connection: winrm
ansible_winrm_server_cert_validation: ignore

# Octopus cofigurations
octopus_tentacle_version: 3.13.1
octopus_tentacle_thumbprint: YFRGUYFDJD769326LJHIUFDTO
octopus_tentacle_port: 10933
octopus_tentacle_apikey: API-YFRGUYFDJD769326LJHIUF
octopus_tentacle_server: http://octopus-server.domain
octopus_tentacle_role: testwebserver
octopus_tentacle_environment: DEV
```

Use the role under playbookname/site.yaml
```
- hosts: windows
  roles:
    - { role: octopus_tentacle }
```
