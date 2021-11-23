class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):

        node = Node(value)
        if self.front == None and self.rear==None:
            self.front = node
            self.rear = node
        elif self.rear == self.front:
            self.rear = node
            self.front.next = self.rear
        else:
          self.rear.next = node
          self.rear = node
          self.rear.next = None

    def dequeue(self):
        if self.front == None :
          raise ValueError
        if self.rear==self.front:
            temp = self.front
            self.rear =  None
            self.front = None
            return temp.value
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.front == None and self.rear == None:
          raise ValueError
        return self.front.value

    def is_empty(self):
        return self.rear == None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            raise ValueError("cannot pop of empty stack")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def is_empty(self):
        return self.top == None

    def peek(self):
        if self.top == None:
            raise ValueError("the stack is empty")

        return self.top.value
