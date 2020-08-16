# 本周总结
## 位运算符  &&  布隆过滤器  && 排序
### 位运算符
      计算机里面数字的表示和存储方式都是2进制，从十进制转换为二进制：除以2，余数到写
#### 常用位运算符
    左/右移：二进制往左/右移动一位，新位补0；按位与：&；按位或：|；按位取反：~；按位异或：^(相同为0，不同为1)
    异或的特点：x^0=x ; x^1s=~x(1s为全1); x^(~x)=1s; x^x=0; c=a^b-->a^c=b, b^c=a; a^b^c=a^(b^c)=(a^b)^c, 结合律 
#### 指定位置的位运算
      1.将x最右边的n位清零：x & (~0<<n)
      2.获取x的第n位值（0或1）：(x>>n) & 1
      3.获取x的第n位的幂值：x & (1<<n)
      4.仅将第n位置为1：x | (1<<n)\
      5.仅将第n位置为0：x &(~(1<<n))
      6.将x最高位至第n位(含)清零：x & ((1<<n)-1)
#### 实战位运算要点
      1.判断奇偶：
        x%2 == 1  ---->   (x&1) == 1
        x%2 == 0  ---->   (x&1) == 0
      2.x>>1  --->   x/2
      3.x=x&(x-1):清零x最低位的1
      4.x&-x:得到最低位的1
      5.x&~x = 0
#### 实战例题
    1.统计1的个数：使用x&(x-1)每次打掉x最后一个1，直到x为0
    2.2的幂：判断一个数是否是2的幂：其实就是判断这个数的二进制里面是否有且仅有一个1，使用x&(x-1)打掉x的最后一个1，判断x是否变为0
    3.颠倒二进制：位运算拿到每一位，然后把第i位放到第32-i位置去
    4.N皇后：使用 或 左右移 来控制DFS中的判重和下探
    5.比特位计数：DP + 位运算
    
### 布隆过滤器和LRU cache
#### 布隆过滤器相关知识
      和哈希表相似。是一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索一个元素是否在一个集合中（只存在还是不在的信息，不存储额外的信息）
      优点是空间效率和查询时间都远远超过一般的算法
      缺点是有一定的误识别率和删除困难
    
      而且是一种模糊查询：如果索引位有一个为0，那么该元素一定不在，但是如果索引位全为1，是一个存在的状态，也只能说可能存在
      一般是用于快速查询，做一个缓存
      
      案例：1.比特币网络；2.分布式系统(Map-reduce)  --hadoop、search engine；3.redis缓存；4.垃圾邮件、评论过滤等
      
      #布隆过滤器  Python实现 
      from bitarray import bitarray 
      import mmh3 
      
      class BloomFilter: 
        def __init__(self, size, hash_num): 
          self.size = size 
          self.hash_num = hash_num 
          self.bit_array = bitarray(size) 
          self.bit_array.setall(0) 
          
        def add(self, s): 
          for seed in range(self.hash_num): 
            result = mmh3.hash(s, seed) % self.size 
            self.bit_array[result] = 1 
            
        def lookup(self, s): 
          for seed in range(self.hash_num): 
            result = mmh3.hash(s, seed) % self.size 
            if self.bit_array[result] == 0: 
              return "Nope" 
          return "Probably" 
          
      bf = BloomFilter(500000, 7) 
      bf.add("dantezhao") 
      print (bf.lookup("dantezhao")) 
      print (bf.lookup("yyj")) 
   
#### LRU cache
      1.两个要素：大小、替换策略
      2.hash table + double linkedlist
      3.O(1)查询，O(1)修改、更新
      
      替换策略：
        LFU:- least frequently used
        LRU:- least recently used (最少最近使用，最近一次使用的时间)
        
      # LRU Cache  Python 实现
      class LRUCache(object): 

        def __init__(self, capacity): 
          self.dic = collections.OrderedDict() 
          self.remain = capacity

        def get(self, key): 
          if key not in self.dic: 
            return -1 
          v = self.dic.pop(key) 
          self.dic[key] = v   # key as the newest one 
          return v 

        def put(self, key, value): 
          if key in self.dic: 
            self.dic.pop(key) 
          else: 
            if self.remain > 0: 
              self.remain -= 1 
            else:   # self.dic is full
              self.dic.popitem(last=False) 
          self.dic[key] = value 
          
### 排序
#### 排序算法
      1.比较类排序：通过比较来决定元素间的相对次序，时间复杂度不能突破O(nlogn), 因此也称为非线性时间比较类排序
          交换排序：冒泡排序、快速排序(nlogn)
          插入排序：简单插入排序、希尔排序
          选择排序：简单选择排序、堆排序(nlogn)
          归并排序(nlogn)：二路归并排序、多路归并排序
      2.非比较类排序：不通过比较来决定元素间的相对次序，可以突破基于比较排序的时间下界，以线性时间运行，因此也称之为线性时间非比较类排序
          计数排序、桶排序、基数排序
#### 初级排序-O(n^2)
      1.选择排序（selection sort）
        每次找到最小值，然后放到待排序数组的起始位置
      2.插入排序（insertion sort）
        从前到后逐步构建有序序列；对于未排序数据，在已排序序列中从后向前扫描，找到相应的位置并插入
      3.冒泡排序（bubble sort）
        嵌套循环，每次查看相邻的元素，如果逆序，则交换
#### 高级排序-O(nlogn)
    1.快速排序（quick sort）
      数组取标杆pivot，将小元素放在pivot左边，大元素放右侧，然后依次对左右两边的子数组继续快排，以达到整个序列有序
      
    #快排 Python代码
    def quick_sort(begin, end, nums):
        if begin >= end:
            return
        pivot_index = partition(begin, end, nums)
        quick_sort(begin, pivot_index-1, nums)
        quick_sort(pivot_index+1, end, nums)

    def partition(begin, end, nums):
        pivot = nums[begin]
        mark = begin
        for i in range(begin+1, end+1):
            if nums[i] < pivot:
                mark +=1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[begin], nums[mark] = nums[mark], nums[begin]
        return mark
    
    2.归并排序（merge sort）  --分治
      a.将长度为n的输入序列分成两个长度为n/2的子序列；
      b.对这两个子序列分别采用归并排序；
      c.将两个排序好的子序列合并成一个最终的排序序列
      
      #归并排序Python代码
      def mergesort(nums, left, right):
          if right <= left:
              return
          mid = (left+right) >> 1
          mergesort(nums, left, mid)
          mergesort(nums, mid+1, right)
          merge(nums, left, mid, right)

      def merge(nums, left, mid, right):
          temp = []
          i = left
          j = mid+1
          while i <= mid and j <= right:
              if nums[i] <= nums[j]:
                  temp.append(nums[i])
                  i +=1
              else:
                  temp.append(nums[j])
                  j +=1
          while i<=mid:
              temp.append(nums[i])
              i +=1
          while j<=right:
              temp.append(nums[j])
              j +=1
          nums[left:right+1] = temp
          
归并和快排具有相似性，但步骤相反
归并：先排序左右数组，然后合并两个有序子数组
快排：先调配出左右子数组，然后对左右子数组进行排序
    

    3.堆排序（heap sort）  --堆插入O(logn)，取最大/小值O(1)
      a.数组元素依次构建小顶堆
      b.依次取堆顶元素，并删除
      
    #堆排序 Python代码
    def heapify(parent_index, length, nums):
        temp = nums[parent_index]
        child_index = 2*parent_index+1
        while child_index < length:
            if child_index+1 < length and nums[child_index+1] > nums[child_index]:
                child_index = child_index+1
            if temp > nums[child_index]:
                break
            nums[parent_index] = nums[child_index]
            parent_index = child_index
            child_index = 2*parent_index + 1
        nums[parent_index] = temp


    def heapsort(nums):
        for i in range((len(nums)-2)//2, -1, -1):
            heapify(i, len(nums), nums)
        for j in range(len(nums)-1, 0, -1):
            nums[j], nums[0] = nums[0], nums[j]
            heapify(0, j, nums)
            
#### 特殊排序-O(n)
1.计数排序（couting sort）
  计数排序要求输入的数据必须是确定范围的整数，将输入的数据值转化为键存储在额外开辟的数组空间中，然后依次把计数大于1的填充回原数组
2.桶排序（bucket sort）
  桶排序的工作原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）
3.基数排序（radix sort）
  基数排序是按照低位先排序，然后收集，再按照高位排序，然后再收集，依次类推，直到最高位，有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序
  
#### 例题
  有效字母的异位词（对字母快排）
  合并区间（排序+一次扫描）
  翻转对：需要重视逆序对
  



