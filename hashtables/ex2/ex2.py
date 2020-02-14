#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        
    for i in range(1, length):
        if hashtable.storage[i - 1]:
            print(hashtable.storage[i - 1].value)
            route[i] = hashtable.storage[i - 1].value
        print("route", route)
    for item in route:
        if item is None:
            route.remove(item)
    return route
