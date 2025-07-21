class Solution:
    def maxMeetings(self, start, end):
        nums = []
        for s, e in zip(start, end):
            nums.append([s, e])
            
        nums.sort(key=lambda x: (x[1], x[0]))
        count = 1
        last_time = nums[0][1]
        
        for i in range(len(nums)):
            if nums[i][0] > last_time:
                count += 1
                last_time = nums[i][1]
        return count

            