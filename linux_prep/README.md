## Prep role
Preparing OS for deployment purpose via ansible. This role must be run as a first.

### Actions:
- Installing packages required by modules
- Flushing existing default connections if 'prep_flush' variable is defined
- Installing/uninstalling  EPEL repository if 'prep_epel' variable is defined
- Installing sysadmins packages if 'prep_epel' variable is defined
- Upgrading packages if 'prep_upgrade' variable is defined
- Configuring SELinux if 'prep_selinux' variable is defined
- Enabling/disabling firewall if 'prep_firewall' variable is defined
- Installing mcelog if 'prep_mcelog' variable is defined

### Compatibility version: 2.3

### Variables:
Optional
- prep_flush (to flush existing default connections)
- prep_omit (required by prep_flush, coma separated list of connections that have to be removed, a connection using by ansible must to be specified here)
- prep_epel (to install epel repository if true or to uninstall the reposotory if false)
- prep_upgrade (to upgrade packages, '*' is available to upgrade all packages)
- prep_selinux (to configure SELinux mode)
- prep_firewall (to enable firewall if true or to disable it if false)
- prep_mcelog (to install mcelog if true)

### Modules:
- flush (to flush existing default connections)
