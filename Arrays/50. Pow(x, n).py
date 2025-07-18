class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = 1
        power = abs(n)
        
        while power > 0:
            if power % 2 == 1:
                answer = answer * x
            x = x * x
            power = power // 2
            
        if n < 0:
            answer = 1 / answer
        return round(answer,5)