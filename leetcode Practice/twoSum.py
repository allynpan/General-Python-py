# 暴力解法，速率会非常慢
def twoSum1(nums,target):
    indexNum = len(nums)-1
    for index1 in range(indexNum):
        for index2 in range(index1+1,len(nums)):
            if nums[index1]+nums[index2]==target:
                return index1,index2

nums = [3,2,4]
print(twoSum1(nums,6))

# 最佳解法，思路如下: 先求出剩余的值，转换key与值，同时是后面的index与前面的index相互比较。
def twoSum2(nums,target):
    map = {}
    for i in range(len(nums)):
        temp = target-nums[i]
        if temp in map:
            return map[temp],i
        map[nums[i]] = i


print(twoSum2(nums,6))