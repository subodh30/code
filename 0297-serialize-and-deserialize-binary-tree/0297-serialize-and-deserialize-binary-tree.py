# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:  
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ser = ""
        def preorder(root):
            nonlocal ser
            if root==None:
                ser+="N,"
                return
            ser+=str(root.val)
            ser+=","
            preorder(root.left)
            preorder(root.right)
            
        preorder(root)
        return ser[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        if len(arr) == 0:
            return None
        i = 0
        def create(arr):
            nonlocal i
            if i >= len(arr) or arr[i] == 'N':
                return None
            
            node = TreeNode(arr[i])
            i+=1
            node.left = create(arr)
            i+=1
            node.right = create(arr)
            return node
        return create(arr)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))