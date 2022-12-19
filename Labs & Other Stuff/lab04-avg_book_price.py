from lab04 import readbooks

books = readbooks()
prices = []

for book in books:
    prices.append (book["Price"])

# checking list
#print (prices)
avg = sum(prices) / len(prices)

print ("The average book price is", round(avg,2))