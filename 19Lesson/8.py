import json
import requests
from dictSupport import *

url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url)
comments = response.json()

saveDataToJsonFile("comments.json", comments)
