from hash_table.hash_table import HashTable

def binary_tree_intersection(tree1,tree2):
    try:
        ht = HashTable()
        arr = []
        if tree1.root != None and tree2.root != None:
            def _treverse(root):
                nonlocal ht 
                nonlocal arr
                if root.value == ht.get(str(root.value)):
                    arr.append(root.value)
                else:
                    ht.add(str(root.value),root.value)
                if root.left:
                    _treverse(root.left)
                if root.right:
                    _treverse(root.right)
            _treverse(tree1.root)
            _treverse(tree2.root)
        return arr
    except AttributeError :
        return "this function takes only trees as an input"

    