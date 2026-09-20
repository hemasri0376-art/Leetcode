class Solution:
    def reverseDegree(self, s: str) -> int:
        su=0
        for i in range(len(s)):
            ans=(27-(ord(s[i])-96))*(i+1)
            su+=ans
        return su   