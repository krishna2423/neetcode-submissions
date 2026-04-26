class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            idx = len(temperatures) - 1 - i
            val = temperatures[idx]
        
            while stack and val >= stack[-1][0]:
                stack.pop()
            if not stack:
                result[idx] = 0 
            else:
                result[idx] = stack[-1][1] - idx

            stack.append([val, idx])
            
        return result


