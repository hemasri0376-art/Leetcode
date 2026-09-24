class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        left,right=p.split('*')
        li=s.find(left)
        ri=s.find(right,li+len(left))
        return li != -1 and ri !=-1