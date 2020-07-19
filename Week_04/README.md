# 本周总结
## 深度优先搜索（DFS）和 广度优先搜索（BFS）
    普通的搜索就是遍历每个节点，且只遍历一次
    还有按照优先级搜索的，这种更符合现实场景，如推荐算法里面的
### 深度优先搜索（DFS）
      Python 代码模板
      递归写法
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
      非递归写法（维护一个栈）
      def DFS(self, tree): 

        if tree.root is None: 
          return [] 

        visited, stack = [], [tree.root]

        while stack: 
          node = stack.pop() 
          visited.add(node)

          process (node) 
          nodes = generate_related_nodes(node) 
          stack.push(nodes) 

        # other processing work 
        ...
### 广度优先搜索（BFS）
      Python 代码模板
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
#### 思维要点
    1.本质是把所有的节点访问一遍
    2.按照节点访问的次序不一样分为深度优先和广度优先
#### 层次遍历问题
    其实这个问题直接想法就是使用BFS，但是其实使用DFS也是一样的，因为不管哪种写法都是遍历所有节点，所以只要在遍历的时候记下节点的层次，然后把节点放到相应的层次（数组）里面去即可。
#### 括号生成问题
    上次讲到递归的时候是用递归写的，但是其实这就是一个深度优先搜索的问题
#### 岛屿问题
    思路是扫描二维数组，遇到1的时候把他的上下左右为1 的点且无限递归下去的1全部标为0（也就是说和1相连的所有的1都写成0，这个是岛屿的特性，如果连通则为同一个岛屿），这个地方就用到了深度优先搜索


### 贪心算法
    在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或者最优
    贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。
    贪心算法可以解决一些最优化问题，
#### 硬币问题，特定的倍数，可以使用最大的去匹配，但没有特殊性时可能不适用。
#### 适用贪心算法的场景
    问题能够分解成子问题来解决，子问题的最优解能够递推到最终问题的最优解，这种子问题最优解称为最优子结构
#### 贪心的角度可能不一样，从前往后，从后往前

#### 分饼干问题：有限满足胃口小的小朋友的需求
#### 买卖股票的最佳时机问题：只要前一天比第二天小，就可以买卖
#### 跳跃游戏问题：从后往前贪心，只要记录最前面的一个下标它能够跳到最后点，只要到最后那个能跳到的下标是第一个点即可！


### 二分查找
 #### 前提：
    1.目标函数单调性（单调递增或递减）
    2.存在上下界（bounded）
    3.能够通过索引访问（index accessible）
    
      Python 代码模板
      left, right = 0, len(array) - 1 
      while left <= right: 
          mid = (left + right) / 2 
          if array[mid] == target: 
              # find the target!! 
              break or return result 
          elif array[mid] < target: 
              left = mid + 1 
          else: 
              right = mid - 1
#### 求一个数的平方根问题
    首先，y=x^2，是一个抛物线，递增；有边界：最大本身，最小1，所以可以使用二分查找
    用牛顿迭代法：在迭代过程中，以直线代替曲线，用一阶泰勒展式（即在当前点的切线）代替原曲线，求直线与x轴的交点，重复这个过程直到收敛（逼近思想）
    r = x
    while r*r > x:
        r = (r + x/r)/2 
    return  r
#### 搜索旋转排序数组问题
     查找中间数，左边界，左边界和目标数的关系，并判断，是否有序，直到最后只有一个元素，最后判断是否与目标相同即可。这其实是一个条件复杂的二分查找
     
## 五毒神掌；四部做题
