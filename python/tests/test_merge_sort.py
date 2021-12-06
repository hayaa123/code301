from merge_sort.merge_sort import merge_sort

#happy path 
def test_ideal_array():
    expected = [4,8,15,16,23,42]
    actual = merge_sort([8,4,23,42,16,15])
    assert expected==actual

def test_one_element_Array():
    expected = [4]
    actual = merge_sort([4])
    assert expected == actual
