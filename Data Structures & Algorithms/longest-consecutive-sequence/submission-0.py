class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_consec = 0
        for num in num_set:
            if ( num -1) not in num_set: # check for start of a consecutive set
                length =1 

                # count up the sequence in num_set
                while (num+length) in num_set:
                    length +=1
                longest_consec = max(longest_consec, length)
        return longest_consec