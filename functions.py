import os

FILEPATH = "todos.txt"

def get_todos(username=None, filepath=FILEPATH):
    """Get todos for a specific user. Create file if it doesn’t exist."""
    if username:
        filepath = f"todos_{username}.txt"
    
    # ✅ Ensure the file exists before reading
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            pass  # just create an empty file
    
    # ✅ Now safely read
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, username=None, filepath=FILEPATH):
    """Write todos for a specific user."""
    if username:
        filepath = f"todos_{username}.txt"
    with open(filepath, 'w') as file:
        file.writelines(todos)

