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

game_images = [rock, paper, scissors]

print("Let's play Rock Paper Scissors!")

try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
except ValueError:
    user_choice = 3

computer_choice = random.randint(0, 2)

print(game_images[user_choice])

print("\nComputer chose:")
print(game_images[computer_choice])

if user_choice == 0:
    if computer_choice == 0:
        print("It's a draw!")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")

elif user_choice == 1:
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("It's a draw!")
    else:
        print("You lose!")

elif user_choice == 2:
    print("\nComputer chose:")
    if computer_choice == 0:
        print("You lose!")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("It's a draw!")

else:
    print("You must type 0, 1 or 2.")

