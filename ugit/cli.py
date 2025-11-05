
"""
ugit: A simple git implementation in Python.
"""

import argparse
import os
import sys

from ugit import data
from ugit import base

def main():
    """
    The main entry point for the ugit command-line interface.
    """
    args = parse_args()
    args.func(args)

def parse_args():
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest="command")
    commands.required = True

    init_parser = commands.add_parser("init")
    init_parser.set_defaults(func=init)

    hash_object_parser = commands.add_parser("hash-object")
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument("file")

    cat_file_parser = commands.add_parser("cat-file")
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument("object")

    write_tree_parser = commands.add_parser("write-tree")
    write_tree_parser.set_defaults(func=cli_write_tree)

    read_tree_parser = commands.add_parser("read-tree")
    read_tree_parser.set_defaults(func = read_tree)
    read_tree_parser.add_argument('tree')


    return parser.parse_args()

def init(args):
    """
    Initializes a new ugit repository.
    """
    _ = args
    data.init()
    print(f"Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}")

def hash_object(args):
    """
    Hashes the content of a file.
    """
    with open(args.file, "rb") as f:
        print(data.hash_object(f.read()))

def cat_file(args):
    """
    Prints the content of a ugit object.
    """
    sys.stdout.flush()

    sys.stdout.buffer.write(data.get_object(args.object, expected=None))

def cli_write_tree(args):
    """
    Writes the current directory to the object store.
    """
    _ = args
    print(base.write_tree())
def read_tree(args):
    '''
    Reads the given OID to fetch directory with which it is associated.
    '''
    base.read_tree(args.tree)
