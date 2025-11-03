
"""
ugit base: Basic higher-level ugit logic.
"""

import os


def write_tree(directory="."):
    """
    Writes the given directory to the object store.
    """
    with os.scandir(directory) as it:
        for entry in it:
            full = f"{directory}/{entry.name}"

            if is_ignored(full):
                continue
            if entry.is_file(follow_symlinks=False):
                pass
            elif entry.is_dir(follow_symlinks=False):
                write_tree(full)

def is_ignored(path):
    """
    Checks if the given path should be ignored.
    """
    return ".ugit" in path.split("/")
