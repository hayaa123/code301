from hash_table.hash_table import HashTable

def hashmap_left_join(ht1,ht2):
    if  isinstance(ht1,HashTable) and isinstance(ht2,HashTable):
        arr = []
        for i in ht1.map:
            temp_arr = []
            if i != None:
                anti = ht2.get(i[0])
                temp_arr.append(i[0])
                temp_arr.append(i[1])
                temp_arr.append(anti)
                arr.append(temp_arr)
        if len(arr) < 1 : 
            arr.append(None)
        return arr
    else :
        raise ValueError (" function input should be a HashTable object type ")