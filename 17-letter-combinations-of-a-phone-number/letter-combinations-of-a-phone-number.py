class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []
        temp = ""

        def bt(i, temp):
            if i == len(digits):
                res.append(temp[:])
                return
            
            num = digits[i]
            for ch in mapping[num]:
                temp+=ch
                bt(i+1, temp)
                temp = temp[:-1]
            
        bt(0,"")
        return res
