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


        if airfare and food and days and excursions and souvenirs != None:
            break


    total_cost = (airfare * 4) + (food * 4 * days) + excursions + souvenirs

    print("\nYour budget summary:\n")

    print(f"Airfare: {airfare * 4:.2f}\n")

    print(f"Food: {food * 4 * days:.2f}\n")

    print(f"Souvenirs: {souvenirs:.2f}\n")

    print(f"Total Cost: {total_cost:.2f}\n")



family_trip()

