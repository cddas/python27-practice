def rock_paper_scissors(choice_1, choice_2):
    if choice_1.lower() == choice_2.lower():
        print("It's a tie")
    elif choice_1.lower() == "rock":
        if choice_2.lower == "scissors":
            print("player 1 wins")
        else:
            print("player 2 wins")
    elif choice_1.lower() == "scissors":
        if choice_2.lower() == "paper":
            print("player 1 wins")
        else:
            print("player 2 wins")
    elif choice_1.lower() == "paper":
        if choice_2.lower() == "rock":
            print("player 1 wins")
        else:
            print("player 2 wins")
    else:
        print("Provide a valid entry \n")


def rock_paper_scissors_v2(choice_1, choice_2):
    game_dict = {"rock": 1, "scissors": 2, "paper": 3}
    player_1_game = game_dict.get(choice_1)
    player_2_game = game_dict.get(choice_2)
    dif = player_1_game - player_2_game

    if dif in [-1, 2]:
        print("Player 1 wins")
    elif dif in [-2, 1]:
        print("Player 2 wins")
    else:
        print("Provide a valid entry \n")


continue_play = "y"
while continue_play.lower() == 'y':
    choice_player1 = raw_input("Player 1's choice - Select from Rock/Paper/Scissors : ")
    choice_player2 = raw_input("Player 2's choice - Select from Rock/Paper/Scissors : ")

    # replace the following function with rock_paper_scissors for another approach
    rock_paper_scissors_v2(choice_1=choice_player1, choice_2=choice_player2)
    continue_play = raw_input("Enter Y to continue playing. Enter any other key to exit : \n")
