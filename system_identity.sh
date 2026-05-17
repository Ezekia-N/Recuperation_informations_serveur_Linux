#!/bin/bash

cat /etc/os-release | awk -F= 'BEGIN {print "{" ; count = 0} 
{
    if ($1 == "PRETTY_NAME")
    {
        print "\t" "\"DISTRIBUTION\"" ":" $2 "," 
    }
}'
echo -e "\t\"KERNEL\":\"$(uname -r)\","
echo -e "\t\"MODEL\":\"$(cat /sys/class/dmi/id/product_name
)\""
echo "}"