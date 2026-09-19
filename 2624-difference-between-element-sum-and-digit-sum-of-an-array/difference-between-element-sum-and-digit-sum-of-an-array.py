class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        s=sum(nums)
        add=0
        for i in nums:
            while i>0:
                r=i%10
                add+=r
                i=i//10
        return abs(s-add)        