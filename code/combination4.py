class Solution(object):
    def combinationSum4(self, nums, target):
        arr=[0]*(target+1)
        arr[0]=1
        for i in range(1,target+1):
            for j in nums:
                if i-j>=0:
                    arr[i]+=arr[i-j]
        return arr[target]