def merge(nums1, m, nums2, n):

    if n == 0:
        return

    r = len(nums1) - 1
    if m == 0:
        nums1 = nums2
        return nums1
    while m != 0 or n != 0:

        if (m != 0 and n == 0):
            nums1[r] = nums1[m - 1]
            r -= 1
            m -= 1

        elif (n != 0 and m == 0):
            nums1[r] = nums2[n - 1]
            r -= 1
            n -= 1

        elif (nums1[m - 1] >= nums2[n - 1]):
            nums1[r] = nums1[m - 1]
            r -= 1
            m -= 1
        elif (nums1[m - 1] < nums2[n - 1]):
            nums1[r] = nums2[n - 1]
            r -= 1
            n -= 1
    return nums1
if __name__ == '__main__':
    print(merge([1,2,3,0,0,0],3,[2,5,6],3))