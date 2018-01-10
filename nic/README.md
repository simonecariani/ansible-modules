## Nic role
Creating and amending NIC which covers connection and relevant device. This refers to IPV4 only.

### Actions:
- flushing connection if 'nic_flush' variable is defined
- shutting down connection if 'nic_shutdown' variable is defined
- bringing up connection if 'nic_up' variable is defined
- creating ethernet connection if 'nic_type' variable equals 'ethernet'
- creating bond connection if 'nic_type' variable equals 'bond'
- creating bond-slave connection if 'nic_type' variable equals 'bond-slave'
- defining IP if 'nic_ip' variable is defined
- defining gateway if 'nic_gw' variable is defined
- defining DNS if 'nic_dns1' and 'nic_dns2' are defined
- defining 802-3-ethernet.mac-address if 'nic_mac' variable is defined
- restarting connection if 'nic_refresh' variable is defined

### Compatibility version: 2.3

### Variables:
Mandatory
- nic_conname (connection name)

Dependant
- nic_type (connection type)
- nic_ifname (device name if nic_type is specified)
- nic_mode (bond mode if nic_type equals 'bond')
- nic_master (master bond if nic_type equals 'bond-slave')

Optional
- nic_flush (to remove connection)
- nic_shutdown (to shutdown connection)
- nic_up (to bring up connection)
- nic_ip (to create IP, it must be CIDR notation if nic_type is specified)
- nic_gw (to add gateway if nic_type is specified)
- nic_dns1 and nic_dns2 (to add DNSes if nic_type is specified)
- nic_mac (to add MAC address)
- nic_refresh (to restart connection)
