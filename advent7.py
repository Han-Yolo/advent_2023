from functools import cmp_to_key

# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
#
# hands = []
# with open("advent7.data", "r") as file:
#     for line in file:
#         parts = line.split(" ")
#         counts = sorted([parts[0].count(card) for card in cards], reverse=True)
#         hand_type = 0
#         if counts[0] == 5:
#             hand_type = 6
#         elif counts[0] == 4:
#             hand_type = 5
#         elif counts[0] == 3 and counts[1] == 2:
#             hand_type = 4
#         elif counts[0] == 3:
#             hand_type = 3
#         elif counts[0] == 2 and counts[1] == 2:
#             hand_type = 2
#         elif counts[0] == 2:
#             hand_type = 1
#         hands.append((parts[0], int(parts[1]), hand_type))


# def cmp(h1, h2):
#     if h1[2] != h2[2]:
#         return h1[2] - h2[2]
#     for i in range(len(h1[0])):
#         if h1[0][i] != h2[0][i]:
#             return cards.index(h1[0][i]) - cards.index(h2[0][i])
#     return 0


# win = [hand[1] * (i + 1) for i, hand in enumerate(sorted(hands, key=cmp_to_key(cmp)))]
# print(sum(win))


cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

hands = []
with open("advent7.data", "r") as file:
    for line in file:
        parts = line.split(" ")
        jocker = 0
        counts = []
        for card in cards:
            count = parts[0].count(card)
            if card == "J":
                jocker = count
            else:
                counts.append(count)
        counts.sort(reverse=True)
        counts[0] += jocker
        hand_type = 0
        if counts[0] == 5:
            hand_type = 6
        elif counts[0] == 4:
            hand_type = 5
        elif counts[0] == 3 and counts[1] == 2:
            hand_type = 4
        elif counts[0] == 3:
            hand_type = 3
        elif counts[0] == 2 and counts[1] == 2:
            hand_type = 2
        elif counts[0] == 2:
            hand_type = 1
        hands.append((parts[0], int(parts[1]), hand_type))


def cmp(h1, h2):
    if h1[2] != h2[2]:
        return h1[2] - h2[2]
    for i in range(len(h1[0])):
        if h1[0][i] != h2[0][i]:
            return cards.index(h1[0][i]) - cards.index(h2[0][i])
    return 0


win = [hand[1] * (i + 1) for i, hand in enumerate(sorted(hands, key=cmp_to_key(cmp)))]
print(sum(win))
