#!/usr/bin/env python3
import sys
from shared import *

def cr(c):
    if c.isdigit():
        return int(c)
    assert c in 'TJQKA'
    return 10 + 'TJQKA'.index(c)

def handkey(hand):
    total = evaluate_hand(hand) * (13**5)
    for i in range(5):
        total += cr(hand[(5-1)-i]) * (13**i)
    return total

games = parse_games(sys.argv[1])
games.sort(key=lambda hb: handkey(hb[0]))
winnings = 0
for i in range(len(games)):
    hand, bid = games[i]
    winnings += (i+1) * bid
print(winnings)
