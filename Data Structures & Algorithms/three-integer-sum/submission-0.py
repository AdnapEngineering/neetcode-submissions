class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums) # must sort first and can use two pointers
        res=[]
        #loop through and set as anchor because a + b+ c = 0 so b +c = -a 
        for i, val in enumerate(sorted_nums):
            if val > 0 : break # needed because no three positive nums can sum to 0
            if i > 0 and val == sorted_nums[i-1]: continue # skip duplicates

            left = i+1
            right = len(sorted_nums) -1

            # two pointer squeeze
            while left < right:
                three_sum = val + sorted_nums[left] + sorted_nums[right]
                if three_sum > 0: right -=1
                elif three_sum <0: left +=1
                else: # match to 0
                    res.append([val, sorted_nums[left], sorted_nums[right]])

                    left += 1
                    right -= 1

        return res
