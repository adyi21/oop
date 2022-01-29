"""
Main program
"""
import sys
import time
from src.hand import Hand
value = True


while value:

    print("Printing the results...\n")
    hand_1 = Hand()

    print(str(hand_1))
    print("\n")
    choice = input("---->>  ")
    if choice == "r":
        hand_1.roll()
        print("Printing after roll...\n")
        print(str(hand_1))
        print("============\n")
        time.sleep(1)
    elif choice == "q":
        sys.exit()
    else:
        print("That is not a valid choice. You can only choose from the menu.")
