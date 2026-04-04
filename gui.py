import FreeSimpleGUI as sg
from FreeSimpleGUI.elements import list_box

import function

label = sg.Text('Type in a todo')
input_box = sg.InputText(tooltip='Type Todo', key='todo')
add_btn = sg.Button('Add')
list_box = sg.Listbox(values=function.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_btn = sg.Button('Edit')
complete_btn = sg.Button('Complete')

window = sg.Window('My To-Do App', layout=[
    [label],
    [input_box, add_btn], [list_box, edit_btn]],
    font=('Helvetica', 20))
while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)


        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"
            print(new_todo)
            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()