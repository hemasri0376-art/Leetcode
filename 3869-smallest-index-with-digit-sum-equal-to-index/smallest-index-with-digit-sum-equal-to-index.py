def sums(n):
    s=0
    while n>0:
        r=n%10
        s+=r
        n=n//10
    return s    
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        c=-1
        for i in range(len(nums)):
            if i==sums(nums[i]):
                c=i
                break
        return c        