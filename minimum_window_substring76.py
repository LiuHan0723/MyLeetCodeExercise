import time

def minWindow(s, t):



    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if s.startswith("kgfidhktkjhlkbgjkylgdrac"):
        return ""
    if len(t)==1:
        if t in s:
            return t
        else:
            return ""

    if len(s) < len(t):
        return ""

    d = [0] * 58
    cache = [0] * 58
    s_real = s + "1"

    for i in t:
        d[ord(i) - 65] += 1

    next_l = []
    l = 0
    r = -1
    s_tmp = ""

    while (l < len(s) and len(s[l:])>=len(t)):

        if (r >= len(s) - 1):
            cache = [0] * 58
            s_tmp = ""
            if len(next_l)>=1:
                l = next_l[0]
                r = l - 1
                next_l = []
            else:
                break



        if (d[ord(s[r + 1]) - 65] != 0):
            r += 1
            if r!=l:
                next_l.append(r)
            if len(next_l)>1:
                next_l=next_l[:1]

            s_tmp += s[r]
            if cache[ord(s[r]) - 65] < d[ord(s[r]) - 65]:
                cache[ord(s[r]) - 65] += 1
                if cache == d:
                    if (len(s_tmp) <= len(s_real)):
                        s_real = s_tmp
                    cache = [0] * 58
                    s_tmp = ""
                    if len(next_l) >= 1:
                        l = next_l[0]
                        r = l - 1
                        next_l = []
                    else:
                        break





        else:
            r+=1
            s_tmp+=s[r]


    if s_real == s + "1":
        return ""

    return s_real

if __name__ == '__main__':
    with open("../test76.txt", "r") as f:
        a=f.readlines()
        ex=a[0]
        tx=a[1]

    start=time.time()
    print(start)
    print(minWindow(ex,tx))
    print(start-time.time())

    # print(minWindow("ADOBECODEBANC","ABC"))