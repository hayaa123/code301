from hash_table.hash_table import HashTable
from linked_list.linked_list import LinkedList
import pytest
# Adding a key/value to your hashtable results in the value being in the data structure
def test_hash_table_add_1_pair():
    ht = HashTable()
    ht.add("AppleABC",15)
    expected = ["AppleABC",15]
    actual = ht.get("AppleABC")
    assert expected == actual

# Retrieving based on a key returns the value stored
def test_hash_get_key(ht):
    expected =["banana",9]
    actual = ht.get("banana")
    assert expected == actual

# Successfully returns null for a key that does not exist in the hashtable
def test_hash_get_no_exist_key(ht):
    expected =None
    actual = ht.get("bana")
    assert expected == actual
# Successfully handle a collision within the hashtable
# def test_collision_in_hash(ht):
#     ht.add("pAple",7)
#     expected = LinkedList()
#     actual = ht.get("pAple")
#     assert expected == actual
# Successfully retrieve a value from a bucket within the hashtable that has a collision

# Successfully hash a key to an in-range value


@pytest.fixture
def ht():
    ht = HashTable()
    ht.add("Apple",15)
    ht.add('banana',9)
    ht.add("orange",88)
    ht.add("dates",90)
    ht.add("grapes",100)
    return ht