class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a=abs(z-x)
        b=abs(z-y)
        if a>b:
            return 2
        elif b>a:
            return 1
        else:
            return 0        