##NO.1  数组的相对排序
# 给你两个数组，arr1 和 arr2，

# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

# 示例：
# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
 

# 提示：
# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# arr2 中的元素 arr2[i] 各不相同
# arr2 中的每个元素 arr2[i] 都出现在 arr1 中

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        #将arr1 counter计数，按照arr2来取
        li = []
        counter = collections.Counter
        count = counter(arr1)
        #按照arr2将arr1的元素存入li
        for val in arr2:
            if val in count:
                l = count[val]
                print(l)
                for i in range(l):
                    li.append(val)
            #被存的元素删除掉
            del count[val]
        #剩下的元素排序放到末尾
        li += sorted(list(count.elements()))
        return li


##NO.2 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true

# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false

# 说明:
# 你可以假设字符串只包含小写字母。

# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    
        # 定义默认布尔值参与后续运算
        result = True
        # 利用 Python 数据结构 set 去重去序
        set_tmp = set(s)
        # 先判断组成字符串的各个字符元素是否一致
        if set_tmp == set(t):
            for i in set_tmp:
                # 利用逻辑运算符判断各个字符元素的数量一致，均为 True 才输出 True
                result = result and (s.count(i) == t.count(i))
        else:
            result = False
        return (result)


##NO.3 合并区间
# 给出一个区间的集合，请合并所有重叠的区间。

# 示例 1:
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

# 示例 2:
# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。

# 提示：
# intervals[i][0] <= intervals[i][1]

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


## NO.4 翻转对
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
# 你需要返回给定数组中的重要翻转对的数量。

# 示例 1:
# 输入: [1,3,2,3,1]
# 输出: 2

# 示例 2:
# 输入: [2,4,3,5,1]
# 输出: 3

# 注意:
# 1.给定数组的长度不会超过50000。
# 2.输入数组中的所有数字都在32位整数的表示范围内。

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, t, c = l, l, 0
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1) >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt
