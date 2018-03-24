def ask_yes_or_no_question(question_text):
    while True:
        answer = raw_input(question_text)
        if answer == 'y' or answer == 'Y' or answer == 'yes':
        # Alternative Kurzversion:
        # if answer in ['y', 'Y', 'yes']:
            return True
        elif answer == 'n' or answer == 'N' or answer == 'no':
            return False
        else:
            print 'invalid input. Enter y or n.'


# answer1 = ask_yes_or_no_question('add another Todo item?')
# if answer1:
#     print 'You want to add a todo'

# answer2 = ask_yes_or_no_question('are you vegetarian?')
# if answer2:
#     print 'You are vegetarian'
# else:
#     print 'You are not vegetarian'