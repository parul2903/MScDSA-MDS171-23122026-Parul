# create a menu in a nested list form
menu = [["Tea", 30],["Coffee", 40],["Lemonade", 35],["Iced Tea", 30],["Espresso", 40],["Latte", 45],["Americano", 20],["Mocha", 25],["Cappuccino", 30],["Soft Drinks", 40]]

# setting up item numbers for the dishes in the menu
item_number = {}
for i in range(0, len(menu)):
    item_number[menu[i][0]] = i+1

# creating a menu dictionary to display in the final application
menu_dict = {}
for i in range(0, len(menu)):
    menu_dict[menu[i][0]] = menu[i][1]

# define a function for generating unique order IDs
import random

def gen_orderId():
    unique_id = []
    for i in range(5):
        unique_id.append(str(random.randint(1,9)))
    
    return "".join(unique_id)

# DEFINE ALL THE FUNCTIONS
# menu driven application
# The application consists of 3 functions
# the first function defines: take the order 
# the second function defines: view the order and returns the details of the order
# the third function defines: generates the bill of the order based on the order id 

order_details = {}

def take_order():
    ask_order = input("What is your order?").title().strip().split(",")
    ask_quantity = input("What quantity of the order you want?").title().strip().split(",")

    order_details["ORDER_ID"] = gen_orderId()
    order_details["ITEMS"] = []

    for i in range(0, len(ask_order)):
        item_details = {}
        item_details["itemnumber"] = item_number[ask_order[i]]
        item_details["quantity"] = ask_quantity[i]
        order_details["ITEMS"].append(item_details)

    print(f'Order taken successfully with order id {order_details["ORDER_ID"]}')
    print("*"*200)

def gen_bill():
    quantity_list = []
    price_list = []
    total_bill = []
    for i in order_details["ITEMS"]:
        quantity_list.append(int(i["quantity"]))

    for i in range(0, len(order_details["ITEMS"])):
        price_list.append(list(menu_dict.values())[order_details["ITEMS"][i]["itemnumber"]-1])

    for i in range(0, len(price_list)):
        total_bill.append(price_list[i]*quantity_list[i])

    print(f'The total bill for the order with id {order_details["ORDER_ID"]} is Rs. {sum(total_bill)}')  
    print("*"*200)

def view_order():
    ask_orderId = input("Enter the order id: ")

    if order_details["ORDER_ID"] == ask_orderId:
        print(order_details)
        print("*"*200)
    
    else:
        print("This order id is not valid.")

#### THE PROGRAM STARTS FROM HERE

print("WELCOME TO CULINARY HAVEN")
print("*"*50)
print("Please choose the order from the following menu:\n", menu_dict)
print("*"*200)
print("Please make a choice\n")
print("1) Choose 1 for giving the order\n2) Choose 2 for viewing the order based on the order id\n3) Choose 3 for generating bill based on the order id\n4) Choose 4 to exit.")
print("*"*200)

while True:

    choice = input("Enter your choice: ")
    print("You have entered choice: ", choice)

    if int(choice) == 1:
        take_order()

    elif int(choice) == 2:
        view_order()

    elif int(choice) == 3:
        ask_orderId = input("Enter the order id: ")
        gen_bill()

    elif int(choice) == 4:
        exit()

    else:
        print("Invalid option..!")