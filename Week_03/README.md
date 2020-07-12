# 本周总结
## 递归（Recursion） 
###   通过函数体来调用自己实现循环（一层一层进去，然后出来）
      Python 代码模板
      def recursion(level, param1, param2, ...): 
          # recursion terminator：递归终止条件
          if level > MAX_LEVEL: 
           process_result 
           return 
          # process logic in current level ：处理当层逻辑
          process(level, data...) 
          # drill down ：下探到下一层
          self.recursion(level + 1, p1, ...) 
          # reverse the current level status if needed：清理当前层
### 模板要点：
    1.递归终止条件：当前层大于最大层
    2.处理当前层的逻辑
    3.下探到下一层
    4.清理当前层（主要是全局变量等，也可不需要）
### 思维要点
    1.不要进行人肉递归（不画状态树）
    2.找到最近最简方法，将其拆解为可重复解决的问题（即重复子问题）
    3.数学归纳法思维：n=1，n=2 → n
### 括号的可能性问题
    先把他想成一个不考虑括号有效性的问题，2n个格子，放置左右括号有多少种结果，然后检查结果的合法性。
    先是终止条件，当前层大于最大层，结束；然后是当前层，上一个加上一个左括号或者上一层加一个右括号，紧接着，下一层，当前层加一个左括号或者加一个右括号，这样就产生了所有的可能。
    接下来，考虑如何判断哪些是合法的，可以写一个函数判断，合法则添加。但是，其实在括号产生的时候就可以判断一下，于是：1.左边括号可以随便加，只要不超过数量限制，2.右括号必须要有多的左括号，也就是添加之前，左括号的数量要大于右括号，这2个条件可以统计所有的合法的可能性，并且不重复（）。于是，改原代码为，参数左右括号的个数，最大个数，结果。终止条件是左右括号都用完了，当左括号还有时，可添加左括号，当左括号大于右括号时，添加右括号。
### 这个题目在中间过程就去掉了没用的分支，可称之为剪枝，并且问题是一步一步思考过来的。

#### 验证二叉搜索树：中序遍历是否递增（中间可看当前节点是否比上一个节点大）？或者使用递归，左子树＜根＜右子树
#### 二叉树的深度：左子树的深度加+1 ，右子树的深度加1  的较大值
   
      
## 分治（Divide Conquer）
### 重复性
    最近重复性:分治，回溯等；最优重复性：动态规划
### 一个大问题分解成若干个子问题---分治
      Python 代码模板
      def divide_conquer(problem, param1, param2, ...): 
        # recursion terminator 
        if problem is None: 
        print_result 
        return 
        # prepare data 
        data = prepare_data(problem) 
        subproblems = split_problem(problem, data) 
        # conquer subproblems 
        subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
        subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
        subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
        …
        # process and generate the final result 
        result = process_result(subresult1, subresult2, subresult3, …)

        # revert the current level states
 ### 模板要点：
    1.递归终止条件：没有问题了
    2.处理当前层的逻辑：如何把大问题分为小问题（比较关键 ）
    3.下探到下一层: 解决更细节的子问题
    4.组装子问题的结果，清理返回
    
## 回溯（Backtracking）
    在每一层试错，找到正确答案，或者错误就回到上一层往寻找别的可能性
#### x的n次方不需要乘以n次，一开始也出乎我的意料，后来分治的思想，其实是每次求减半，大问题子问题化，然后对于减半可能出现的结果需要分别后处理，最后组合结果
      
## 总结：总重要的一点，如何分解为子问题（或者如何找到子问题）

