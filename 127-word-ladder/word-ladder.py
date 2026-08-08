class Solution:
    def ladderLength(self, start: str, end: str, wordList: List[str]) -> int:
        words = set(wordList)
        words.add(start)
        

        adj = defaultdict(list)
        for word in words: 
            for i in range(len(word)):
                temp = ""
                for j in range(ord('a'), ord('z')+1):
                    temp = word[:i]+chr(j)+word[i+1:]
                    if temp in words and temp != word:
                        adj[word].append(temp)

        q = deque()
        vis = set()
        cur = start
        q.append(start)
        vis.add(start)
        depth = 0
        while q:
            l = len(q)
            depth+=1
            for i in range(l):
                w = q.popleft()
                if w == end:
                    return depth
                for nei in adj[w]:
                    if nei not in vis:
                        q.append(nei)
                        vis.add(nei)     
        
        return 0