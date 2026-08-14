class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for char in s:
            #is closing - check top of stack (last element) 
                #if it matches remove from stack.
                #else invalid close - return False
            #is opening (not in bracket_map) - add to stack    
            if char in bracket_map:
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else: return False
            else: 
                stack.append(char)
        return len(stack) == 0