from stack_and_queue.stack_and_queue import Queue

def breadth_first(tree):
    if not tree.root:
        raise Exception
    arr = []
    queue = Queue ()
    queue.enqueue(tree.root)
    while queue.front:
      front = queue.dequeue()
      print(front)
      arr.append(front.value)
      if front.left :
         queue.enqueue(front.left)
      if front.right :
         queue.enqueue(front.right)
    return arr 