class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,val):
        if not self.root:
            self.root=Node(val)
        else:
            self._insert(val,self.root)
    
    def _insert(self,val,curr):
        if val<curr.val:
            if not curr.left:
                curr.left=Node(val)
            else:
                self._insert(val, curr.left)
        else:
            if not curr.right:
                curr.right=Node(val)
            else:
                self._insert(val,curr.right)
    
    def search(self,val):
        return self._search(val,self.root)

    def _search(self,val,curr):
        if not curr:
            return False
        if curr.val==val:
            return True
        if val <curr.val:
            return self._search(val,curr.left)
        else:
            return self._search(val, curr.right)

    def inorder_traversal(self, curr=None):
        if curr is None:
            curr =self.root
        if curr:
            self.inorder_traversal(curr.left)
            print(curr.val)
            self.inorder_traversal(curr.right)