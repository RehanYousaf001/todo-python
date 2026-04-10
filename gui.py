import function
import FreeSimpleGUI as sg
import time

sg.theme('DarkBlue')
clock = sg.Text('', key='clock')
todos = function.get_todos()
label = sg.Text('Type in a todo')
input_box = sg.InputText(tooltip='Type Todo', key='todo')
add_btn = sg.Button(size=3, image_source='add.png', mouseover_colors='LightBlue2', tooltip='Add Todo', key='Add')
list_box = sg.Listbox(values=function.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_btn = sg.Button('Edit')
complete_btn = sg.Button(size=3, image_source='complete.png', mouseover_colors='LightBlue2', tooltip='Complete the Todo', key='Complete')
exit_btn = sg.Button('Exit')

window = sg.Window('My To-Do App', layout=[
    [clock],
    [label],
    [input_box, add_btn],
    [list_box, edit_btn, complete_btn],
    [exit_btn]],
    font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case 'Add':
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)


        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                print(new_todo)
                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                sg.popup('Please select an item first', font=('Helvetica', 20))

        case 'Complete':
            try:
                todo_complete = values['todos'][0]
                todos = function.get_todos()
                todos.remove(todo_complete)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                sg.popup('Please select an item first', font=('Helvetica', 20))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()