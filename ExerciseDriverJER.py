from programexerciseJER import shopping

def listobjects():
    shoppinglist = []
    numitems = 0
    while numitems <= 0: 
        try:
            numitems = int(input("How many number of items do you have?"))
            if numitems <= 0:
                print ("Number of items must be atleast 1")
        except ValueError:
            print("enter a valid number")
    
    for i in range(1, numitems + 1):
        print(f"Item {i}")
        food = input("enter food: ")
        amount = 0.0
        while amount <= 0:
            try:
                amount = int(input("Enter the amount of pounds: "))
                if amount <= 0:
                    print("Amount of pounds must be greater than 0.")
            except ValueError:
                print("Please enter a valid number for pounds.")
        shoppinglist.append(shopping(food, amount))
    return shoppinglist
        
def display_shopping_list(shoppinglist):
    for item in shoppinglist:
        print(item)

def calculatecost(shoppinglist):
    totalcost = sum(item.cost() for item in shoppinglist)
    return totalcost

def main():
    shopping_list = listobjects()
    print("\nHere is the summary of the items purchased")
    display_shopping_list(shopping_list)
    totalcost = calculatecost(shopping_list)
    print(f"Total cost: ${totalcost:.2f}")

if __name__ == "__main__":
    main()
    

        