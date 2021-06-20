class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max=nums[0]
        cur_sum=nums[0]
        i,j=0,1
        while j<len(nums):
            if nums[j]+cur_sum<nums[j]:
                cur_sum=nums[j]
            else:
                cur_sum+=nums[j]
            cur_max=max(cur_sum,cur_max)
            j+=1
        return cur_max