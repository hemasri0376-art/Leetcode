class Solution(object):
    def removeOuterParentheses(self, s):
        stack=[]
        open=0
        for c in s:
            if c=="(" and open>0:
                stack.append(c)
            if c==")" and open>1 :
                stack.append(c)
            if(c=="("): open+=1
            else: open-=1    
        return "".join(stack)            
        