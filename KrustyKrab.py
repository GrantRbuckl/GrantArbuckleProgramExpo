"""
Welcome to the Krusty Krab! Here's our menu:

(k) Krabby Patty............. 1.25  | (km)  Krabby Meal............ 3.50
(kc) w/sea cheese............ 1.50  | (2km) Double Krabby Meal..... 3.75
(2k) Double Krabby Patty..... 2.00  | (3km) Triple Krabby Meal..... 4.00
(2kc) w/sea cheese........... 2.25  | (ssd) Salty Sea Dog.......... 1.25
(3k) Triple Krabby Patty..... 3.00  | (fl)  Footlong............... 2.00
(3kc) w/sea cheese........... 3.25  | (ss)  Sailor's Surprise...... 3.00
                                    | (gl)  Golden loaf............ 2.00
                                      (gls)  w/sauce............... 2.50
(c) Coral Bits -
small.......... 1.00 | (ks) Kelp Shake............ 2.00
medium......... 1.25 | 
large.......... 1.50 | (sda) Seafoam Soda -
                     | small............ 1.00
(kr) Kelp Ring. 1.50 | medium........... 1.25
  salty sauce... .50 | large............ 1.50

"""

import Sentry
ui = ""
loop = True
subtotal = 0
total = 0
currentOrder = []
subtotalList = []
orders = []
possibleFood = ["k","kc","2k","2kc","3k","3kc","km","2km","3km","ssd","fl","ss","gl","gls","n"]
possibleOther = ["c","ks","kr","sda","n"]

def printFood():        #prints 1st menu
    print("""    
Welcome to the Krusty Krab! What would you like to eat?  
(k)  Krabby Patty............ 1.25 | (km)  Krabby Meal........... 3.50   
(kc)  w/sea cheese........... 1.50 | (2km) Double Krabby Meal.... 3.75       
(2k) Double Krabby Patty..... 2.00 | (3km) Triple Krabby Meal.... 4.00        
(2kc) w/sea cheese........... 2.25 | (ssd) Salty Sea Dog......... 1.25        
(3k) Triple Krabby Patty..... 3.00 | (fl)  Footlong.............. 2.00        
(3kc) w/sea cheese........... 3.25 | (ss)  Sailor's Surprise..... 3.00        
                                   | (gl)  Golden loaf........... 2.00
(n)  None                          | (gls)  w/sauce.............. 2.50
""")

def printOther():    #prints 2nd menu
    print("""
Would you like any other items?
(c) Coral Bits -
     small.......... 1.00 | (ks) Kelp Shake.... 2.00
     medium......... 1.25 | 
     large.......... 1.50 | (sda) Seafoam Soda -
                          | small............ 1.00
(kr) Kelp Rings..... 1.50 | medium........... 1.25
      salty sauce.... .50 | large............ 1.50    
(n)  None

""")

def checkFood(): #Checks if items are valid and if they are appends the price to the subtotal
    global subtotal
    global loop
    if ui == "k":
        currentOrder.append("Krabby Patty")
        subtotal+=1.25
    elif ui == "kc":
        currentOrder.append("Krabby Patty with Sea Cheese")
        subtotal+=1.50
    elif ui == "2k":
        currentOrder.append("Double Krabby Patty")
        subtotal+=2
    elif ui == "2kc":
        currentOrder.append("Double Krabby Patty with Sea Cheese")
        subtotal+=2.25
    elif ui == "3k":
        currentOrder.append("Triple Krabby Patty")
        subtotal+=3
    elif ui == "3kc":
        currentOrder.append("Triple Krabby Patty with Sea Cheese")
        subtotal+=3.25
    elif ui == "km":
        currentOrder.append("Krabby Meal")
        subtotal+=3.50
    elif ui == "2km":
        currentOrder.append("Double Krabby Meal")
        subtotal+=3.75
    elif ui == "3km":
        currentOrder.append("Triple Krabby Meal")
        subtotal+=4
    elif ui == "ssd":
        currentOrder.append("Salty Sea Dog")
        subtotal+=1.25
    elif ui == "fl":
        currentOrder.append("Foot Long")
        subtotal+=2
    elif ui == "ss":
        currentOrder.append("Sailor's Surprise")
        subtotal+=3
    elif ui == "fl":
        currentOrder.append("Foot Long")
        subtotal+=2
    elif ui == "gl":
        currentOrder.append("Golden Loaf")
        subtotal+=2
    elif ui == "gls":
        currentOrder.append("Golden Loaf with Sauce")
        subtotal+=2.5
    elif ui == "n":
        loop = False

def checkOther(): #same as other check function but for the second menu
    global subtotal
    if ui == "c":
        kind = input("What size of Coral Bits would you like? (s/m/l) ")
        coralLoop = True
        while(coralLoop):
            if kind == "s":
                currentOrder.append("Small Coral Bits")
                subtotal+=1
                coralLoop=False
            elif kind == "m":
                currentOrder.append("Medium Coral Bits")
                subtotal+=1.25
                coralLoop=False
            elif kind == "l":
                currentOrder.append("Large Coral Bits")
                subtotal+=1.50
                coralLoop=False
    elif ui == "kr":
        sauceLoop = True
        while(sauceLoop):
            sauce = input("Would you like to add Salty Sauce? (y/n) ")
            if sauce == "y":
                currentOrder.append("Kelp Rings with Salty Sauce")
                subtotal+=2
                sauceLoop = False
            elif sauce == "n":
                currentOrder.append("Kelp Rings with No Sauce")
                subtotal+=1.5
                sauceLoop = False
    elif ui == "ks":
        currentOrder.append("Kelp Shake")
        subtotal+=2
    elif ui == "sda":
        size = input("What size of Seafoam Soda would you like? (s/m/l) ")
        sodaLoop = True
        while(sodaLoop!=False):
            if size == "s":
                currentOrder.append("Small Seafoam Soda")
                subtotal+=1
                sodaLoop=False
            elif size == "m":
                currentOrder.append("Medium Seafoam Soda")
                subtotal+=1.25
                sodaLoop=False
            elif size == "l":
                currentOrder.append("Large Seafoam Soda")
                subtotal+=1.50
                sodaLoop=False

def orderFood():  #prints menu, asks item, rejects item if not on the menu
    global ui
    loop = True
    while(loop):
        printFood()
        ui = input("")
        loop = rejectui(possibleFood)   #Credit to Mr. Bander
    
def orderOther():  #same as other order function but for the second menu
    global ui
    loop = True
    while(loop):
        printOther()
        ui = input("")
        loop = rejectui(possibleOther)

#Sentry-esque function
def rejectui(possible):   #This function acts like the sentry class is supposed to, 
#it takes the item the user wants and decides whether or not it is on the menu
    if not ui in possible:
        print("Sorry, our systems can't understand that, please enter a valid item.")
        return  True
    else:
        print("O-K!")
        return False

#"edit" function - 

def editOrder():  #allows the user to edit items in an order (INCOMPLETE)
    global orders
    edit = input("Would you like to edit an item from an order? (y/n) ")
    while(edit!="y" and edit!="n"):
      edit = input("Would you like to edit an item from an order? (y/n) ")
    if edit == "y":
      print("\nThe items in the order start from zero (from left to right) and increase by one.")
      for i, each in enumerate(orders): #Found by user "Kartik" in a GeeksForGeeks page https://www.geeksforgeeks.org/python/enumerate-in-python/
          print(f"Order No. : {orders.index(each)}")
          print(f"{each}\n")
      listToEdit = int(input("Which order would you like to change? (number) "))
      itemToEdit = int(input("Which item in this order would you like to edit? (number) "))
      while(listToEdit>len(orders) or itemToEdit>len(orders)):
        print("Invalid. Try again.")
        listToEdit = int(input("Which order would you like to change? (number) "))
        itemToEdit = int(input("Which item in this order would you like to edit? (number) "))
      menu = input("Which menu would you like to order on?")
        



#"delete" function
def delOrder():     #Permits the user to delete items in an order   (COMPLETE)
    global orders
    delete = input("Would you like to delete an item from an order? (y/n) ")
    while(delete!="y" and delete!="n"):
      delete = input("Would you like to delete an item from an order? (y/n) ")
    if delete == "y":
      print("\nThe items in the order start from zero (from left to right) and increase by one.")
      for i, each in enumerate(orders):
          print(f"Order No. : {orders.index(each)}")
          print(f"{each}\n")
      listToDelete = int(input("Which order would you like to change? (number) "))
      itemToDelete = int(input("Which item in this order would you like to delete? (number) "))
      while(listToDelete>len(orders) or itemToDelete>len(orders)):
        print("Invalid. Try again.")
        listToDelete = int(input("Which order would you like to change? (number) "))
        itemToDelete = int(input("Which item in this order would you like to delete? (number) "))
      orders[listToDelete].pop(itemToDelete)
      



end = False
#Main loop 
while(not end):
    subtotal = 0
    currentOrder = []
    foodCont = True
    while(foodCont):
#loop=Sentry.rejectui(ui,possibleFood)
        orderFood()   #1st half - first menu
#Add food stuff and many probably redundant if-statements that could definitely be replaced by more efficient code in way less lines but y'know what we ball 
        checkFood()
        valid = False
        while(not valid):
            cont = input("Would you like to add anything else? (y/n) ")
            if cont == "n":
                foodCont = False
                valid = True
            elif cont == "y":
                foodCont = True
                valid = True
            else:
                print("Please enter a valid response.")
       #Part two of ordering, to not overload the player and cram everything into one menu 
    otherCont = True
    loop = True
    while(otherCont):
        orderOther()
        checkOther()
        valid = False
        while(not valid):
            cont = input("Would you like to add anything else? (y/n) ")
            if cont == "n":
                otherCont = False
                valid = True
            elif cont == "y":
                otherCont = True
                valid = True
            else:
                print("Please enter a valid response.")

    #add "total" area
    print(f"Your subtotal is ${subtotal}")
    endLoop = True
    while(endLoop):    
        again = input("Would you like to add another order? (y/n) ")
        if again == "n":
            endLoop = False
            end = True
        elif again == "y":
            endLoop = False
    orders.append(currentOrder) #appends orders to the list containing all orders
    subtotalList.append(subtotal) #appends subtotals to the list containing all subtotals
    total+=subtotal
delOrder()
editOrder()
print("Your orders are:")
i=0
for eachOrder in orders:                            #For loop that prints out the final receipt
    print(f"Order No. : {orders.index(eachOrder)+1}")
    for eachItem in eachOrder:
        print(eachItem)
    if ("Krabby Patty" in eachOrder or "Double Krabby Patty" in eachOrder or "Footlong" in eachOrder) and ("Small Coral Bits"in eachOrder or"Medium Coral Bits"in eachOrder or"Large Coral Bits"in eachOrder) and ("Small Seafoam Soda" in eachOrder or "Large Seafoam Soda"in eachOrder):
      print("Krab's Kombo Discount applied! 10 percent off!")
      subtotalList[i] = subtotalList[i]*.9
    print(f"Subtotal: {subtotalList[i]:.2f}")
    i+=1
    print("\n")
tax = total*.07
total = total + tax
print(f"Your tax is {tax:.2f}\nYour total for all orders is ${total:.2f}")
