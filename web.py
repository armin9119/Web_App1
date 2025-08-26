import streamlit as st
from func import *

def add_todo():
    todo_add = st.session_state['new_todo']
    todos.append(todo_add + '\n')
    write(todos)

todos = read()

st.title('My Todo App')
st.subheader('this is my todo app')
st.write('this app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        write(todos)
        del st.session_state[f"todo_{index}"]  
        st.rerun()

st.text_input(label='', placeholder='add new todo...',
              on_change=add_todo, key='new_todo')
print('armin')