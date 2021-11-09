

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    this class is to make a linked list data structure 

    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        try:
            node = Node(value)
            if self.head == None:
                self.head = node
            else:
                node.next = self.head
                self.head = node
        except:
            return "ops,some error ocurred"

    def includes(self, value):
        try:
            current = self.head
            while current:
                if current.value == value:
                    return True
                else:
                    current = current.next
            return False
        except:
            return "ops,some error ocured"

    def __str__(self) -> str:
        current = self.head
        if current == None:
            return "None"
        else:
            string = ""
            while current:
                string += f"{{{current.value}}}->"
                current = current.next
            string += "Null"
            return string

    def append(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def insert_before(self, val, new_val):

        
        
        if self.head.value == val:
            self.insert(new_val)
        else:
            node = Node(new_val)
            current = self.head
            while current.next.value != val:
                current = current.next
            node.next = current.next
            current.next = node

    def insert_after(self, val, new_val):
        node = Node(new_val)
        current = self.head
        while current.value != val:
            current = current.next
        node.next = current.next
        current.next = node
    def kthFromEnd(self,K):
        try:
            if K < 0:
                raise Exception
            current =self.head
            temp = self.head
            gap =0 
            while current.next != None:
                if gap == K :
                    temp = temp.next
                    gap-=1
                current = current.next
                gap+=1
            
            if gap <K: 
                raise Exception
            
            return temp.value
        except Exception:
            return "Exception"


    def linked_list_zip(self,otherll):
        try:
            if otherll == None:
                raise ValueError
            
            other_current = otherll.head
            current = self.head

            # in this function I got some help from my collegue hannen darwish 
            while current !=None and otherll != None:
                temp_other = other_current.next
                temp = current.next

                other_current.next = temp_other
                current = other_current
        
                other_current = temp_other.next 
                current = temp.next
        except ValueError:
            return "you should input a linked list as an argument"


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(4)
    ll.insert(5)
    ll.append(3)
    ll.append(1)
    print(ll.__str__())
    print(ll.kthFromEnd(4))
