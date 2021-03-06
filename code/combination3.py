class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        global_result=[]        
        def helper(index,remain_k,remain_n,result):
            if remain_k==0 and remain_n==0:
                global_result.append(result)
            else:
                if remain_n>0 and remain_k>0:
                    for i in range(index,10):
                        if remain_k<i:
                            break
                        else:
                            helper(i+1,remain_k-i,remain_n-1,result+[i])
        helper(1,n,k,[])
        return global_result