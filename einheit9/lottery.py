from random import randint

def get_lottery_number():
    # random number between 1 an 45
    number = randint(1, 45)
    return number

def get_lottery_numbers(n):
    # get a list of lottery numbers without duplicates
    lottery_list = []
    for i in range(n):
        while True:
            mynumber = get_lottery_number()
            # wenn mynumber noch nicht in der liste steht, beende die Schleife
            # ansonsten, erstelle wieder eine neue Zahl
            if mynumber not in lottery_list:
                # verlasse die while-schleife
                break
        lottery_list.append(mynumber)
    return lottery_list