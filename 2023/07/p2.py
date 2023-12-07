#!/usr/bin/env python3
import sys
from shared import *

def cr(c):
    return 'J23456789TQKA'.index(c)

def jokerspread(hand):
    if 'J' not in hand:
        return [hand]
    myspread = [hand]
    for opt in '23456789TQKA':
        myspread += jokerspread(hand.replace('J', opt, 1))
    return myspread

def handkey(hand):
    evaluated = max([evaluate_hand(h) for h in jokerspread(hand)])
    total = evaluated * (14**5)
    for i in range(5):
        total += cr(hand[(5-1)-i]) * (14**i)
    return total


games = parse_games(sys.argv[1])
games.sort(key=lambda hb: handkey(hb[0]))
winnings = 0
for i in range(len(games)):
    hand, bid = games[i]
    winnings += (i+1) * bid
print(winnings)
