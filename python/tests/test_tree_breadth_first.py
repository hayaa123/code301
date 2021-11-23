from tree.tree import BinaryTree , Node
from tree_breadth_first.tree_breadth_first import breadth_first
import pytest
# can sucessfully deal with empty tree 
def test_breadth_first_on_empty_tree ():
    tree = BinaryTree()
    with pytest.raises(Exception) as E :
        breadth_first(tree)
# can deal with tree with one node 
def test_breadth_first_on_one_node_tree ():
  tree = BinaryTree()
  tree.root = Node(5)
  expected = [5]
  actual = breadth_first(tree)
  assert expected == actual
# can sort a fully tree sucessfully

def test_breadth_first_on_multi_node_tree ():
  tree = BinaryTree()
  tree.root = Node(5)
  tree.root.left = Node(4)
  tree.root.right = Node(3)
  tree.root.left.left = Node(2)
  tree.root.left.right = Node (1)
  tree.root.right.left = Node(0)
  expected = [5,4,3,2,1,0]
  actual = breadth_first(tree)
  assert expected == actual