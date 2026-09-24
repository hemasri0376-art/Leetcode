class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        res=""
        for i in words:
            if i==i[::-1]:
                res+=i
                break
        return res        