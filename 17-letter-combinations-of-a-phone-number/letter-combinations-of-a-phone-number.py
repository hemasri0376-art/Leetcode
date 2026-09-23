class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        combi={
            2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",
            7:"pqrs",8:"tuv",9:"wxyz"
        }
        res=[""]
        for i in digits:
            ans=combi[int(i)]
            res=[k+j for k in res for j in ans]
        return res    
