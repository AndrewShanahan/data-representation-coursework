# Write a program in python that will read a file from a repository,
# The program should then replace all the instances of the text "Andrew" with your name
# The program should then commit those changes and push the file back to the repository.
# Marks: Marks will be given for the functionality and 
# layout of the code; I do expect minimal comments to indicate you know what the program is doing.

# Required imports
from github import Github
from config import tempgit as tmpg
import requests

gh = Github(tmpg["githubtmpg"]) # naming my key as "githubtmpg"
search_text = "Never"
replace_text= "Andrew"

# repo I want to clone:
repo = gh.get_repo("https://github.com/AndrewShanahan/data-representation-coursework/tree/main")

# using repo varriable, getting test text file
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

response = requests.get(urlOfFile)
contentOfFile = response.text

# replace function 
new_contents = contentOfFile.replace(search_text,replace_text)

# Update file and push to repository
gitHubResponse=repo.update_file(fileInfo.path,"New",
new_contents,fileInfo.sha)


# References:
# [01] Medium (2023) Import and Export Files to and from GitHub via API. Available at: https://medium.com/plumbersofdatascience/import-and-export-files-to-and-from-github-via-api-626efd7dd859. Accessed 25/11/2023
# [02] python forum IO (2020) Read content of GitHub file. Available at: https://python-forum.io/thread-26072.html (Accessed 25/11/2023)