from stack_and_queue.stack_and_queue import Stack

class PsudoQueue:
    """
    this class is to implement a psudo queue using stack data structure
    """
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack ()

    # got help from this toturial https://www.youtube.com/watch?v=nPvjcQBplH4
    def enqueue (self,value):
        #node = Node(value)
        """
        this method is used to add nodes to the rear_stack of the queue
        """
        
        while not self.stack1.is_empty() :
            self.stack2.push(self.stack1.pop())
        
        self.stack1.push(value)

        while not self.stack2.is_empty() :
            self.stack1.push(self.stack2.pop())

    def dequeue (self):
        """
        this method is used to remove one node fron the front_stack of the queue
        """
        self.stack1.pop()

    def peek (self):
        """
        this returns the front_stack value of the queue 
        """
        if self.stack1.top == None :
            raise ValueError
        return self.stack1.top.value

    def is_empty (self):
        """
        this method used to check if the queue is empty
        """
        if self.rear_stack.top == None :
            return True 
        return False
