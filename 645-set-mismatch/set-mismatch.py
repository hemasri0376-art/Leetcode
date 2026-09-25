class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = -1
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        total_sum = (n * (n + 1)) // 2
        actual_sum = sum(set(nums))
        missing = total_sum - actual_sum
        return [duplicate, missing]
