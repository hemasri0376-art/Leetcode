class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        c=1
        maxi=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                c+=1
            else:
                c=1
            maxi=max(maxi,c)        
        return  maxi        
