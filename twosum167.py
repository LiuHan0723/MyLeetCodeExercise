

def twoSum(nums,target):

    for i in range(len(nums)):

        l=i+1
        r=len(nums)-1
        real=target-nums[i]
        while(l<=r):

            mid=l+(r-l)//2

            if nums[mid]==real:
                return i,mid

            elif nums[mid]>real:
                r=mid-1

            else:
                l=mid+1

def twoSum_doublePoint(numbers,target):

    l=0
    r=len(numbers)-1

    while(l<r):
        if numbers[l]+numbers[r]==target:
            return [l+1,r+1]

        elif numbers[l]+numbers[r]<target:
            l+=1

        else:
            r-=1


if __name__ == '__main__':
    print(twoSum_doublePoint([1,2,4,5],9))




