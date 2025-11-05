
"""
ugit base: Basic higher-level ugit logic.
"""

import os
from ugit import data


def write_tree(directory="."):
    """
    Writes the given directory to the object store.
    """
    entries =  []
    with os.scandir(directory) as it:
        for entry in it:
            full = f"{directory}/{entry.name}"

            if is_ignored(full):
                continue
            if entry.is_file(follow_symlinks=False):
                type_ = "blob"
                with open(full,'rb') as f:
                    oid = data.hash_object(f.read());
            elif entry.is_dir(follow_symlinks=False):
                type_ = "tree"
                oid  = write_tree(full)
            else :
                continue
            entries.append((entry.name,oid,type_))

    tree = ''.join(f'{type} {oid} {name}\n' for name, oid, type_ in sorted(entries))
    return data.hash_object(tree.encode(),'tree')


def is_ignored(path):
    """
    Checks if the given path should be ignored.
    """
    return ".ugit" in path.split("/")
