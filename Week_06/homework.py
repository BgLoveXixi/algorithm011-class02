##NO.1 解码方法
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。

# 示例 1:
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

# 示例 2:
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s or s[0] == '0': # 基本情况，直接返回 0
            return 0
        dp = [None] * len(s) # 构建 dp 数组
        dp[0] = 1 # 只有一个数时肯定为 1
        if len(s) > 1: # 为 dp[1] 填充值
            if s[1] == '0': # s[i] 为 ‘0’ 时
                if int(s[0:2]) <= 26: # 截取前两数，判断是否小于或等于 26
                    dp[1] = 1 # 因为 s[i] 为 ‘0’ 所以 dp[1] 只有 1 种可能
                else:
                    return 0 # 比如 60 , 此时该序列无法翻译
            else: # s[i] 不为 ‘0’ 时
                if int(s[0:2]) <= 26:
                    dp[1] = 2 # 比如 16，有两种翻译结果
                else:
                    dp[1] = 1 # 比如 27，只有一种结果
        else: # 只有一个数
            return 1

        for i in range(2, len(s)): # 从 2 开始
            if s[i] == '0': # s[i] 为 ‘0’ 时
                if s[i-1] == '0': # 前一个为 ‘0’
                    return 0 # 无解
                else: # 前一个不为 ‘0’
                    if int(s[i-1:i+1]) <= 26: # s[i-1] 和 s[i] 组成的数 <= 26
                        dp[i] = dp[i-2]
                    else:
                        return 0
            else: # s[i] 不为 ‘0’
                if s[i-1] == '0': # 前一个为 ‘0’
                    dp[i] = dp[i-1]
                else: # 前一个不为 ‘0’
                    if int(s[i-1:i+1]) <= 26: # s[i-1] 和 s[i] 组成的数 <= 26
                        dp[i] = dp[i-1] + dp[i-2]
                    else: # s[i-1] 和 s[i] 组成的数 > 26
                        dp[i] = dp[i-1]

        return dp[len(s) - 1]


##NO.2  回文子串
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

# 示例 1:
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".

# 示例 2:
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

# 注意:
# 输入的字符串长度不会超过1000


# 从每一个回文串中心开始统计回文串数量。回文区间 [a, b] 表示 S[a], S[a+1], ..., S[b] 是回文串，根据回文串定义可知 [a+1, b-1] 也是回文区间。
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in xrange(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans


##NO.3  最小覆盖子串
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

# 示例：
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"

# 说明：
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j,c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c = s[i] 
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j-i < res[1] - res[0]:   #记录结果
                    res = (i,j)
                need[s[i]] += 1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0] : res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果

