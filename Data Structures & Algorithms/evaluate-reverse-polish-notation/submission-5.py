class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                second = stack.pop()
                first = stack.pop()
                if tokens[i] == '+':
                    stack.append(first + second)
                elif tokens[i] == '-':
                    stack.append(first - second)
                elif tokens[i] == '*':
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
    
        return stack[0]