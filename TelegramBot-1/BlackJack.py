deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

import random

random.shuffle(deck)

print("Let's start our game")
count = 0

while True:
    choice = input('Do u want to get a card? y/n\n')
    if choice == 'y':
        currrent = deck.pop()
        print('Вам попалась карта достоинством %d' % currrent)
        count += currrent
        if count > 21:
            print('You lose')
            break
        elif count == 21:
            print('Congrats! You win!')
            break
        else:
            print('You have %d point' % count)
    elif choice == 'n':
        print('You have %d points and you end game' % count)
        break
