import requests
from sys import stdout
import time



def write(print):
  for i in print:
    stdout.write(i)
    stdout.flush()
    time.sleep(.087)
write("""The tool made by 2hell#7101
""")


token = input(f'Enter your token : ')
id_group = input(f'Enter id group or channel : ')
id_message = input(f'Enter id message : ')

headers = {"Authorization": token}
headers["Content-Type"] = "application/json"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

tohell = "https://discord.com/api/v9/channels/" + id_group + "/pins/" + id_message

while True:
 pin = requests.put(tohell, headers=headers)
 print ("done pin " + id_message)
 pion = requests.delete(tohell, headers=headers)
 print("done unpin " + id_message)