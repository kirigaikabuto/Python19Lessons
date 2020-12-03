import json
import requests


url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url)
comments = response.json()

print(comments)


