import json
import subprocess

output = subprocess.run(['./system_identity.sh'], capture_output=True, text=True)
systemID = json.loads(output.stdout)

# nombre de cœurs CPU : 8
# mémoire totale : 30 G
# mémoire libre : 10867 M
# taille du disque : 20G
# architecture du système : 64
# nombre de processus : 40
# nombre de logiciels installés : 1389
# adresse IP : 1.32.X.X

print(f"Distribution      : {systemID['DISTRIBUTION']}")
print(f"Version  du noyau : {systemID['KERNEL']}")
print(f"Modèle            : {systemID['MODEL']}")
print(f"Architecture      : {systemID['ARCHITECTURE']}")
print(f"Uptime            : {systemID['UPTIME']}")
print(f"Package           : {systemID['DPKG']} (dpkg) {systemID['FLATPAK']} (flatpak) {systemID['SNAP']} (snap) {systemID['PIP']} (pip)")
print(f"Shell             : {systemID['SHELL']}")
print(f"Résolution        : {systemID['RESOLUTION']}")
print(f"Environnement     : {systemID['DE']}")
print(f"CPU               : {systemID['CPU'].strip()}")
print(f"GPU               : {systemID['GPU'].strip()}")
print(f"RAM               : {systemID['RAM'].strip()}")
print(f"Ip public         : {systemID['PUBLICIP'].strip()}")
print(f"Nombre de coeurs  : {systemID['COEUR'].strip()}")
print(f"Disque total      : {systemID['DISKTOTAL'].strip()}")
