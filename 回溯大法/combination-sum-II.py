def combinationSum2(candidates,target):
    res = []
    length = len(candidates)
    c_fre = {}
    for i in candidates:
        c_fre.setdefault(i, 0)
        c_fre[i] += 1

    c_fre_list = list(c_fre.items())
    c_fre_list.sort()
    def dfs(pos, target):
        nonlocal sub
        if sum(sub) == target:
            res.append(sub.copy())
            return

        if sum(sub) > target:
            return
        if pos==len(c_fre_list):
            return
        for i in range(1, c_fre_list[pos][1] + 1):

            sub.append(c_fre_list[pos][0])
            dfs(pos + 1, target)

            sub.pop()



    sub = []
    for t in range(len(c_fre_list)):
        dfs(t,target)
        sub = []
    return res

if __name__ == '__main__':
    print(combinationSum2([3,1,3,5,1,1],8))