import os

BASE_DIR = os.path.dirname(__file__)  # ensures paths are relative to project folder

def get_todos(username=None):
    """Get todos for a specific user. Creates file if it doesn’t exist."""
    filename = "todos.txt" if not username else f"todos_{username}.txt"
    filepath = os.path.join(BASE_DIR, filename)

    # Create file if it doesn't exist
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            pass  # empty file

    # Read todos
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, username=None):
    """Write todos for a specific user."""
    filename = "todos.txt" if not username else f"todos_{username}.txt"
    filepath = os.path.join(BASE_DIR, filename)

    with open(filepath, 'w') as file:
        file.writelines(todos)
