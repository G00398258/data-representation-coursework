# for files
from xml.dom.minidom import parse

filename = "somefile.xml"
doc = parse(filename)

# or

with open(filename) as f:
    doc = parse(f)

# for content from the cloud
import requests
from xml.dom.minidom import parseString

url = "http://someurl.com"

page = requests.get(url)
doc = parseString(page.content)

# check it works
print (doc.toprettyxml(), end "")

