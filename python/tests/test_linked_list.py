from abc import ABC
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
    assert ll.head.value == 6

# 3-The head property will properly point to the first node in the linked list
def test_head_point_to_1st_node():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    expected = 5
    actual = ll.head.next.value
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

# Can successfully add a node to the end of the linked list
def test_append():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert str(ll) == "{1}->{2}->Null"


# Can successfully add multiple nodes to the end of a linked list\

def test_append(ll2):
    assert str(ll2) == "{1}->{2}->{3}->Null"

# # Can successfully insert a node before a node located i the middle of a linked list

def test_isert_0_before_2(ll2):
    expected = "{1}->{0}->{2}->{3}->Null"
    ll2.insert_before(2,0)
    assert expected == str(ll2)

# # Can successfully insert a node before the first node of a linked list

def test_insert_befor_1st_node (ll2):
    expected = "{0}->{1}->{2}->{3}->Null"
    ll2.insert_before(1,0)
    assert expected == str(ll2)

# Can successfully insert after a node in the middle of the linked list

def test_isert_0_after_2(ll2):
    expected = "{1}->{2}->{0}->{3}->Null"
    ll2.insert_after(2,0)
    assert expected == str(ll2)


# Can successfully insert a node after the last node of the linked list

def test_isert_0_after_3(ll2):
    expected = "{1}->{2}->{3}->{0}->Null"
    ll2.insert_after(3,0)
    assert expected == str(ll2)

# Where k is greater than the length of the linked list

def test_kthFromEnd_4_in_len_3_list(ll2):
    expected = "Exception" 
    actual = ll2.kthFromEnd(4)
    assert actual == expected

# Where k and the length of the list are the same
def test_kthFromEnd_2_in_len_3_list(ll2):
    expected = 1
    actual = ll2.kthFromEnd(2)
    assert actual == expected

# Where k is not a positive integer
def test_kthFromEnd_negative2_in_len_3_list(ll2):
    expected =  "Exception" 
    actual = ll2.kthFromEnd(-2)
    assert actual == expected

# Where the linked list is of a size 1
def test_kthFromEnd_of_len_1():
    ll = LinkedList()
    ll.insert(1)
    actual = ll.kthFromEnd(0)
    expected = 1

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_kthFromEnd_k_in_middle (ll2):
    expected = 2
    actual = ll2.kthFromEnd(1)

# def test_linked_list_azip(ll2):
#     ll1 = LinkedList()
#     ll1.insert(5)
#     ll1.append(6)
#     ll1.append(7)
#     ll1.linked_list_zip(ll2)
#     expected = "{1}->{5}->{2}->{6}->{3}->{7}->Null"
#     actual = str(ll2)
#     assert actual==expected
    


@pytest.fixture
def ll ():
    ll= LinkedList()

    ll.insert(5)
    ll.insert(6)
    return ll 

@pytest.fixture 
def ll2 ():
    ll2 = LinkedList()
    ll2.append(1)
    ll2.append(2)
    ll2.append(3) 
    return ll2