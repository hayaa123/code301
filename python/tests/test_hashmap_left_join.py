from hash_table.hash_table import HashTable 
from hashmap_left_join.hashmap_left_join import hashmap_left_join
import pytest

# sucessfully join 2 tables together 
def test_join_left_2_ht(ht1,ht2):

    expected = [["happy","cheerful","sad"],["falafel","delisious","fofo"],["flexible","pliable",None],["rich","wealthy","poor"]]
    actual = hashmap_left_join(ht1,ht2)
    assert expected == actual

# sucessfully return none joining 2 table one of them is empty 
def test_join_left_ht_one_empty(ht1):
    ht2 = HashTable()
    expected = [["happy","cheerful",None],["falafel","delisious",None],["flexible","pliable",None],["rich","wealthy",None]]
    actual = hashmap_left_join(ht1,ht2)
    assert expected == actual


# raise an error if anything other than hashtable input 
def test_join_left_none_ht():

    with pytest.raises(ValueError) :
        hashmap_left_join("123",None)


@pytest.fixture
def ht1 ():
    ht1 = HashTable()
    ht1.add("falafel","delisious")
    ht1.add("happy","cheerful")
    ht1.add("rich","wealthy")
    ht1.add("flexible","pliable")
    return ht1

@pytest.fixture
def ht2 ():
    ht2 = HashTable()
    ht2.add("falafel","fofo")
    ht2.add("happy","sad")
    ht2.add("rich","poor")
    return ht2