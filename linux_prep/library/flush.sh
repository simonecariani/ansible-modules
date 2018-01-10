#!/usr/bin/env bash

# Flush module
# Removing existing default connections.
#
# Required variables:
# - omit (coma separated list of connections that have to be omitted,
#         a connection using by ansible must to be specified)

# Passing ansible arguments
eval $(sed -e "s/\([a-z]*\)=\([a-zA-Z0-9\/\.\,]*\)/\1='\2'/g" $1 2>/dev/null)

# Looking at variables required by module
if [[ -z ${omit} ]]; then
	echo '{"failed": true, "msg": "Module needs omitted NICs specified"}'
	exit 1
fi

# Listing existing connections
LIST=$(nmcli -f NAME -t c)

# Transforming passed variables to a new line based list
OMITTED=$(tr , '\n' <<< "${omit}")

# Setting 'removed' flag
REMOVED=0

# Parsing connections list
while read CONNECTION; do

	# Testing if currently parsing connection matches omitted connections
	grep -q ^"${CONNECTION}"$ <<< "${OMITTED}" 2>/dev/null

	# If not, removing the connection
	if [[ $? -ne 0 ]]; then
		nmcli c del "${CONNECTION}" >/dev/null 2>&1

			# Returning failed state if any errors occur
			if [[ $? -ne 0 ]]; then
				echo '{"failed": true, "msg": "Removing connection error"}'
				exit 1
			fi

		# Switching 'removed' flag if no errors
		REMOVED=1
	fi
done <<< "${LIST}"

# Testing 'removed' flag
if [[ ${REMOVED} -eq 1 ]]; then
	echo '{"changed": true, "msg": "Connections have been flushed"}'
	exit 0
else
	echo '{"changed": false, "msg": "Nothing to flush"}'
fi

exit 0
