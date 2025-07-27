class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = sorted(zip(deadline,profit),key = lambda x:x[1], reverse=True)
        max_deadline = max(deadline)
        slots = [-1] * (max_deadline + 1)
        
        count = 0
        total_profit = 0
        
        for d,p in jobs:
            for t in range(d,0,-1):
                if slots[t] == -1:
                    slots[t] = p
                    count += 1
                    total_profit += p
                    break
        return[count,total_profit]
        
        
        
        