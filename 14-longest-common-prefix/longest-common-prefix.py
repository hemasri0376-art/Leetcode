class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res=[]
        for i in zip(*strs):
            if len(set(i))==1:
                res.append(i[0])
            else:
                break
        return "".join(res)            