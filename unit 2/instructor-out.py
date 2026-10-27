def vending_machine():
    while True:
        choice = input("Enter a vending machine number (or 'q' to quit): ").upper()

        if choice == "Q":
            print("Thank you for using the vending machine!")
            break
        elif choice == "B3":
            print("Dispensing Nacho Chips")
        elif choice == "G4":
            print("Dispensing BBQ Chips")
        elif choice == "G7":
            print("Dispensing Plain Chips")
        elif choice == "D3":
            print("Dispensing Water")
        elif choice == "G5":
            print("Dispensing Cola Soda")
        else:
        
(10 points!")
else:
score -= 5
                print("You lost 5 points!")import random

def dice_rolling_game():
    score = 0

    while True:
        choice = input("Enter 'r' to roll or 'q' to quit: ").lower()

        if choice == "q":
            print("Game over!")
            print("Your final score is:", score)
            break

        elif choice == "r":
            roll = random.randint(1, 7)
            print("You rolled a", roll)

            if roll == 7:
                score += 10
                print("You win! You earned 

            print("Your current score is:", score)

        else:
            print("Invalid choice. Enter 'r' or 'q'.")

dice_rolling_game()

 


import random

def rock_paper_scissors():
    player_score = 0
    cpu_score = 0
    rounds = 0

    choices = ["rock", "paper", "scissors"]

    while rounds < 3:
        player = input("Enter r for rock, p for paper, s for scissors, or q to quit: ").lower()

        if player == "q":
            break

        elif player not in ["r", "p", "s"]:
            print("Invalid choice. Try again.")
            continue

        if player == "r":
            player_choice = "rock"
        elif player == "p":
            player_choice = "paper"
        else:
            player_choice = "scissors"

        cpu_choice = choices[random.randint(0, 2)]

        print("You chose:", player_choice)
        print("Computer chose:", cpu_choice)

        if player_choice == cpu_choice:
            print("It's a tie!")

        elif (
            (player_choice == "rock" and cpu_choice == "scissors")
            or (player_choice == "paper" and cpu_choice == "rock")
            or (player_choice == "scissors" and cpu_choice == "paper")
        ):
            print("You win this round!")
            player_score += 1

        else:
            print("The computer wins this round!")
            cpu_score += 1

        rounds += 1
        print("Your score:", player_score)
        print("Computer score:", cpu_score)
        print()

    print("Game over!")
    print("Final player score:", player_score)
    print("Final computer score:", cpu_score)

rock_paper_scissors()
