import random

valid_choices = ['rock', 'paper', 'scissors']

# create function to compute the result of the game
def compute_result(choice, computer_choice):
    if choice == computer_choice:
        return 0
    elif choice == 'rock' and computer_choice == 'scissors':
        return 1
    elif choice == 'paper' and computer_choice == 'rock':
        return 1
    elif choice == 'scissors' and computer_choice == 'paper':
        return 1
    else:
        return -1

# create function to play the game
def play_round():
    # read user choice from command line
    choice = ''
    while (choice not in valid_choices):
        choice = input('Please enter your choice (rock, paper or scissors): ')
        choice = choice.lower()
        if choice not in valid_choices:
            print('Invalid choice. Please try again.')

    # make computer choice
    computer_choice = random.choice(valid_choices)

    # print computer choice
    print('Computer choice is: ' + computer_choice)

    # check who is the winner
    roundScore = compute_result(choice, computer_choice)
    if roundScore == 0:
        print('It is a draw!')
    elif roundScore == 1:
        print('You win!')
    elif roundScore == -1:
        print('You lose!')

    return roundScore

# write Hello message to the console
print('Welcome to rock-paper-scissors game.')

# read user name from command line
name = input('Please enter your name: ')

print('Hello, ' + name + '!')
print()

gameScore = 0
rounds = 0

decision = 'Y'
while decision == 'Y':
    gameScore += play_round()
    print("Your score is: " + str(gameScore))
    rounds += 1
    decision = input("Continue Y/N ? ")

# print goodbye message
print()
print("Final score : " + str(gameScore) + " (" + str(rounds) + " rounds played).")
print('Goodbye, ' + name + '!')