import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'King': 0, 'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10}


class Card:
    """Represents a regular playing card."""

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents the full deck of 52 playing cards."""

    def __init__(self, discard='null'):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))
        self.discard = discard

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.all_cards)

    def deal_one(self):
        """Deals out one card."""
        return self.all_cards.pop()


class Game:
    """Determines last turn"""

    def __init__(self):
        self.last_player = 0
        self.on = True

    def change_turn(self):
        self.last_player != self.last_player

class Player:
    """Represents the cards that each player has."""

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def player_action(self):
        entry = 'null'
        print("\n\033[1m" + f"{self.name}'s turn" + "\033[0m")
        while entry != 'd' and entry != 's' and entry != 'k':
            entry = input('Draw from deck (d), discard (s), or knock (k)? ')
            if entry == 'd' or entry == 's':
                if entry == 'd':
                    hand = my_deck.deal_one()  # Put a card from the deck in player's hand
                    print(f'The card is the {hand}.')
                else:
                    hand = Deck.discard  # Put the discard card in player's hand
                position = 'null'
                while position not in ['1', '2', '3', '4']:
                    position = input('Which card do you want to replace (1, 2, 3, or 4)? ')
                p = int(position)
                Deck.discard = self.swap_card(hand, p)
                show_board()
            elif entry == 'k':
                game.on = False
        game.change_turn()
``
    def swap_card(self, hand, position):
        """Swaps the card the player has been picked up
         in a given position and discards the card that was in
         that position.
         """
        Deck.discard = self.cards[position - 1]
        self.cards[position - 1] = hand
        return Deck.discard


def show_hand(player_cards):
    """Prints the cards in the given player's hand."""
    print(f'1 {player_cards[0]}')
    print(f'2 {player_cards[1]}')
    print('3 []')
    print('4 []\n')


def show_board():
    """Shows both players hands and the last discarded card."""
    print('Player 1 Cards:')
    show_hand(player_one.cards)
    print('Player 2 Cards:')
    show_hand(player_two.cards)
    print('Discard:')
    print(Deck.discard)
    print('\n')


# GAMEPLAY
playing = True
game.on = True
game = Game()
while playing:
    my_deck = Deck()
    my_deck.shuffle()

    # Setup players
    player_one = Player('Player 1', [])
    player_two = Player('Player 2', [])

    # Deal four cards to each player
    for x in list(range(0, 4)):
        player_one.cards.append(my_deck.deal_one())
        player_two.cards.append(my_deck.deal_one())

    # Deal one card into the discard pile
    Deck.discard = my_deck.deal_one()

    # Show starting hands
    show_board()

    while game.on:
        # Player action
        player_one.player_action()
        player_two.player_action()

    # Knock has occurred - player one takes one more turn if player two went last
    if game.last_player == 0:
        player_one.player_action()

    # Show all cards
    print('\nPlayer 1 Cards:')
    for card in [1, 2, 3, 4]:
        print(f'{card} {player_one.cards[card-1]}')
    print('\nPlayer 2 Cards:')
    for card in [1, 2, 3, 4]:
        print(f'{card} {player_two.cards[card-1]}')

    # Player with the lowest sum wins
    player_one_sum = sum(c.value for c in player_one.cards)
    player_two_sum = sum(c.value for c in player_two.cards)
    if player_one_sum < player_two_sum:
        print('\nPlayer 1 wins!')
    if player_one_sum > player_two_sum:
        print('\nPlayer 2 wins!')
    playing = False