class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        prev_day_stack = []

        for i, temp in enumerate(temperatures): 
            while prev_day_stack and temp > temperatures[prev_day_stack[-1]]:
                prev_day = prev_day_stack.pop()
                result[prev_day] = i - prev_day
            prev_day_stack.append(i) 
        return result    
