rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)_____
          ________)
          ________)
         ________)
---.__________)
'''

scissors = '''
    _______
---'   ____)_____
          _______)
       ___________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user = input("please choose, Rock, Paper, Scissors: ")
luser = user.lower()

if luser == "rock":
  print(rock)
elif luser == "paper":
  print(paper)
elif luser == "scissors":
  print(scissors)

computer = ["rock", "paper", "scissors"]
a = random.randint(0,2)

if (computer[a]) == "rock":
  print(rock)
elif (computer[a]) == "paper":
  print(paper)
elif (computer[a]) == "scissors":
  print(scissors)

if luser == "rock":
  if computer[a] == "rock":
    print("draw")
  elif computer[a] == "scissors":
    print("you won")
  elif computer[a] == "paper":
    print("you lost")

if luser == "paper":
  if computer[a] == "paper":
    print("draw")
  elif computer[a] == "rock":
    print("you won")
  elif computer[a] == "scissors":
    print("you lost")

if luser == "scissors":
  if computer[a] == "scissors":
    print("draw")
  elif computer[a] == "paper":
    print("you won")
  elif computer[a] == "rock":
    print("you lost")


