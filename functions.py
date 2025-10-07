import os

# Base path relative to current working directory
BASE_DIR = os.getcwd()  # safer than __file__ on Streamlit Cloud
FILEPATH = os.path.join(BASE_DIR, "todos.txt")

def get_todos(username=None):
    """Get todos for a specific user. Create file if it doesn’t exist."""
    path = FILEPATH
    if username:
        path = os.path.join(BASE_DIR, f"todos_{username}.txt")
    
    # Create the file if it doesn't exist
    if not os.path.exists(path):
        with open(path, 'w') as file:
            pass
    
    # Read todos
    with open(path, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos, username=None):
    """Write todos for a specific user."""
    path = FILEPATH
    if username:
        path = os.path.join(BASE_DIR, f"todos_{username}.txt")
    
    with open(path, 'w') as file:
        file.writelines(todos)

