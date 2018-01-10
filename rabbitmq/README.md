## Install RabbitMQ on Linux

Install RabbitMQ on Linux

Actions:
- Install RabbitMQ on Linux with watchdog


### Compatibility version: 2.3.0

Mandatory for RabbitMQ

- rabbitmq_admin_user: "RabbitMQ web admin username"
- rabbitmq_admin_password: "RabbitMQ web admin password"
- rabbitmq_enable_watchdog: True/False

Optional:

- rabbitmq_watermark: "Value set for high watermark (default is 0.4)"
- rabbitmq_email: "email for watchdog notifications"

### Example playbook


Define the following variables under playbookname/group_vars/all
```
# RabbitMQ
rabbitmq_watermark: 0.7
rabbitmq_admin_user: admin
rabbitmq_admin_password: ****
rabbitmq_enable_watchdog: True
rabbitmq_email: user@domain
```

Use the role under playbookname/site.yaml
```
- hosts: linux
  remote_user: root
  roles:
    - { role: rabbitmq }
```
