class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        count1, count2 = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(s1)):
            count1[s1[i]] += 1
            count2[s2[i]] += 1
        i = 0
        for j in range(len(s1), len(s2) + 1):
            if count1 == count2: return True
            if j < len(s2): count2[s2[j]] += 1
            count2[s2[i]] -= 1 
            if count2[s2[i]] == 0: count2.pop(s2[i])
            i += 1
        return False