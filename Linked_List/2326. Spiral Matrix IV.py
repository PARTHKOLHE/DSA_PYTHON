from typing import Optional, List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        srow = scol = 0
        erow = m - 1
        ecol = n - 1
        result = [[-1] * n for _ in range(m)]

        while head and srow <= erow and scol <= ecol:
            for j in range(scol, ecol + 1):
                if not head:
                    return result
                result[srow][j] = head.val
                head = head.next

            for i in range(srow + 1, erow + 1):
                if not head:
                    return result
                result[i][ecol] = head.val
                head = head.next

            for j in range(ecol - 1, scol - 1, -1):
                if not head:
                    return result
                if srow == erow:
                    break
                result[erow][j] = head.val
                head = head.next

            for i in range(erow - 1, srow, -1):
                if not head:
                    return result
                if ecol == scol:
                    break
                result[i][scol] = head.val
                head = head.next

            srow += 1
            scol += 1
            erow -= 1
            ecol -= 1
        return result
