class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j=0,0
        cur_sum=0
        result=float('inf')
        while j<len(nums):
            cur_sum+=nums[j]
            if cur_sum<target:
                j+=1           
            else:
                result=min(result,j-i+1)
                if result==1:
                    break
                cur_sum-=(nums[i]+nums[j])
                i+=1
            
        return 0 if result==float("inf") else result