
from collections import Counter

def convert_hand(hand):
    card_value = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 1,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    
    return [card_value[card] for card in hand]

file = open('day7/input.txt')
hands = []

five_kind = []
four_kind = []
full_kind = []
three_kind = []
two_two_kind = []
two_kind = []
one_kind = []

ordered_hands = [five_kind,four_kind,full_kind,three_kind,two_two_kind,two_kind,one_kind]
ordered_hands = ordered_hands[::-1]


for index,line in enumerate(file):
    hands.append(line.split())
    hands[index][0] = convert_hand(hands[index][0])

for hand in hands:

    j_amount = hand[0].count(1)

    counts = Counter(hand[0])

    unique_counts = set(counts.values())

    print(hand[0], counts, unique_counts)

    if 5 in unique_counts: # five of a kind ???
        index_to_append = 7

    elif 4 in unique_counts: # poker 
        if j_amount == 1:
            index_to_append = 7
        elif j_amount == 4: 
            index_to_append = 7
        else:    
            index_to_append = 6 # poker 
    
    elif 3 in unique_counts and 2 in unique_counts: # full house
        if j_amount == 3 or j_amount == 2:
            index_to_append = 7 # five of a kind
        else:    
            index_to_append = 5 # full house

    elif 3 in unique_counts: # triple
        if j_amount == 1 or j_amount == 3:
            index_to_append = 6 
        else:
            index_to_append = 4

    elif 2 in unique_counts and len(counts) == 3:  # double couple
        if j_amount == 1:
            index_to_append = 5  # full house
        elif j_amount == 2: # poker 
            index_to_append = 6
        else: 
            index_to_append = 3 # double couple

    elif 2 in unique_counts : # couple
        if j_amount == 1:
            index_to_append = 4 # triple
        elif j_amount == 2:
            index_to_append = 4 # triple
        else:
            index_to_append = 2  # couple
    else: # nothing 
        if j_amount == 1:
            index_to_append = 2  # couple
        else:
            index_to_append = 1  # lone

    ordered_hands[index_to_append - 1].append(hand)

hands = ordered_hands

one_kind.sort()
two_kind.sort()
two_two_kind.sort()
three_kind.sort()

full_kind.sort()
four_kind.sort()
five_kind.sort()


counter = 0
total_sum = 0 

print('--- sorted list ---')

for kind in hands:
    for hand in kind:
        counter += 1
        total_sum += int(hand[1]) * counter 
        print(hand[0],hand[1],total_sum, counter) 

print(counter)
print(total_sum)

file.close()
