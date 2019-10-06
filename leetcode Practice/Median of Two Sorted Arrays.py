# 暴力解法
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    num3:list = nums1 +nums2
    num3.sort()
    print(num3)
    medianIndex = len(num3)%2
    print(medianIndex)
    if medianIndex == 0:
        num1 = num3[len(num3)//2]
        num2= num3[len(num3)//2-1]
        print(num1,num2)
        median = (num1+num2)/2
    else:
        median = num3[len(num3)//2]
    return median

nums1 = [1,2]
nums2 = [3,4]

print(findMedianSortedArrays(nums1,nums2))