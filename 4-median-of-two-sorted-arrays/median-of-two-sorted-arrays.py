class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        l1, l2 = 0,0

        while l1< len(nums1) and l2<len(nums2):
            if nums1[l1] <= nums2[l2]:
                res.append(nums1[l1])
                l1+=1
            else:
                res.append(nums2[l2])
                l2+=1
            
        while l1< len(nums1):
            res.append(nums1[l1])
            l1+=1

        while l2< len(nums2):
            res.append(nums2[l2])
            l2+=1
        
        #print(res)
        if len(res)%2 == 1:
            return res[len(res)//2]
        else:
            h = res[len(res)//2]
            l = res[len(res)//2 - 1]
            return (l+h)/2