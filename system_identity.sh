#!/bin/bash

cat /etc/os-release | awk -F= 'BEGIN {print "{" ; count = 0} 
{
    if ($1 == "PRETTY_NAME")
    {
        print "\t" "\"DISTRIBUTION\"" ":" $2 "," 
    }
}'
echo -e "\t\"KERNEL\":\"$(uname -r)\","
echo -e "\t\"MODEL\":\"$(cat /sys/class/dmi/id/product_name)\","
echo -e "\t\"ARCHITECTURE\":\"$(uname -p)\","
echo -e "\t\"UPTIME\":\"$(uptime -p)\","
echo -e "\t\"DPKG\":\"$(dpkg-query -f '${binary:Package}\n' -W | wc -l)\","
echo -e "\t\"RPM\":\"$(rpm -qa | wc -l)\","
echo -e "\t\"PACMAN\":\"$(pacman -Q | wc -l)\","
echo -e "\t\"SNAP\":\"$(snap list 2>/dev/null | tail -n +2 | wc -l)\","
echo -e "\t\"FLATPAK\":\"$(flatpak list 2>/dev/null | wc -l)\","
echo -e "\t\"PIP\":\"$(pip3 list 2>/dev/null | tail -n +3 | wc -l)\","
echo -e "\t\"NODE\":\"$(npm list -g --depth=0 2>/dev/null | grep -c '└──')\","
echo -e "\t\"SHELL\":\""$SHELL"\","
echo -e "\t\"RESOLUTION\":\""$(xrandr | grep '*' | awk -F" " '{print $1}')"\","
echo -e "\t\"DE\":\""$(echo $XDG_CURRENT_DESKTOP | awk -F":" '{print $2}')"\","
echo -e "\t\"CPU\":\""$(lscpu | grep -E "Nom de modèle|Model name|Core\(s\) per socket|Thread\(s\) per core" | awk -F":" '{print $2}')"\","
echo -e "\t\"GPU\":\""$(lspci | grep -i vga | awk -F":" '{print $3}')"\","
echo -e "\t\"RAM\":\""$(free -h | awk '/^Mem:/ {print $2}')"\","
echo -e "\t\"COEUR\":\""$(nproc)"\","
echo -e "\t\"DISKTOTAL\":\""$(df -h --total | grep total | awk '{print $2}')"\","
echo -e "\t\"PUBLICIP\":\""$(curl ifconfig.me)"\""
echo "}"
