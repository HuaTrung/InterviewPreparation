from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tmp=defaultdict(lambda : 0)
        largest=0
        res,left=0,0
        for i in range(len(s)):
            tmp[s[i]]+=1
            if tmp[s[i]]>largest:
                largest=tmp[s[i]]
            while i-left+1-largest>k:
                tmp[s[left]]-=1
                left+=1
            res=max(res,i-left+1)
        return res
                    
                