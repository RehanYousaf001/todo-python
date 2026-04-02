import FreeSimpleGUI as sg

label = sg.Text('Type in a todo')
input_box = sg.InputText(tooltip='Type Todo')
add_btn = sg.Button('Add')

edit_btn = sg.Button('Edit')
complete_btn = sg.Button('Complete')

window = sg.Window('My To-Do App', layout=[
    [label],
    [input_box, add_btn],
])
window.read()
window.close()