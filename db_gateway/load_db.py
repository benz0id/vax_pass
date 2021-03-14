"""import json
import os

print(os.path.abspath('my_creds.json'))
print(os.getcwd())
data = json.load(open('my_creds.json'))
print(data)
"""


import sheets_gw

gw = sheets_gw.SheetsGateway('f')

print(gw.get_first_names())
