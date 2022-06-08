

def containsNearbyAlmostDuplicate(nums, k, t):
    s= set()
    for i in range(len(nums)):

        fil = filter(lambda x: x >= nums[i] - t, s)

        for f in fil:
            if f in s and f <= nums[i] + t:
                return True
            break

        s.add(nums[i])

        if len(s) == k + 1:
            s.remove(nums[i - k])

    return False

if __name__ == '__main__':
    print(containsNearbyAlmostDuplicate([-3,3,-6],2,3))