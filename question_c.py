class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)  # Creating Head Node
        self.tail = Node(None, None)  # Creating Head Node
        # Point Head to Tail and vice versa
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        Return Node value if key is found on the Cache and then move this node to the Head of the list, to make it as a Most recently used item,
        Return read data from database (-1)
        """
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        return -1  # Not found, Read data from DB and perform Insert

    def insert(self, key, value):
        """
        @param key, value
        If get duplicate item, remove that node and move it to head as a Most Recently used item
        If get new Item, add item to Top of the List and add to cache
        If get new Item but the cache is full, Remove the Least Recently used Item (The Last one), add the item to Top of the List and add to cache
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                removed_node = self.remove_tail()
                del self.cache[removed_node.key]
            new_node = Node(key, value)
            self.add_to_head(new_node)
            self.cache[key] = new_node

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def add_to_head(self, node):
        """
        @param node, to remove current Node from the list
        Add the current node top of the list (After Head)
        """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        """
        @param node, to remove current Node from the list
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def remove_tail(self):
        if len(self.cache) > 0:
            tail_node = self.tail.prev
            self.remove_node(tail_node)
            return tail_node

    def get_cache(self):
        """
        @return dict
        Returns the cache dict
        """
        return self.cache

    def get_list(self):
        """
        @return list
        Returns the whole doubly link list using a list
        """
        current_node = self.head.next
        linked_list = []
        while current_node is not None and current_node != self.tail:
            linked_list.append(current_node.value)
            current_node = current_node.next
        return linked_list


# Example usage:
lru_cache = LRUCache(2)  # Set storage capacity = 2

lru_cache.insert(1, 1)  # Insert 1 to cache : Cache status [1]
lru_cache.insert(2, 2)  # Insert 2 to cache : Cache status [2, 1]
print(lru_cache.get_list())

print(lru_cache.get(1))  # Least recently used 1 moves to the top : Cache status [1, 2]
print(lru_cache.get_list())


print(lru_cache.get(3))  # Not found, Return -1

lru_cache.insert(5, 5)  # Insert 5 to cache and evicts 2 : Cache status [5,1]
print(lru_cache.get_list())

print(lru_cache.get(1))  # Least recently used 1 moves to the top : Cache status [1, 5]
print(lru_cache.get_list())
