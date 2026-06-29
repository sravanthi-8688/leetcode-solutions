# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodes = {}
        children = set()

        for x, y, is_left in descriptions:
            if x not in nodes:
                nodes[x] = TreeNode(x)
            if y not in nodes:
                nodes[y] = TreeNode(y)
            if is_left:
                nodes[x].left = nodes[y]
            else:
                nodes[x].right = nodes[y]
            children.add(y)

        for x, node in nodes.items():
            if x not in children:
                return node
        