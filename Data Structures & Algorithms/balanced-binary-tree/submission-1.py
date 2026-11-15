class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True  # Start assuming the tree is balanced
        
        def get_height(node):
            if not node:
                return 0  # A null node has a height of 0
            
            # 1. Get the height of both subtrees (each runs exactly once)
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # 2. Check the balance condition at the current node
            if abs(left_height - right_height) > 1:
                self.balanced = False  # Found an unbalanced spot!
                
            # 3. Return the actual height of this node to its parent
            return max(left_height, right_height) + 1

        get_height(root)
        return self.balanced
