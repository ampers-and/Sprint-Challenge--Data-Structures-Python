class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value less that node of current tree
        if value < self.value:
            # go down to left node
            if self.left:
                # if it exists, recurse
                self.left.insert(value)
            else:
                # else, create new BinarySearchTree at node
                self.left = BinarySearchTree(value)

        # repeat with right if value greater than node of current tree
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

        else:
            pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if target == self.value:
            return True

        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value

        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # assume node is current (self.value)
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
        else:
            pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        if node:
            print(node.value)
            if node.left:
                self.bft_print(node.left)
            if node.right:
                self.bft_print(node.right)

        else:
            pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)
        else:
            pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)

        else:
            pass
