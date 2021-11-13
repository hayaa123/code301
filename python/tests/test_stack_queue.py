from stack_and_queue.stack_and_queue import Stack,Queue
import pytest


# Can successfully push onto a stack

def test_push_to_stack(stack):
    expected = 3
    actual = stack.peek()
    assert expected == actual

# Can successfully push multiple values onto a stack

def test_push_multiple_values_to_stack(stack):
    add_multi = stack
    add_multi.push(5)
    add_multi.push(6)
    expected = 6
    actual = add_multi.peek()
    assert expected == actual

# Can successfully pop off the stack
def test_pop_off_stack(stack):
    poped_value = stack.pop()
    expected_pop = 3
    actual_pop = poped_value
    assert expected_pop ==  actual_pop
    expected = 2
    actual = stack.peek()
    assert expected == actual

# Can successfully empty a stack after multiple pops

def test_pop_off_stack_until_empty(stack):
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.top
    expected = None
    assert actual == expected



# Can successfully peek the next item on the stack

def test_peek_stack(stack):
    actual =stack.peek()
    expected = 3
    assert expected == actual

# Can successfully instantiate an empty stack

def test_instantiate_empty_stack():
    stack = Stack()
    actual = stack.top
    expected = None
    assert expected == actual

# Calling pop or peek on empty stack raises exception
#https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest

def test_raise_error_in_peek_and_pop_empty_stack():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.pop()
    with pytest.raises(ValueError):
        stack.peek()


# Can successfully enqueue into a queue
def test_enqueue_into_queue(queue):
    actual = queue.peek()
    expected = 1
    assert expected ==actual

# Can successfully enqueue multiple values into a queue

def test_enqueue_multiple_values (queue):
    actual = queue.rear.value
    expected = 3
    assert actual == expected

# Can successfully dequeue out of a queue the expected value

def test_dequeue(queue):
    queue.dequeue()
    actual = queue.front.value
    expected = 2
    assert actual == expected

# Can successfully peek into a queue, seeing the expected value

def test_peek_queue(queue):
    actual = queue.peek()
    expected = 1
    assert expected ==actual

# Can successfully empty a queue after multiple dequeues

def test_empting_queue(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    expected = None
    actual = queue.rear    
    assert actual == expected


# Can successfully instantiate an empty queue

def test_instantiate_empty_queue():
    queue = Queue()
    expected = None
    actual = queue.front
    assert expected == actual

# Calling dequeue or peek on empty queue raises exception

def test_dequeue_or_peek_empty_queue():
    queue = Queue()
    with pytest.raises(ValueError):
        queue.dequeue()
    with pytest.raises(ValueError):
        queue.peek()





@pytest.fixture
def stack():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack

@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue







