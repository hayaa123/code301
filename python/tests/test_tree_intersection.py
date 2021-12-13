from tree.tree import BinaryTree ,Node
import pytest
from tree_intersection.tree_intersection import binary_tree_intersection
# test normal tow bnary trees 
def test_tree_intersection (tree1,tree2):
    actaul = set(binary_tree_intersection(tree1,tree2))
    expected ={0,1,3,4}
    assert expected == actaul

def test_tree_intersection_one_empty (tree1):
    tree2 = BinaryTree()
    actaul = binary_tree_intersection(tree1,tree2)
    expected = []
    assert expected == actaul

def test_tree_intersection_two_empty ():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    actaul = binary_tree_intersection(tree1,tree2)
    expected = []
    assert expected == actaul

def test_none_tree_intersection():
    tree1 = [2,4,6,7]
    tree2 = 'hellow world'
    actaul = binary_tree_intersection(tree1,tree2)
    expected = 'this function takes only trees as an input'
    assert expected == actaul


@pytest.fixture
def tree1 ():
    tree = BinaryTree()
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(4)
    tree.root.right = Node(3)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node (1)
    tree.root.right.left = Node(0)
    return tree

@pytest.fixture
def tree2 ():
    tree = BinaryTree()
    tree = BinaryTree()
    tree.root = Node(6)
    tree.root.left = Node(4)
    tree.root.right = Node(3)
    tree.root.left.left = Node(7)
    tree.root.left.right = Node (1)
    tree.root.right.left = Node(0)
    return tree