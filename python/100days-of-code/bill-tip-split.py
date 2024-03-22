#!/usr/bin/python3
print ("\n")
print("  Welcome to the tip calculator app!")
print ("\n")
bill = float(input("  What is the amount of the bill? $"))
tip = int(input("  What amount of tip would you like to give? 10, 12 or 15%? "))
pers = int(input("  How many person to split the bill? "))
print()
print (f"  You'll need to pay $ {round(bill * (1 + tip / 100) / pers, 2)}  per person" )
print()

