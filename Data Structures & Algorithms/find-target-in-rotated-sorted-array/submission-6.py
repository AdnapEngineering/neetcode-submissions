class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search to get logn time,  should use two pointers
        l,r = 0 , len(nums) -1 # pointer indicies
        while l <= r:
            mid = ( r + l ) // 2 # No Int overflow due to arbitatry presicion 
            if target == nums[mid]:
                return mid
            ## check which is sorted l or r of mid
            if nums[l] <= nums[mid]: 
                # look for value in left sorted
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else: l = mid + 1
            else:
                # right must be sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else: r = mid - 1
    
        return -1