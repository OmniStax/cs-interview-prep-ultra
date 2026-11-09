# Prefix sums and difference arrays

<!-- block prefix-sums · source oiwiki · oiwiki:basic/prefix-sum#引入 (with its 规定 box), #前缀和 (its heading dropped) and #一维前缀和 -->

## 引入

前缀和与差分是算法竞赛中常用的技巧，前者用于快速求区间和，后者用于高效进行区间修改．

???+ tip "规定"
    为方便讨论，本文默认数组 $\{a_i\}$ 下标从 $1$ 开始，并补充定义 $a_0 = 0$．

## 前缀和

前缀和可以简单理解为「数列的前 $n$ 项的和」，是一种重要的预处理方式．

### 一维前缀和

对于长度为 $n$ 的序列 $\{a_i\}$，如果要多次查询区间 $[l,r]$ 中序列数字的和，就可以考虑使用前缀和．序列的前缀和就是

$$
S_{i} = \sum_{j=1}^i a_j.
$$

它可以通过递推关系式

$$
S_0 = 0,~ S_i = S_{i-1} + a_i
$$

逐项计算得到．要询问区间 $[l,r]$ 内的序列的和，只需要计算差值

$$
S([l,r]) = S_r - S_{l-1}.
$$

就这样，通过 $O(n)$ 时间预处理，能够将单次查询区间和的复杂度降低到 $O(1)$．

???+ example "参考实现"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_1.py:core"
        ```

C++ 标准库中实现了前缀和函数 [`std::partial_sum`](https://zh.cppreference.com/w/cpp/algorithm/partial_sum)，定义于头文件 `<numeric>` 中．从 C++17 开始，标准库还提供了一个功能相同的前缀和函数 [`std::inclusive_scan`](https://zh.cppreference.com/w/cpp/algorithm/inclusive_scan)，同样定义于头文件 `<numeric>` 中．

<!-- block prefix-sums-2d · source oiwiki · oiwiki:basic/prefix-sum#二维/多维前缀和 (its opening), #基于容斥原理 and #逐维前缀和 -->

### 二维/多维前缀和

将一维前缀和拓展到多维的情形，就是多维前缀和．常见的多维前缀和的求解方法有两种．

#### 基于容斥原理

这种方法多用于二维前缀和的情形．给定大小为 $m\times n$ 的二维数组 $A$，要求出其前缀和 $S$．那么，$S$ 同样是大小为 $m\times n$ 的二维数组，且

$$
S_{i,j} = \sum_{i'\le i}\sum_{j'\le j}A_{i',j'}.
$$

类比一维的情形，$S_{i,j}$ 应该可以基于 $S_{i-1,j}$ 或 $S_{i,j-1}$ 计算，从而避免重复计算前面若干项的和．但是，如果直接将 $S_{i-1,j}$ 和 $S_{i,j-1}$ 相加，再加上 $A_{i,j}$，会导致重复计算 $S_{i-1,j-1}$ 这一重叠部分的前缀和，所以还需要再将这部分减掉．这就是 [容斥原理](../math/combinatorics/inclusion-exclusion-principle.md)．由此得到如下递推关系：

$$
S_{i,j} = A_{i,j} + S_{i-1,j} + S_{i,j-1} - S_{i-1,j-1}. 
$$

实现时，直接遍历 $(i,j)$ 求和即可．

???+ note "示例"
    考虑一个具体的例子．
    
    ![二维前缀和示例](./images/prefix-sum-2d.svg)
    
    其中，$S$ 是矩阵 $A$ 的前缀和．根据定义，$S_{3,3}$ 是左图中虚线方框中的子矩阵的和．而且，$S_{3,2}$ 是蓝色子矩阵的和，$S_{2,3}$ 是红色子矩阵的和，它们重叠部分的和是 $S_{2,2}$．由此可见，如果直接相加 $S_{3,2}$ 和 $S_{2,3}$，会重复计算 $S_{2,2}$，所以应该有
    
    $$
    S_{3,3} = A_{3,3} + S_{2,3} + S_{3,2} - S_{2,2} = 5 + 18 + 15 - 9 = 29.
    $$

同样的道理，在已经预处理出二维前缀和后，要查询左上角为 $(i_1,j_1)$、右下角为 $(i_2,j_2)$ 的子矩阵的和，可以计算

$$
S_{i_2,j_2} - S_{i_1-1,j_2} - S_{i_2,j_1-1} + S_{i_1-1,j_1-1}.
$$

这可以在 $O(1)$ 时间内完成．

在二维的情形，以上算法的时间复杂度可以简单认为是 $O(mn)$，即与给定数组的大小成线性关系．但是，当维度 $k$ 增大时，由于容斥原理涉及的项数以指数级的速度增长，时间复杂度会成为 $O(2^kN)$，其中 $k$ 是数组维度，而 $N$ 是给定数组大小．因此，该算法不再适用．

???+ example "[洛谷 P1387 最大正方形](https://www.luogu.com.cn/problem/P1387)"
    在一个 $n\times m$ 的只包含 $0$ 和 $1$ 的矩阵里找出一个不包含 $0$ 的最大正方形，输出边长．

??? note "参考代码"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_2.cpp:full-text"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_2.py:full-text"
        ```

#### 逐维前缀和

对于一般的情形，给定 $k$ 维数组 $A$，大小为 $N$，同样要求得其前缀和 $S$．这里，

$$
S_{i_1,\cdots,i_k} = \sum_{i'_1\le i_1}\cdots\sum_{i'_k\le i_k} A_{i'_1,\cdots,i'_k}.
$$

从上式可以看出，$k$ 维前缀和就等于 $k$ 次求和．所以，一个显然的算法是，每次只考虑一个维度，固定所有其它维度，然后求若干个一维前缀和，这样对所有 $k$ 个维度分别求和之后，得到的就是 $k$ 维前缀和．

??? example "三维前缀和的参考实现"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_4.cpp:core"
    ```

因为考虑每一个维度的时候，都只遍历了整个数组一遍，这样的算法复杂度是 $O(kN)$ 的，通常可以接受．

<!-- block difference-array · source oiwiki · oiwiki:basic/prefix-sum#差分 (its opening) and #一维差分 -->

## 差分

差分是一种与前缀和相对的策略，是前缀和的逆运算．相较于给定某一序列求它的差分，竞赛中更为常见的情景是，通过维护差分序列的信息，实现多次区间修改．在区间修改结束后，可以通过前缀和恢复原序列的信息，实现对原序列的查询．注意修改操作一定要在查询操作之前．

如果需要支持多次修改和查询的混合操作，需要使用 [树状数组](../ds/fenwick.md)，但是它们的思想是共通的．

### 一维差分

对于序列 $\{a_i\}$，它的差分序列 $\{D_i\}$ 是指

$$
D_i = a_i - a_{i-1},~ a_0 = 0.
$$

C++ 标准库中实现了差分函数 [`std::adjacent_difference`](https://zh.cppreference.com/w/cpp/algorithm/adjacent_difference)，定义于头文件 `<numeric>` 中．

前缀和与差分的关系如下：

???+ note "性质"
    设 $\{D_i\}$ 是 $\{a_i\}$ 的差分序列，那么，有
    
    -   序列 $\{a_i\}$ 是序列 $\{D_i\}$ 的前缀和，即
    
        $$
        a_i = \sum_{j=1}^i D_j.
        $$
    -   序列 $\{a_i\}$ 的前缀和为
    
        $$
        S_i = \sum_{j=1}^i\sum_{k=1}^jD_k = \sum_{j=1}^i(i-j+1)D_j. 
        $$

差分信息常常用于维护多次对序列的一个区间加上一个数，并在之后一次或多次询问序列某一位的取值．

假设要将序列 $\{a_i\}$ 在区间 $[l,r]$ 中的每个数都加上一个 $v$．可以在它的差分序列 $\{D_i\}$ 上做如下操作：

$$
D_{l} \gets D_{l} + v,~ D_{r+1}\gets D_{r+1} - v.
$$

在所有修改操作结束后，可以通过前缀和操作恢复更新后的 $\{a_i\}$ 的值．单次修改是 $O(1)$ 的．查询时，需要做一次 $O(n)$ 的前缀和操作，随后每次查询都是 $O(1)$ 的．

???+ example "参考代码"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_6.cpp:core"
    ```

<!-- block difference-array-2d · source oiwiki · oiwiki:basic/prefix-sum#二维/多维差分 -->

### 二维/多维差分

差分同样可以推广到多维的情形．将多维差分看作多维前缀和的逆运算，那么，求多维差分数组的操作就相当于根据多维前缀和求它的原数组．根据前文讨论，可以利用容斥原理．例如，二维差分的定义是

$$
D_{i,j} = a_{i,j} - a_{i-1,j} - a_{i,j-1} + a_{i-1,j-1}.
$$

但是，如果要计算整个差分数组，更为简单高效的做法是逐维差分，即穷举所有维度，沿着每个维度都计算一遍数组的差分．

二维差分信息常用于维护二维数组的多次矩形加．例如，要对左上角为 $(x_1,y_1)$、右下角为 $(x_2,y_2)$ 的矩阵中的每个数字都加上 $v$，可以对它的差分数组 $\{D_{i,j}\}$ 做如下操作：

$$
\begin{aligned}
D_{x_1,y_1} &\gets D_{x_1,y_1} + v, \\
D_{x_1,y_2+1} &\gets D_{x_1,y_2+1} - v,\\
D_{x_2+1,y_1} &\gets D_{x_2+1,y_1} - v,\\
D_{x_2+1,y_2+1} &\gets D_{x_2+1,y_2+1} + v.
\end{aligned}
$$

在所有修改操作结束后，只需要执行一遍二维前缀和，就可以快速查询更新后的数组的值．

??? example "参考代码"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_7.cpp:core"
    ```

当然，类似的想法对于维度 $k>2$ 也成立，但是单次修改操作需要的时间复杂度为 $O(2^k)$，随着 $k$ 增大而不再实用．

## Footnotes


