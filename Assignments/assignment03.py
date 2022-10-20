# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
# and stores it into a file called "cso.json"
# Mostly followed Andrew's example in this week's lecture for this ask

import requests
import json

# full url for Exchequer Account (Historical Series) dataset:
#https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en

urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

# connects to CSO API and retrieves the data for the given dataset
def getAll(dataset):   
    url = urlBeginning + dataset + urlEnd
    response = requests.get(url)
    return response.json()

# writes data retrieved by getAll() to a file called cso.json
def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)


# main method
if __name__ == "__main__":
    # took FIQ02 from full url
    getAllAsFile("FIQ02")