import os
import unittest
import tempfile
import shutil

from ugit import base
from ugit import data

class TestWriteTree(unittest.TestCase):
    def test_write_tree(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a test directory structure
            os.makedirs(os.path.join(temp_dir, "test_dir"))
            with open(os.path.join(temp_dir, "test_file.txt"), "w") as f:
                f.write("hello world")
            with open(os.path.join(temp_dir, "test_dir", "nested_file.txt"), "w") as f:
                f.write("nested hello")

            # Set the ugit directory
            data.GIT_DIR = os.path.join(temp_dir, ".ugit")
            data.init()

            # Call write_tree
            tree_oid = base.write_tree(temp_dir)

            # Check the tree object
            tree_content = data.get_object(tree_oid, "tree").decode()
            self.assertIn("blob", tree_content)
            self.assertIn("test_file.txt", tree_content)
            self.assertIn("tree", tree_content)
            self.assertIn("test_dir", tree_content)


class TestReadTree(unittest.TestCase):
    def test_read_tree(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a test directory structure
            os.makedirs(os.path.join(temp_dir, "test_dir"))
            with open(os.path.join(temp_dir, "test_file.txt"), "w") as f:
                f.write("hello world")
            with open(os.path.join(temp_dir, "test_dir", "nested_file.txt"), "w") as f:
                f.write("nested hello")

            # Set the ugit directory
            data.GIT_DIR = os.path.join(temp_dir, ".ugit")
            data.init()

            # Call write_tree
            tree_oid = base.write_tree(temp_dir)

            # Create a new directory to read the tree into
            read_dir = os.path.join(temp_dir, "read_dir")
            os.makedirs(read_dir)
            os.chdir(read_dir)

            # Call read_tree
            base.read_tree(tree_oid)

            # Check that the files were created
            self.assertTrue(os.path.exists("test_file.txt"))
            self.assertTrue(os.path.exists("test_dir/nested_file.txt"))

            # Check the file contents
            with open("test_file.txt", "r") as f:
                self.assertEqual(f.read(), "hello world")
            with open("test_dir/nested_file.txt", "r") as f:
                self.assertEqual(f.read(), "nested hello")
if __name__ == '__main__':
    unittest.main()
