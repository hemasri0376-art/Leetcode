from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res=[]
        for i in permutations(nums):
            res.append(i)
        return res    