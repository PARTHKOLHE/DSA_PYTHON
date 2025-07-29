from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        valu = 0
        for i in range (len(operations)):
            if operations[i] == '--X' or operations[i] == 'X--' :
                valu -= 1
            else:
                valu += 1
        return valu