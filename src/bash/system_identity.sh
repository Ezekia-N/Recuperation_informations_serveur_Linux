#!/bin/bash

INTERFACE=$(ip route | grep default | awk '{print $5}' | head -n 1)

RX1=$(cat /proc/net/dev | grep "$INTERFACE:" | awk '{print $2}')
TX1=$(cat /proc/net/dev | grep "$INTERFACE:" | awk '{print $10}')

sleep 1

RX2=$(cat /proc/net/dev | grep "$INTERFACE:" | awk '{print $2}')
TX2=$(cat /proc/net/dev | grep "$INTERFACE:" | awk '{print $10}')

SPEED_DOWN=$(echo "scale=2; ($RX2 - $RX1) / 1024" | bc)
SPEED_UP=$(echo "scale=2; ($TX2 - $TX1) / 1024" | bc)

cat /etc/os-release | awk -F= 'BEGIN {print "{" ; count = 0} 
{
    if ($1 == "PRETTY_NAME")
    {
        print "\t" "\"DISTRIBUTION\"" ":" $2 "," 
    }
}'
echo -e "\t\"KERNEL_VERSION\":\"$(uname -r)\","
echo -e "\t\"KERNEL_NAME\":\"$(uname -s)\","
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
echo -e "\t\"RESOLUTION\":\""$(xrandr | grep '*' | awk -F" " '{print $1}')"\","

echo -e "\t\"GPU\":\""$(lspci | grep -i vga | awk -F":" '{print $3}')"\","

echo -e "\t\"BUFFERS\":\""$(cat /proc/meminfo | grep "Buffers:" | awk '{printf "%.2f GB\n", $2/1024/1024}')"\","
echo -e "\t\"CACHE\":\""$(cat /proc/meminfo | grep "^Cached:" | awk '{printf "%.2f GB\n", $2/1024/1024}')"\","
echo -e "\t\"RAM_TOTAL\":\""$(free -h | awk '/^Mem:/ {print $2}')"\","
echo -e "\t\"RAM_LIBRE\":\""$(cat /proc/meminfo | grep "MemFree:" | awk '{printf "%.2f GB\n", $2/1024/1024}')"\","
echo -e "\t\"SWAP_TOTAL\":\""$(cat /proc/meminfo | grep "SwapTotal:" | awk '{printf "%.2f GB\n", $2/1024/1024}')"\","
echo -e "\t\"SWAP_UTILISE\":\""$(cat /proc/meminfo | awk '/SwapTotal/ {total=$2} /SwapFree/ {free=$2} END {printf "%.2f GB\n", (total-free)/1024/1024}')"\","
echo -e "\t\"RAM_UTILISE\":\""$(free -h | awk '/^Mem:/ {print $3}')"\","
echo -e "\t\"BAR_NUMBER\":\""$(sudo LANG=C dmidecode -t memory | grep -E "^\s*Size:" | grep -v "No Module Installed" | wc -l)"\","
echo -e "\t\"RAM_TOTAL_M\":\""$(free -m | awk '/^Mem:/ {print $2}')"\","
echo -e "\t\"RAM_UTILISE_M\":\""$(free -m | awk '/^Mem:/ {print $3}')"\","
echo -e "\t\"RAM_SLOT_NUMBER\":\""$(sudo dmidecode -t memory | grep -E "Number Of Devices" | awk -F":" '{print $2}')"\","
echo -e "\t\"RAM_MAX_CAPACITY\":\""$(sudo dmidecode -t memory | grep -E "Maximum Capacity" | awk -F":" '{print $2}')"\","
echo -e "\t\"RAM_TYPE\":\""$(sudo dmidecode -t memory | grep -E "DDR" | awk -F":" '{print $2}')"\","
echo -e "\t\"FAB_RAM\":\""$(sudo LANG=C dmidecode -t memory | grep "Manufacturer:" | grep -v "Unknown" | head -n 1 | awk '{print $2}')"\","
echo -e "\t\"FREQ_RAM\":\""$(sudo LANG=C dmidecode -t memory | grep "Configured Memory Speed:" | grep -v "Unknown" | head -n 1 | awk '{print $4 " " $5}')"\","

echo -e "\t\"DISK_TOTAL\":\""$(df -h --total | grep total | awk '{print $2}')"\","
echo -e "\t\"DISK_UTILISE\":\""$(df -h --total | grep total | awk '{print $3}')"\","
echo -e "\t\"DISK_NAME\":\""$(lsblk -dno NAME | head -n 1)"\","
echo -e "\t\"DISK_TYPE\":\""$(lsblk -dno NAME | head -n 1 | awk '{print ($0 ~ "nvme") ? "NVMe" : "SATA"}'; cat /sys/block/$(lsblk -dno NAME | head -n 1)/queue/rotational | awk '{print ($1 == 0) ? " (SSD)" : " (HDD)"}')"\","
echo -e "\t\"DISK_SIZE\":\""$(lsblk -dno SIZE | head -n 1)"\","
echo -e "\t\"DISK_TEMPERATURE\":\""$(sudo smartctl -A /dev/$(lsblk -dno NAME | head -n 1) | grep -i temperature | awk '{print $10 " °C"}')"\","
echo -e "\t\"DISK_SERIAL\":\""$(lsblk -dno SERIAL | head -n 1)"\","
echo -e "\t\"DISK_INTERFACE\":\""$(lsblk -dno NAME | head -n 1 | awk '{print ($0 ~ "nvme") ? "NVMe" : "SATA"}')"\","
echo -e "\t\"MOUNT_POINT\":\""$(df -h / | awk 'NR==2 {print $6}')"\","
echo -e "\t\"FILE_SYSTEM\":\""$(df -hT / | awk 'NR==2 {print $2}')"\","
echo -e "\t\"PARTITION_SIZE\":\""$(df -h / | awk 'NR==2 {print $2}')"\","
echo -e "\t\"PARTITION_USAGE\":\""$(df -h / | awk 'NR==2 {print $5}')"\","


echo -e "\t\"PUBLICIP\":\""$(curl ifconfig.me)"\","
echo -e "\t\"BIOS_VERSION\":\""$(sudo dmidecode -t bios | grep -E "Version" | awk -F":" '{print $2}')"\","
echo -e "\t\"BIOS_DATE\":\""$(sudo dmidecode -t bios | grep -E "Release Date" | awk -F":" '{print $2}')"\","
echo -e "\t\"DATE_INSTA\":\""$(stat -c %w / | awk -F"." '{print $1}')"\","
echo -e "\t\"TYPE\":\""$(uname -o)"\","

echo -e "\t\"USER\":\""$(printenv USER)"\","
echo -e "\t\"HOME\":\""$(printenv HOME)"\","
echo -e "\t\"LANG\":\""$(printenv LANG)"\","
echo -e "\t\"DESKTOP_SESSION\":\""$(printenv DESKTOP_SESSION)"\","
echo -e "\t\"PWD\":\""$(printenv PWD)"\","
echo -e "\t\"SHELL\":\""$SHELL"\","
echo -e "\t\"RUNLEVEL\":\""$(sudo systemctl get-default) $(runlevel)"\","
echo -e "\t\"DE\":\""$(echo $XDG_CURRENT_DESKTOP | awk -F":" '{print $2}')"\","

echo -e "\t\"CPU\":\""$(lscpu | grep -E "Nom de modèle|Model name|Core\(s\) per socket|Thread\(s\) per core" | awk -F":" '{print $2}')"\","
echo -e "\t\"COEUR\":\""$(nproc)"\","
echo -e "\t\"FABRICANT\":\""$(LANG=C lscpu | grep "Vendor ID:" | awk '{print $3}')"\","
echo -e "\t\"MODELE\":\""$(LANG=C lscpu | grep "Model name:" | sed 's/Model name:[ \t]*//')"\","
echo -e "\t\"ARCHITECTURE_PROC\":\""$(LANG=C lscpu | grep "Architecture:" | awk '{print $2}')"\","
echo -e "\t\"SOCKET_NUMBER\":\""$(LANG=C lscpu | grep "Socket(s):" | awk '{print $2}')"\","
echo -e "\t\"COEUR_PHYSIQUE\":\""$(LANG=C lscpu | grep "Core(s) per socket:" | awk '{print $4}')"\","
echo -e "\t\"THREAD_NUMBER\":\""$(nproc)"\","
echo -e "\t\"FREQ_ACTUELLE\":\""$(LANG=C lscpu | grep "CPU MHz:" | awk '{print $3 " MHz"}')"\","
echo -e "\t\"FREQ_MAX\":\""$(LANG=C lscpu | grep "CPU max MHz:" | awk '{print $4 " MHz"}')"\","
echo -e "\t\"TEMPERATURE\":\""$(cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null | awk '{print $1/1000 " °C"}')"\","
echo -e "\t\"CL1\":\""$(LANG=C lscpu | grep "L1d cache:\|L1i cache:" | awk '{print $3}' | paste -sd+ - | bc)"\","
echo -e "\t\"CL2\":\""$(LANG=C lscpu | grep "L2 cache:" | awk '{print $3}')"\","
echo -e "\t\"CL3\":\""$(LANG=C lscpu | grep "L3 cache:" | awk '{print $3}')"\","



echo -e "\t\"NET_NAME\":\""${INTERFACE}"\","
echo -e "\t\"NET_IPV4\":\""$(ip -4 addr show dev $INTERFACE | grep inet | awk '{print $2}' | cut -d/ -f1)"\","
echo -e "\t\"NET_IPV6\":\""$(ip -6 addr show dev $INTERFACE | grep inet6 | awk '{print $2}' | cut -d/ -f1 | head -n 1)"\","
echo -e "\t\"NET_MAC\":\""$(ip link show dev $INTERFACE | grep link/ether | awk '{print $2}')"\","
echo -e "\t\"NET_MTU\":\""$(ip link show dev $INTERFACE | grep mtu | awk '{print $5}')"\","
echo -e "\t\"NET_STATE\":\""$(cat /sys/class/net/$INTERFACE/operstate | tr 'a-z' 'A-Z')"\","
echo -e "\t\"NET_GATEWAY\":\""$(ip route | grep default | awk '{print $3}' | head -n 1)"\","
echo -e "\t\"NET_DNS\":\""$(grep -i nameserver /etc/resolv.conf | head -n 1 | awk '{print $2}')"\","
echo -e "\t\"NET_IP_ASSIGN\":\""$(LANG=C nmcli device show $INTERFACE 2>/dev/null | grep -i 'IP4.DHCP' | awk '{print ($2) ? "DHCP" : "Statique"}')"\","
echo -e "\t\"NET_TX_BYTES\":\""$(cat /proc/net/dev | grep "$INTERFACE:" | awk '{print $10}')"\","
echo -e "\t\"NET_RX_BYTES\":\""$(cat /proc/net/dev | grep "$INTERFACE:" | awk '{print $2}')"\","
echo -e "\t\"NET_SPEED_DOWN\":\""${SPEED_DOWN} Ko/s"\","
echo -e "\t\"NET_SPEED_UP\":\""${SPEED_UP} Ko/s"\","

echo -e "\t\"BOARD_VENDOR\":\""$(sudo cat /sys/class/dmi/id/board_vendor)"\","
echo -e "\t\"BOARD_NAME\":\""$(sudo cat /sys/class/dmi/id/board_name)"\","
echo -e "\t\"BOARD_VERSION\":\""$(sudo cat /sys/class/dmi/id/board_version)"\","
echo -e "\t\"BIOS_VERSION\":\""$(sudo cat /sys/class/dmi/id/bios_version)"\","
echo -e "\t\"BIOS_DATE\":\""$(sudo cat /sys/class/dmi/id/bios_date)"\","
echo -e "\t\"GPU_NAME\":\""$(lspci | grep -E "VGA|3D" | head -n 1 | cut -d: -f3 | sed 's/^[ \t]*//')"\","
echo -e "\t\"GPU_VRAM\":\""$(lspci -v -s $(lspci | grep -E "VGA|3D" | head -n 1 | awk '{print $1}') | grep -i "memory" | grep "size=" | head -n 1 | awk -F'size=' '{print $2}' | cut -d] -f1)"\","
if command -v nvidia-smi &> /dev/null; then
    echo -e "\t\"GPU_TEMP\":\""$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits)" °C\","
# Si vous utilisez un GPU intégré Intel ou AMD (via les sondes standard du noyau) :
else
    echo -e "\t\"GPU_TEMP\":\""$(cat /sys/class/drm/card0/device/hwmon/hwmon*/temp1_input 2>/dev/null | head -n 1 | awk '{print $1/1000 " °C"}')"\","
fi

# Initialisation du tableau JSON pour les partitions
echo -e "\t\"PARTITIONS\": ["
first=true

df -hT | grep -E '^/dev/' | while read -r line; do
    # Extraction des colonnes de df : FS, Type, Taille, Utilise, Dispo, Pourcentage, PointMontage
    FS=$(echo "$line" | awk '{print $1}')
    TYPE=$(echo "$line" | awk '{print $2}')
    SIZE=$(echo "$line" | awk '{print $3}')
    USAGE=$(echo "$line" | awk '{print $6}')
    MOUNT=$(echo "$line" | awk '{print $7}')

    # Gestion de la virgule entre les objets JSON
    if [ "$first" = true ]; then
        first=false
    else
        echo -e ","
    fi

    echo -e "\t\t{"
    echo -e "\t\t\t\"MOUNT_POINT\": \"$MOUNT\","
    echo -e "\t\t\t\"FILE_SYSTEM\": \"$TYPE\","
    echo -e "\t\t\t\"PARTITION_SIZE\": \"$SIZE\","
    echo -e "\t\t\t\"PARTITION_USAGE\": \"$USAGE\""
    echo -e "\t\t\c"
    echo -n "}"
done
echo -e "\n\t],"


echo -e "\t\"DATE\":\""$(date)"\""
echo "}"


