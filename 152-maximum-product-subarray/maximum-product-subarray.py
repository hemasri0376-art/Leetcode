class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=nums[0]
        mini=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            curr=nums[i]
            temp=max(curr,maxi*curr,mini*curr)
            mini=min(curr,mini*curr,maxi*curr)
            maxi=temp
            res=max(maxi,res)
        return res    