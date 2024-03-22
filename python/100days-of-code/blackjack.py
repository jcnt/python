logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack(): 

  os.system('clear')
  print(logo)
  
  def deal_card():
    return(random.choice(cards))
  
  player = []
  computer = []
  
  for i in range(2):
    player.append(deal_card())
    computer.append(deal_card())
  
  def calculate_score(list):
    a = (sum(list))
    if a == 21:
      return(0)
    elif a > 21:
      for i in list:
        if i == 11:
          list.remove(11)
          list.append(1)
        return(sum(list))
    else:
      return(a)
  
  gameover = False
  
  score_player = calculate_score(player)
  score_computer = calculate_score(computer)
  
  if score_player == 0 or score_player > 21 or score_computer == 0 or score_computer > 21: 
    gameover = True 
  
  while not gameover: 
    print()
    print(f"You have the following cards: {player} all together {calculate_score(player)}")
    print()

    if input("Do you want another card? y/n: ") == "y": 
      player.append(deal_card())
      score_player = calculate_score(player)
      if score_player > 21:
        gameover = True
  
    if score_computer < 17 and not score_computer == 0: 
      computer.append(deal_card())
      score_computer = calculate_score(computer)
      if score_computer > 21 or score_computer == 0:
        gameover = True
  
    else: 
      gameover = True
  
  
    score_player = calculate_score(player)
    score_computer = calculate_score(computer)
    
    if score_computer == score_player:
      print(f"Computer: {score_computer}, Player: {score_player} It's a draw!")
    elif score_computer > 21 and score_player > 21:
      print(f"Computer: {score_computer}, Player: {score_player} It's a draw!")
    elif score_computer == 0:
      print(f"Computer: {score_computer}, Player: {score_player} Computer wins!")
    elif score_player == 0:
      print(f"Computer: {score_computer}, Player: {score_player} Player wins!")
    elif score_computer > 21 and score_player <= 21:
      print(f"Computer: {score_computer}, Player: {score_player} Player wins!")
    elif score_player > 21 and score_computer <= 21:
      print(f"Computer: {score_computer}, Player: {score_player} Computer wins!")
    elif score_computer > score_player: 
      print(f"Computer: {score_computer}, Player: {score_player} Computer wins!")
    elif score_computer < score_player: 
      print(f"Computer: {score_computer}, Player: {score_player} Player wins!")
    else:
      print("someting is not OK")
  
  
  compare()
  
# run the main block of code
blackjack()


moreblackjack = True

while moreblackjack:
  print()    
  if input("Do you want to play a new game? y/n ") == "y": 
    moreblackjack = True
    blackjack()
  else: 
    moreblackjack = False
     

