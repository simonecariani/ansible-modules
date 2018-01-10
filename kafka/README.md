## Install Confluent Kafka Cluster

Install Kafka cluster

### Variables

Mandatory:
- kafka_cluster_name: Confluent Kafka cluster name


Optional (if not set the default values are taken):
- zookeeper_datadir: Zookeeper datadir (Default is /var/lib/zookeeper)
- kafka_datadir: Kafka datadir (default is /var/lib/kafka)


### Compatibility version: 2.3.0

### Example Playbook
Install Confluent 2.11 Kafka and configure the cluster

1) Define the host group in "playbookname/hosts" (the group name MUST have the same name of the kafka_cluster_name)
```
[kafka_cluster_rms]
ip_address_kafka1
ip_address_kafka2
ip_address_kafka3
```

2) Use the role under playbookname/site.yaml
```
- hosts: kafka_cluster_rms
  remote_user: root
  roles:
    - { role: kafka, kafka_cluster_name: kafka_cluster_rms }
```
