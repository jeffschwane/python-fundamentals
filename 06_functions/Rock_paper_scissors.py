'''Instructions
take in a number 0-2 from the user that represents their hand
generate a random number 0-2 to use for the computer's hand
call the function get_hand to get the string representation of the user's hand
call the function get_hand to get the string representation of the computer's hand
call the function determine_winner to figure out who won
print out the player hand and computer hand
print out the winner'''

import random

def get_hand(hand):
    # gets the string representation of the user's and computer's hand
    # args: hand
    # outputs: string
    if hand == 0:
        return 'Rock'
    if hand == 1:
        return 'Paper'
    if hand == 2:
        return 'Scissors'

def determine_winner(hand_1,hand_2):
    # Determines who won the game
    # args: hand_1 (user), hand_2 (comp)
    if hand_1 == hand_2:
        return 'Tie!'
    if hand_1 == 'Rock' and hand_2 == 'Paper':
        return 'Computer wins'
    if hand_1 == 'Rock' and hand_2 == 'Scissors':
        return 'You win!'
    if hand_1 == 'Scissors' and hand_2 == 'Paper':
        return 'You win!'
    if hand_1 == 'Scissors' and hand_2 == 'Rock':
        return 'Computer wins'
    if hand_1 == 'Paper' and hand_2 == 'Rock':
        return 'You win!'
    if hand_1 == 'Paper' and hand_2 == 'Scissors':
        return 'Computer wins'


# Get user input for user hand
entry = ""
while entry not in [0, 1, 2]:
    try:
        entry = int(input('Rock (0), Paper (1) or Scissors (2): '))
    except:
        continue

#Generate computer hand
    comp = random.randint(0, 2)

#Call function get_hand to get string representation of the hands
user_hand = get_hand(entry)
comp_hand = get_hand(comp)

#Call the function determine_winner to figure out who won
winner = determine_winner(user_hand,comp_hand)

#Print out hands
print(f'Your move was {user_hand}')
print(f"The computer's move was {comp_hand}")

#Print out who won
print(winner)
