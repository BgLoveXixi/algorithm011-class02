##NO.1. 二叉树的最近公共祖先
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#             3
#     5              1
# 6     2          0     8
#     7  4

# 示例 1:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#回溯
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #终止条件
        if not root or root == p or root == q: #空树或者只有p，q时
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: 
            return right
        if not right: 
            return left
        return root


##NO.2  全排列 II
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。

# 示例:

# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

#间接递归
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # 先对数组排序
        self.res = []
        self.recursion(nums,[])
        return self.res

    def recursion(self,nums,temp):
        if nums == []:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #每当进入新的构成，先考虑该构成的首字符是否和上一个一样
                continue
            self.recursion(nums[:i]+nums[i+1:],temp+[nums[i]]) #nums[:i]+nums[i+1:] 避免了重复利用
