# Write a program in python that will read a file from a repository, replace all the instances of the text 
# "Andrew" with your name, commit those changes and push the file back to the repository

# I based most of this code on Andrew's example in Lab05.3

from github import Github
import requests
from config_assignment04 import config as cfg

apiKey = cfg["apiKey"]
g = Github(apiKey)

repo = g.get_repo("G00398258/data-representation-coursework")

# text file is in a subfolder called "Assignments"
fileInfo = repo.get_contents("Assignments/textfile_assignment04.txt")

urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contents = response.text
#print (contents)

# using the replace method as per: https://www.w3schools.com/python/ref_string_replace.asp
newContents = contents.replace("Andrew", "Gillian")

#print (newContents)

gitHubResponse = repo.update_file(fileInfo.path,"Updated by assignment04-github.py",
                                    newContents,fileInfo.sha)

# printing the response to confirm everything worked properly
print (gitHubResponse)
