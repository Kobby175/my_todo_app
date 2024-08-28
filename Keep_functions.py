FILEPATH = "todos.txt"


def get_todo(filepath=FILEPATH):
    """ Read a text file and return a to-do list"""
    with open(filepath, 'r') as files:
        todo_local = files.readlines()
    return todo_local


def write_todo(todo_arg, filepath=FILEPATH):
    """Write in a to-do items list in a text file"""
    with open(filepath, "w") as file:
        file.writelines(todo_arg)


if __name__ == "__main__":
    """ this code here allow us to work with only the functions
    upwards when we import it into another file to use it
    But when we are working in this file then there is no need for the if function
    This code inhibit every code you put inside 
    """
    print(help(get_todo))  # this display the DOCSTRING, giving meaning to the function
