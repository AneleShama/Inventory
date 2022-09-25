 # References 1
 # I used L1T27 materials were very helpful to complete the task including it examples.

 # Reference 2
 # I used Build the future with software resources
 # https://www.adamsmith.haus/python/answers/how-to-skip-the-first-line-of-a-file-in-python
 # I did not know how I can skip the first line from the file
 # the resource helped me understand how I can do this
 
 
 # Nike Warehouse


 # Shoes class defined
 # the class initialses 5 variables
 # country, code, product, cost, quantity

class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self. product = product
        self.cost = cost
        self.quantity = quantity
    

 # This method returns cost of shoe
    def get_cost(self):
        return self.cost
    

 # This method returns quantity of the shoes
    def get_quantity(self):
        return self.quantity

 # This method returns a string representation of the class
    def __str__(self):
        return self.country + ", " + self.code + ", " + self. product + ", " + str(self.cost) + ", " + str(self.quantity)


 # This list stores stores a list of Shoes object
 # The data here is extracted from inventory.txt
list_of_shoes = []


 # This function open the file, inventory and read data
 # from it, the fill content is append to list_of_shoes as an object
def read_shoes_data():
    try:
        with open("inventory.txt", "r+") as file:

 # readlines()[1:] ensures the first line
 # which is a header is not read
            lines = file.readlines()[1:]
            for line in lines:
                view_shoes = line.strip().split(",")
                country = view_shoes[0]
                code = view_shoes[1]
                product = view_shoes[2]
                cost = view_shoes[3]
                quantity = view_shoes[4]
 
 # append the attributes of file to ist_of_shoes
 # as Shoes object
                list_of_shoes.append(Shoes(country, code, product, int(cost), int(quantity)))

        print("\nData from inventory has been extracted successfully\n")

    except FileNotFoundError:
        print("\nThe file that you are trying to open does not exist\n")


 # This function will be used everytime a file need to be updated
 # for example, when the user add new product or
 # add quantity
def update_file():
    with open("inventory.txt", "w") as update_file:
        update_file.write("Country, Code, Product, Cost, Quantity\n")
        for i in list_of_shoes:
            update_file.write(str(i) + "\n")    

 # This function allow the user to capture new
 # data about the show
def capture_shoes():
    add_country = input("Enter the country:\t")
    add_code = input("Enter the shoe code:\t")
    add_product = input("Enter product name:\t")
    add_cost = input("Enter cost of product:\t")
    add_quantity = input("Enter the quantity:\t")
 
 # the data is the added to ist_of_shoes and 
 # subsequently added to the file
    list_of_shoes.append(Shoes(add_country, add_code, add_product, add_cost, add_quantity))


 # This function is used to view all
 # details about the shoes
def view_all():
    for i in list_of_shoes:
        print(i)


 # this function finds shoe with the lowest stock
 # and ask the user if they want to stock more quantity
def re_stock():
    try:
        lowest_qty = list_of_shoes[0]

        for i in list_of_shoes:
            if i.get_quantity() < lowest_qty.get_quantity():
                lowest_qty = i

        print(f"Shoes with lowest quantity:\n{lowest_qty}")

 # ask the user if they want to restock this shoe
        restock_shoe = input('''
Do you want to add quantity of shoe?
Yes
No
:   ''').lower()

 # if yes, asked them how many shoes do they want to add
        if restock_shoe == "yes":
            while True:
                try:
                    qty_shoe = int(input("Enter the quantity you want to add:\t"))

 # add new quantity to the old quantity
                    lowest_qty.quantity = lowest_qty.get_quantity() + qty_shoe
                    break
                except ValueError:
                    print("Not a valid input. Please enter a number of shoe quantity tp re stock")
 
 # if the user select something else,
 # an else statement is excuted
        else:
            print("\nNo quantity will be added")
    except Exception:
        print("\nYou have not loaded the data from inventory file, select option A and try again")


 # The function allow the user to seach a shoe
 # using shoe code object, the show detail is the printed
def seach_shoe():
    code = input("Enter code for the shoe to be searched:\t")
    for i in list_of_shoes:
        if i.code == code:
            print(i)
        

 # The function calculate the total value for each item
 # the print out total value for each item
def value_per_item():
    value = 0
    for i in list_of_shoes:
        value = i.get_cost() * i.get_quantity()
        print(f"{i} Total Value: R {value}")


 # The function finds the shoe with highest quantity 
def highest_qty():

    try:
        highest_qty = list_of_shoes[0]
    
        for i in list_of_shoes:
            if i.get_quantity() > highest_qty.get_quantity():
                highest_qty = i

        print(f"Shoes with highest quantity, this shoe must be on sale:\n{highest_qty}")

    except Exception:
        print("\nYou have not loaded the data from inventory file, select option A and try again")

choice = ""

 # until the user select q, this program will continue to run
 # ask the user what would they want to do
while choice.lower() != "q":
    choice = input('''
What would you like to select?

A   - Read shoes data
B   - Capture shoe data
C   - View all shoes data
D   - Restock shoes with lowest quantity
E   - Seach Shoe
F   - Get total value for each item in the stock
G   - Shoe with highest quantiy
Q   - Close the program
:   - ''').lower()

 # based on user's choice, an appropriate function is called

    if choice == "a":
        read_shoes_data()

    elif choice == "b":
        read_shoes_data()
        capture_shoes()
        update_file()

    elif choice == "c":
        view_all()

    elif choice == "d":
        re_stock()
        update_file()

    elif choice == "e":
        seach_shoe()
        
    elif choice == "f":
        value_per_item()

    elif choice == "g":
        highest_qty()
        
    elif choice == "q":
        print("Goodbye!!")
    else:
        print("\nYou have made a wrong choice, Please Try again\n")
    
