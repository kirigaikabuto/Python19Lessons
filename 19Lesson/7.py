# https://jsonplaceholder.typicode.com
# pip install requests
# https://python-scripts.com/json
import requests
import json
from dictSupport import *

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()

saveDataToJsonFile("usersAll.json", users)
