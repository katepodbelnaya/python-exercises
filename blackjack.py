import random
from IPython.display import clear_output

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)
    
    def __str__(self):
        return "\n".join(str(item) for item in self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
    
class Hand:
        
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1  

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 
            
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(users_chips):
    print("You'r have {}$".format(users_chips.total))
    while True:
        try:
            bet = int(input("What is your bet? "))
        except ValueError:
            print("Error! Try again!")
            continue
        else:
            if users_chips.total-bet>=0:
                print("Your bet is {}$".format(bet))
                users_chips.bet = bet
                break
            else:
                print("Your don't have enough money! Try again!")
                continue

def hit(deck,hand):
    
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        turn = input("Hit or Stand? H/S ")
        if turn.lower() != "h" and turn.lower() != "s":
            print("Choose H or S ")
            continue
        elif turn.lower() == "h":
            hit(deck,hand)
            break
        elif turn.lower() == "s":
            playing = False
            break
            
def show_some(player,dealer):
    clear_output()
    flag = True
    print("Dealer's hand:")
    for card in dealer.cards:
        if flag:
            print("Hidden Card ")
            flag = False
        else:
            print(card)
    print()
    print("Your hand:")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    clear_output()
    print("Dealer's hand:")
    for card in dealer.cards:
        print(card)
    print("Total value: {}".format(dealer.value))
    print()
    print("Your hand:")
    for card in player.cards:
        print(card)
    print("Total value: {}".format(player.value))
    
def player_busts(chips):
    print("You have busted!")
    chips.lose_bet()

def player_wins(chips):
    print("You win!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer have busted! You win!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer win!")
    chips.lose_bet()
    
def push(chips):
    print("Push!")
    chips.bet = 0

player_chips = Chips()
playing = True
while True:
    # Print an opening statement
    clear_output()
    print("Let's play BlackJack!")
    playing = True
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
        
    # Set up the Player's chips
    #player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            #player_busts(player_chips)
            break
            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        elif dealer_hand.value <= 17:
            hit(deck,dealer_hand)
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand,dealer_hand)
    
    # Show all cards
    show_all(player_hand,dealer_hand)
    
    # Run different winning scenarios
    if player_hand.value > 21:
        player_busts(player_chips)
    elif dealer_hand.value > 21:
        dealer_busts(player_chips)
    elif 21 - player_hand.value < 21 - dealer_hand.value:
        player_wins(player_chips)
    elif 21 - player_hand.value > 21 - dealer_hand.value:
        dealer_wins(player_chips)
    elif 21 - player_hand.value == 21 - dealer_hand.value:
        push(player_chips)
    
    # Inform Player of their chips total 
    print("Your total is {}$".format(player_chips.total))
    # Ask to play again
    while True:
        again = input("Do you want to play again? Y/N ")
        if again.lower() != "y" and again.lower() != "n":
            print("Please choose Y or N")
            continue
        else:
            break
    if again.lower() == "n":
        break
    else:
        continue
