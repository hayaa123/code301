from stack_queue_pseudo.stack_queue_pseudo import PsudoQueue
import pytest


def test_enqueue_into_queue(queue):
    actual = queue.peek()
    expected = 1
    assert expected ==actual

# # Can successfully enqueue multiple values into a queue

def test_enqueue_multiple_values (queue):
    actual = str(queue)
    expected = '[1]->[2]->[3]->Null'
    assert actual == expected

# # # Can successfully dequeue out of a queue the expected value

def test_dequeue(queue):
    queue.dequeue()
    actual = queue.stack1.top.value
    expected = 2
    assert actual == expected

# # Can successfully peek into a queue, seeing the expected value

def test_peek_queue(queue):
    actual = queue.peek()
    expected = 1
    assert expected ==actual

# # Can successfully empty a queue after multiple dequeues

def test_empting_queue(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    expected = None
    actual = queue.stack1.top   
    assert actual == expected


# # Can successfully instantiate an empty queue

def test_instantiate_empty_queue():
    queue = PsudoQueue()
    expected = None
    actual = queue.stack1.top
    assert expected == actual

# # Calling dequeue or peek on empty queue raises exception

def test_dequeue_or_peek_empty_queue():
    queue = PsudoQueue()
    with pytest.raises(ValueError):
        queue.dequeue()
    with pytest.raises(ValueError):
        queue.peek()


@pytest.fixture
def queue():
    queue = PsudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue



