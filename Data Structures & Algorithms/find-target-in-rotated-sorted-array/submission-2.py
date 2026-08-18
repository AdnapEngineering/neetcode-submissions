class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <=r:
            mid = (r+l)//2
            mid_val = nums[mid]
            if target == mid_val: return mid
            if nums[l] <= mid_val: # left side sorted, make check
                if nums[l] <= target < mid_val:
                    r = mid-1
                else: l = mid+1
            else: ## right side sorted
                if mid_val < target <= nums[r]:
                    l = mid + 1
                else: r = mid-1

        return -1