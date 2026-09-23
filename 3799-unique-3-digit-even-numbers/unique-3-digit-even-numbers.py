import itertools
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res=set()
        for i in itertools.permutations(digits,3):
            if i[0]==0:
                continue
            ans=i[0]*100+i[1]*10+i[2]
            if ans%2==0:
                res.add(ans)
        return len(res)            