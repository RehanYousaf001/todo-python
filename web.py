import streamlit
import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    print(todo)
    todos.append(todo)
    function.write_todos(todos)
    del st.session_state['new_todo']
    st.session_state['new_todo'] = '' 


def remove_todo(remove_item):
    todos.remove(remove_item)
    function.write_todos(todos)
    del st.session_state[remove_item]


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')
for item in todos:
    st.checkbox(item, on_change=remove_todo, key=item, args=(item,))

streamlit.text_input(label='', placeholder='Enter a todo', on_change=add_todo, key='new_todo')

st.session_state