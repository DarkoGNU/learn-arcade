import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")
    print()

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_miles_traveled = -20
    drinks_in_canteen = 3

    while True:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        choice = input("What is your choice? ").strip().upper()
        traveling = False
        print()

        if choice == "Q":
            print("Quitting...")
            break
        elif choice == "E":
            print(f"Miles traveled: {miles_traveled:2}")
            print(f"Drinks in canteen: {drinks_in_canteen:2}")
            print(f"The natives are {miles_traveled - natives_miles_traveled} miles behind you.")
            print()
            continue
        elif choice == "D":
            camel_tiredness = 0
            print("You are resting. The camel is happy.")
        elif choice == "C":
            traveling = True
            miles_to_travel = random.randrange(10, 21)
            miles_traveled += miles_to_travel
            print(f"You have traveled {miles_to_travel} miles.")
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
        elif choice == "B":
            traveling = True
            miles_to_travel = random.randrange(5, 13)
            miles_traveled += miles_to_travel
            print(f"You have traveled {miles_to_travel} miles.")
            thirst += 1
            camel_tiredness += 1
        elif choice == "A":
            if drinks_in_canteen > 0:
                print("You are drinking...")
                drinks_in_canteen -= 1
                thirst = 0
            else:
                print("You don't have any drinks.")
                print()
                continue

        if traveling:
            if random.randrange(20) == 0:
                print("You have found an oasis!")
                drinks_in_canteen = 3
                thirst = 0
                camel_tiredness = 0

        if thirst > 6:
            print("You died of thirst!")
            break
        elif thirst > 4:
            print("You are thirsty.")

        if camel_tiredness > 8:
            print("Your camel is dead.")
            break
        elif camel_tiredness > 5:
            print("Your camel is getting tired.")

        natives_miles_traveled += random.randrange(7, 15)

        if miles_traveled - natives_miles_traveled <= 0:
            print("The natives caught you!")
            break
        elif miles_traveled - natives_miles_traveled < 15:
            print("The natives are getting close!")

        if miles_traveled > 200:
            print("You escaped!")
            break

        print()


if __name__ == "__main__":
    main()
