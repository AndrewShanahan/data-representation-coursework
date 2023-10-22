# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO,
# and stores it into a file called "cso.json".

# Import libraries/packages 
import requests
import json

# create a variable for the dataset web address and calling it URL
# Note that in the URL, the "FY003B is the Dataset"
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FY003B/JSON-stat/2.0/en"

# Function to retrieve and parse JSON data from the URL:
def read_data():
    # Send Get request
    response = requests.get(url)
    # Parse JSON response 
    return (response.json())