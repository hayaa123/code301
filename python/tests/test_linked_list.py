import pytest
from linked_list.linked_list import LinkedList


# 1-Can successfully instantiate an empty linked list
def test_empty():
    ll = LinkedList()
    assert str(ll) == "None"

# 2-Can properly insert into the linked list
def test_insert_1():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    assert ll.head.current == 6

# 3-The head property will properly point to the first node in the linked list
def test_head_point_to_1st_node():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    expected = 5
    actual = ll.head.next.current
    assert expected == actual

# 4-Can properly insert multiple nodes into the linked list
def test_multiple_nodes():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    assert str(ll) == "{6}->{5}->Null"

# 5-Will return true when finding a value within the linked list that exists
def test_includes_5():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    expected = True
    actual = ll.includes(5)
    assert actual == expected

# 6-Will return false when searching for a value in the linked list that does not exist
def test_notincludes_5():
    ll = LinkedList()
    ll.insert(4)
    ll.insert(6)
    expected = False
    actual = ll.includes(5)
    assert actual == expected

# 7-Can properly return a collection of all the values that exist in the linked list
def test_print(ll):
    # ll = LinkedList()
    # ll.insert(5)
    # ll.insert(6)
    assert str(ll) == "{6}->{5}->Null"


@pytest.fixture
def ll ():
    ll= LinkedList()

    ll.insert(5)
    ll.insert(6)
    return ll 