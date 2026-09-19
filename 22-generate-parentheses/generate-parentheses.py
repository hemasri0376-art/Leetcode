class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def build_pair(curr,opend,close):
            if len(curr)==2*n:
                res.append(curr)
            if opend<n:
                build_pair(curr +"(",opend+1,close)    
            if close <opend:
                build_pair(curr+")",opend,close+1)
        build_pair("",0,0)
        return res        