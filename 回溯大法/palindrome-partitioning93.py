def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    res = []
    '''
    benl
    enev
    '''
    def dfs(strs, start, end, sub):
        if start == end:
            res.append(sub.copy())
            return

        for i in range(1, len(s[start:end])+1):
            s_tmp = s[start:start + i]
            if isPali(s_tmp):
                sub.append(s_tmp)
                dfs(strs, start + i, end, sub)
                sub.pop()

    def isPali(strs):
        l = 0
        r = len(strs) - 1
        while l <= r:
            if strs[l] != strs[r]:
                return False
            l += 1
            r -= 1
        return True

    subb=[]
    dfs(s,0,len(s),subb)
    return res

if __name__ == '__main__':
    print(partition("aab"))