class MinStack:

    def __init__(self):
        self.self_stack = []
        self.min_stack = []        

    def push(self, val: int) -> None:
        self.self_stack.append(val)

        #if min_stack is empty append, else, check the top and compare for smallest value
        if not self.min_stack:
            self.min_stack.append(val)
        else :
            current_min = self.min_stack[-1]
            self.min_stack.append(min(current_min, val))

    def pop(self) -> None:
        self.min_stack.pop()
        self.self_stack.pop()

    def top(self) -> int:
        return self.self_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
