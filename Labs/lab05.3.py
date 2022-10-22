from github import Github
import requests
from config_assignment04 import config as cfg

apiKey = cfg["apiKey"]
# use your own key
g = Github(apiKey)

for repo in g.get_user().get_repos():
    print(repo.name)

repo = g.get_repo("G00398258/data-representation-coursework")
print(repo.clone_url)

#https://github.com/G00398258/data-representation-coursework/tree/main/Assignments


fileInfo = repo.get_contents("test file.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print (gitHubResponse)


