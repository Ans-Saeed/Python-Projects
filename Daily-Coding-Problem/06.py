import ctypes

# Node class for XOR linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.both = None

class XORLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = []

    def add(self, element):
        node = Node(element)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.both = ctypes.cast(self.tail, ctypes.py_object).value ^ id(node)
            self.tail.both = ctypes.cast(id(self.tail) ^ id(node), ctypes.py_object).value
            self.tail = node
        self.__nodes.append(node)

    def get(self, index):
        if index >= len(self.__nodes):
            return None
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both
            if next_id:
                prev_id = id(node)
                node = ctypes.cast(next_id, ctypes.py_object).value
            else:
                return None
        return node.val