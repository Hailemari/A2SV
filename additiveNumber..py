class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):
            for j in range(i+1, n):
                
                if num[0] == "0" and i > 1:
                    break
                if num[i] == "0" and j > i+1:
                    break
                    
                number1 = int(num[:i])
                number2 = int(num[i:j])
                k = j

                while k < n:
                    
                    number3 = number1 + number2
                    if num[k:].startswith(str(number3)):
                        k += len(str(number3))
                        number1 = number2
                        number2 = number3
                    else:
                        break
                if k == n:
                    return True
                
        return False