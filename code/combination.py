class Solution(object):
    def helper(self,index,candidates,target,result):
        if target==0:
            self.global_result.append(list(result))
        else:
            for i in range(index,len(candidates)):
                if target-candidates[i]<0:
                    continue
                if target-candidates[i]>=0:
                    result.append(candidates[i])
                    self.helper(i,candidates,target-candidates[i],result)
                    result.pop()
                    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.global_result=[]
        result=[]
        for i in range(len(candidates)):
            if target-candidates[i]<0:
                continue
            if target-candidates[i]>=0:
                result.append(candidates[i])
                self.helper(i,candidates,target-candidates[i],result)
                result.pop()
        return self.global_result