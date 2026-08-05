class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = defaultdict(list)
        for i,ch in enumerate(s):
            if ch not in map:
                map[ch] = [i,i]
            else:
                map[ch][1] = i
        
        res = []
        temp = []
        for key, val in map.items():
            if not temp:
                temp = val
                continue
            if val[0] <= temp[1]:
                temp[0] = min(val[0], temp[0])
                temp[1] = max(val[1], temp[1])
            else:
                res.append(temp[1]-temp[0]+1)
                temp.clear()
                temp = val
        if temp:
            res.append(temp[1]-temp[0]+1)
        return res
            
        
            