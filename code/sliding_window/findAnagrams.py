from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        tmp1,tmp2=defaultdict(int),defaultdict(int)
        for i in range(len(p)):
            tmp1[p[i]]+=1
            tmp2[s[i]]+=1
        result=[]
        left=0
        for i in range(len(p),len(s)+1):
            if tmp1==tmp2: result.append(left)
            if i<len(s): tmp2[s[i]]+=1
            tmp2[s[left]]-=1
            if tmp2[s[left]]==0: tmp2.pop(s[left])
            left+=1
        return result