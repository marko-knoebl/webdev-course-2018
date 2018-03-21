from __future__ import print_function

from random import randint

secret_number = randint(1, 10)
continue_program = True

while continue_program:
    print('enter a number')
    guess = raw_input()

    guess_int = int(guess)

    if guess_int == secret_number:
        print('correct!')
        continue_program = False
    elif guess_int < secret_number:
        print('wrong - too small')
    else:
        print('wrong - too big')
        