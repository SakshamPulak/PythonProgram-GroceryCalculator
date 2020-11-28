GroceryList = {"Mango Juice" : 20, "Bread" : 35, "Milk" : 30, "Cheese" : 55, "Shampoo" : 120}
GroceryAmount = {"Mango Juice" : 0, "Bread" : 0, "Milk" : 0, "Cheese" : 0, "Shampoo" : 0}
SerialNo=1
SubTotal=0
Total=0

for ItemName in GroceryList:
    print (SerialNo,". ",ItemName," : $",GroceryList[ItemName])
    SerialNo=SerialNo+1
    SubTotal=SubTotal + GroceryList[ItemName]
    
print ("Sub total of all items in the list = $",SubTotal)
print ("-----------------------------------------")

SerialNo=1
for ItemName in GroceryAmount:
    print ("Enter Quantity for - ",ItemName," : ",end='')
    Quantity = int (input(""))
    GroceryAmount[ItemName] = Quantity

print ("-----------------------------------------")
    
for ItemAmount in GroceryAmount and GroceryList:
    print (SerialNo,". ",ItemAmount," : ",GroceryAmount[ItemAmount]," Unit")
    SerialNo=SerialNo+1
    Total = Total +(GroceryAmount[ItemAmount] * GroceryList[ItemAmount])

print ("Total of all items in the list = $",Total)
