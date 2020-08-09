# 本周总结
## 字典树和并查集
### 字典树（trie）
      又称为单次朝查找树或者键树，是一种树形结构。典型的应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计
      优点：最大限度的减少无谓的字符串比较次数，查询效率比哈希表高。
#### 基本性质
      1.结点本身不存完整单词；
      2.从根结点到某一结点，路径上经过的字符连起来，为该结点对应的字符串；
      3.每个结点的所有子结点路径代表的字符都不相同。
#### 结点存储额外信息：可以是频次
#### 核心思想
      空间换时间
      利字符串的公共前缀来降低查询时间的开销以达到提高效率的目的
      
      # Trie树 Python代码模板 （字母指向的字母的26分叉树（插入，查找），方便的实现以什么字符串开头）
      
      class Trie(object):

        def __init__(self): 
          self.root = {} 
          self.end_of_word = "#" 

        def insert(self, word): 
          node = self.root 
          for char in word: 
            node = node.setdefault(char, {}) 
          node[self.end_of_word] = self.end_of_word 

        def search(self, word): 
          node = self.root 
          for char in word: 
            if char not in node: 
              return False 
            node = node[char] 
          return self.end_of_word in node 

        def startsWith(self, prefix): 
          node = self.root 
          for char in prefix: 
            if char not in node: 
              return False 
            node = node[char] 
          return True
    
#### 例题 单词搜索
        1.遍历word，对于word中的每一个单词在board中查找是否存在，
            时间复杂度：O(N*m*m*4^k)
        2.使用word构建一棵tire树，对board进行DFS，然后搜索是否存在（注意对使用过的字母进行标记）

### 并查集（Disjoint Set）
    适用场景：组团、配对问题（group or not）
#### 基本操作
    1.makeSet(s)：建立一个新的并查集，其中包含s个单元素集合。
    2.unionSet(x,y)：把元素x和元素y所在的集合合并，要求x和y所在的集合不相交，如果相交则不合并。
    3.find(x)：找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。
    
#### 例题  朋友圈问题
     1.DFS(BFS)，类似岛屿问题
     2.并查集
#### 并查集操作
    初始化（init），查询（find）、合并（union）
     
      # 并查集 Python代码模板  
      def init(p): 
        # for i = 0 .. n: p[i] = i; 
        p = [i for i in range(n)] 

      def union(self, p, i, j): 
        p1 = self.parent(p, i) 
        p2 = self.parent(p, j) 
        p[p1] = p2 

      def parent(self, p, i): 
        root = i 
        while p[root] != root: 
          root = p[root] 
        while p[i] != i: # 路径压缩 ?
          x = i; i = p[i]; p[x] = root 
        return root
   
#### 什么问题使用并查集
      问有多少个朋友圈，或者问它属于谁，或者问任意给你2个人问他们是不是朋友

## 高级搜索
      1.朴素搜索
      2.优化方式：不重复（fibonacci）、剪枝（生成括号问题）
      3.搜索方向：
        DFS
        BFS
        双向搜索、启发式搜索
### 剪枝
    剪掉不合理的分支（一般是条件判断）
    
N皇后问题：在DFS时，处理列 行 撇和捺位置也是一种剪枝
数独问题：验证是否合法（人脑的话，会先选填空的格子少的块，所以优化的话可以将剩下格子数作为优先级搜索来解决）
    
### 双向BFS
    两端同时开始BFS
#### 例题 单词接龙
    分别从开始单词和结束单词开扩撒，如果2个相遇，说明可以成功转换，并且次数即为2个BFS的深度和
   
### 启发式搜索 (Heuristic Search , A*)
      # A* Python 代码模板 
      def AstarSearch(graph, start, end):
        pq = collections.priority_queue() # 优先级 —> 估价函数
        pq.append([start]) 
        visited.add(start)
        while pq: 
          node = pq.pop() # can we add more intelligence here ?先弹出优先级最高的处理
          visited.add(node)
          process(node) 
          nodes = generate_related_nodes(node) 
         unvisited = [node for node in nodes if node not in visited]
          pq.push(unvisited)

#### 优先级如何定
    估价函数：或者叫启发式函数：h(n)，用来评价那些结点最有希望的是一个我们要找的结点，h(n)会返回一个非负实数，也可以认为是从结点n的目标结点路径的估计成本
    启发式函数是一种告知搜索方向的方法，它提供了一种明智的方法来猜测哪个邻居结点会导向一个目标
    
#### 例题 二进矩阵中的最短路径
      1.DP
      2.BFS
      3.A*：估价函数：计算当前点与目标点的绝对距离，根据优先级加入优先队列(pq)
#### 例题 滑动谜题
      1.DFS
      2.BFS：更快找到最优解
      3.A*:用相应位置的坐标差来判定优先级（进阶：双向A*+曼哈顿距离）
#### 二维矩阵的距离（或者判断状态的相似性） 估价函数：曼哈顿距离：横纵坐标差的绝对值之和
      
## AVL树和红黑树
    保持一棵树的平衡：平衡二叉树
### AVL树
    平衡因子：左子树的高度减去右子树的高度
    通过旋转操作来进行平衡（4种）
    
    始终保证平衡因子不超过绝对值1
    
    左旋：右右子树；     左旋：左左子树:右旋
    左右子树：左右旋；   右左子树：右左旋
    
    带有左右子树时，注意子树需要更换父结点

#### 总结
    1.平衡二叉树
    2.每个结点存balance factor = {-1,0,1}
    3.四种旋转操作
    
    不足：结点需要存储额外信息、且调整次数频繁（维护成本高）
 
 ### 红黑树 
    是一种近似平衡的二叉搜索树，它能够确保任何一个结点的左右子树的高度差小于2倍，具体来说，红黑树满足如下条件的二叉搜索树：
    。每个结点要么是红色，要么是黑色
    。根结点是黑色
    。每个叶结点(NIL结点，空结点)是黑色的
    。不能有相邻接的两个红色结点
    。从任何一结点到其每个叶子的所有路径都包含相同数目的黑色结点
    
    关键性质：从根到叶子的最长的可能路径不多于最短的可能路径的两倍长
#### 面试问题
      对比
      • AVL trees providefaster lookupsthan Red Black Trees because they aremore strictly balanced.
      • Red Black Trees providefaster insertion and removal operations than AVL trees as fewer rotations are done due to relatively relaxed balancing.
      • AVL trees store balancefactors or heights with each node, thus requires storage for an integer per node whereas Red Black Tree requires only 1 bit of information per node.
      • Red Black Trees are used in most of thelanguage libraries likemap, multimap, multisetin C++whereas AVL trees are used in databaseswhere faster retrievals are required.


### 平衡树：
    2–3 tree
    AA tree
    AVL tree
    B-tree
    Red–black tree
    Scapegoat tree
    Splay tree
    Treap
    Weight-balanced tree





