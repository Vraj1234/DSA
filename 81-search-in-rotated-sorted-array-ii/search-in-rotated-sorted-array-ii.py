class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n-1

        def bs(l,r,target):
            while l<=r:
                mid = (l+r)//2
                if target == nums[mid]:
                    return True
                elif target< nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            
            return False

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l+=1
                r-=1
                continue
            if nums[l] <= nums[mid]: #first half is sorted
                if nums[l]<= target <= nums[mid]: #element exists in sorted part
                    return bs(l,mid,target)
                else: #element not in unsorted part
                    l = mid+1
            else: #second half is sorted
                if nums[mid]<= target <= nums[r]: #element exists in sorted part
                    return bs(mid,r,target)
                else: #element not in unsorted part
                    r = mid-1

        return False