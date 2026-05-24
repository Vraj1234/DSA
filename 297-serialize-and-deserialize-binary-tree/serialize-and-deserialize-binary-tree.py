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
        if not root:
            return ""
        q = deque()
        res = ""
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                res+= str(node.val) + ","
            else:
                res+="#,"
                continue
            left = node.left if node.left else None
            q.append(left)
            right = None if not node.right else node.right
            q.append(right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data[:-1]
        ls = data.split(',')
        q = deque()
        i = 0
        head = TreeNode(ls[i])
        temp = head
        q.append(temp)
        i+=1
        while q:
            temp = q.popleft()
            if ls[i] == "#":
                temp.left = None
            else:
                temp.left = TreeNode(ls[i])
                q.append(temp.left)
                
            i+=1
            if ls[i] == "#":
                temp.right = None
            else:
                temp.right = TreeNode(ls[i])
                q.append(temp.right)
            i+=1
            
            
            

        return head

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))