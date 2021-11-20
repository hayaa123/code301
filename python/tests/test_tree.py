
# Can successfully instantiate an empty tree
from tree.tree import BinartSearchTree, BinaryTree
import pytest

def test_empty_tree ():
    expected = None
    actual = BinartSearchTree().root
    assert actual == expected

# Can successfully instantiate a tree with a single root node
def test_add_root ():
    expected = 4
    binart_tree =  BinartSearchTree()
    binart_tree.add(4) 
    actual = binart_tree.root.value
    assert actual == expected

# Can successfully add a left child and right child to a single root node

def test_add_left_to_root ():
    expected = 3
    binart_tree =  BinartSearchTree()
    binart_tree.add(4) 
    binart_tree.add(3)
    actual = binart_tree.root.left.value
    assert actual == expected

def test_add_right_to_root ():
    expected = 5
    binart_tree =  BinartSearchTree()
    binart_tree.add(4) 
    binart_tree.add(5)
    actual = binart_tree.root.right.value
    assert actual == expected
    
# Can successfully return a collection from a preorder traversal
def test_pre_order_treverse(tree):
    expected = [10,8,7,9,15,14]
    actual = tree.pre_order()
    assert expected == actual
# Can successfully return a collection from an inorder traversal
def test_in_order_treverse(tree):
    expected = [7,8,9,10,14,15]
    actual = tree.in_order()
    assert expected == actual
# Can successfully return a collection from a postorder traversal
def test_post_order_treverse(tree):
    expected = [7,9,8,14,15,10]
    actual = tree.post_order()
    assert expected == actual


@pytest.fixture
def tree ():
    tree = BinartSearchTree()
    tree.add(10)
    tree.add(8)
    tree.add(15)
    tree.add(7)
    tree.add(9)
    tree.add(14)
    return tree