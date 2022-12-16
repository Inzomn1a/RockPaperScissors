import random

rock_art = '''
    _______
---'   ____)
      (_____)
      (_____) Rock
      (____)
---.__(___)
'''

paper_art = '''
    _______
---'   ____)____
          ______)
          _______) Paper
         _______)
---.__________)
'''

scissors_art = '''
    _______
---'   ____)____
          ______)
       __________) Scissors
      (____)
---.__(___)
'''

player_score = 0
computer_score = 0

while 0 != 1:
    #player chosses rock paper or Scissors
    player_choice = int(input("Rock(1), Paper(2), Scissors(3)?: "))
    if player_choice == 1:
        print(rock_art)
    elif player_choice == 2:
        print(paper_art)
    elif player_choice == 3:
        print(scissors_art)
    else: #exit program if anything but 1,2 or 3 is entered
        print("Exit Program")
        exit()
        

    #computer randomly picks one
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        print(rock_art)
    elif computer_choice == 2:
        print(paper_art)
    else:
        print(scissors_art)

    #PLAYER LOOSE CONDITIONS
    # #Paper beats Rock
    if player_choice == 1 and computer_choice == 2:
        computer_score += 1
        print("You loose.")
        print(f"Current Score: You:{player_score} Com:{computer_score}")

    #Scissors beats Paper
    elif player_choice == 2 and computer_choice == 3:
        computer_score += 1
        print("You loose.")
        print(f"Current Score: You:{player_score} Com:{computer_score}")

    #Rock beats Scissors
    elif player_choice == 3 and computer_choice == 1:
        computer_score += 1
        print("You loose.")
        print(f"Current Score: You:{player_score} Com:{computer_score}")

    #PLAYER WIN CONDITIONS
    #Paper beats Rock
    elif player_choice == 2 and computer_choice == 1:
        player_score += 1
        print("You win.")
        print(f"Current Score: You:{player_score} Com:{computer_score}")

    #Scissors beats Paper
    elif player_choice == 3 and computer_choice == 2:
        player_score += 1
        print("You win.")
        print(f"Current Score: You:{player_score} Com:{computer_score}")

    #Rock beats Scissors
    elif player_choice == 1 and computer_choice == 3:
        player_score += 1
        print("You win.")
        print(f"Current Score: You:{player_score} Com:{computer_score}")

    #Draw Condition
    else:
        print("Draw")
        print(f"Current Score: You:{player_score} Com:{computer_score}\n\n\n")