# Ansible-Core
This repo is carrying roles and customized modules for all ansible playbooks

## Synopsis
Ansible acts as a main provisioning engine and orchestrator within SPIN and SSLN. It is based on the roles layout to bring flexibility and simplicity. Roles can be called from playbooks and they support customised variables as arguments.

## Layout
All files are grouped into directories and they can refer to each other either relatively or absolutely.

* /ansible
  * playbooks
    - \<playbook\>
      - hosts
      - site.yaml
      - group_vars\all
      - \<other files\>
  * roles
    - \<role\>
      - tasks
        - main.yaml
        - \<other files\>
      - vars
        - \<other files\>
      - handlers
        - \<other files \>
      - files
        - \<other files \>
      - templates
        - \<other files \>
      - meta
        - \<other files \>
      - defaults
        - \<other files \>

## Roles
All roles are built in the same way. Please stick to that. Each role must include the correct header. All variables must be named as <b>\<role name\>\_\<variable name\></b>.

Header pattern
```
---

# Role name
# Description
#
# Actions:
# - <action> (<action description if needed>)
#
# Compatibility version: <ansible version>
#
# Variables:
# Mandatory
# - <variable> (<variable description>)
#
# Dependant
# - <variable> (<variable description>)
#
# Optional
# - <variable> (<variable description>)
#
# Modules:
# - <module> (<module description>)
```

## Playbooks
Each playbook must include <b>hosts</b> inventory file and <b>main.yaml</b> or <b>site.yaml</b> file. All variables within inventory and playbook files must be named as <b>\<playbook name\>\_\<variable name\></b>. A playbook may consist several files.

Playbook pattern
```
- hosts: <host group>
- roles:
   - { role: <role name>, <role variable>: <value> }
```

