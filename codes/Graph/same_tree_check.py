#check whether two trees are same or not and there node values should be same

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def sameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)

if __name__ == "__main__":
    p=TreeNode(1,TreeNode(2),TreeNode(3))
    q=TreeNode(1,TreeNode(2), TreeNode(3))
    sol=Solution()
    print(sol.sameTree(p,q))

