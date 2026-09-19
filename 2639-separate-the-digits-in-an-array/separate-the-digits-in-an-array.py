class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res=[]
        for i in nums:
            for j in str(i):
                res.append(int(j))
        return res            