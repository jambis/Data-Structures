from doubly_linked_list import DoublyLinkedList, ListNode
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.max = limit
        self.DLL = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage:
            return None
        
        # Update the head of our DLL when getting entry from our dict
        self.DLL.move_to_front(self.storage[key])
        return self.storage[key].value[1]
        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if self.DLL.length == self.max:
            # If key is not in our dict we remove the oldest entry from
            # our dict, and then proceed to update our DLL and add new
            # entry into our dict, only if we are at the limit
            if key not in self.storage:
                del self.storage[self.DLL.tail.value[0]]

            self.DLL.remove_from_tail()
            self.DLL.add_to_head((key, value))
            self.storage[key] = self.DLL.head

        # If we're not at the limit just add newest values to the head
        # and add entry to our dict
        else:
            self.DLL.add_to_head((key, value))
            self.storage[key] = self.DLL.head