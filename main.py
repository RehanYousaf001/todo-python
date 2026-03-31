# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import  function

def learning():
    # Use a breakpoint in the code line below to debug your script.
    while True:
        user_input = input("Type add, show, edit, complete or exit: ").strip()
        match user_input:
            case 'add':
                todo = input('Enter a todo: ') + '\n'

                todos= function.get_todos()
                todos.append(todo + '\n')
                function.write_todos(todos)

            case 'show':
                todos = function.get_todos()
                for index, item in enumerate(todos):
                    print(f"{index+1}-{item.strip('\n')}")
            case 'edit':
                todos = function.get_todos()
                number = int(input('Enter a number: '))
                index = number-1
                new_todo = input('Enter new todo: ') + '\n'
                todos[index] = new_todo
                function.write_todos(todos)

            case 'complete':
                todos = function.get_todos()
                number = int(input('Enter a number: '))
                todos.pop(number - 1)
                function.write_todos(todos)
            case 'exit':
                break
    print('by!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    learning()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
