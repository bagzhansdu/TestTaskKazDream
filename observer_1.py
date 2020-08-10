import random
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.numbers = random.sample(range(1,99),5)
    def update(self, number):
        if(number in self.numbers):
            self.numbers.remove(number)
            if(len(self.numbers)==0):
                print('{} BINGO!!!'.format(self.name))
                sys.exit()
                
class Observer:
    def __init__(self):
        self.players = set()
        self.numbers = list(range(1,100))
    def register(self,who):
        self.players.add(who)
    def dispatch(self):
        number = random.choice([x for x in range(99) if x in self.numbers])
        self.numbers.remove(number)
        print("We got number:"+str(number)+"\n")
        for player in self.players:
            player.update(number)

        
