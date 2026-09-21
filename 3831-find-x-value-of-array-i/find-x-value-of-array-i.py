class Solution(object):
    def resultArray(self, nums, k):
        freq=res=[0]*k
        for i in nums:
            i=i%k
            cur=[0]*k
            cur[i]=1
            for x,y in enumerate(freq):
                cur[x*i%k]+=y
            freq=cur
            for x,y in enumerate(freq):
                res[x]+=y
        return res            