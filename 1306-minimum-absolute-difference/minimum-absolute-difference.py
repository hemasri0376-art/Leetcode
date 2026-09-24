class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        res=[]
        arr.sort()
        diff=float('inf')
        for i in range(len(arr)-1):
            curr=arr[i+1]-arr[i]
            if curr<diff:
                diff=curr
                res = [[arr[i], arr[i+1]]]
            elif curr==diff:
                res.append([arr[i],arr[i+1]])    
        return res        