class HashTable:
    def __init__(self,size=1024):
        self.size = size
        self.map = [[] for i in range(size)]
    def hash(self,key):
         sum=0 
         for char in key :
               sum+= ord(char)
         temp = sum*19
         index = temp%self.size
         return index 
    def add (self,key,value):
         index = self.hash(key)
         self.map[index].append([key,value])
             

    def get (self,key):
        index = self.hash(key)
        return self.map[index]
    def contains(self,key):
        index = self.hash(key)
        return self.map[index] != None


if __name__ == "__main__":
    ht= HashTable()
    ht.add("apple",15)
    # ht.add("strawry",16)
    ht.add("pepla",20)
    # print(ht.get("strawry"))
    print(ht.map)