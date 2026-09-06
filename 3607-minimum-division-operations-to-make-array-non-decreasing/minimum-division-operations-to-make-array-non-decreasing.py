from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def smallest_prime_factor(n):
            if n%2==0:
                return 2
            factor=3
            while factor*factor<=n:
                if n%factor==0:
                    return factor
                factor+=2
            return n
        operations = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=nums[i+1]:
                continue
            nums[i]=smallest_prime_factor(nums[i])
            operations+=1
            if nums[i]>nums[i+1]:
                return -1

        return operations