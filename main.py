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

#Write your code below this line 👇
lis = [rock, paper, scissors]
import random
print("welcome to rock, paper,scissors game.")
user_choice = int(input("choose 0 for rock, 1 for paper, and 2 for scissors. "))
computer_choice = random.randint(0, 2)

if user_choice <0 or user_choice >2:
    print("you choose wrong number. Game over. You lose.")

else:
    print(f"you choose {lis[user_choice]}")
    print(f"computer choose {lis[computer_choice]}")
    if user_choice ==0 and computer_choice ==2:
        print("you win")
    elif user_choice ==2 and computer_choice ==0:
        print("you lose.")
    elif user_choice > computer_choice:
        print("you win.")
    elif user_choice < computer_choice:
        print("you lose.")
    elif user_choice == computer_choice:
        print("draw.")

