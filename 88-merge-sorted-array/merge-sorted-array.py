class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return 
        
        if m == 0:
            nums1[:] = nums2
            return
        
        l1, l2 = m-1, n-1
        r = len(nums1)-1
        while l2>=0 and l1>=0:
            if nums1[l1]>=nums2[l2]:
                nums1[r] = nums1[l1]
                l1-=1
                r-=1
            else:
                nums1[r] = nums2[l2]
                l2-=1
                r-=1
        
        if l1<0:
            for i in range(l2+1):
                nums1[i] = nums2[i]

        return


        