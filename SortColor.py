
def removeDuplicates(nums):
    i = 0
    for e in nums:
        if i < 3 or e != nums[i - 3]:
            nums[i] = e
            i += 1

    return i

    return k

def sortColor(nums):
    zero=-1
    two=len(nums)
    i=0
    while i <two:
        if nums[i]==0:
            zero+=1
            nums[i]=nums[zero]
            nums[zero]=0
            i+=1
        elif nums[i]==1:
            i+=1
        else:
            two-=1
            nums[i]=nums[two]
            nums[two]=2
    return nums



if __name__ == '__main__':
    print(sortColor([0,2,0,2 ,2]))