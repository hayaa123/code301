from linked_list.linked_list import LinkedList

class HashTable:
    def __init__(self,size=1024):
        self.size = size
        self.map = [None]*size
    def hash(self,key):
         sum=0 
         for char in key :
               sum+= ord(char)
         temp = sum*19
         index = temp%self.size
         return index 
    def add (self,key,value):
         index = self.hash(key)
         if self.map[index]==None:
               self.map[index] = [key,value]
         else : 
               if isinstance(self.map[index],LinkedList):
                   self.map[index].append([key,value])
               else : 
                   chain = LinkedList()
                   existing_pair = self.map[index]
                   new_pair = [key,value]
                   chain.append(existing_pair) 
                   chain.append(new_pair)
                   self.map[index] = chain
                   

    def get (self,key):
        index = self.hash(key)
        if self.map[index] != None:
            if isinstance(self.map[index],LinkedList):
                    current = self.map[index].head
                    while current :
                            if current.value[0] == key :
                                return current.value[1]
                            current = current.next
                    else:
                        return "your key does not exist in the hash map" 
            return self.map[index][1]
        else : 
            return None
    def contains(self,key):
        index = self.hash(key)
        return self.map[index] != None