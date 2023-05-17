import os


def create_dirs(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)


paths = [
    'test1',
    'folder1/test2',
    'folder1/folder2/test3',
]

create_dirs(paths)
