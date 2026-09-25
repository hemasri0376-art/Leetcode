class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res=[]
        for i in range(len(tasks)):
            res.append(sum(tasks[i]))
        return min(res)    