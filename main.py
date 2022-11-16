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

money = 0


def insert_coins():
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total_coins


def generate_report(available_resources, cash):
    """Prints the available resources including the cash available in the machine"""
    print(f"Water: {available_resources['water']}ml\n"
          f"Milk: {available_resources['milk']}ml\n"
          f"Coffee: {available_resources['coffee']}ml\n"
          f"Money: ${cash}")


def check_ingredients(drink, available_ingredients, recipe):
    """Verifies there is enough ingredients/resources available for the selected drink"""
    if available_ingredients['water'] < recipe[drink]['ingredients']['water']:
        print("Sorry, there is not enough water.")
        return False
    elif drink != "espresso" and available_ingredients['milk'] < recipe[drink]['ingredients']['milk']:
        print("Sorry, there is not enough milk.")
        return False
    elif available_ingredients['coffee'] < recipe[drink]['ingredients']['coffee']:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True


def dispense_drink(drink, available_ingredients, recipe):
    """Dispenses the selected drink and reduces the available resources accordingly"""
    available_ingredients['water'] -= recipe[drink]['ingredients']['water']
    available_ingredients['coffee'] -= recipe[drink]['ingredients']['coffee']
    if drink != "espresso":
        available_ingredients['milk'] -= recipe[drink]['ingredients']['milk']
    return available_ingredients


machine_on = True

while machine_on:
    command = input(f"Coffee Menu:\n   Espresso\n   Latte\n   Cappuccino\n(or type 'report' for machine status)\nWhat would you like? : ").lower()
    if command == "report":
        generate_report(resources, money)
    elif command == "off":
        machine_on = False
    elif command == "espresso" or "latte" or "cappuccino":
        if check_ingredients(command, resources, MENU):
            drink_cost = MENU[command]["cost"]

            print(f"{command} costs ${drink_cost}")
            print("Please insert coins.")

            coins_inserted = insert_coins()
            if coins_inserted < drink_cost:
                print("Sorry, that's not enough Money. Money refunded.")
            else:
                change = round(coins_inserted - drink_cost, 2)
                money += drink_cost
                resources = dispense_drink(command, resources, MENU)

                if change != 0:
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {command}. Enjoy!")


