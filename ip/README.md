## Ip role
Adding or removing additional IP per connection

### Actions:
- Adding additional IP to a connection if 'ip_add' variable is defined
- Removing IP from a connection if 'ip_remove' variable is defined

### Compatibility version: 2.3

### Variables:
Mandatory
- ip_address (IP address in CIDR format)
- ip_connection (connection)

Optional
- ip_add (to add IP)
- ip_remove (to remove IP)
