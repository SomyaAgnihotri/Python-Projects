import random
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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# game_images = [rock, paper, scissors]
you_chose = int(input("what do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
# print(game_images[you_chose])
comp_chose = random.randint(0,2)
print(f"Computer chose: {comp_chose}")
# print(game_images[comp_chose])
if you_chose >= 3 or you_chose < 0: 
  print("You typed an invalid number, you lose!") 
elif you_chose == 0 and comp_chose == 2:
  print("You win!")
elif comp_chose == 0 and you_chose == 2:
  print("You lose")
elif comp_chose > you_chose:
  print("You lose")
elif you_chose > comp_chose:
  print("You win!")
elif comp_chose == you_chose:
  print("It's a draw")
  

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!")
# else:
#   print(game_images[user_choice])
  
#   computer_choice = random.randint(0, 2)
#   print("Computer chose:")
#   print(game_images[computer_choice])
  
  
#   if user_choice == 0 and computer_choice == 2:
#     print("You win!")
#   elif computer_choice == 0 and user_choice == 2:
#     print("You lose")
#   elif computer_choice > user_choice:
#     print("You lose")
#   elif user_choice > computer_choice:
#     print("You win!")
#   elif computer_choice == user_choice:
#     print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end