import streamlit as st
import functions as fun

todos = fun.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos = fun.get_todos()
    todos.append(todo)
    fun.write_todos(todos)
    st.session_state["new_todo"] = ""

def complete_task(todo, index):
    # Remove todo
    todos.pop(index)
    fun.write_todos(todos)
    # Only delete key if it exists
    if todo in st.session_state:
        del st.session_state[todo]
    # Rerun safely inside a callback
    st.experimental_rerun()

st.title("My To-Do App")
st.subheader("This a todo app.")
st.write("The To-Do app helps users organize their daily tasks by allowing them to create, edit, and manage task lists. "
         "It acts as a digital planner where users can keep track of what needs to be done, set priorities, and mark "
         "tasks as completed — improving productivity and reducing the chance of forgetting important activities.")

# Render all todos
for index, todo in enumerate(todos):
    st.checkbox(todo, key=todo, on_change=complete_task, args=(todo, index))

st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key='new_todo')
