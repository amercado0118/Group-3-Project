
# Group 3 Pizza Ordering Project

# Team Members:
# Divine Isibor
# Ahmed Zihni
# Amanda Mercado
# Dominick Garcia


#   Names for pizza size
PIZZA_SIZE_NAMES = {
    "S": "Small",
    "M": "Medium",
    "L": "Large"
}


#   Prices for each pizza sizes
PIZZA_PRICES = {
    "S": 15,
    "M": 20,
    "L": 25,
}

#   Prices for pepperoni accounting for pizza size
PEPPERONI_PRICES = {
    "S": 2,
    "M": 3,
    "L": 3,
}

#   Price for extra cheese (uniform with every size)
CHEESE_PRICE = 1


#   Asks pizza size, input S, M, or L, capitalization unnecessary. If those options not entered, customer will be prompted to type S, M, or L
def askPizzaSize():
    while True:
        size = input("Select pizza size (S = Small, M = Medium, L = Large): ")
        size = size.upper() 

        if size in PIZZA_PRICES:
            return size
        else:
            print("Invalid size. Please enter sizes S, M, or L.")


#   Asks for toppings, inputs Y or N, capitalization unnecessary. If those options not entered, customer will be prompted to type Y or N
def askYesNo(prompt):
    while True:
        answer = input(prompt)
        answer = answer.upper()

        if answer in ("Y", "N"):
            return answer
        else:
            print("Invalid input. Please enter Y or N.")


#   Price calculation with or without toppings, with different sizes of pizza
def calculatePrice(size, pepperoni_choice, extra_cheese_choice):
    total_price = 0

    base_price = PIZZA_PRICES[size]
    total_price += base_price

    pepperoni_price = 0
    if pepperoni_choice == "Y":
        pepperoni_price = PEPPERONI_PRICES[size]
        total_price += pepperoni_price

    extra_cheese_price = 0
    if extra_cheese_choice == "Y":
        extra_cheese_price = CHEESE_PRICE
        total_price += extra_cheese_price

    
    return total_price, base_price, pepperoni_price, extra_cheese_price


# Header and prices of pizza and toppings printed
print("")
print("Group 3 Pizza Ordering System")
print("")
print("Pizza Prices")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")
print("Pepperoni Topping: $2 (Small), $3 (Medium/Large)")
print("Extra Cheese: $1 (All sizes)")
print("")

#   Main code body, prints header, prints questions to customer, calls calculation for total accumulated price as a certain base size, adds requested toppings, then prints order summary
def pizzaPrompt ():
    print("==============================================================")
    print("")
    size = askPizzaSize()
    print("")

    pepperoni_choice = askYesNo("Add Pepperoni? (Y/N): ")
    print("")

    extra_cheese_choice = askYesNo("Add Extra Cheese? (Y/N): ")
    print("")

    total, base, pepperoni_price, cheese_price = calculatePrice(
        size,
        pepperoni_choice,
        extra_cheese_choice
    )

    print ("Order Summary")
    print (f"Pizza Size: {PIZZA_SIZE_NAMES[size]} (${base})")

    if pepperoni_choice == "Y":
        print(f"Pepperoni: Yes (${pepperoni_price})")
    else:
        print("Pepperoni: No ($0)")

    if extra_cheese_choice == "Y":
        print(f"Extra Cheese: Yes (${cheese_price})")
    else:
        print("Extra Cheese: No ($0)")

    
    print("")
    print(f"Final Total: ${total:}")
    print("")
    print("==============================================================")
    print("")
    print("Thank you for ordering with Group 3 Pizza!")
    print("")


if __name__ == "__main__":
        pizzaPrompt()