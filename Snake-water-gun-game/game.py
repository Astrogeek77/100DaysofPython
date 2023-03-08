'''


P C 0 1 2
0   D W L
1   L D W
2   W L D

D -> 2
L -> 0
W -> 1

Snake Water Gun in python
'''

import random

print('-' * 50)
print("  Snake Water Gun Game  ".center(50, "*"))
print('-' * 50)

game_mat = [[2, 1, 0], [0, 2, 1], [1, 0, 2]]  # O-> Loss; 1 -> Win; 2 -> Draw
user_score = 0
computer_score = 0
drawn_games = 0


def quit_game():
    if (computer_score > user_score):
        print("Mr. Computer won the game.")
    elif (computer_score < user_score):
        print("You won the game.")
    else:
        print("The game is drawn.")
    print("quiting game...")


def game_result():
    return game_mat[computer_option][user_option]


# def print_result(result, computer_score, user_score):
#     pass


# def print_score(computer_score, user_score):


while True:
    computer_option = random.randint(0, 2)
    possible_choice = ["Snake", "Water", "Gun"]

    print('\nChoose options : \n 1 for Snake\n 2 for Water \n 3 for Gun\n 0 for quit\n')

    user_input = input("Enter your option: ")

    if user_input in ['Quit', 'quit', 'exit', "QUIT", '0']:
        quit_game()
        break
    elif user_input in ['Snake', 'snake', '1']:
        user_option = 0
    elif user_input in ['Water', 'water', '2']:
        user_option = 1
    elif user_input in ['Gun', 'gun', '3']:

        user_option = 2
    else:
        print("Please provide a valid option to play the game. :)")
        continue

    result = game_result()
    print(f"\nYou chose {possible_choice[user_option]}")
    print(f"\nMr. Computer chose {possible_choice[computer_option]}")

    match result:
        case 2:
            print("\nRound is drawn.")
            drawn_games += 1
        case 1:
            print("\nMr. Computer won the round.")
            computer_score += 1
        case 0:
            print("\nYou won the round.")
            user_score += 1

    print(
        f"\nComputer score: {computer_score} User score: {user_score} Drawn games: {drawn_games}")
    # q = input("\n\nWant to play again? (Y/N) \n")
    # if q in ['Y', 'y', 'yes', 'Yes', '1']:
    #     pass
    # else:
    #     print("\nThank you for playing this game ...")
    #     break
