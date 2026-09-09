class Solution:
    def countCommas(self, n: int) -> int:
        maxi=1000
        total_commas=0
        while n>=maxi:
            total_commas+=(n-maxi+1)
            maxi*=1000
        return total_commas    