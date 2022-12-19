import requests
URL = "https://andrewbeatty1.pythonanywhere.com/books"

#response = requests.get(URL)
#print (response.json())

def readbooks():
    response = requests.get(URL)
    # we could do checking for correct response code here
    return response.json()

def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    # we could do checking for correct response code here
    return response.json()

def createbook(book):
    response = requests.post(URL, json=book)
    # should check we have the correct status code
    return response.json()

def updatebook(id, book):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()



if __name__ == "__main__":
    #print (readbooks())
    #print (readbook(93))
    
    #book = {"Author": "GKM", "Price": 1500, "Title": "Test from Gillian"}
    #print (createbook(book))
    #print (updatebook(98, book))
    print (deletebook(98))


