from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # if max storage already, overwrite
        if self.storage.length == self.capacity:
            self.current.value = item

            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

        else:
            # just add to tail
            self.storage.add_to_tail(item)
            # make the pointer add to the latest addition
            self.current = self.storage.tail
            
    def get(self):
        # like the get_max() function
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        #look at the head first as it is the oldest
        current = self.storage.head

        while current != None:
            # go to next node
            list_buffer_contents.append(current)
            current = current.next
            
        return list_buffer_contents



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
