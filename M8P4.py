totalExtended = 0
orderCount = 0
infile = open("orders.txt", 'r')
nextLine = infile.readline()
while not nextLine == '':
    item = nextLine
    nextLine = infile.readline()
    quantity = int(nextLine)
    nextLine = infile.readline()
    price = float(nextLine)
    nextLine = infile.readline()
    extendedPrice = quantity * price
    totalExtended = totalExtended + extendedPrice
    orderCount = orderCount + 1
    print(item + " " + str(quantity) + " " + str(price) + " " + str(extendedPrice))
infile.close()
averageOrder = float(totalExtended) / orderCount
print("Total extended prices: $" + str(totalExtended))
print("Number of orders: " + str(orderCount))
print("Average order: $" + str(averageOrder))
