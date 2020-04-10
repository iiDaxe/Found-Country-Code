import requests
import re
from termcolor import cprint
resp = requests.get("https://www.worldstandards.eu/other/tlds/")
matchObj = re.findall(r'<td>(.*)</td>', str(resp.text))
i = 0
cprint('''
  ___ ___                    _     
 | __/ __|  ___   __ ___  __| |___ 
 | _| (__  |___| / _/ _ \/ _` / -_)
 |_| \___|       \__\___/\__,_\___|
                                   
''', 'cyan')
s = input("Enter The Country : ").lower()
length = len(matchObj)

while i < length:
    if s == matchObj[i].lower():
        cprint(matchObj[i+1].split(' ')[0], 'green')
    i += 1
