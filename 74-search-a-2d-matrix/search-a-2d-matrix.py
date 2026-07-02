class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #First narrow down row using BS
        #Narrow down col using BS
        def bs(arr, target):
            l,r = 0, len(arr)-1
            while l<=r:
                mid = l + ((r-l)//2)
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            
            return False

        l, r = 0, len(matrix)-1
        while l<=r:
            mid = l + ((r-l)//2)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return bs(matrix[mid], target)
            elif target < matrix[mid][0]:
                r = mid-1
            else:
                l = mid+1
        
        return False