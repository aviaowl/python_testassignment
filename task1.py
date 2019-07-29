import subprocess
import json

device_name = None
with open('task1_file.txt') as file:
    device_name = file.readline()
if device_name.startswith('/dev/'):
    device_name = device_name[5:]
else:
    print(f"Error: Path must starts with /dev/, found: {device_name}")
    exit()

command = "lsblk -lbnaJo NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT".split()
answer = subprocess.check_output(command).decode("utf-8")

for device in json.loads(answer)['blockdevices']:
    if device['name'] == device_name:
        if device['type'] != 'part':
            size = str(int(device['size']) // 1024 ** 3) + 'GB'
            print('/dev/' + device['name'], device['type'], size)
        else:
            size = str(int(device['size']) // 1024 ** 3) + 'GB'
            command = f"df -hBM /dev/{device_name}".split()
            a = subprocess.check_output(command).decode("utf-8")
            available_size = a.split()[-3]

            print('/dev/' + device['name'], device['type'], size, available_size, device['fstype'],
                  device['mountpoint'])
