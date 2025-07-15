from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        srow = scol = 0
        erow = len(matrix) - 1
        ecol = len(matrix[0]) - 1
        result = []
          
        while srow <= erow and scol <= ecol:      
            for j in range (scol,ecol + 1):
                result.append(matrix[srow][j])
            
            for i in range(srow + 1, erow + 1):
                result.append(matrix[i][ecol])
                
            for j in range (ecol - 1,scol - 1, -1):
                if srow == erow :
                    break
                result.append(matrix[erow][j])
                
            for i in range(erow - 1, srow, -1):
                if ecol == scol:
                    break
                result.append(matrix[i][scol])
            
            srow += 1
            scol += 1
            erow -= 1
            ecol -= 1
        return result