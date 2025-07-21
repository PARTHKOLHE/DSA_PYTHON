#User function Template for python3

class Solution:   
    def minimumPlatform(self,arr,dep):
        nums = []
        for a,d in zip(arr,dep):
            nums.append([a,d])
            
        nums.sort(key = lambda x: (x[1],x[0]))
        count = 0
        min_val = []
        
        for i in range(len(nums)):
            for j in range(len(min_val)):
                if nums[i][0] > min_val[j]:
                    min_val.pop(j)
                    min_val.append(nums[i][1])
                    
                else:
                    count += 1
                    min_val.append(nums[i][1])
        return count
                
                
                
        