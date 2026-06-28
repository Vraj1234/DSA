class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        res = []
        n = len(digits)
        def dfs(temp, i):
            if i == n:
                res.append(temp)
                return
            
            for ch in mapping[int(digits[i])]:
                temp += ch
                dfs(temp, i+1)
                temp = temp[:-1]
        
        dfs("", 0)
        return res
            
