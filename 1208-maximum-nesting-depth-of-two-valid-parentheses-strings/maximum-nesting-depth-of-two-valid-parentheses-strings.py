class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        return [(i + (c == '(')) % 2 for i, c in enumerate(seq)]