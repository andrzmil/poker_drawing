import numpy as np

#built card deck by using dictionary
deck = {'2':['H','C','S','D'], '3':['H','C','S','D'], '4':['H','C','S','D'],
        '5':['H','C','S','D'], '6':['H','C','S','D'], '7':['H','C','S','D'],
        '8':['H','C','S','D'], '9':['H','C','S','D'], '10':['H','C','S','D'],
        '11':['H','C','S','D'], '12':['H','C','S','D'], '13':['H','C','S','D'],
        '14':['H','C','S','D']}

def drawing_process():
    #defines how many numbers are currently in deck
    numbers = deck.keys()

    #draw number which represent number in deck
    def random_number():
        return str(np.random.randint(2, len(numbers)+2))

    chosen_number = random_number()
    numbers_length = len(deck.get(chosen_number))

    def random_color():
        return np.random.randint(0, numbers_length)

    chosen_color = deck.get(chosen_number)[random_color()]
    deck[str(chosen_number)].remove(chosen_color)

    return [chosen_number, chosen_color]

#convert numbers to correct card figures (J,Q,K,A)


#draw player and board cards
player_one = [drawing_process(), drawing_process()]
player_two = [drawing_process(), drawing_process()]
board = [drawing_process(), drawing_process(), drawing_process(), drawing_process(), drawing_process()]

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

print("Player 1: "+ str(change_figures(player_one))) # str(player_one))
print("Player 2: "+ str(change_figures(player_two)))
print("Board: FLOP = " + str(change_figures(board[0:3]))+", TURN = " + str(change_figures(board[3:4])) + ", RIVER = " + str(change_figures(board[4:5])))


# if __name__ == '__main__':
#     main()


print("result")