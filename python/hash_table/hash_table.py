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

    def get (self,key):
        index = self.hash(key)
        return self.map[index]
    def contains(self,key):
        index = self.hash(key)
        return self.map[index] != None