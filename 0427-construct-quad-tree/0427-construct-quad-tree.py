"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)-1
        def getNode(top, bottom, left, right):
            # print("top: {}, bottom: {}, left: {}, right:{}".format(top, bottom, left, right))
            if top == bottom and left == right:
                return Node(grid[top][left], True, None, None, None, None)
            node = Node(-1, False, None, None,None,None)
            half = top + (bottom - top)//2
            ralf = left + (right - left) // 2
            node.topLeft = getNode(top, half, left, ralf)
            node.topRight = getNode(top, half, ralf+1, right)
            node.bottomLeft = getNode(half+1, bottom, left, ralf)
            node.bottomRight = getNode(half+1, bottom, ralf+1, right)
            return node
        ans = getNode(0, n, 0, n)
        
        def update(node):
            if node.isLeaf:
                return
            update(node.topLeft)
            update(node.topRight)
            update(node.bottomLeft)
            update(node.bottomRight)
            if node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val:
                if node.topLeft.val != -1:
                    node.isLeaf = True
                    node.val = node.topLeft.val
                    node.topLeft = node.topRight = node.bottomLeft = node.bottomRight = None                
            return
        update(ans)
        return ans