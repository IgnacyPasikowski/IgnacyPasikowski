## This script requires "requests": http://docs.python-requests.org/
## To install: pip install requests

import requests
import json

api_key = "xyz"
domain = "xyz"
password = "xyz"



r = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ticket_id, auth = (api_key, password))

for i in r:
  print(i)