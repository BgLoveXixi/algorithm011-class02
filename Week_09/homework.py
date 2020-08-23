##NO.1  反转字符串中的单词 III
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

# 示例：
# 输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
 
# 提示：

# 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split(' ')[::-1])[::-1] ##2次反转


##NO.2 同构字符串
# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

# 示例 1:
# 输入: s = "egg", t = "add"
# 输出: true

# 示例 2:
# 输入: s = "foo", t = "bar"
# 输出: false

# 示例 3:
# 输入: s = "paper", t = "title"
# 输出: true

# 说明:
# 你可以假设 s 和 t 具有相同的长度。

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return [s.index(i) for i in s] == [t.index(i) for i in t]   #同构代表两个字符串中每个位置上字符在自身第一次出现的索引相同


##NO.3 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。

# 示例 2：
# 输入: "cbbd"
# 输出: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = ""
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j + 1 <= 3 or dp[j+1][i-1]):
                    dp[j][i] = 1
                    res = max(res, s[j:i+1], key=len)   
        return res


## NO.4  最长有效括号
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

# 示例 1:
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"

# 示例 2:
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i>0 and s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res

