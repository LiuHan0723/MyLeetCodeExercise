def reverseNumber(nums):

    n=len(nums)
    l=0
    r=n-1

    return __split(nums,l,r)


def __split(nums,l,r):

    mid=l+(r-l)//2
    count=0
    if l>=r:
        return 0

    count+=__split(nums,l,mid)
    count+=__split(nums,mid+1,r)
    count+=__mergefind(nums,l,mid,r)

    return count

def __mergefind(nums,l,mid,r):

    num=0
    aux=[0]*(r-l+1)
    for i in range(l,r+1):
        aux[i-l]=nums[i]

    j=l
    k=mid+1
    for t in range(l,r+1):
        if j>mid:
            nums[t]=aux[k-l]
            k+=1

        elif k>r:
            nums[t]=aux[j-l]
            j+=1

        elif(aux[j-l]>aux[k-l]):
            num+=(mid-j+1)
            nums[t]=aux[k-l]
            k+=1

        else:
            nums[t]=aux[j-l]
            j+=1

    return num

if __name__ == '__main__':
    print(reverseNumber([1,3,2,3,1]))