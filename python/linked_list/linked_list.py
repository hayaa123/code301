class Node :
    def __init__(self,current):
        self.current = current
        self.next = None

class LinkedList:
    """
    this class is to make a linked list data structure 

    """

    def __init__(self):
        self.head = None


    def insert(self,value):
        try:
            node = Node(value)
            if self.head == None:
                self.head = node
            else :
                node.next = self.head
                self.head = node
        except:
            return "ops,some error ocurred"

    def includes (self,value):
        try:
            current = self.head
            while current :
                if current.current == value:
                    return True
                else :
                    current = current.next
            return False
        except:
            return "ops,some error ocured"

    def __str__(self) -> str:
        current = self.head 
        if current == None:
            return "None"
        else :
            string = ""
            while current :
                string += f"{{{current.current}}}->"
                current= current.next
            string+="Null"
            return string



if __name__=="__main__":
    ll = LinkedList()
    ll.insert(4)
    ll.insert(5)
    print(ll)