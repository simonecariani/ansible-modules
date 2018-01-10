## Users role
Adding or removing or managing users

### Actions:
- Adding user default group if 'users_add' variable is defined and 'users_primarygroup' variable is not defined
- Adding user primary group if 'users_add' variable is defined and 'users_primarygroup' variable is defined
- Setting UID if 'users_uid' variable is defined
- Setting password if 'users_password' variable is defined
- Creating home directory if 'users_home' is defined
- Configuring shell if 'users_shell' variable is defined
- Adding user to groups if 'users_addgroups' variable is defined
- Removing user from all secondary groups if 'users_removegroups' variable is defined
- Removing user if 'users_remove' variable is defined

### Compatibility version: 2.3

### Variables:
Mandatory
- users_name (user name)

Dependant
- users_add (to create user)
- users_uid (user uid)
- users_password (use mkpasswd or passlib)
- users_home (to create user directory)
- users_shell (user shell)
- users_primarygroup (user primary group)
- users_addgroups (coma separated list of groups)
- users_removegroups (to remove user from all secondary groups)
- users_remove (to remove user account)

### Password
To generate crypted value for users_password variable:

- mkpasswd option
  ```
  yum install expect
  mkpasswd --method=sha-512
  ```

- passlib option
  ```
  pip install passlib
  python -c "from passlib.hash import sha512_crypt; import getpass; print sha512_crypt.using(rounds=5000).hash(getpass.getpass())"
  ```
