class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        freq={}
        n=len(nums)//2
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i,c in freq.items():
            if c==n:
                return i
                break    