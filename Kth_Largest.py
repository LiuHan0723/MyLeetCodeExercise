

def kthLargest(nums,k):

    n=len(nums)

    return kPartion(nums,0,n-1,k)

def kPartion(nums,l,r,k):

    pivot=nums[l]
    j=l
    for i in range(l+1,r+1):
        if(nums[i]>pivot):
            j+=1
            tmp=nums[i]
            nums[i]=nums[j]
            nums[j]=tmp

    tmp1=nums[j]
    nums[j]=nums[l]
    nums[l]=tmp1

    if(k<j+1):
        return kPartion(nums,l,j-1,k)
    elif(k>j+1):
        return kPartion(nums,j+1,r,k)
    else:
        return nums[j]

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """

    if (len(s) == 1):
        return

    metas = []
    idx = []
    for i in range(len(s)):
        if (s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
            metas.append(s[i])
            idx.append(i)

    l = 0
    r = len(metas) - 1
    while (l < r):
        metas[l], metas[r] = metas[r], metas[l]
        l += 1
        r -= 1

    s_list=list(s)

    for i in range(len(metas)):
        s_list[idx[i]]=metas[i]
    return ''.join(s_list)

def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    r = -1
    s = 0
    res = len(nums) + 1

    while (l < len(nums)):

        if (r < len(nums) - 1 and s < target):
            r += 1
            s += nums[r]

        else:

            s -= nums[l]
            l += 1

        if s >= target:
            res = min(res, r - l + 1)

    if res == len(nums) + 1:
        return 0

    return res


def findAnagrams( s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """

    l = 0
    r = -1
    res = []

    cache =[0]*26
    d = [0]*26
    for i in list(p):
        d[ord(i)-97]+=1

    while (l < len(s)):

        if(r<len(s)-1 and s[r+1] in p):
            r+=1
            cache[ord(s[r])-97]+=1
            if cache[ord(s[r])-97]>d[ord(s[r])-97]:
                # if s[l]==s[r]:
                #     cache[ord(s[r])-97]-=1
                #     l+=1
                # else:
                #     l=r-1
                #     r=l-1
                #     cache = [0] * 26
                cache[ord(s[r]) - 97] -= 1
                r-=1
                cache[ord(s[l]) - 97] -= 1
                l+=1

        else:
            r+=1
            l=r+1
            cache = [0] * 26

        if cache==d:
            res.append(l)
            cache[ord(s[l]) - 97]-=1
            l+=1
    return res


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if len(t) == 1:
        if t in s:
            return t
        else:
            return ""

    if len(s) < len(t):
        return ""

    d = [0] * 58
    cache = [0] * 58
    s_count = 0

    for i in t:
        d[ord(i) - 65] += 1
    l = 0
    r = -1

    t_len = len(t)
    s_len = len(s)
    min_len = len(s) + 1
    start_index = -1
    while (l < s_len):

        if (r+1 < s_len and s_count < t_len):
            r += 1
            cache[ord(s[r]) - 65] += 1
            if (cache[ord(s[r]) - 65] <= d[ord(s[r]) - 65]):
                s_count += 1

        else:

            if (s_count == t_len and r - l + 1 < min_len):
                start_index = l
                min_len = r - l + 1

            cache[ord(s[l]) - 65] -= 1
            if cache[ord(s[l]) - 65] < d[ord(s[l]) - 65]:
                s_count -= 1

            l += 1

    if start_index == -1:
        return ""

    return s[start_index:start_index+min_len]

def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    snums = sorted(nums)

    l = 0
    r = len(nums) - 1

    cache = []
    while (l < r):

        if snums[l] + snums[r] > target:
            r -= 1

        elif snums[l] + snums[r] < target:
            l += 1

        else:
            cache.append(snums[l])
            cache.append(snums[r])
            break
    res = []
    if cache[0] == cache[1]:
        res.append(nums.index(cache[0]))
        res.append(nums.index(cache[1], res[0] + 1))

        return res

    for i in cache:
        res.append(nums.index(i))


    return res
if __name__ == '__main__':
    print(minWindow("ADOBECODEBANC","ABC"))
    print(twoSum([2,7,11,15],9))
