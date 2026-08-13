from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dictionary = defaultdict(list)
        for s in strs:
            count = [0]* 26 # [0,0,0,0,...,0] scorecard per string input
            for char in s: 
                count[ord(char) - ord('a')] += 1 #cab = [1, 1, 1, 0, ... 0]
            ## now count is a list of lowercase letters tally
            group_dictionary[tuple(count)].append(s) # make list immutable tuple and setup dictionary with [] of words
        return list(group_dictionary.values())
        # group_dictionary .keys() gives us scorecards, .values() gives us the lists.
        
