from __future__ import print_function
from __future__ import unicode_literals

print('Willkommen beim Rechner')
continue_program = True
while continue_program == True:
    print('Operation (+, -, *, /):')
    operation = raw_input()
    print('erste Zahl')
    a = raw_input()
    fa = float(a)
    print('zweite Zahl')
    b = raw_input()
    fb = float(b)
    if operation == '+':
        print('Ergebnis:', fa+fb)
    elif operation == '-':
        print('Ergebnis:', fa-fb)
    elif operation == '*':
        print('Ergebnis:', fa*fb)
    elif operation == '/':
        print('Ergebnis:', fa/fb)
    else:
        print('Ungueltige Rechenoperation!')

    print('Neue Rechnung?')
    answer = raw_input()
    if answer != 'y':
        continue_program = False

print('Auf Wiedersehen!')
