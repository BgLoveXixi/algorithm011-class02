##两数之和
##给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

##你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #使用字典
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return dic[target-nums[i]],i
            else:
                dic[nums[i]] = i


##加1
##给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#你可以假设除了整数 0 之外，这个整数不会以零开头。

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sums = 0
        for i in digits:
            sums = sums * 10 + i #10进制乘以10，进行累积和；
        sums_str = str(sums + 1)
        return map(int, list(sums_str))
