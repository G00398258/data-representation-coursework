# for files
from xml.dom.minidom import parse

filename = "exercise1.1.xml"
doc = parse(filename)

print (doc.toprettyxml(), end="")