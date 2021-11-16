from stack_queue_animal_shelter.stack_queue_animal_shelter import Shelter,Cat,Dog
import pytest


def test_enqueue_into_queue(queue):
    actual = str(queue.cats.front.value)
    expected = str(Cat("lolo"))
    assert expected ==actual

# # Can successfully enqueue multiple values into a queue

def test_enqueue_multiple_values (queue):
    queue.enqueue(Dog("riks")) 
    actual = str(queue.dogs.front.value)
    expected = str(Dog("mushmush"))
    assert actual == expected

# # # # Can successfully dequeue out of a queue the expected value

def test_dequeue(queue):
    queue.dequeue("cat")
    actual = str(queue.cats.front.value)
    expected = str(Cat("mio"))
    assert actual == expected

# # # Can successfully empty a queue after multiple dequeues

def test_empting_queue(queue):
    queue.dequeue("cat")
    queue.dequeue("cat")
    # queue.dequeue("cat")

    expected = None
    actual = queue.cats.front 
    assert actual == expected


# # # Can successfully instantiate an empty queue

def test_instantiate_empty_queue():
    queue = Shelter()
    expected = None
    actual = queue.cats.front
    assert expected == actual

# # # Calling dequeue or peek on empty queue raises exception

# def test_dequeue_or_peek_empty_queue():
#     queue = PsudoQueue()
#     with pytest.raises(ValueError):
#         queue.dequeue()
#     with pytest.raises(ValueError):
#         queue.peek()


@pytest.fixture
def queue():
    queue = Shelter()
    queue.enqueue(Cat("lolo"))
    queue.enqueue(Dog("mushmush"))
    queue.enqueue(Cat("mio"))
    queue.enqueue(Dog("fofo"))
    return queue


