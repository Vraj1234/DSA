class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u,d = 0, len(matrix)-1
        
        def find_row(matrix, u, d):
            while u<=d:
                mid = (u+d)//2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return matrix[mid]
                elif target < matrix[mid][0]:
                    d = mid-1
                else:
                    u = mid+1
            return -1
        
        def find_target(nums, l, r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid]== target:
                    return True
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return False
        
        nums = find_row(matrix, u, d)
        if nums == -1:
            return False

        
        l,r = 0, len(nums)-1 

        return find_target(nums, l, r)

        




