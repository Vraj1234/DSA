class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # res = set()
        # def f(s, temp):
        #     if s == target:
        #         temp.sort()
        #         res.add(tuple(temp[:]))
        #         return
            
        #     if s >target:
        #         return
            
        #     for i in range(len(candidates)):
        #         temp.append(candidates[i])
        #         s+=candidates[i]
        #         f(s,temp)
        #         num = temp.pop()
        #         s-=num
        
        # f(0, [])
        # return [list(x) for x in res]

        res = set()
        def f(s, temp):
            if s == target:
                new = temp[:]
                new.sort()
                res.add(tuple(new))
                return
            
            if s >target:
                return
            
            for i in range(len(candidates)):
                temp.append(candidates[i])
                s+=candidates[i]
                f(s,temp)
                num = temp.pop()
                s-=num
        
        f(0, [])
        return [list(x) for x in res]