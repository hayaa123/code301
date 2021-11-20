class Node :
    def __init__(self,value) :
        self.value = value
        self.left = None
        self.right = None

class BinaryTree :
    def __init__(self):
        self.root = None
    
    def pre_order (self):
        arr = [] 
        def _treverse (root):
            arr.append(root.value)
            if root.left :
                _treverse(root.left)
            if root.right :
                _treverse(root.right)
            return arr 
        return _treverse(self.root)

    def in_order (self):
        arr = [] 
        def _treverse (root):
            if root.left :
                _treverse(root.left)
            arr.append(root.value)
            if root.right :
                _treverse(root.right)
            return arr 
        return _treverse(self.root)

    def post_order (self):
        arr = [] 
        def _treverse (root):
            if root.left :
                _treverse(root.left)
            if root.right :
                _treverse(root.right)
            arr.append(root.value)
            return arr 
        return _treverse(self.root)


class BinartSearchTree(BinaryTree):
    def add (self,value):
        node = Node(value)

        if not self.root :
            self.root = node
        else :
            def _search_and_add (root):
                if node.value > root.value :
                    if root.right == None:
                        root.right = node 
                    else :
                        _search_and_add(root.right)

                elif node.value <= root.value :
                    if root.left == None:
                        root.left = node 
                    else :
                        _search_and_add(root.left)                   
            _search_and_add(self.root)
    
    def contains (self,value):
        if self.root == None : 
            raise Exception("the tree is empty")
        else:
            def _search_and_find(root):
                if root.value == value:
                    return True
                elif value > root.value:
                    _search_and_find(root.right)
                elif value <= root.value:
                    _search_and_find(root.left)
            _search_and_find(self.root)