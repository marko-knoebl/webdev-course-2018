from yesorno import ask_yes_or_no_question

print 'Welcome to the todolist app'

# alte Datenstruktur
# todos = ['Einkaufen', 'Waesche']

todos = {
    'Einkaufen': True,
    'Waesche waschen': False
}

# Moegliche alternative Datenstruktur: liste von dictionaries
# todos = [
#     {'description': 'Einkaufen', 'done': True, 'priority': 2},
#     {'description': 'Waesche', 'done': False, 'priority': 3}
# ]

while True:
    answer = ask_yes_or_no_question('Add todo?')
    if answer:
        new_todo = raw_input('enter new todo: ')
        todos[new_todo] = False
    else:
        break

print todos