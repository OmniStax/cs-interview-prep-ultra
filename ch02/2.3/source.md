# Two pointers and sliding windows

<!-- block two-pointers · source oiwiki · oiwiki:misc/two-pointer#引入 -->

## 引入

双指针是一种简单而又灵活的技巧和思想，单独使用可以轻松解决一些特定问题，和其他算法结合也能发挥多样的用处．

双指针顾名思义，就是同时使用两个指针，在序列、链表结构上指向的是位置，在树、图结构中指向的是节点，通过或同向移动，或相向移动来维护、统计信息．

接下来我们来看双指针的几个具体使用方法．

<!-- block sorted-pair · source oiwiki · oiwiki:misc/two-pointer#利用序列有序性 (its opening, 例题 4 as a link, and 过程) -->

## 利用序列有序性

很多时候在序列上使用双指针之所以能够正确地达到目的，是因为序列的某些性质，最常见的就是利用序列的有序性．

???+ note "例题 4 [leetcode 167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)"
    给定一个已按照 **升序排列** 的整数数组 `numbers`，请你从数组中找出两个数满足相加之和等于目标数 `target`．

### 过程

这种问题也是双指针的经典应用了，虽然二分也很方便，但时间复杂度上多一个 $\log{n}$，而且代码不够简洁．

接下来介绍双指针做法：既然要找到两个数，且这两个数不能在同一位置，那其位置一定是一左一右．由于两数之和固定，那么两数之中的小数越大，大数越小．考虑到这些性质，那我们不妨从两边接近它们．

首先假定答案就是 1 和 n，如果发现 $num[1]+num[n]\gt \mathit{target}$，说明我们需要将其中的一个元素变小，而 $\mathit{num}[1]$ 已经不能再变小了，所以我们把指向 $n$ 的指针减一，让大数变小．

同理如果发现 $num[1]+num[n]\lt \mathit{target}$，说明我们要将其中的一个元素变大，但 $\mathit{num}[n]$ 已经不能再变大了，所以将指向 1 的指针加一，让小数变大．

推广到一般情形，如果此时我们两个指针分别指在 $l,r$ 上，且 $l\lt r$, 如果 $num[l]+num[r]\gt \mathit{target}$，就将 $r$ 减一，如果 $num[l]+num[r]\lt \mathit{target}$，就将 $l$ 加一．这样 $l$ 不断右移，$r$ 不断左移，最后两者各逼近到一个答案．

<!-- block three-sum · source wikipedia · wikipedia:3SUM (the lead’s first sentence) and #Quadratic algorithm -->

{{Short description|Problem in computational complexity theory}}
{{CS1 config|mode=cs2}}

In [[computational complexity theory]], the '''3SUM''' problem asks if a given set of <math>n</math> real numbers contains three elements that sum to zero.

== Quadratic algorithm ==
Suppose the input array is <math>S[0..n-1]</math>.  In integer ([[word RAM]]) models of computing, 3SUM can be solved in <math>O(n^2)</math> time on average by inserting each number <math>S[i]</math> into a [[hash table]], and then, for each index <math>i</math> and <math>j</math>, checking whether the hash table contains the integer <math>-(S[i]+S[j])</math>.

It is also possible to solve the problem in the same time in a [[Comparison (computer programming)|comparison]]-based model of computing or [[real RAM]], for which hashing is not allowed. The algorithm below first sorts the input array and then tests all possible pairs in a careful order that avoids the slowdown of a [[binary search]] per pair, achieving worst-case <math>O(n^2)</math> time, as follows.<ref>[http://www.ti.inf.ethz.ch/ew/courses/CG09/materials/v12.pdf Visibility Graphs and 3-Sum] by Michael Hoffmann</ref>
 sort(S);
 '''for''' i = 0 '''to''' n - 2 '''do'''
     a = S[i];
     start = i + 1;
     end = n - 1;
     '''while''' (start < end) '''do'''
         b = S[start]
         c = S[end];
         '''if''' (a + b + c == 0) '''then'''
             '''output''' a, b, c;
             // Continue search for all triplet combinations summing to zero.
             // We need to update both end and start together since the array values are distinct.
             start = start + 1;
             end = end - 1;
         '''else''' '''if''' (a + b + c > 0) '''then'''
             end = end - 1;
         '''else'''
             start = start + 1;
     '''end'''
 '''end'''

The following example shows this algorithm's execution on a small [[sorted array]]. Current values of '''a''' are shown in red, values of '''b''' and '''c''' are shown in magenta.
  <span style="color:red">-25</span> <span style="color:magenta">-10</span> -7 -3 2 4 8 <span style="color:magenta">10</span>  (a+b+c==-25)
  <span style="color:red">-25</span> -10 <span style="color:magenta">-7</span> -3 2 4 8 <span style="color:magenta">10</span>  (a+b+c==-22)
  . . .
  <span style="color:red">-25</span> -10 -7 -3 2 4 <span style="color:magenta">8</span> <span style="color:magenta">10</span>  (a+b+c==-7)
  -25 <span style="color:red">-10</span> <span style="color:magenta">-7</span> -3 2 4 8 <span style="color:magenta">10</span>  (a+b+c==-7)
  -25 <span style="color:red">-10</span> -7 <span style="color:magenta">-3</span> 2 4 8 <span style="color:magenta">10</span>  (a+b+c==-3)
  -25 <span style="color:red">-10</span> -7 -3 <span style="color:magenta">2</span> 4 8 <span style="color:magenta">10</span>  (a+b+c==2)
  -25 <span style="color:red">-10</span> -7 -3 <span style="color:magenta">2</span> 4 <span style="color:magenta">8</span> 10  (a+b+c==0)

The correctness of the algorithm can be seen as follows. Suppose we have a solution a + b + c = 0. Since the pointers only move in one direction, we can run the algorithm until the leftmost pointer points to a. Run the algorithm until either one of the remaining pointers points to b or c, whichever occurs first. Then the algorithm will run until the last pointer points to the remaining term, giving the affirmative solution.

<!-- block merge · source wikipedia · wikipedia:Merge_algorithm#Merging two lists -->

== Merging two lists ==
Merging two sorted lists into one can be done in [[linear time]] and linear or constant space (depending on the data access model). The following [[pseudocode]] demonstrates an algorithm that merges input lists (either [[linked list]]s or [[Array data structure|arrays]]) {{mvar|A}} and {{mvar|B}} into a new list {{mvar|C}}.<ref name="skiena">{{cite book |last=Skiena |first=Steven |author-link=Steven Skiena |title=The Algorithm Design Manual |publisher=[[Springer Science+Business Media]] |edition=2nd |year=2010 |isbn=978-1-849-96720-4 |page=123}}</ref>{{r|toolbox}}{{rp|104}} The function {{mono|head}} yields the first element of a list; "dropping" an element means removing it from its list, typically by incrementing a pointer or index.

 '''algorithm''' merge(A, B) '''is'''
     '''inputs''' A, B : list
     '''returns''' list
 
     C := new empty list
     '''while''' A is not empty and B is not empty '''do'''
         '''if''' head(A) ≤ head(B) '''then'''
             append head(A) to C
             drop the head of A
         '''else'''
             append head(B) to C
             drop the head of B
 
     ''// By now, either A or B is empty. It remains to empty the other input list.''
     '''while''' A is not empty '''do'''
         append head(A) to C
         drop the head of A
     '''while''' B is not empty '''do'''
         append head(B) to C
         drop the head of B
 
     '''return''' C

When the inputs are linked lists, this algorithm can be implemented to use only a constant amount of working space; the pointers in the lists' nodes can be reused for bookkeeping and for constructing the final merged list.

In the merge sort algorithm, this [[subroutine]] is typically used to merge two sub-arrays {{mono|A[lo..mid]}}, {{mono|A[mid+1..hi]}} of a single array {{mono|A}}. This can be done by copying the sub-arrays into a temporary array, then applying the merge algorithm above.{{r|skiena}} The allocation of a temporary array can be avoided, but at the expense of speed and programming ease. Various in-place merge algorithms have been devised,<ref>{{cite journal |last1=Katajainen |first1=Jyrki |first2=Tomi |last2=Pasanen |first3=Jukka |last3=Teuhola |title=Practical in-place mergesort |journal=Nordic J. Computing |volume=3 |issue=1 |year=1996 |pages=27–40 | url = https://dl.acm.org/doi/10.5555/642136.642138}}</ref> sometimes sacrificing the linear-time bound to produce an {{math|''O''(''n'' log ''n'')}} algorithm;<ref>{{Cite conference| doi = 10.1007/978-3-540-30140-0_63| title = Stable Minimum Storage Merging by Symmetric Comparisons| conference = European Symp. Algorithms| volume = 3221| pages = 714–723| series = Lecture Notes in Computer Science| year = 2004| last1 = Kim | first1 = Pok-Son| last2 = Kutzner | first2 = Arne| isbn = 978-3-540-23025-0}}</ref> see {{slink|Merge sort|Variants}} for discussion.

<!-- block moving-average · source wikipedia · wikipedia:Moving_average#Simple moving average, from its opening to “…and only 3 arithmetic steps.” -->

== Simple moving average ==
[[File: Moving Average Types comparison - Simple and Exponential.png|thumb]]
In financial applications a '''simple moving average''' ('''SMA''') is the unweighted [[arithmetic mean|mean]] of the previous <math>k</math> data-points. However, in science and engineering, the mean is normally taken from an equal number of data on either side of a central value. This ensures that variations in the mean are aligned with the variations in the data rather than being shifted in time. {{Anchor|algorithm}}An example of a simple equally weighted running mean is the mean over the last <math>k</math> entries of a data-set containing <math>n</math> entries. Let those data-points be <math>p_1, p_2, \dots, p_n</math>. This could be closing prices of a stock. The mean over the last <math>k</math> data-points (days in this example) is denoted as <math>\textit{SMA}_{k}</math> and calculated as:
<math display="block">\begin{align}
  \textit{SMA}_{k} &= \frac{p_{n-k+1} + p_{n-k+2} + \cdots + p_{n}}{k} \\
  &= \frac{1}{k} \sum_{i=n-k+1}^{n} p_{i}
\end{align}</math>

When calculating the next mean <math>\textit{SMA}_{k,\text{next}}</math> with the same sampling width <math>k</math> the range from <math> n - k + 2 </math> to <math> n+1 </math> is considered. A new value <math>p_{n+1}</math> comes into the sum and the oldest value <math>p_{n-k+1}</math> drops out. This simplifies the calculations by reusing the previous mean <math>\textit{SMA}_{k,\text{prev}}</math>.
<math display="block">
\begin{align}
   \textit{SMA}_{k, \text{next}} &= \frac{1}{k} \sum_{i=n-k+2}^{n+1} p_{i} \\
              &= \frac{1}{k} \Big( \underbrace{ p_{n-k+2} + p_{n-k+3} + \dots + p_{n} + p_{n+1} }_{ \sum_{i=n-k+2}^{n+1} p_{i} } + \underbrace{ p_{n-k+1} - p_{n-k+1} }_{= 0} \Big) \\
              &= \underbrace{ \frac{1}{k} \Big( p_{n-k+1} + p_{n-k+2} + \dots + p_{n} \Big) }_{= \textit{SMA}_{k, \text{prev}}} - \frac{p_{n-k+1}}{k} + \frac{p_{n+1}}{k} \\
              &= \textit{SMA}_{k, \text{prev}} + \frac{1}{k} \Big( p_{n+1} - p_{n-k+1} \Big)
\end{align}
</math>
This means that the moving average filter can be computed quite cheaply on real time data with a FIFO / [[circular buffer]] and only 3 arithmetic steps.

<!-- block variable-window · source oiwiki · oiwiki:misc/two-pointer#维护区间信息 (its opening, 例题 1 as a link, and its 过程) -->

## 维护区间信息

如果不和其他数据结构结合使用，双指针维护区间信息的最简单模式就是维护具有一定单调性，新增和删去一个元素都很方便处理的信息，就比如正数的和、正整数的积等等．

### 例题 1

???+ note "例题 1 [leetcode 713. 乘积小于 K 的子数组](https://leetcode-cn.com/problems/subarray-product-less-than-k/)"
    给定一个长度为 $n$ 的正整数数组 $\mathit{nums}$ 和整数 $k$，找出该数组内乘积小于 $k$ 的连续子数组的个数．
    
    其中，$1 \leq n \leq 3 \times 10^4, 1 \leq nums[i] \leq 1000, 0 \leq k \leq 10^6$．

#### 过程

设两个指针分别为 $l,r$，另外设置一个变量 $\mathit{tmp}$ 记录 $[l,r]$ 内所有数的乘积．最开始 $l,r$ 都在最左面，先向右移动 $r$，直到第一次发现 $\mathit{tmp}\geq k$，这时就固定 $r$，右移 $l$，直到 $\mathit{tmp}\lt k$．那么对于每个 $r$，$l$ 是它能延展到的左边界，由于正整数乘积的单调性，此时以 $r$ 为右端点的满足题目条件的区间个数为 $r-l+1$ 个．
