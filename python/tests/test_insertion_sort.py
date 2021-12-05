from insertion_sort.insertion_sort import insertion_sort
import pytest

# happy path 

def test_ideal_array():
    expected = [1,2,3,4,5]
    actual = insertion_sort([2,5,4,1,3])
    assert actual == expected

# Few uniques testing 

def test_few_unique():
    expected = [5,5,5,7,7,12]
    actual = insertion_sort([5,12,7,5,5,7])
    assert actual ==expected

# nearly sorted
def test_Nearly_sorted():
    expected = [2,3,5,7,11,13]
    actual = insertion_sort([2,3,5,7,13,11])
    assert actual ==expected
