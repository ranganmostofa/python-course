choices = ["rock", "scissors", "paper"]  # initialize list of choices
play = True
user1_wins = 0
user2_wins = 0
round_ID = 1

while play:
    print(f" Round {round_ID}, FIGHT! ".center(40, "="))
    user1_choice = input("User 1, please choose rock, paper, or scissors: ")  # users enter choice
    user2_choice = input("User 2, please choose rock, paper, or scissors: ")

    user1 = choices.index(user1_choice) + 1  # get values for user choice (1 = rock, 2 = scissors, 3 = paper)
    user2 = choices.index(user2_choice) + 1

    # always include spaces between operators
    winner = (user2 - user1) % len(choices)  # formula based on number assignment
    if winner == 0:  # they picked the same thing
        print("No winners")
    elif winner == 1:  # user 1 picked an item that beats user 2's item
        user1_wins += 1
        print(f"{user1_choice}, user 1, beats {user2_choice}, user 2.")
    elif winner == 2:  # user 2 picked an item that beats user 1's item
        user2_wins += 2
        print(f"{user2_choice}, user 2, beats {user1_choice}, user 1.")

    # if user1_choice == user2_choice:
    #     print("No winners")
    # elif (
    #         (user1_choice == "rock" and user2_choice == "paper") or
    #         (user1_choice == "paper" and user2_choice == "scissors") or
    #         (user1_choice == "scissors" and user2_choice == "rock")
    #     ):
    #     user2_wins += 1
    #     print(f"{user2_choice}, user 2, beats {user1_choice}, user 1.")
    # else:
    #     user1_wins += 1
    #     print(f"{user1_choice}, user 1, beats, {user2_choice}, user 2.")
    print(f"Stats after round {round_ID} \n User 1 dubs: {user1_wins} \n User 2 dubs: {user2_wins}".center(40, "-"))
    replay = input("Y'all lame, would you like to play again? y/n: ")  # ask the bozos to play again

    while replay not in ["y", "n"]:
        replay = input("You illiterate fuck, would you like to play again? y/n. Just type 'y' or 'n': ")

    play = replay == "y"
    round_ID += 1

print(f"GGs \nUser 1 dubs: {user1_wins} \nUser 2 dubs: {user2_wins}")  # once game ends, print results
