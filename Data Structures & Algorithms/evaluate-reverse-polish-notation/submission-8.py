class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val.lstrip('-').isdigit():
                stack.append(int(val))
            else:
                a = stack.pop()
                b = stack.pop()
                if val == "+":
                    res = a + b
                elif val == '-':
                    res = b - a
                elif val == '*':
                    res = a * b
                elif val == '/':
                    res = int(b/a)
                stack.append(res)
            print(stack)
        return stack.pop()