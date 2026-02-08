class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0

        mn = sys.maxsize
        for x in strs:
            if len(x) < mn:
                mn = len(x)
                smallest = x

        while i < mn:
            target = strs[0][i] #f
            for s in strs:
                if s[i] != target: #
                    return res
            res+=s[i]
            i+=1
        return res