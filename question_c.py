class Node:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.node = Node(None)
        self.init = self.node
        self.cache = {}

    def insert(self, value):
        new_node = Node(value)
        self.node.tail = new_node
        self.node.value = value
        new_node.head = self.node
        self.node = new_node
        self.cache[value] = new_node

    def get_list(self):
        current_node = self.init
        linked_list = []
        while current_node.tail != None:
            linked_list.append(current_node.value)
            current_node = current_node.tail
        return linked_list

    def get_cache(self):
        return self.cache


list = LinkedList()

list.insert(10)
list.insert(15)
list.insert(105)
list.insert(13)

print(list.get_list())
print(list.get_cache())
