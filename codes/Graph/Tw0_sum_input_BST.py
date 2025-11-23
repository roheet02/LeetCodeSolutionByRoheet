#BST tree
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def findtarget(self,root,k):
        ls=set()
        def dfs(node):
            if not node:
                return False
            if (k-node.val) in ls:
                return True
            ls.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)


result = Solution().findtarget(root,9)
print(result)
#BST tree
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def findtarget(self,root,k):
        ls=set()
        def dfs(node):
            if not node:   #check whether node is present it or not 
                return False
            if (k-node.val) in ls: #do traverse and append in above list
                return True
            ls.add(node.val)
            return dfs(node.left) or dfs(node.right) #and change node either left or right 
        return dfs(root)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)


result = Solution().findtarget(root,9)
print(result)