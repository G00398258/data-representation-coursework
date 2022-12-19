import requests
import urllib.parse
import json
from config_github import config as cfg

url = 'https://api.github.com/repos/G00398258/aprivateone'
apiKey = cfg["apiKey"]
filename = "github_info"

response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()

# confirmed this is working, so no need to print it anymore
# print (response.json())

print (response)

with open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)

