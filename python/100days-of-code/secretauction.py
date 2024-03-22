logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os

print(logo)
bidding = {}


# print(logo)
isGameOn = "yes"

while isGameOn == "yes" :
  name = input("What is your name?: ")
  bid = input("What is your max bid?: ")
  bidding[name] = int(bid)
  isGameOn = input("Is there anyone bidding? yes/no: ")
  os.system('clear')

winner = 0
person = ""
for i in bidding:
  if bidding[i] > winner:
    winner = bidding[i]
    person = i


print(f"The winner of this acution is {person} with a winning bid of ${winner}")


