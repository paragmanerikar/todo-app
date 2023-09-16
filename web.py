import streamlit as st
import storageutils as su

todos = su.read_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    su.write_todos(todos)


st.title("My Todo App")
st.subheader("Simple app to increase your productivity.")

st.text_input(label="", placeholder="Enter todo ....", key="new_todo",
              on_change=add_todo)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        su.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
