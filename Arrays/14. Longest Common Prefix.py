from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ""

        for j in range(len(strs[0])):
            ch = strs[0][j]
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != ch:
                    return result
            result += ch

        return result
