FFILEPATH = "todos.txt"

def get_todos(username=None, filepath=FILEPATH):
    """Return todos for a specific user, or the default file."""
    if username:
        filepath = f"todos_{username}.txt"  # unique file per user
    try:
        with open(filepath, 'r') as file:
            todos = file.readlines()
    except FileNotFoundError:
        # create empty file if it doesn't exist
        with open(filepath, 'w') as file:
            pass
        todos = []
    return todos


def write_todos(todos, username=None, filepath=FILEPATH):
    """Write todos for a specific user, or default file."""
    if username:
        filepath = f"todos_{username}.txt"
    with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print(get_todos("nomaan"))
