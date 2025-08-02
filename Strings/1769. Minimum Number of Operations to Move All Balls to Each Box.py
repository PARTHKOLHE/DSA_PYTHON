from typing import List
class Solution:
    def minOperations(boxes: str) -> list[int]:
        n = len(boxes)
        answer = []

        for i in range(n):
            steps = 0
            for j in range(n):
                if boxes[j] == '1':
                    steps += abs(i - j)
            answer.append(steps)

        return answer

                
        