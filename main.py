coffee_menu = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
    "mocha": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24, "chocolate": 20},
        "cost": 3.5,
    },
    "americano": {
        "ingredients": {"water": 300, "coffee": 18},
        "cost": 2.0,
    },
    "macchiato": {
        "ingredients": {"water": 50, "milk": 50, "coffee": 18},
        "cost": 2.8,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "chocolate": 50,
}

def is_resource_sufficient(order_ingredients):
    """Returns True if the resources are sufficient to make the drink, False otherwise."""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    try:
        total = int(input("How many quarters? ")) * 0.25
        total += int(input("How many dimes? ")) * 0.1
        total += int(input("How many nickels? ")) * 0.05
        total += int(input("How many pennies? ")) * 0.01
        return total
    except ValueError:
        print("Invalid input. Please insert coins again.")
        return process_coins()

def is_transaction_successful(money_received, drink_cost):
    """Returns True if the transaction is successful, False otherwise."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, you don't have enough money. Money refunded.")
        return False

def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

is_on = True

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino/macchiato/mocha/americano): ").lower()
    if order == "off":
        is_on = False
        print("Coffee Machine is turning off. Goodbye!")
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Chocolate: {resources['chocolate']}g")
        print(f"Money: ${profit}")
    elif order not in coffee_menu:
        print("Sorry, we don't serve that drink.")
    else:
        drink = coffee_menu[order]
        print(f"Your order costs: ${drink['cost']}")
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
