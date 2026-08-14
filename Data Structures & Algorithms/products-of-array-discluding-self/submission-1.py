class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## We could just loop throug hthe array and multiply everything together, and for every index, divide that total by the value, when not 0 and store it in a returned array. O(2n) However for this we will use pre-fix and postfix
        length = len(nums)
        res = [1] * length
        prefix = 1
        for i in range(length):
            res[i] = prefix 
            prefix *= nums[i]
        postfix = 1
        for i in range(length -1, -1, -1):
            res[i] *= postfix
            postfix *=nums[i]


        return res
