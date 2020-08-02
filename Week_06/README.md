# 本周总结
## 动态规划
    寻找重复性
    本质就是一个递归问题或者分治问题：分治+最优子结构，将一个复杂问题分解为更简单的子问题（使用递归方法）
### 关键点
      动态规划和递归或者分治没有根本上的区别（关键看有无最优子结构）
      共性：找到重复子问题
      差异性：最优子结构、中途可以淘汰次优解
      
      #递归Python 代码模板
      def recursion(level, param1, param2, ...): 
          # recursion terminator 
          if level > MAX_LEVEL: 
           process_result 
           return 
          # process logic in current level 
          process(level, data...) 
          # drill down 
          self.recursion(level + 1, p1, ...) 
          # reverse the current level status if needed



        #分治Python 代码模板
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

#### 例题1 斐波拉契数列
        1.递归加记忆化搜索（分治+记忆搜素）
        2.使用for循环直接进行自底向上的计算（动态规划的模板）
#### 例题2 计算路径（count the paths）
        从最开始来想，迈出第一步只有2种可能，且2种可能解法不一样，而且合在一起包含所有的解法，于是问题分解为2个子问题，求从A,B走到终点的解法。接着，从A到C、D，从B到C、E，于是子问题A、B又拆解为C、D、E，如此下去直到终点（有些类似斐波拉契数列）。
        再换种角度想，终点可以由2个格子走过来，那么往回递推，每个格子有多少种走法可以标记出来，障碍物的地方是0，最下边和最右边的一排格子都是1，于是得到状态转移方程（DP方程）：
        opt[i,j] = opt[i+1,j] + opt[i,j+1]
        完整的逻辑：
        if a[i,j] = "空地"：
          opt[i,j] = opt[i+1,j] + opt[i,j+1]
        else:
          opt[i,j] = 0
### 动态规划关键点
    1.最优子结构 opt[n] = best_of(opt[n-1],opt[n-2],...)  ----（子问题）
    2.存储中间状态： opt[i]  ----（dp数组）
    3.递推公式    ----（dp方程）
          Fib: opt[i] = opt[i-1] + opt[i-2]
          二维路径：opt[i,j] = opt[i+1,j] + opt[i,j+1] (且判断a[i,j]是否是空地)
          
#### 例题3 最长公共子序列
    对于字符串问题，一般是变成一个2维数组，行和列分别是2个字符串。
    考虑从最后面开始，组成的网格表示子串和另外的子串的最长公共子序列，对于下一个，比较最后一个字符是否相同，如果相同，则为去掉最后一个字符的子串的最长公共子序列+1，如果不同，则为2个子串任意一个去掉最后字符的最大公共子序列的较大值。
    if s1[-2] != s2[-1]:
        LCS[s1,s2] = max(LCS[s1-1,s2],LCS[s1,s2-1])
    if s1[-1] == s2[-1]:
        LCS[s1-1,s2-1] + 1
#### 动态规划小结
     1.打破自己的思维惯性，形成机器思维（即找重复性）
     2.理解复杂逻辑的关键
     3.也是职业进阶的要点要领（不必亲力亲为，分治好）
#### MIT 动态规划课程 五步动态规划：
      分治→猜递推方程→合并子问题的解→递归记忆化 or 把DP的状态表建立起来，自底向上递推
    可以使用递归（分治）+记忆搜索  然后建立DP表求解，练习使用2种方法
    
#### 例题4 爬楼梯
    从最简单的加上限制条件，相邻的步数不能相同，变为中级dp问题
    
#### 例题5 三角形最小路径和
      其实就是二维棋盘切掉一个对角线
      1.暴力：递归：左或右：2^n
      2.DP：
          a.重复性（分治） problem(i,j) = min(sub(i+1, j), sub(i+1,j+1)) + a[i,j]
          b.定义状态数组：f[i,j]
          c.DP方程：f[i,j] = min(f[i+1,j], f[i+1, j+1]) + a[i,j]
      使用自顶向下的递归方法时，为了避免超时，在python里面可以LRU cache来存储中间状态

#### 例题6 最大子序列和
    dp[i] = max(num[i], num[i] + dp[i-1])
    最大子序列  = 当前元素最大  或者  包含之前后最大

#### 例题7 硬币问题
    1.暴力：递归
    2.BFS：用1,2,5分叉构造状态树，按层搜索节点为0的层
    3.DP： f(n) = min{(f(n-k),for k in [1,2,5])} + 1 
    
#### 例题8  偷房子
    要记录房子偷没偷的状态，需要再开一维数组
    a[i][0,1]: 0:偷， 1：不偷
    
    a[i][0] = max(a[i-1][0], a[i-1][1])
    a[i][1] = a[i-1][0] + num[i]
    
    换一种定义方式：a[i]:表示0...i能偷的最大值：max(a)
    a[i]:0...i天，且num[i]必偷的最大值
    a[i] = max(a[i-1], a[i-2] + num[i])
    
#### 例题9  股票买卖问题
    labuladong：一个方法团灭6道股票问题，用通用的方法，一个框架来解决这类问题
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/
