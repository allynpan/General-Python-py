# 简单的方法

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    sum = ""
    length = 0
    for i in s:
        if i in sum:
            sum = sum[sum.index(i) + 1:]
        sum += i
        if len(sum) > length:
            result = sum
        length = max(length, len(sum))
    print(result)
    return length


s1 = "abcabcbb"

print(lengthOfLongestSubstring(s1))


# 参考答案,原理很简单，发现一个重复的数，则将指针指向下一个数据的索引，
def lengthOfLongestSubstring1(s):
    dct = {}
    max_so_far = curr_max = start = 0
    for index, i in enumerate(s):
        if i in dct and dct[i] >= start:
            max_so_far = max(max_so_far, curr_max)
            curr_max = index - dct[i]
            start = dct[i] + 1
        else:
            curr_max += 1
        dct[i] = index
    return max(max_so_far, curr_max)
