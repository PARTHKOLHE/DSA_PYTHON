import math
from typing import List
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            gifts.sort()
            gift_val = math.isqrt(gifts[-1])
            gifts.pop(-1)
            gifts.append(gift_val)
        return sum(gifts)