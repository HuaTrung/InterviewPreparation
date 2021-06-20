def longest_substring_with_k_distinct(str, k):
    print(str)
    tmp=set()
    cur_max=0
    left=0
    for i in range(len(str)):
        tmp.add(str[i])
        if len(tmp)>k:
            while len(tmp)>k:
                tmp.remove(str[left])
                left+=1
        else:
            cur_max=max(cur_max,i-left+1)
    return cur_max
