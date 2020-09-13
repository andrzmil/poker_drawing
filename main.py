import numpy as np
import pandas as pd
from tkinter import messagebox



#built card deck by using dictionary
deck = {'H':[2,3,4,5,6,7,8,9,10,11,12,13,14], 'C':[2,3,4,5,6,7,8,9,10,11,12,13,14],
        'D':[2,3,4,5,6,7,8,9,10,11,12,13,14], 'S':[2,3,4,5,6,7,8,9,10,11,12,13,14]}

def drawing_process():
    colors = deck.keys()

    def random_color():
        return np.random.randint(1, len(colors)+1)

    chosen_color = list(colors)[random_color()-1]
    numbers_length = len(deck.get(chosen_color))

    def random_number():
        return np.random.randint(2, numbers_length+2)

    temp_deck_check = pd.DataFrame.from_dict(deck, orient="index")
    temp_deck_check.to_csv('check.csv', mode='a')


    chosen_number = random_number()


    deck[chosen_color].remove(chosen_number)





    return [chosen_color, chosen_number]



player_one = [drawing_process(), drawing_process()]
player_two = [drawing_process(), drawing_process()]


board = [drawing_process(), drawing_process(), drawing_process(), drawing_process(), drawing_process()]


print("Player 1: "+ str(player_one))
print("Player 2: "+ str(player_two))
print("Board: FLOP = " + str(board[0:3])+", TURN = " + str(board[3:4]) + ", RIVER = " + str(board[4:5]))
# count = 0
# for key, value in deck.items():
#     if isinstance(value, list):
#         count += len(value)


# if __name__ == '__main__':
#     main()


print("result")