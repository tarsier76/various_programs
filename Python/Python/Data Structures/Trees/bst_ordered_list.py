class BSTNode:
    def inorder(self, visited):
        if self.left:
            self.left.inorder(visited)

        visited.append(self.val)

        if self.right:
            self.right.inorder(visited)

        return visited

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
