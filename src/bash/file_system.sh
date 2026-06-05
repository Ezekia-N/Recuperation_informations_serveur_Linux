#!/bin/bash
echo -e "{"
du -xd 1 / 2>/dev/null | awk -v total=$(df / | awk 'NR==2 {print $3}') '{printf "\t\"%s\":\"%.2f,%.2f\",\n", $2, $1/(1024),($1/total)*100}' | sort -rnk2
echo -e "\t\"\"":"\"\""
echo -e "}"