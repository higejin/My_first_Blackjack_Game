
import random

card = ['sA', 's2','s3','s4','s5','s6','s7','s8','s9','s10','sJ','sQ','sK',
        'hA', 'h2','h3','h4','h5','h6','h7','h8','h9','h10','hJ','hQ','hK',
        'cA', 'c2','c3','c4','c5','c6','c7','c8','c9','c10','cJ','cQ','cK',
        'dA', 'd2','d3','d4','d5','d6','d7','d8','d9','d10','dJ','dQ','dK']
num = {'sA':1,'s2':2,'s3':3,'s4':4,'s5':5,'s6':6,'s7':7,'s8':8,'s9':9,'s10':10,'sJ':10,'sQ':10,'sK':10,
       'hA':1,'h2':2,'h3':3,'h4':4,'h5':5,'h6':6,'h7':7,'h8':8,'h9':9,'h10':10,'hJ':10,'hQ':10,'hK':10,
       'cA':1,'c2':2,'c3':3,'c4':4,'c5':5,'c6':6,'c7':7,'c8':8,'c9':9,'c10':10,'cJ':10,'cQ':10,'cK':10,
       'dA':1,'d2':2,'d3':3,'d4':4,'d5':5,'d6':6,'d7':7,'d8':8,'d9':9,'d10':10,'dJ':10,'dQ':10,'dK':10,}

class Player(object):

    def __init__(self,bankroll=100):
        self.bankroll = bankroll
        self.hand = []

    def check_bankroll(self):
        print("Your bankroll is : " + str(player1.bankroll))

    def add_bankroll(self,amount):
        self.bankroll += amount

    def bet(self):
        while True:
            self.betAmount = int(input("How much do you bet? : "))
            if self.betAmount > self.bankroll:
                print("Over betting.")
                continue
            else:
                print("You are now betting " + str(self.betAmount))
                break

    def show_hand(self):
        print("Player's hand : ", end = "")
        for mycard in self.hand:
            print(mycard + "  ", end = "")

        print(" (" + self.check_hand() + ")")

    def check_hand(self):
        x = 0
        includeA = False

        for i in self.hand:
            if i == ('sA' or 'hA' or 'cA' or 'dA'):
                includeA = True
            x += num[i]

        if includeA == True and x < 12:
            x += 10

        if x > 21:
            return 'Bust!'

        elif len(self.hand) == 2 and x == 21:
            return 'Natural 21!'

        else:
            return str(x)

class Dealer(object):
    def __init__(self):
        self.hand = []

    def show_firsthand(self):
        print("Dealer's hand : " + self.hand[0] + " + Hole card.")

    def show_hand(self):
        print("Dealer's hand : ", end ="")
        for mycard in self.hand:
            print(mycard + "  ", end ="")

        print(" (" + str(self.check_hand()) + ")")

    def check_hand(self):
        x = 0
        includeA = False

        for i in self.hand:
            if i == ('sA' or 'hA' or 'cA' or 'dA'):
                includeA = True
            x += num[i]

        if includeA and x < 12:
            x += 10

        if x > 21:
            return 'Bust!'

        elif len(self.hand) == 2 and x == 21:
            return 'Natural 21!'

        else:
            return x

class Decks(object):

    def __init__(self, numberOfDecks = 1):
        self.numberOfDecks = numberOfDecks
        self.card = ['sA', 's2','s3','s4','s5','s6','s7','s8','s9','s10','sJ','sQ','sK',
                     'hA', 'h2','h3','h4','h5','h6','h7','h8','h9','h10','hJ','hQ','hK',
                     'cA', 'c2','c3','c4','c5','c6','c7','c8','c9','c10','cJ','cQ','cK',
                     'dA', 'd2','d3','d4','d5','d6','d7','d8','d9','d10','dJ','dQ','dK']

    def random_pic(self):
        while True:

            try:
                selectedCard = random.choice(self.card)

            except:
                print("there is no card.")
                exit()
            else:
                self.card.remove(selectedCard)
                return selectedCard



new_deck = Decks()
player1 = Player(bankroll=1000)
dealer = Dealer()

def deal_cards(player):
    player.hand.clear()
    player.hand.append(new_deck.random_pic())
    player.hand.append(new_deck.random_pic())

def hit_cards(player):
    player.hand.append(new_deck.random_pic())

def determine_outcome(p,d):
    if p.check_hand() == 'Bust!':
        print('You lose!')
        p.add_bankroll(-(p.betAmount))

    elif p.check_hand() == 'Natural 21!':
        if d.check_hand() == 'Natural 21!':
            print('push')
        else:
            print('You win!')
            p.add_bankroll(p.betAmount)
    else:
        if d.check_hand() == 'Natural 21!':
            print('You lose!')
            p.add_bankroll(-(p.betAmount))
        elif d.check_hand() == 'Bust!':
            print('You win!')
            p.add_bankroll(p.betAmount)
        elif d.check_hand() == int(p.check_hand()):
            print('push')
        elif int(d.check_hand()) > int(p.check_hand()):
            print('You lose!')
            p.add_bankroll(-(p.betAmount))
        else:
            print('You win!')
            p.add_bankroll(p.betAmount)
    print(" ")

def replay():

    return input('Do you want to continue? Enter Yes or No: ').lower().startswith('y')


while True:

    player1.check_bankroll()
    player1.bet()

    deal_cards(dealer)
    dealer.show_firsthand()

    deal_cards(player1)
    player1.show_hand()

    sel = input("Please select: 'hit' or 'stand' or 'double down' or 'surrender'.").lower()
    print(" ")
    if sel.startswith('su'):
        player1.add_bankroll(-(player1.betAmount)//2)
        if replay():
            continue
        else:
            break
    elif sel.startswith('h'):
        hit_cards(player1)
        dealer.show_firsthand()
        player1.show_hand()
        while player1.check_hand() != 'Bust!':
            print(" ")
            if input("Hit again? Enter Y/N : ").lower().startswith('y'):
                hit_cards(player1)
                dealer.show_firsthand()
                player1.show_hand()
            else:
                break
    elif sel.startswith('d'):
        player1.betAmount *= 2
        print("You are now betting " + str(player1.betAmount))
        hit_cards(player1)
        dealer.show_firsthand()
        player1.show_hand()
        while player1.check_hand() != 'Bust!':
            print(" ")
            if input("Hit again? Enter Y/N : ").lower().startswith('y'):
                hit_cards(player1)
                dealer.show_firsthand()
                player1.show_hand()
            else:
                break
    else:
        pass

    print(" ")
    print("open dealer's hole card.")
    print(" ")

    dealer.show_hand()
    player1.show_hand()

    while True:
        print(" ")
        if dealer.check_hand() == 'Bust!':
            break
        elif dealer.check_hand() == 'Natural 21!':
            break
        elif dealer.check_hand() > 16:
            break
        else:
            hit_cards(dealer)
            dealer.show_hand()
            player1.show_hand()

    print(" ")
    determine_outcome(player1,dealer)
    if replay():
        continue
    else:
        break
