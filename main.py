import numpy as np
from collections import Counter

players_count = 9

#built card deck by using dictionary
deck = {2:['H','C','S','D'], 3:['H','C','S','D'], 4:['H','C','S','D'],
        5:['H','C','S','D'], 6:['H','C','S','D'], 7:['H','C','S','D'],
        8:['H','C','S','D'], 9:['H','C','S','D'], 10:['H','C','S','D'],
        11:['H','C','S','D'], 12:['H','C','S','D'], 13:['H','C','S','D'],
        14:['H','C','S','D']}

def drawing_process():
    #defines how many numbers are currently in deck
    numbers = deck.keys()

    #draw number which represent number in deck
    def random_number():
        return np.random.randint(2, len(numbers)+2)

    #try to draw figure
    chosen_number = None
    while chosen_number is None:
        try:
            chosen_number = random_number()
        except Exception:
            print(Exception)

    numbers_length = len(deck.get(chosen_number))

    def random_color():
        return np.random.randint(0, numbers_length)

    #try to draw color
    drawn_color = None
    while drawn_color is None:
        try:
            drawn_color = random_color()
        except Exception:
            print(Exception)

    chosen_color = deck.get(chosen_number)[drawn_color]
    deck[chosen_number].remove(chosen_color)

    return [chosen_number, chosen_color]



#convert numbers to correct card figures (J,Q,K,A)
def change_figures(list_cards):
    new_list_cards = list_cards
    for list in new_list_cards:
        for num, element in enumerate(list):
            if element == "11":
                list[num] = "J"
            if element == "12":
                list[num] = "Q"
            if element == "13":
                list[num] = "K"
            if element == "14":
                list[num] = "A"
    return


class Player(object):
    def __init__(self, cards):
        self.cards = [drawing_process(), drawing_process()]

players = []

#draw all players and board cards
for i in range(players_count):
    players.append(Player(i))

board = [drawing_process(), drawing_process(), drawing_process(), drawing_process(), drawing_process()]

def evaluate_cards(player_cards):
    board_and_player = board + player_cards
    board_and_player.sort(key=lambda x: x[0], reverse=True)
    bap_zip = list(zip(*board_and_player))



    figures = list(bap_zip[0])
    colors = list(bap_zip[1])

    final_result = []

    def fig_freq():
        return Counter(figures)

    def col_freq():
        return Counter(colors)

    def straight():
        low_straight = [2,3,4,5,14]
        for i in range(3):
            if figures[i] == figures[i+4]+4:
                return [5, figures[i:i+5], figures, sum(figures[i:i+5])]

    def three_of_a_kind():
        three_of_a_kind_check = [key for (key, value) in fig_freq().items() if value == 3]
        if len(three_of_a_kind_check) == 1:
            return [4, three_of_a_kind_check[0], figures[:5], sum(figures[:5])]
        elif len(three_of_a_kind_check) == 2:
            return [4, three_of_a_kind_check[0], figures[:5], sum(figures[:5])]

    def two_pairs():
        two_pairs_check = [key for (key, value) in fig_freq().items() if value == 2]
        if len(two_pairs_check) == 2:
            return [3, [two_pairs_check[0],two_pairs_check[1]], figures[:5]]
        elif len(two_pairs_check) == 3:
            return [3, [two_pairs_check[0],two_pairs_check[1],two_pairs_check[2]], figures[:5], sum(figures[:5])]

    def one_pair():
        one_pair_check = [key for (key, value) in fig_freq().items() if value == 2]
        if len(one_pair_check) == 1:
            return [2,one_pair_check[0], figures[:5],sum(figures[:5])]

    def high_card():
        return [1, figures, figures[:5], sum(figures[:5])]

    print(straight())
    print(three_of_a_kind())
    print(two_pairs())
    print(one_pair())
    print(high_card())
    print(col_freq())
    return board_and_player


for i in range(players_count):
    print(evaluate_cards(players[i].cards))












print("Player 1: "+ str(players[0].cards)) # str(player_one))
print("Player 2: "+ str(players[1].cards))
print("Board: FLOP = " + str(board[0:3])+", TURN = " + str(board[3:4]) + ", RIVER = " + str(board[4:5]))


# if __name__ == '__main__':
#     main()


print("result")