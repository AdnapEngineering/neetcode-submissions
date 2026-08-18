class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) -1
        while l <=r:
            mid = (r+l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target: # we know it's left side so set r to mid and do again
                r = mid - 1
            else: 
                l = mid +1

        return -1    