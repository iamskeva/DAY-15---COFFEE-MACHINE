MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

espresso_cost = (MENU['espresso']['cost'])
latte_cost = (MENU['latte']['cost'])
cappuccino_cost = (MENU['cappuccino']['cost'])


money = 0


def is_resources_sufficient(order_ingredients):
    """ Return True when order can be made and returns False if ingredients is not enough"""

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True


def process_coins():
    """Returns total coin calculated from the inserted coin"""

    print("Please insert coins.")
    quarters_coin = int(input("how many quarters?: ")) * 0.25
    dimes_coin = int(input("how many dimes?: ")) * 0.10
    nickles_coin = int(input("how many nickles?: ")) * 0.05
    pennies_coin = int(input("how many pennies?: ")) * 0.01
    amount_paid = quarters_coin + dimes_coin + nickles_coin + pennies_coin

    return amount_paid


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or false if the money is insufficient"""

    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")
    elif choice != "off" and choice != "report" and choice != "espresso" and choice != "latte" and\
            choice != "cappuccino":
        print("Invalid input")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])