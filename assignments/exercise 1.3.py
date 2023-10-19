# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO,
# and stores it into a file called "cso.json".

# Import libraries/packages 
import requests
import json

url =

# Data from the url returns a json response:
def read_data():
    response = requests.get(url)
    return (response.json())