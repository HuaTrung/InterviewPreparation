class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        global_result=[]
        candidates=sorted(candidates)
        def helper(index,remain,result):
            if remain==0:
                global_result.append(result)
            else:
                for i in range(index,len(candidates)):
                    if i>index and candidates[i]==candidates[i-1]:
                        continue
                    if remain<candidates[i]:
                        break
                    helper(i+1,remain-candidates[i],result+[candidates[i]])
        helper(0,target,[])
        return global_result