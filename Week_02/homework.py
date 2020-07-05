##NO.1 N叉树的前序遍历
##给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
##你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
##给定一个 N 叉树，返回其节点值的前序遍历。
##例如，给定一个 3叉树 :
##              1
##        3     2       4
##       5 6
##返回其前序遍历: [1,3,5,6,2,4]。

# 直接递归
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None: #直至为空
            return []
        result = [root.val] #存为链表
        for node in root.children:
            result.extend(self.preorder(node)) #根节点后添加子节点的值，前序遍历
        return result


# 迭代法
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        s = [root]
        result = []
        while s:
            node = s.pop()
            result.append(node.val)
            s.extend(node.children[::-1]) #添加所有孩子的值
        return result


##NO.2 N叉树的层序遍历
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
# 例如，给定一个 3叉树 :
#               1
#        3      2      4
#       5  6
#返回其层序遍历:
#
#[
#     [1],
#     [3,2,4],
#     [5,6]
#]

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        queue = collections.deque([root]) ##双向列表
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        return result


##NO.3 丑数
#我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
# 
#示例:
#输入: n = 10
#输出: 12
#解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#说明:  
#1 是丑数。
#n 不超过1690。

#动态规划解
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: 
                a += 1
            if dp[i] == n3: 
                b += 1
            if dp[i] == n5: 
                c += 1
        return dp[-1]