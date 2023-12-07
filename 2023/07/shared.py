HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIR = 3
THREE_OF_A_KIND = 4
FULL_HOUSE = 5
FOUR_OF_A_KIND = 6
FIVE_OF_A_KIND = 7
def evaluate_hand(hand):
    ranks = {k:hand.count(k) for k in hand}
    if max(ranks.values()) == 1:
        return HIGH_CARD
    values = list(ranks.values())
    assert sum(values) == 5
    if max(values) == 2:
        return HIGH_CARD + values.count(2)
    if max(values) == 3:
        return THREE_OF_A_KIND + values.count(2)
    if max(values) == 4:
        return FOUR_OF_A_KIND
    return FIVE_OF_A_KIND

def parse_games(fn):
    games = []

    for line in open(fn, 'r'):
        hand, bid = line.split(' ')
        bid = int(bid)
        games.append((hand, bid))
    return games


