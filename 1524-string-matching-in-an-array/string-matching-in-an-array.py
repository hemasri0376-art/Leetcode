class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        res=[]
        n=len(words)
        for i in range(n):
            for j in range(n):
                if i!=j and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res            