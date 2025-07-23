#User function Template for python3
import heapq
class Solution:    
    def minimumPlatform(self,arr,dep):
        n = len(arr)
        trains = sorted(zip(arr, dep), key = lambda x: x[0])
        heap = []
        heapq.heappush(heap,trains[0][1])
        
        for i in range(1, n):
            if trains[i][0] > heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, trains[i][1])
        
        return len(heap)
                
                
                
        