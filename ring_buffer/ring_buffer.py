from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # 2 cases - capacity - length of dll = capacity and not

        # print("Initial: ", self.get(), " ",
        #       self.storage.length, " Current: ", self.current)

        if self.storage.length == self.capacity:

            node = self.storage.head

            while node.value != self.current:
                node = node.next

            # print("val f: ", node.value)
            # print(self.storage.tail.value)
            # print(node == self.storage.tail)

            if node == self.storage.tail:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = item

            else:
                if node.next == self.storage.tail:
                    self.storage.remove_from_tail()
                    self.storage.add_to_tail(item)

                else:
                    self.storage.delete(node.next)
                    node.insert_after(item)
                    self.storage.length += 1

                self.current = item

            # print("After: ", self.get(), " Current: ", self.current)

        else:
            self.storage.add_to_tail(item)
            self.current = item

            # print("After: ", self.get())

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head

        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents


r = RingBuffer(5)
r.append("a")
r.append("b")
r.append("c")
r.append("d")
print("Should have 4: ", r.get())

r.append("e")
print("Should have 5: ", r.get())

r.append("f")
print("Should replace 'a': ", r.get())

r.append("g")
r.append("h")
r.append("i")
print("Should end with 'e': ", r.get())

r.append("j")
r.append("k")
print("Should sandwich between 'k' and 'j': ", r.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):

        self.capacity = capacity
        self.current = None
        self.storage = [None for i in range(capacity)]

    def append(self, item):

        # if len(self.storage) == self.capacity:

        if self.storage[self.capacity - 1] == self.current:
            self.storage[0] = item
            self.current = item

        else:
            i = self.storage.index(self.current)
            self.storage[i+1] = item
            self.current = item

        # else:
        #     self.storage.append(item)
        #     self.current = item

    def get(self):
        list_buffer = []

        for val in self.storage:
            if val:
                list_buffer.append(val)

        return list_buffer


a = ArrayRingBuffer(5)
a.append("a")
a.append("b")
a.append("c")
a.append("d")
print("Should have 4: ", a.get())

a.append("e")
print("Should have 5: ", a.get())

a.append("f")
print("Should replace 'a': ", a.get())

a.append("g")
a.append("h")
a.append("i")
print("Should end with 'e': ", a.get())

a.append("j")
a.append("k")
print("Should sandwich between 'k' and 'j': ", a.get())
