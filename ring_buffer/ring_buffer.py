from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # case 1: if have not reached max capacity, add
        # use DLL length to check capacity
        # then add item to tail as it is the newest element
        # now, point current to the newest addition???
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail 

        # case 2: if reached max, then overwrite
        if self.storage.length == self.capacity:

            # fix current to the item
            self.current.value = item

            # if pointer is pointing at tail, 
            # meaning it has reached the end of the DLL
            # then replace the oldest with the newest

            # if pointer has not reached the tail yet,
            # i.e. if d != c
            # then keep going
            # until c = c
            if self.current is self.storage.tail:
                # set the current value to the head as the newest addition
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # set pointer to the head/oldest
        current = self.storage.head

        # as long as list isn't empty
        while current != None:
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
