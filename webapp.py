import streamlit as st
import functions as fun

st.title("My Todo App")

username = st.text_input("Enter username:")

if username:
    todos = fun.get_todos(username)

    def add_todo():
        new_task = st.session_state["new_todo"].strip()
        if new_task:
            todos_local = fun.get_todos(username)
            todos_local.append(new_task + "\n")
            fun.write_todos(todos_local, username)
            st.session_state["new_todo"] = ""
            st.experimental_rerun()

    st.text_input("Add New Task", on_change=add_todo, key="new_todo")

    st.write("### Your Tasks")
    for index, todo in enumerate(todos):
        if st.checkbox(todo.strip(), key=f"{username}_{index}"):
            todos.pop(index)
            fun.write_todos(todos, username)
            del st.session_state[f"{username}_{index}"]
            st.rerun()

    # Optional: manual refresh button
   



if st.button("Reload Page 🔄"):
    st.rerun()  # re-runs the script and refreshes the page

