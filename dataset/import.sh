#!/bin/bash
# To be executed as sudo

# Before executing this scipt, make sure to set variables:
# - $VIRTUOSO_PWD: Virtuoso password for user dba
# - $VIRTUOSO_CONTAINER: name of the Docker container running Virtuoso

if [ -f "env.sh" ]; then
   . ./env.sh
fi

docker exec virtuoso \
	isql -H localhost -U dba -P pass \
        exec="LOAD /dataset_wheatgenomicsslkg/import.isql"
