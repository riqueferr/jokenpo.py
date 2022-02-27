import random
from random import *

#

# for i in range(1, 8):
#     if (i == 5):
#         continue
#     print(i)
#
# for counter_hashtag in range(1, 11):
#     print("#" * counter_hashtag)
#
# counter_hashtag = 1
#
# while counter_hashtag < 11:
#     print("#" * counter_hashtag)
#     counter_hashtag = counter_hashtag + 1


def jogar():
    list_objects = ['tesoura', 'papel', 'pedra']
    computer = randint(0, 2)
    print(f'Ops, olha a dica! Computador escolheu: {list_objects[computer]}\n')

    player = int(input("Vai: "))

    while player < 0 or player > 2:
        player = int(input("Vai, tenta de novo: "))

    if player == computer:
        print('Ora, ora! Ambos escolheram {}.'.format(list_objects[player]))
    elif player == 0:
        if computer == 1:
            print("Você escolheu {} e o computador {}. Parabéns, você ganhou!".format(list_objects[player],
                                                                                      list_objects[computer]))
        else:
            print("Você escolheu {} e o computador {}. Que pena, você perdeu!".format(list_objects[player],
                                                                                      list_objects[computer]))
    elif player == 1:
        if computer == 2:
            print("Você escolheu {} e o computador {}. Parabéns, você ganhou!".format(list_objects[player],
                                                                                      list_objects[computer]))
        else:
            print("Você escolheu {} e o computador {}. Que pena, você perdeu!".format(list_objects[player],
                                                                                      list_objects[computer]))
    elif player == 2:
        if computer == 1:
            print("Você escolheu {} e o computador {}. Parabéns, você ganhou!".format(list_objects[player],
                                                                                      list_objects[computer]))
        else:
            print("Você escolheu {} e o computador {}. Que pena, você perdeu!".format(list_objects[player],
                                                                                      list_objects[computer]))
