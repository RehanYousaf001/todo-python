FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read the text file and return a list of the todos """
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos

def write_todos(todos, filepath=FILEPATH):
    """ Write the todos into a text file """
    with open(filepath, 'w') as file:
        file.writelines(todos)
