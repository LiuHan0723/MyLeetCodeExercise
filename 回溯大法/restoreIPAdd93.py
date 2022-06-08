def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    ssubRes = []
    length = len(s)

    def dfs(subRes, index):
        if len(subRes) == 4 and index == length:
            res.append(".".join(subRes))
            return
        if len(subRes) == 4 and index != length:
            return
        for i in range(1, 4):
            if index + i > length:
                return

            if i != 1 and s[index] == "0":
                return

            strs = s[index:index + i]
            if int(strs) > 255:
                return

            subRes.append(strs)
            dfs(subRes, index + i)
            subRes.pop()

    res = []
    dfs(ssubRes, 0)
    return res

if __name__ == '__main__':
    print(restoreIpAddresses("0000"))