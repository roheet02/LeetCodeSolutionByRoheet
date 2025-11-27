#Mirror and symentree check

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
#solution
class Solution():
    def isSymmetric(self,root):
        if not root:
            return True
        return self.isMirror(root.left,root.right)
    #helper function to check whether tree is mirror ot not and we are using recursion here 
    def isMirror(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val!=right.val:
            return False
        return self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)
    

if __name__ == "__main__":
    # p=TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(3,TreeNode(3),TreeNode(4)))
    p = TreeNode(1,TreeNode(2, TreeNode(3), TreeNode(4)),TreeNode(2, TreeNode(4), TreeNode(3)))    
    sol=Solution()
    print(sol.isSymmetric(p))

