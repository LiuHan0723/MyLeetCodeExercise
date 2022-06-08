
def rotate(nums,k):
    length = len(nums)
    k = k % length
    if k == 0:
        return
    l = 0
    r = k - 1
    while r < length-1:
        l += 1
        r += 1
    tmp = nums[:l].copy()
    for i in range(r - l+1):
        nums[i] = nums[l]
        l += 1
    t=k
    for i in tmp:
        nums[t]=i
        t+=1


if __name__ == '__main__':
    nums=[1,2,3,4,5,6,7]
    rotate(nums,3)
    print(nums)