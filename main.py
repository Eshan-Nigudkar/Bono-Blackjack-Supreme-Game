############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################


from replit import clear
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def drawcard():
  a=random.randint(0,12)
  b=random.randint(0,12)
  c=[cards[a],cards[b]]
  return c


def draw_new_card():
  a=cards[random.randint(0,12)]
  return a
  
                 
def score_func(list):
  sum_score=0
  for i in range(0,len(list)):
    sum_score+=list[i]
  return sum_score

  
# Logo and starting game
from art import logo

    
def playgame():
  print(logo)
  
  # Cards_drawn by user
  card_drawn=drawcard()
  score= score_func(card_drawn)
  print(f"Your cards: {card_drawn}, current score: {score}")
  #  Cards drawn by computer
  computer_card=drawcard()
  print(f"Computer's first card: {computer_card[0]}")
  computer_score=score_func(computer_card)
  # print(f"Computer points are {computer_score}")
  user_draw_card=True
  computer_draw=True
  
  # user playing
  while (score<=21 and user_draw_card==True):
   
    draw_card_ask=input("Want to draw another card? y for yes and n for no ")
    
    if draw_card_ask=="y":
      card_drawn.append(draw_new_card())
      score=score_func(card_drawn)
      if(score>21 and 11 in card_drawn):
        card_drawn.remove(11)
        card_drawn.append(1)
        score=score_func(card_drawn)
      
      
      print(card_drawn)
      
      print(f"Your Points are {score}")
      
  
    elif draw_card_ask=="n":
      user_draw_card=False

      
  # Computer card playing
  while(computer_score<21 and computer_draw==True ):
    if(computer_score<17):
      computer_card.append(draw_new_card())
      computer_score=score_func(computer_card)
      
    elif(computer_score>=17):
      computer_draw=False
      
    
  if(score==21):
    print(f"Your final cards: {card_drawn}, final score: {score}")
    print(f"Computer's final cards: {computer_card}, final score: {computer_score}")
    print("That's a BlackJack. You win.")
  elif computer_score==21:
    
    print(f"Your final cards: {card_drawn}, final score: {score}")
    print(f"Computer's final cards: {computer_card}, final score: {computer_score}")
    print("That's a black jack, Computer wins!")
      
  elif(score>21):
    print(f"Your final cards: {card_drawn}, final score: {score}")
    print(f"Computer's final cards: {computer_card}, final score: {computer_score}")
    print("You lose!")
  elif(score<21 and score>computer_score):
    print(f"Your final cards: {card_drawn}, final score: {score}")
    print(f"Computer's final cards: {computer_card}, final score: {computer_score}")
    print("Congratulations! You Won!")
  elif(computer_score>21):
    
    print(f"Your final cards: {card_drawn}, final score: {score}")
    print(f"Computer's final cards: {computer_card}, final score: {computer_score}")
    print("Congratulations! You Won!")
  elif(computer_score==score):
    
    print(f"Your final cards: {card_drawn}, final score: {score}")
    print(f"Computer's final cards: {computer_card}, final score: {computer_score}")
    print("It's a Draw.")
  else:
    
    print("Computer Wins!")
    print(f"Computer's final cards: {computer_card}, final score: {computer_score}")
    
  if(input("do you want to play again? y or n ")=="y"):
    clear()
    playgame()  
  else:
    clear()
    

if(input("Do you want to play Blackjack? Type y to start or n to exit. ")=="y"):
  
   playgame() 
else:
  clear()