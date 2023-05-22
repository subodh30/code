class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x in '+-*/':
                right = stack.pop()
                left = stack.pop()
                if x=='+':
                    stack.append(left+right)
                elif x=='-':
                    stack.append(left-right)
                elif x=='*':
                    stack.append(left*right)
                else:
                    stack.append(int(left/right))
            else:
                stack.append(int(x))
        return stack.pop()
        