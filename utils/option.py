class OrderProduct:
    def __init__(self, data = []):
        self.list_item = ["RAM", "CPU", "MOBO", "CASE", "RGB FAN", "SSD", "HDD", "MONITOR", "KEYBOARD", 
                                    "MOUSE", "HEADSET", "PSU", "GPU"]
        self.list_price = [2000, 9000, 7499, 1399, 120, 950, 800, 5500, 1199, 499, 899, 2995, 19200]
        self.data = data
        self.dp1 = ["|   0601","|    RAM","     |      2000       |"]
        self.dp2 = ["|   0602","|    CPU","     |      9000       |"]
        self.dp3 = ["|   0603","|    MOBO","    |      7499       |"]
        self.dp4 = ["|   0604","|    CASE","    |      1399       |"]
        self.dp5 = ["|   0605","|    RGB FAN"," |      120        |"]
        self.dp6 = ["|   0606","|    SSD","     |      950        |"]
        self.dp7 = ["|   0607","|    HDD","     |      800        |"]
        self.dp8 = ["|   0608","|    MONITOR"," |      5500       |"]
        self.dp9 = ["|   0609","|    KEYBOARD","|      1199       |"]
        self.dp10= ["|   0610","|    MOUSE","   |      499        |"]
        self.dp11= ["|   0611","|    HEADSET"," |      899        |"]
        self.dp12= ["|   0612","|    PSU","     |      2995       |"]
        self.dp13= ["|   0613","|    GPU","     |      19200      |"]
        self.dp14= ["+--------------------------------------------------------+"]
        self.dplay = [self.dp1, self.dp2, self.dp3, self.dp4, self.dp5, self.dp6, self.dp7, 
                    self.dp8, self.dp9, self.dp10, self.dp11, self.dp12, self.dp13, self.dp14]
        
    def display_column(self):
        print("+----------------+---------------------+-----------------+")
        print("|----------------|---------------------|-----------------|")
        print("|   ProductID    |    ProductName      |      Price      |")
        print("|----------------|---------------------|-----------------|")
        print("+----------------+---------------------+-----------------+")
        for i in self.dplay: #DISPLAYING PRODUCT
            print("         ".join(i))
    
    def order_product(self, product):
        print("\n")
        print("+----------------+---------------------+-----------------+")
        print("|----------------|---------------------|-----------------|")
        print("|   ProductID    |    ProductName      |      Price      |")
        print("|----------------|---------------------|-----------------|")
        print("+----------------+---------------------+-----------------+")
        
        for i in range(0,13):
            if self.list_item[i] == product:
                print("         ".join(self.dplay[i]))
                print("\n")
                
                customer_name = str(input("Enter Customer Name: "))
                while True:
                    try:
                        amount = int(input("Order Amount: "))
                    except ValueError:
                        print("\nPlease Input Numbers Only")
                    else:
                        total = amount * self.list_price[i]
                        break
                    
                print("\n")
                confirmation = input("Confirm Order [y] | [n]: ")
                if confirmation == "y" or confirmation == "Y":
                        print("\n")
                        print(" ------------------------------------")
                        print(" |  Computer Parts Ordering System  |")
                        print(" |       Rizal Ave. Bats City       |")
                        print(" |      www.computerpartsos.com     |")
                        print(" |     Welcome to Computer Parts    |")
                        print(" |          Ordering System         |")
                        print(" ------------------------------------")
                        print("     Customer Name: ", customer_name)
                        print(" ------------------------------------")
                        print("     Item: ", self.list_item[i])
                        print("     Amount: ", amount)
                        print(" ------------------------------------")
                        print("     Total Price: ", total)
                        print(" ------------------------------------")
                        customer_list = " ".join(["Customer Name:", customer_name, "Item:", self.list_item[i], "Amount:", str(amount), "Total Price:", str(total)])
                        self.data.append(customer_list) 
                        break
                else:
                        print("\n+-------------------------------------+")
                        print("|      You cancelled your order       |")
                        print("+-------------------------------------+")
                        break
        else:
            print("\n+-------------------------------------+")
            print("|    Invalid Product Name or ID       |")
            print("+-------------------------------------+")
            order_class = OrderProduct()
            order_class.display_order()

    def viewOrder(self):
        if self.data != []:
            print("---------------------------------------------------------------------\n")
            print("\n\n".join(self.data))
            print("\n---------------------------------------------------------------------\n\n")
        if self.data == []: 
            print("+-----------------------------------------+")
            print("|         There's no record here!         |")
            print("+-----------------------------------------+\n\n")                
    def display_order(self):
        print(" ")
        order_class = OrderProduct()
        product = input("Order Product: ")
        order_class.order_product(product)
        print(" ")     
