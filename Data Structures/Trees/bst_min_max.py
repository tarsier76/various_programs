class BSTNode:
    def get_min(self):
        min_so_far = self.val 
        if self.left:
            compared = self.left.get_min()
            if min_so_far > compared:
                min_so_far = compared 
        return min_so_far
        
    def get_max(self):
        max_so_far = self.val
        if self.right:
            compared = self.right.get_max()
            if max_so_far < compared:
                max_so_far = compared 
        return max_so_far

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