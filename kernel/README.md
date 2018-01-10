## Kernel role
Adding or removing kernel parameters

### Actions:
- Adding kernel parameter if 'kernel_value' variable is defined
- Removing kernel parameter if 'kernel_remove'  variable is defined
- Reloading kernel parameters if 'kernel_reload' variable is defined

### Compatibility version: 2.3

### Variables:
Mandatory
- kernel_parameter (sysctl variable)

Dependant
- kernel_value (sysctl variable value)
- kernel_file (absolute path to sysctl config file)
- kernel_remove (to remove parameter)

Optional
- kernel_reload (to reload kernel parameters)
