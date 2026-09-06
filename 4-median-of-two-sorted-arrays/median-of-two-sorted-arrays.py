class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1<=n2:
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1
        
        l,r = 0, len(smaller)
        half_size = (n1+n2)//2
        while l<=r:
            mid = l + ((r-l)//2)
            l2 = float('-inf') if mid == 0 else smaller[mid-1]
            r2 = float('inf') if mid == len(smaller) else smaller[mid]
            l1 = float('-inf') if half_size-mid-1 < 0 else larger[half_size-mid-1]
            r1 = float('inf') if half_size-mid == len(larger) else larger[half_size-mid]
            if l1<=r2 and l2<=r1:
                if (n1+n2)%2 == 0: #even
                    return float((max(l1,l2) + min(r1,r2))/2)
                else:
                    return float(min(r1,r2))
                
            elif l1 > r2:
                l = mid+1
            else:
                r = mid-1