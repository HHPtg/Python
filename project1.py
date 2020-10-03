item=input("please input the item being purchased: ")
price=input("please input the price of item being purchased: ")
print("would you like to add another item? yes/no ")
print("maximum two items")
while True:
    choice = input("")

    if choice in ('yes'):
      item2=input("please input the item being purchased: ")
      price2=input("please input the price of item being purchased: ")
      tt = (int(price) + int(price2))
    if choice in ('no'):
      print("your reciept:   " + item + "       " + price + "         " + item2 + "          " + price2 + "                total")
      print(tt)
      input("")
      input("")
