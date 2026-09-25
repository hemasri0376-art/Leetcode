class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        c=0
        s=sum(apple)
        capacity.sort(reverse=True)
        total=0
        for i in capacity:
            total+=i
            c+=1
            if total>=s:
                break
        return c        