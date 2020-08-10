from observer_1 import Player, Observer
import random

obs = Observer()

azamat = Player('Azamat')
bagzhan = Player('Bagzhan')
medet = Player('Medet')
tima = Player('Tima')
yerasyl = Player('Yerasyl')

obs.register(azamat)
obs.register(bagzhan)
obs.register(medet)
obs.register(tima)
obs.register(yerasyl)
print("Welcome to the bingo game\n")
while(True):
    obs.dispatch()
