import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # for this function to work, must already have a tree or root existing
        # if value < self.value, go left 
        # else go right
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
                # keep going -- recursion 
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
                # keep going
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        # base case:
        if target == self.value:
            return True 
        
        # left side
        elif target < self.value:
            if self.left == None:
                return False 
            else: 
                # recurse
                return self.left.contains(target)
        
        # right side
        else: 
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        if self.right != None:
            # recurse
            return self.right.get_max()
        else: 
            return self.value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        # check left
        if self.left != None:
            self.left.for_each(cb)
        
        # check right
        if self.right != None:
            self.right.for_each(cb)

duplicates = []   

# create a binary search tree with all the names in names_1
# instantiate BST with very first name
names = BinarySearchTree(names_1[0])

# insert rest of the names to create the BST
for name in names_1:
    names.insert(name)

# now loop through names_2
for index in range(len(names_2)):
    # if there is a match, append to duplicates []
    if names.contains(names_2[index]):
        duplicates.append(names_2[index])

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
print(set(names_1) & set(names_2), len(set(names_1) & set(names_2)))

print(set(names_1).intersection(names_2))