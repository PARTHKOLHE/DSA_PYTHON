from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for a in range(len(matrix[0])):
                        if matrix[i][a] != 0:
                            matrix[i][a] = -1
                    for b in range(len(matrix)):
                        if matrix[b][j] != 0:
                            matrix[b][j] = -1
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == -1:
                    matrix[x][y] = 0
