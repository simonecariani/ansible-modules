## Install role
Installing or removing packages

### Actions:
- Installing packages defined in a variable if 'install_add' and 'install_packages' variables are defined
- Installing packages defined in a file if 'install_add' and 'install_file' variables are defined
- Removing packages defined in a variable if 'install_remove' and 'install_packages' variables are defined
- Removing packages defined in a file if 'install_remove' and 'install_file' variables are defined

### Compatibility version: 2.3

### Variables:
Mandatory
- install_packages (to install packages defined in a variable, this can be coma separated list of packages or package groups)
- install_file (to install packages defined in a file, the path is relative and the current playbook directory is a root)

Dependant
- install_add (to install if True)
- install_remove (to remove if True)
