#!/usr/bin/env python

from ansible.module_utils.basic import * 
from string import Template
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
from ansible.module_utils.ovirt import *

#get the parameters from the ansible playbook
fields = {
  "auth": {"required": True, "type": "dict"},
  "hostname": {"required": True, "type": "str"},
  "admin_password": {"required": True, "type": "str"},
  "dns_servers": {"required": True, "type": "str"},
  "dns_search": {"required": True, "type": "str"},
  "nic_ip_address": {"required": True, "type": "str"},
  "nic_netmask": {"required": True, "type": "str"},
  "nic_gateway": {"required": True, "type": "str"},
}

module = AnsibleModule(argument_spec=fields)

#authenticate to ovirt using the auth module
connection = create_connection(module.params.pop('auth'))

# Try to find the virtual machine
vms_service = connection.system_service().vms_service()

try:
  vm = vms_service.list(search = "name=" + module.params['hostname'])[0]

#exit the module in case the vm is not found
except IndexError:
  module.fail_json(msg="VM not found")

# Find the service that manages the virtual machine:
vm_service = vms_service.vm_service(vm.id)

#check the vm status: start the machine with sysprep only if the vm is down
vm = vm_service.get()
if vm.status == types.VmStatus.UP:
  module.exit_json(changed=False, msg="VM already initialized")


#open the sysprep template file
f = open("~/ansible/roles/ovirt_windows/library/sysprep_2k12R2","r")

#get and split dns retrieved from ansible params
dns = module.params['dns_servers'].split()

#read the sysprep template
sysprep_template = Template( f.read() )

#replace sysprep template variables with vm paramenters retrieved from the playbook
d={ 'hostname':module.params['hostname'], 'admin_password':module.params['admin_password'], 'dns_server1':dns[0], 'dns_server2':dns[1], 'dns_search':module.params['dns_search'], 'nic_ip_address':module.params['nic_ip_address'], 'nic_netmask':module.params['nic_netmask'], 'nic_gateway':module.params['nic_gateway'] }

sysprep = sysprep_template.substitute(d)


# Start the virtual machine passing the sysprep
vm_service.start(
  use_sysprep = True,
    vm = types.Vm(
      initialization=types.Initialization(
        custom_script=sysprep,
    )
  )
)

module.exit_json(changed=True, msg="VM initialized with sysprep done")
connection.close(logout=False)

