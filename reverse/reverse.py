class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):

    # set current to the first one
    # set prev to None, as just starting out
    current = self.head
    prev = None

    while current != None:
      # first, save next pointer
      next = current.get_next()

      # second, point current.next to prev
      current.set_next(prev)

      # move along 
      prev = current 
      current = next 

    # when the while loop has finished
    # prev is sitting at the new head (the "end" now the "start" of the SLL)
    # so assign the new head to prev
    self.head = prev

# best resource: https://www.youtube.com/watch?v=O0By4Zq0OFc
    
