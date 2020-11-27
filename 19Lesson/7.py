# https://jsonplaceholder.typicode.com
# pip install requests
import requests
import json
from dictSupport import *

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()
for i in users:
    print(i["id"], i["name"])
