'''
Develop a program that will calculate the total cost for a family vacation. This will include:
    - Airfare (per person) -
    - Food Costs (Daily, per person) -
    - Excursions and Activities -
    - Souvenir Budget -

The overall final trip should not be over $6000. Recommend adjustments if the price exceeds $6000.
'''

print("\nWelcome to the Family Trip Budget Calculator!\n\n")

'''
1.
Ask the user for various inputs such as:

    Airfare Cost (Per person).
    Daily Food Budget (Per person).
    Number of days on the trip.
    Excursion or Activities costs (For the entire family).
    Souvenir Budget (For the entire family).

'''

def family_trip():

    while True:
    # Values are set to 'None' incase the if the user enters an invalid input value.
        airfare = None
        food = None
        days = None
        excursions = None
        souvenirs = None
        
        try:
            airfare = float(input("How much for tickets? (Per person, shouldn't exceed $400) "))
        
            food = float(input("How much for food? (Per person) "))

            days = int(input("How many days on the trip? "))

            excursions = float(input("How much for excursion/activity costs? "))

            souvenirs = float(input("How much spending on souvenirs? "))

        except ValueError:
            print("\nThat was not a valid input, perhaps you made a typo? Please re-enter your information.\n")

# When all values are not equal to 'None' (meaning the user did not enter an invalid value), then the program continues on.
        if airfare and food and days and excursions and souvenirs != None:
            break
# If the conditions above are NOT met, then the program asks the user to re-enter all of their info until the conditions 
# are met.

    total_cost = (airfare * 4) + (food * 4 * days) + excursions + souvenirs

    print("\nYour budget summary:\n")
    # Prints and displays the cost of each fee to the user.

    print(f"Airfare: ${airfare * 4:.2f}\n")

    print(f"Food: ${food * 4 * days:.2f}\n")
    
    print(f"Excursions: ${excursions:.2f}\n")

    print(f"Souvenirs: ${souvenirs:.2f}\n")

    print(f"Total Cost: ${total_cost:.2f}\n")

    if total_cost < 6000:
        remaining = 6000 - total_cost # If trip is within the budget, show user the remaining expenses they can spend on.
        print("Your trip is within your budget!")
        print(f"\nYou have ${remaining:.2f} remaining for any extra expenses!")

    elif total_cost > 6000:
        print("Your trip is overbudget!\n")
        debt = total_cost - 6000 # If trip exceeds the budget of $6000. show the user how much they are overbudget.

        if (food * 4 * days) > (airfare * 4) and excursions and souvenirs:
            # If food costs are higher than airfare, excursions, and souvenirs...
            print(f"You should reduce costs by ${debt:.2f}. Maybe try reducing your food costs?")

        elif excursions > (food * 4 * days) and souvenirs and (airfare * 4):
            # If excursion costs are higher than food, airfare, and souvenirs...
            print(f"You should reduce costs by ${debt:.2f}. Maybe try reducing your excursion costs?")

        elif souvenirs > (food * 4 * days) and (airfare * 4) and excursions:
            # If souvenirs costs are higher than food, airfare, and excursions...
            print(f"You should reduce costs by ${debt:.2f}. Maybe try reducing your souvenir costs?")

        else:
            # Airfare costs shouldn't be higher than the other fees. This else statement is if for some reason, if all of
            # the other elif statements are not met (If the values of the fees were the same).
            print(f"You should reduce costs by ${debt:.2f}.")


family_trip()