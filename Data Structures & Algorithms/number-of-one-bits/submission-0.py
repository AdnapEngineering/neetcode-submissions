class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1 # returns 1 if both are 1
            n = n >> 1

        return count
