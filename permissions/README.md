## Permissions role
Setting permissions to a file or directory

### Actions:
- Setting owner and group if 'permissions_user' variable is defined
- Setting mode if 'permissions_mode' variable is defined

### Compatibility version: 2.3

### Variables:
Mandatory
- permissions_path (absolute path to a file or directory)

Optional
- permissions_user (file/directory owner)
- permissions_group (file/directory gorup, it is required by permissions_user)
- permissions_mode (mode the file or directory should be. Modes are actually octal numbers like 0644. Leaving off the leading zero will likely have unexpected results. The mode may be specified as a symbolic mode for example u+rwx or u=rw,g=r,o=r)

