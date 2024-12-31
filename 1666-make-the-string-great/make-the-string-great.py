class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for val in s:
            if stack and stack[-1] != val and stack[-1].lower() == val.lower():
                    stack.pop()
            else:
                stack.append(val)

        return "".join(stack)