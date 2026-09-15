class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        results =[0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                mul = digit1 * digit2
                p1, p2 = i + j, i + j + 1
                total = mul + results[p2]
                
                results[p1] += total // 10
                results[p2] = total % 10          
        ans = []
        for digit in results:
            if not (len(ans) == 0 and digit == 0):
                ans.append(chr(digit + ord('0')))         
        return "".join(ans)