from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # if max storage already, overwrite
        if self.storage.length == self.capacity:
            # remove from head
            self.storage.remove_from_head()
            # add new item to tail
            self.storage.add_to_tail(item)

        else:
            # just add to tail
            self.storage.add_to_tail(item)
            #self.current = self.storage.head
            
    def get(self):
        # like the get_max() function
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        #look at the head first as it is the oldest
        current = self.current
        list_buffer_contents.append(current)

        while current != self.storage.head:
            # go to next node
            current = current.next
            # add to list
            list_buffer_contents.append(current)

        return list_buffer_contents



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
