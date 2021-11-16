from stack_queue_brackets.stack_queue_brackets import bracet_validation

# can identify a correct one open and close bracets 

def test_bracet_validation_one_pair():
    excepted = True
    actual = bracet_validation("()")
    assert excepted == actual

# can identify wrong senario adding extra bracet 

def test_bracet_validation_extra_1():
    excepted = False
    actual = bracet_validation("{}[]}]")
    assert excepted == actual

# can identify extra bracet after the last close 

def test_bracet_validation_extra_end():
    excepted = False
    actual = bracet_validation("{}[])))")
    assert excepted == actual   

# start with close bracet

def test_bracet_validation_start():
    excepted = False
    actual = bracet_validation("))){}[]")
    assert excepted == actual     

# examples from the lab 

def test_bracet_validation_1():
    expected = True
    actual = bracet_validation("{}{Code}[Fellows](())")
    assert expected == actual     

def test_bracet_validation_2():
    expected = True
    actual = bracet_validation("{}")
    assert expected == actual  

def test_bracet_validation_3():
    expected = True
    actual = bracet_validation("{}(){}")
    assert expected == actual  

def test_bracet_validation_4():
    expected = True
    actual = bracet_validation("()[[Extra Characters]]")
    assert expected == actual  

def test_bracet_validation_5():
    expected = True
    actual = bracet_validation("(){}[[]]")
    assert expected == actual  

def test_bracet_validation_6():
    expected = False
    actual = bracet_validation("[({}]")
    assert expected == actual  

def test_bracet_validation_7():
    expected = False
    actual = bracet_validation("(](")
    assert expected == actual  

def test_bracet_validation_8():
    expected = False
    actual = bracet_validation("{(})")
    assert expected == actual  

def test_bracet_validation_9():
    expected = False
    actual = bracet_validation("[}")
    assert expected == actual  




