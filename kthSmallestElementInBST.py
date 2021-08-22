"""https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Medium

EG:     
        3
       / \
      1   4
    /
   2
    Input: root = [3,1,4,null,2], k = 1
    Output: 1  


             5
            / \
           3   6
          / \
        2    4
       /
      1
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# my solution, recursive inorder traversal
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        traversal = []
        self.kthSmallestDFS(root, k, traversal)

        return traversal[k-1]

    def kthSmallestDFS(self, root, k, traversal):
        if root is None:
            return
        self.kthSmallestDFS(root.left, k, traversal)
        traversal.append(root.val)
        self.kthSmallestDFS(root.right, k, traversal)
        return traversal


# iterative inorder traversal solution (QUITE SMART)
# class Solution:
#     def kthSmallest(self, root, k):
#         """
#         :type root: TreeNode
#         :type k: int
#         :rtype: int
#         """
#         stack = []

#         while True:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             k -= 1
#             if not k:
#                 return root.val
#             root = root.right
