FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a txt file and return thr list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list to a txt file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# print("I am outside")
if __name__ == "__main__":
    print("Hello")
    print(get_todos())