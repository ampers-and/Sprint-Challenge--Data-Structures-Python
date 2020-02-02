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
        # TO BE COMPLETED
        if not self.head:
            return None

        if not self.head.get_next():
            return self.head

        else:
            temp1 = self.head
            temp2 = temp1.get_next()
            temp3 = temp1

            while temp2.get_next():
                temp2 = temp2.get_next()
                temp3 = temp3.get_next()

            self.add_to_head(temp2.get_value())
            temp3.set_next(None)
            temp1 = self.head

            while temp1:  # loop 1
                if temp1.get_next():
                    temp2 = temp1.get_next()
                    temp3 = temp1
                    curr_next = temp1.get_next()

                    if not temp2.get_next():
                        temp3 = temp3.get_next()
                    while temp2.get_next():  # loop 2
                        temp2 = temp2.get_next()
                        temp3 = temp3.get_next()

                    temp1.set_next(temp2)
                    temp2.set_next(curr_next)
                    temp3.set_next(None)
                temp1 = temp1.get_next()

        self.print_list()

    def print_list(self):
        if not self.head:
            print(None)

        else:
            current = self.head
            list_to_print = []

            while current:
                list_to_print.append(current.value)
                current = current.get_next()

            print(list_to_print)

# We need to keep a reference to 3 nodes
# to reverse the list in a single loop
# left -> cur -> right
#   left = self.head
#   cur = left.get_next()
#   left.set_next(None)
#   while cur and cur.get_next():
#   right = cur.get_next()
#   cur.set_next(left)
#   left = cur
#   cur = right
#   cur.set_next(left)
# Update HEAD after we've processed
# the last element
# self.head = cur 
