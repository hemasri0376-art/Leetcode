class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        word=""
        for i in words:
            word+=i
            if word==s:
                return True
            if len(word)>len(s):
                break
        return False            