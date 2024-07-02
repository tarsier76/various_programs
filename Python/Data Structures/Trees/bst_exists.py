class BSTNode:
    def exists(self, val):
        found = False 

        if self.left:
            state_left = self.left.exists(val)
            if state_left == True:
                return state_left

        if self.right:
            state_right = self.right.exists(val)
            if state_right == True:
                return state_right

        if self.val == val:
            found = True

        return found

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
