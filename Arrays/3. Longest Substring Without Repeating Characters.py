class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        count = 1
        st = "s[0]"
        for i in range(1, len(s)):
            for j in range(len(s)):
                if s[i] == st[j]:
                    if max_count < count:
                        max_count = count

            else:
                st += s[i]
                count += 1
