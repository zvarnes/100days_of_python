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
import random

choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors. "))
comp_choice = random.randint(0,2)

if choice == 0 and comp_choice == 1:
    print(f"You chose {rock}\nThe computer chose {paper}")
    print("You lose")
elif choice == 0 and comp_choice == 2:
    print(f"You chose {rock}\nThe computer chose {scissors}")
    print("You Win!")
elif choice == 0 and comp_choice == 0:
    print(f"You chose {rock}\nThe computer chose {rock}")
    print("Tie")
elif choice == 1 and comp_choice == 1:
    print(f"You chose {paper}\nThe computer chose {paper}")
    print("Tie")
elif choice == 1 and comp_choice == 2:
    print(f"You chose {paper}\nThe computer chose {scissors}")
    print("You lose")
elif choice == 1 and comp_choice == 0:
    print(f"You chose {paper}\nThe computer chose {rock}")
    print("You Win!")
elif choice == 2 and comp_choice == 1:
    print(f"You chose {scissors}\nThe computer chose {paper}")
    print("You win!")
elif choice == 2 and comp_choice == 2:
    print(f"You chose {scissors}\nThe computer chose {scissors}")
    print("Tie")
elif choice == 2 and comp_choice == 0:
    print(f"You chose {scissors}\nThe computer chose {rock}")
    print("You lose")