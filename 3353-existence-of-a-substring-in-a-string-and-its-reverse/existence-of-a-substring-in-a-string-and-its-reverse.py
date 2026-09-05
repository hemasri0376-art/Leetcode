from itertools import pairwise
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev=s[::-1]
        return bool(set(pairwise(s)) & set(pairwise(rev)))
