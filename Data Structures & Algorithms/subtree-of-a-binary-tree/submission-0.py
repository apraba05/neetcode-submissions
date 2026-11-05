# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def sub(p,q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return sub(p.left,q.left) and sub(p.right,q.right)

        def hasSubTree(root):
            if not root:
                return False
            
            if sub(root,subRoot):
                return True
        
            return hasSubTree(root.left) or hasSubTree(root.right)
        
        return hasSubTree(root)
        # Time: O(m*n)
        # Space: O(h1 + h2)