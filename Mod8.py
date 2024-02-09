#The following code is borrowed from MOD4
class ItemToPurchase:          #creates the name of the class
	def __init__(item, name, price, quantity, description):     # defines the attributes for the objects of the class. Description is newly added.
		item.name = name
		item.price = price
		item.quantity = quantity
		item.description = description

#The following code is borrowed from MOD6        
class ShoppingCart: #Creates a class called ShoppingCart.
    def __init__(self, customer_name = "none", date = "January 1, 2024"): #defines the initial variables given to the ShoppingCart class
        self.customer_name = customer_name 
        self.date = date 
        self.cart_items = [] 
    def add_item(self, ItemToPurchase): #Defines a function that will add an ItemToPurchase object to the cart. (not implemented)
            self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name): #Defines a function that will remove an item from the cart using its name by checking names of items.
        for item in self.cart_items: 
            if item.name == item_name: 
                self.cart_items.remove(item) 
            else:                     #tells the progam what to do if the item was not found.
                print("Item not found in cart. Nothing removed.") 
            

    def modify_item(self, item_name): #Defines a function that will allow items to be modified from the cart.(not implemented)
                if self.cart_items:
                        for item in self.cart_items:
                                if item_name == item.name:
                                        new_item_quantity = int(input("Enter a new quantity:"))
                                        item.quantity = new_item_quantity
                else:
                        print("No items in cart.")

    def get_num_items_in_cart(self): #Defines a function that get the number of items in the cart.
        if self.cart_items:
            return sum(item.quantity for item in self.cart_items)
        else:
            print("No items in cart.")
 #Checks the quantity of items for each item in the cart and returns the sum to the user.

    def get_cost_of_cart(self): #Defines a function that will get the cost of each item in the cart.
        if self.cart_items:
            return sum(item.price * item.quantity for item in self.cart_items)   
        else:
            print("Cart is empty.") 
 #Calculates the cost of each item in the cart by multiplying the item's price by its quantity.
                                                                           #Then sums the total for all items.

    def print_total(self):             #Defines a function that will print the total cost of the cart.
        if not self.cart_items: 
            print("SHOPPING CART IS EMPTY") 
            
        else: 
            total_cost = self.get_cost_of_cart() #defines a variable called total_cost which gets its value from get_cost_of_cart
            print(f"{self.customer_name}'s Shopping Cart - {self.date}") 
            print(f"Number of items: {self.get_num_items_in_cart()}") 
            for item in self.cart_items: 
                print(f"{item.name} {item.quantity} @ ${item.price} = {item.quantity * item.price}") 
            print(f"Total:") 
            return total_cost            
    
    def print_descriptions(self): #Defines a function that will print out the description of each item.
        print(f"{self.customer_name}'s Shopping Cart - {self.date}") 
        print("Item Descriptions") 
        for item in self.cart_items: 
            print(f"{item.name}: {item.description}") 
            
          
def print_menu(Cart):
    allow_loop = True #Creates a boolean variable for the loop
    while allow_loop == True: #Creates a while loop that will continuously repeat the bellow code.
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        
        user_choice = str(input("\nChoose an option:")) #defines a variable called user choice which takes the user's input for the menu.
        if user_choice.lower() == "a":
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_desc = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_desc)
            Cart.add_item(item)

        elif user_choice.lower() == "c":
                for item in Cart.cart_items:
                        print(item.name)
                item_name = str(input("Enter the item you want to change:"))
                Cart.modify_item(item_name)

        elif user_choice.lower() == "r":
                print("Here are the items in the cart:\n")
                for item in Cart.cart_items:
                        print(item.name)
                item_name = str(input("Choose an item to remove: \n"))
                Cart.remove_item(item_name)
                
        elif user_choice.lower() == "q": 
            allow_loop = False 
            
        elif user_choice.lower() == "o": #Checks if the user input o
            print("\nOUTPUT SHOPPING CART") 
            print(Cart.print_total()) 
            
        elif user_choice.lower() == "i": #Checks if the user input i
            print(Cart.print_descriptions()) 
        
        else: #Tells the computer what to do if the an improper variable is provided.
            print("An invalid option was given. Please try again.")
            
#Creating a test case for the code to run
#Each ItemToPurchase object has a name, price, quantity, description
    
username = str(input("Enter your first and last name"))
print(username)
todaysdate = str(input("Enter today's date"))
print(todaysdate)
Raphaels_Cart = ShoppingCart(username,todaysdate,)
print_menu(Raphaels_Cart)
