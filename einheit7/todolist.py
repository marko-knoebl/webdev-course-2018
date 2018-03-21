# -*- coding: utf-8 -*-

print 'Welcome to the todolist app'

todos = ['Einkaufen', 'Waesche waschen', 'Gartenarbeit']

todos[1] = 'relaxen'

print todos

print todos[0]

print len(todos)

# index = 0
# while index < len(todos):
#     print todos[index]
#     index = index + 1

for todo in todos:
    print todo

add_todo = True

while add_todo:
    answer = raw_input('continue?')
    if answer != 'y':
        add_todo = False
    else:
        new_todo = raw_input('enter new todo: ')
        todos.append(new_todo)

print 'TODOS:'
for todo in todos:
    print '* ' + todo

todo_file = open("todo.txt", "w+")

for todo in todos:
    todo_file.write(todo + '\n')

todo_file.close()