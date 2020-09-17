# rock beats scissor, scissor beats paper and paper beats rock

import random

player_moves = ["rock", "scissor", "paper"]
comp_moves = ["rock", "scissor", "paper"]

Your_Score = 0
Comp_Score = 0

while True:
    player_choice = random.choice(player_moves)
    comp_choice = random.choice(comp_moves)

    player_choice_1 = input("Enter the choice :")

    print("You Choose '{}'".format(player_choice_1))
    print("Comp Chooses '{}'".format(comp_choice))

    if player_choice_1 == "rock" and comp_choice == "scissor":
        print("You Win\nComp looses!!")
        Your_Score = Your_Score + 1
        # break

    elif player_choice_1 == "rock" and comp_choice == "paper":
        print("Comp Won\nYou loose!!")
        Comp_Score = Comp_Score + 1
        # break

    elif player_choice_1 == "scissor" and comp_choice == "paper":
        print("You Won\nComp loose!!")
        Your_Score = Your_Score + 1

    elif player_choice_1 == "scissor" and comp_choice == "rock":
        print("Com Won\nYou loose!!")
        Comp_Score = Comp_Score + 1

    elif player_choice_1 == "paper" and comp_choice == "scissor":
        print("Comp Won\nYou loose!!")
        Comp_Score = Comp_Score + 1

    elif player_choice_1 == "paper" and comp_choice == "rock":
        print("You Won\nComp loose")
        Your_Score = Your_Score + 1

    elif player_choice_1 == "rock" and comp_choice == "rock":
        print("Match Tied")

    elif player_choice_1 == "paper" and comp_choice == "paper":
        print("Match Tied")

    elif player_choice_1 == "scissor" and comp_choice == "scissor":
        print("Match Tied")

    elif player_choice_1 == "exit":
        break

    else:
        print("Some Thing Went Wrong!!")

print("You Score", Your_Score)

print("Comp Score", Comp_Score)


