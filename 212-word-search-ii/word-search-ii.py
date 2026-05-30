class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
        return cur

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        res = set()

        rows = len(board)
        cols = len(board[0])
        vis = set()

        def dfs(i,j,node,w):
            if(i<0 or j<0
            or i>=rows or j>=cols
            or (i,j) in vis
            or board[i][j] not in node.children):
                return 
            
            vis.add((i,j))
            node = node.children[board[i][j]]
            w += board[i][j]
            if node.is_end:
                res.add(w)

            dfs(i+1,j,node,w)
            dfs(i-1,j,node,w)
            dfs(i,j+1,node,w)
            dfs(i,j-1,node,w)

            vis.remove((i,j))

        
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root,"")
        
        return list(res)