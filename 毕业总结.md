# 毕业总结
## 序言
转眼间，2个月的时间过去了，从最开始进入算法营，到至今写下这篇毕业总结，还是收获了很多的东西，也学到了很多，感谢极客大学。虽然从一开始，我每次都是最后才留出时间来学习，但每次都学习的比较认真，唯一的缺憾就是动手还不够，需要多拿点时间来更加努力的学习算法。
## 知识提纲
#### 1 数据结构、算法复杂度、数组、链表、跳表、栈、队列、优先队列、双端队列
#### 2 哈希表、映射、集合、树、二叉树、二叉搜索树、堆和二叉堆、图
#### 3 泛型递归、树的递归、分治、回溯
#### 4 深度优先和广度有限搜索、贪心算法、二分查找
#### 6 动态规划
#### 7 字典树和并查集、高级搜索、红黑树和AVL树
#### 8 位运算、布隆过滤器和LRU缓存、排序算法
#### 9 高级动态规划、字符串算法

其中还有一个期中(5)和期末(6)考试，主要是对半阶段的知识学习的总结和回顾

## 难点重点
数据结构和算法，以数据结构为先，所以最基础的是要掌握好各种常见的数据结构的定义以及用法（如前两周学习的数据结构）,对于数组、链表、栈和队列、哈希表、集合、(二叉)树，堆等要熟练掌握它的特点和用法。递归是很重要的，因为超哥讲过，计算机，只会简单的重复操作，if...else  for... loop 以及递归所以递归的地位可见一斑，也是DFS和BFS的基础

      ###递归 Python 代码模板
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
          
          
      ###DFS的Python 代码模板
      visited = set() 

      def dfs(node, visited):
          if node in visited: # terminator
            # already visited 
            return 

        visited.add(node) 

        # process current node here. 
        ...
        for next_node in node.children(): 
          if next_node not in visited: 
            dfs(next_node, visited)
                # reverse the current level status if needed：清理当前层
                 
        ###BFS的Python 代码模板
        def BFS(graph, start, end):
            visited = set()
          queue = [] 
          queue.append([start]) 
          while queue: 
            node = queue.pop() 
            visited.add(node)
            process(node) 
            nodes = generate_related_nodes(node) 
            queue.push(nodes)
          # other processing work 
          ...
          
 接着下一个难点便是动态规划了
 
     动态规划关键点
    1.最优子结构 opt[n] = best_of(opt[n-1],opt[n-2],...)  ----（子问题）
    2.存储中间状态： opt[i]  ----（dp数组）
    3.递推公式    ----（dp方程）
          Fib: opt[i] = opt[i-1] + opt[i-2]
          二维路径：opt[i,j] = opt[i+1,j] + opt[i,j+1] (且判断a[i,j]是否是空地)
      
     动态规划小结
     1.打破自己的思维惯性，形成机器思维（即找重复性）
     2.理解复杂逻辑的关键
     3.也是职业进阶的要点要领（不必亲力亲为，分治好）
          
     动态规划状态转移方程 一些经典的例题回顾：
        爬楼梯：使用动规，O(2^N) ---> O(n)  ( 可以写一个for循环，for i in range(2:n): dp[i] = dp[i-1] + dp[i-2]) )
        不同路径：f(x,y) = f(x-1,y) + f(x,y-1)  (二维数组)
        打家劫舍：多开一维维度：表示nums[i]偷和没偷，分别写出状态转移方程
        最小路径：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + A[i][j]
        股票买卖：dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]), 今天没有持有股票
                  dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]), 今天持有股票  
              
字符串也是常考的笔试面试题之一，所以对于常见的字符串算法，需要刻意练习，熟练掌握，如
最长子串、子序列

    1.最长子序列：dp[i][j] = dp[i-1][j-1] + 1(if s1[i-1]==s2[j-1])
              else dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    2.最长子串：dp[i][j] = dp[i-1][j-1] + 1(if s1[i-1]==s2[j-1])
              else dp[i][j] = 0
最长回文子串

    1.暴力：从左从右滑动，枚举所有子串，然后判断子串是否是回文串
    2.改进：回文串最左最右相同：枚举回文串中心，可以在一个字母上（此时回文串长度奇数，从中心扩散，一直到左右两边字母不同，返回最大长度），也可以是在2个字母中间，
    3.DP：定义P(i,j) = true  s[i,j]是回文串，s[i,j]表示从i到j的字符串
                     = false s[i,j]不是回文串
           P(i,j) = (P(i-1,j-1) && S[i] = S[i] == S[j])
       
       
 ## 总结
 从超哥那里学到了一些使用的技巧和方法，如吸收世界代码精华----看国际站；刻意练习（记住模版）；收藏优秀的代码的习惯（化为己用）；切题四件套和五毒神掌，以及最近重复子问题。
 对于切题四件套和五毒神掌，我十分可：

切题四件套：

    clarification 明确题⽬意思、边界、数据规模
    possible solutions 穷尽所有可能的解法
    compare（time/space）&& optimal（学习最优解加强）
    coding（多写）代码简洁、⾼性能、美感   final：test cases

五毒神掌：

    第一遍 五分钟：读题 + 思考 直接看解法：多看几种，比较解法优劣 背诵、默写好的解法 
    第二遍 马上自己写 ——> Leetcode提交 多种解法比较、体会 ——> 优化！ 
    第三遍 过了一天后，再重复做题 不同解法的熟练程度——>专项练习 
    第四遍 过了一周后：反复回来练习相同的题目 
    第五遍 面试前一周恢复性训练

算法的路，注定不会十分轻松，但仍然要坚持和努力，希望都能成为算法的高手，实现自己的理想！
  
