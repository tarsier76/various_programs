class LinkedList:
    def add_to_tail(self, node):
        current_node = self.head 
        if not current_node:
            self.head = node 
        else:
            while current_node.next:
                current_node = current_node.next 
            current_node.next = node 

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val