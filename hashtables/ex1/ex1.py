#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length <= 1:
        return None
    for i in range(length):
        finding = limit - weights[i]
        
        if hash_table_retrieve(ht, finding) or hash_table_retrieve(ht, finding)==0:
            
            print([i,hash_table_retrieve(ht, finding)])
            if hash_table_retrieve(ht, finding) != i:
                print("get", hash_table_retrieve(ht, finding))
                
                return [i,hash_table_retrieve(ht, finding)]
        else:
           
            hash_table_insert(ht, weights[i], i)
         

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
