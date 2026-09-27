class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        curr=""
        for i in s:
            if i=='(':
                stack.append(curr)
                curr=""
            elif i==')':
                curr=stack.pop()+curr[::-1]
            else:
                curr+=i
        return curr            