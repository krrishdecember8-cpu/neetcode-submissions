# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        
        while queue:
            n = len(queue)
            
            for i in range(n):
                current_node = queue.popleft()
                
                # 💡 THE MAGIC TRICK: 
                # If 'i' is equal to 'n - 1', we are currently looking at the 
                # absolute LAST node on this level. Grab its value immediately!
                if i == n - 1:
                    ans.append(current_node.val)
                
                # Standard child processing
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
        return ans
  
                

                
                    

            


    
        


        