import os
FILENAME = r"todos.txt"


def read_todos(file_path: object = FILENAME) -> object:
    with open(file_path, 'r') as file:
        todos = file.readlines()
        todos = [t.replace('\n','') for t in todos]
    return todos;


def write_todos(todos,file_path=FILENAME):
    with open(file_path, 'w') as file:
        file.writelines("%s\n" % l.title() for l in todos)


def file_exists(file_path=FILENAME):
    return os.path.exists(file_path)


def create_empty_file(file_path=FILENAME):
    with open(file_path, 'w') as file:
        pass