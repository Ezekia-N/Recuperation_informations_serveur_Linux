import json
import subprocess

output = subprocess.run(['./system_identity.sh'], capture_output=True, text=True)
systemID = json.loads(output.stdout)

print(systemID)