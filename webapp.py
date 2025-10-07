import streamlit as st
import functions as fun

st.title("My Todo App")
st.subheader("A personalized To-Do Manager")
st.write("Each user manages their own tasks independently ✅")

# Step 1: Ask for username
username = st.text_input("👤 Enter your username:", placeholder="e.g. nomaan")

# Only continue when username is entered
if username:
    todos = fun.get_todos(username)

    def add_todo():
        todo = st.session_state["new_todo"].strip()
        if todo:
            todos_local = fun.get_todos(username)
            todos_local.append(todo + "\n")
            fun.write_todos(todos_local, username)
            st.session_state["new_todo"] = ""
            st.experimental_rerun()

    # Display current todos
    st.write("### 📝 Your Tasks")
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo.strip(), key=f"{username}_{index}")
        if checkbox:
            todos.pop(index)
            fun.write_todos(todos, username)
            del st.session_state[f"{username}_{index}"]
            st.experimental_rerun()

    # Add new todo
    st.text_input(
        label="Add New Task",
        placeholder="Type your task and press Enter",
        on_change=add_todo,
        key="new_todo"
    )

else:
    st.info("Please enter your username above to view your personal To-Do list.")


if st.button("Reload Page 🔄"):
    st.rerun()  # re-runs the script and refreshes the page

