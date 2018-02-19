
import random

suits = ['h', 's', 'c', 'd']
ranking = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def grab_rank(self):
        return self.rank

    def draw(self):
        print(self.suit + self.rank, end="")


class Hand:

    def __init__(self):
        self.hand = []
        self.value = 0
        self.includeAce = False

    def card_add(self, card):
        self.hand.append(card)

        # Check for Aces (Ace can also be 11)
        if card.rank == 'A':
            self.includeAce = True

        self.value += card_val[card.rank]

    def calc_val(self):
        # Calculate the value of the hand, make aces an 11 if they don't bust the hand
        if self.includeAce == True and self.value < 12:
            return self.value + 10
        else:
            return self.value

    def show_hand(self, man = 'You', hidden = False):
        print(man + " : ", end="")
        # Hole card is dealer's card which is hidden first
        if hidden == True:
            self.hand[0].draw()
            print(" + Hole card")
        else:
            for x in range(0, len(self.hand)):
                self.hand[x].draw()
                print(" ", end="")
            print("  (" + str(self.calc_val()) + ") ")

class Decks:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Player:

    def __init__(self, bankroll = 100):
        self.bankroll = bankroll

    def check_bankroll(self):
        print("Your bankroll is now : " + str(player1.bankroll))

    def add_bankroll(self, amount):
        self.bankroll += amount

    def make_bet(self):
        self.bet = 0
        while self.bet == 0:
            bet_amount = int(input("How much do you bet? : "))
            if bet_amount > self.bankroll:
                print("Invalid bet, you only have " + str(self.bankroll) + " remaining")
            elif bet_amount < minimum_bet:
                print("Invalid bet, minimum bet is " + str(minimum_bet))
            else:
                self.bet = bet_amount


minimum_bet = 10
player1 = Player(bankroll=1000)


def determine_outcome(p_hand,d_hand,p):
    print("")
    if p_hand.calc_val() > 21:
        print('Busted! You lose!')
        p.add_bankroll(-(p.bet))
    elif p_hand.calc_val() == 21 and len(p_hand.hand) == 2:
        if d_hand.calc_val() == 21 and len(d_hand.hand) == 2:
            print('Both Natural Blackjack!! push!!')
        else:
            print('Natural Blackjack! You win!')
            p.add_bankroll(p.bet)
    else:
        if d_hand.calc_val() == 21 and len(d_hand.hand) == 2:
            print('Dealer got Natural Blackjack! You lose!')
            p.add_bankroll(-(p.bet))
        elif d_hand.calc_val() > 21:
            print('Dealer busts! You win!')
            p.add_bankroll(p.bet)
        elif p_hand.calc_val() == d_hand.calc_val():
            print('Tied up, push!')
        elif p_hand.calc_val() < d_hand.calc_val():
            print('You lose!')
            p.add_bankroll(-(p.bet))
        else:
            print('You win!')
            p.add_bankroll(p.bet)
    print("")

def replay():
    x = input('Do you want to continue? Enter Yes or No: ').lower().startswith('y')
    print("")
    return x


while True:

    deck = Decks()
    deck.shuffle()
    deck.shuffle()
    deck.shuffle()

    player1.check_bankroll()
    player1.make_bet()

    # Set up or Clear both player and dealer hands
    player1_hand = Hand()
    dealer_hand = Hand()

    # First deal
    player1_hand.card_add(deck.deal())
    player1_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    print("")
    player1_hand.show_hand('You   ')
    dealer_hand.show_hand('Dealer', hidden=True)
    print("")

    while True:
        select = input("Please Enter ('h' to hit / 'st' to stand / 'd' to double down / 'su' to surrender) : ").lower()
        if select.startswith('d') and player1.bet * 2 > player1.bankroll:
            print("You are betting now " + str(player1.bet))
            print("and you only have " + str(player1.bankroll) + " now, so you can't double down.")
        else:
            break
    print("")

    # Surrender: fold hand and receive half of bet back
    if select.startswith('su'):
        player1.add_bankroll(-(player1.bet)//2)
        print("You surrendered.")
        print("")
        if replay():
            continue
        else:
            print("Your final bankroll is " + str(player1.bankroll))
            print("Good bye!")
            break

    # Hit: ask another card (you can do repeatedly until you bust)
    elif select.startswith('h'):
        player1_hand.card_add(deck.deal())
        player1_hand.show_hand('You   ')
        dealer_hand.show_hand('Dealer', hidden=True)
        while player1_hand.calc_val() <= 21:
            print("")
            if input("Hit again? Enter Y/N : ").lower().startswith('y'):
                player1_hand.card_add(deck.deal())
                print("")
                player1_hand.show_hand('You   ')
                dealer_hand.show_hand('Dealer', hidden=True)
            else:
                break

    # Double down: double your bet and must hit once and you can hit only one time
    elif select.startswith('d'):
        player1.bet *= 2
        print("You are now betting " + str(player1.bet))
        player1_hand.card_add(deck.deal())
        player1_hand.show_hand('You   ')
        dealer_hand.show_hand('Dealer', hidden=True)

    # Stand: hold hand and end turn
    else:
        pass


    print("")
    player1_hand.show_hand('You   ')
    dealer_hand.show_hand('Dealer', hidden=False)

    # Soft 17 rule: the dealer must hit until the cards total 17 or more points
    while dealer_hand.calc_val() < 17:
        dealer_hand.card_add(deck.deal())
        print("")
        player1_hand.show_hand('You   ')
        dealer_hand.show_hand('Dealer', hidden=False)

    determine_outcome(player1_hand, dealer_hand, player1)

    if replay():
        continue
    else:
        print("Your final bankroll is " + str(player1.bankroll))
        print("Good bye!")
        break
