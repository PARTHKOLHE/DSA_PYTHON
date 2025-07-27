class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        items = sorted(zip(val,wt),key = lambda x:x[0]/x[1], reverse=True)
        sum_weight = 0
        total_val = 0
        for val,wt in items:    
            if cap > sum_weight + wt:
                sum_weight += wt
                total_val += val
            else:
                remain = cap - sum_weight
                total_val += val * (remain/wt)
                break
        return total_val
                
                      
                      