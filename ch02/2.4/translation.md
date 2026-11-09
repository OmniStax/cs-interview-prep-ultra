<!-- block prefix-sums · source oiwiki · oiwiki:basic/prefix-sum#引入 (with its 规定 box), #前缀和 (its heading dropped) and #一维前缀和 -->

## Introduction

Prefix sums and differences are techniques often used in competitive programming: the former for finding range sums quickly, the latter for carrying out range updates efficiently.

???+ tip "Convention"
    For convenience of discussion, this article takes the indices of the array $\{a_i\}$ to start from $1$ by default, and additionally defines $a_0 = 0$.

A prefix sum can be understood simply as “the sum of the first $n$ terms of a sequence”; it is an important kind of preprocessing.

### One-dimensional prefix sums

For a sequence $\{a_i\}$ of length $n$, if the sum of the numbers of the sequence in a range $[l,r]$ is to be queried many times, prefix sums are worth considering. The prefix sums of the sequence are

$$
S_{i} = \sum_{j=1}^i a_j.
$$

They can be computed from the recurrence relation

$$
S_0 = 0,~ S_i = S_{i-1} + a_i
$$

term by term. To query the sum of the sequence over the range $[l,r]$, it is enough to compute the difference

$$
S([l,r]) = S_r - S_{l-1}.
$$

In this way, with $O(n)$ time of preprocessing, the complexity of a single range-sum query is brought down to $O(1)$.

[[code-prefix-sum]]

The C++ standard library implements a prefix-sum function, [`std::partial_sum`](https://en.cppreference.com/w/cpp/algorithm/partial_sum), defined in the header `<numeric>`. Since C++17 the standard library has also provided a prefix-sum function that does the same, [`std::inclusive_scan`](https://en.cppreference.com/w/cpp/algorithm/inclusive_scan), likewise defined in the header `<numeric>`.

<!-- block prefix-sums-2d · source oiwiki · oiwiki:basic/prefix-sum#二维/多维前缀和 (its opening), #基于容斥原理 and #逐维前缀和 -->

### Two-dimensional and multidimensional prefix sums

Extending one-dimensional prefix sums to the multidimensional case gives multidimensional prefix sums. There are two common ways of computing multidimensional prefix sums.

#### Based on the inclusion–exclusion principle

This method is used mostly for two-dimensional prefix sums. Given a two-dimensional array $A$ of size $m\times n$, its prefix sum $S$ is to be found. Then $S$ is likewise a two-dimensional array of size $m\times n$, and

$$
S_{i,j} = \sum_{i'\le i}\sum_{j'\le j}A_{i',j'}.
$$

By analogy with the one-dimensional case, $S_{i,j}$ ought to be computable from $S_{i-1,j}$ or $S_{i,j-1}$, so as to avoid computing the sums of the earlier terms again. But if $S_{i-1,j}$ and $S_{i,j-1}$ are added directly and $A_{i,j}$ is then added, the prefix sum of their overlap, $S_{i-1,j-1}$, is counted twice, so that part has to be subtracted again. This is the [inclusion–exclusion principle](/cs-interview-prep-ultra/ch40/40.4/). This gives the following recurrence relation:

$$
S_{i,j} = A_{i,j} + S_{i-1,j} + S_{i,j-1} - S_{i-1,j-1}.
$$

In an implementation, it is enough to go through $(i,j)$ directly and sum.

???+ note "Example"
    Consider a concrete example.

    [[sim-prefix-2d]]

    Here $S$ is the prefix sum of the matrix $A$. By definition, $S_{3,3}$ is the sum of the submatrix in the dashed box of the left figure. Moreover, $S_{3,2}$ is the sum of the blue submatrix and $S_{2,3}$ the sum of the red submatrix, and the sum of their overlap is $S_{2,2}$. So if $S_{3,2}$ and $S_{2,3}$ are added directly, $S_{2,2}$ is counted twice, and we should have

    $$
    S_{3,3} = A_{3,3} + S_{2,3} + S_{3,2} - S_{2,2} = 5 + 18 + 15 - 9 = 29.
    $$

In the same way, once the two-dimensional prefix sums have been preprocessed, to query the sum of the submatrix whose upper-left corner is $(i_1,j_1)$ and whose lower-right corner is $(i_2,j_2)$, one can compute

$$
S_{i_2,j_2} - S_{i_1-1,j_2} - S_{i_2,j_1-1} + S_{i_1-1,j_1-1}.
$$

This can be done in $O(1)$ time.

In the two-dimensional case, the time complexity of the algorithm above can be taken simply as $O(mn)$, that is, linear in the size of the given array. But as the dimension $k$ grows, the number of terms the inclusion–exclusion principle involves grows exponentially, and the time complexity becomes $O(2^kN)$, where $k$ is the dimension of the array and $N$ the size of the given array. So the algorithm is no longer suitable.

#### Prefix sums dimension by dimension

For the general case, given a $k$-dimensional array $A$ of size $N$, its prefix sum $S$ is likewise to be found. Here,

$$
S_{i_1,\cdots,i_k} = \sum_{i'_1\le i_1}\cdots\sum_{i'_k\le i_k} A_{i'_1,\cdots,i'_k}.
$$

The formula above shows that a $k$-dimensional prefix sum is just $k$ summations. So an obvious algorithm is to consider one dimension at a time, holding all the other dimensions fixed, and compute a number of one-dimensional prefix sums; once this has been done along each of the $k$ dimensions in turn, the result is the $k$-dimensional prefix sum.

Because each dimension is considered in a single pass over the whole array, the complexity of this algorithm is $O(kN)$, which is usually acceptable.

<!-- block difference-array · source oiwiki · oiwiki:basic/prefix-sum#差分 (its opening) and #一维差分 -->

## Differences

Taking differences is a strategy opposite to the prefix sum: it is the inverse operation of the prefix sum. Rather than finding the differences of a given sequence, the more common situation in competitions is to carry out many range updates by maintaining the information of the difference sequence. When the range updates are finished, the information of the original sequence can be recovered by a prefix sum, so that the original sequence can be queried. Note that the update operations must come before the query operations.

If a mix of many updates and queries has to be supported, a [Fenwick tree](/cs-interview-prep-ultra/ch30/30.2/) is needed, but the ideas behind the two are the same.

### One-dimensional differences

For a sequence $\{a_i\}$, its difference sequence $\{D_i\}$ is

$$
D_i = a_i - a_{i-1},~ a_0 = 0.
$$

The C++ standard library implements a difference function, [`std::adjacent_difference`](https://en.cppreference.com/w/cpp/algorithm/adjacent_difference), defined in the header `<numeric>`.

The relation between prefix sums and differences is as follows:

???+ note "Properties"
    Let $\{D_i\}$ be the difference sequence of $\{a_i\}$. Then

    -   the sequence $\{a_i\}$ is the prefix sum of the sequence $\{D_i\}$, that is,

        $$
        a_i = \sum_{j=1}^i D_j.
        $$
    -   the prefix sum of the sequence $\{a_i\}$ is

        $$
        S_i = \sum_{j=1}^i\sum_{k=1}^jD_k = \sum_{j=1}^i(i-j+1)D_j.
        $$

Difference information is often used to keep up with many additions of a number to a range of a sequence, followed by one or more queries of the value at some position of the sequence.

Suppose $v$ is to be added to every number of the sequence $\{a_i\}$ in the range $[l,r]$. The following operation can be done on its difference sequence $\{D_i\}$:

$$
D_{l} \gets D_{l} + v,~ D_{r+1}\gets D_{r+1} - v.
$$

Once all the updates are finished, the updated values of $\{a_i\}$ can be recovered by a prefix-sum operation. A single update is $O(1)$. To query, one $O(n)$ prefix-sum operation is needed, after which every query is $O(1)$.

[[sim-range-add]]

<!-- block difference-array-2d · source oiwiki · oiwiki:basic/prefix-sum#二维/多维差分 -->

### Two-dimensional and multidimensional differences

Differences generalise to the multidimensional case as well. Seen as the inverse operation of the multidimensional prefix sum, finding a multidimensional difference array amounts to recovering the original array from its multidimensional prefix sum. By the discussion above, the inclusion–exclusion principle can be used. For example, the two-dimensional difference is defined as

$$
D_{i,j} = a_{i,j} - a_{i-1,j} - a_{i,j-1} + a_{i-1,j-1}.
$$

But to compute the whole difference array, a simpler and more efficient way is to take differences dimension by dimension: go through every dimension and compute the differences of the array once along each of them.

Two-dimensional difference information is often used to keep up with many rectangle additions on a two-dimensional array. For example, to add $v$ to every number of the matrix whose upper-left corner is $(x_1,y_1)$ and whose lower-right corner is $(x_2,y_2)$, the following operations can be done on its difference array $\{D_{i,j}\}$:

$$
\begin{aligned}
D_{x_1,y_1} &\gets D_{x_1,y_1} + v, \\
D_{x_1,y_2+1} &\gets D_{x_1,y_2+1} - v,\\
D_{x_2+1,y_1} &\gets D_{x_2+1,y_1} - v,\\
D_{x_2+1,y_2+1} &\gets D_{x_2+1,y_2+1} + v.
\end{aligned}
$$

After all the updates are finished, a single pass of two-dimensional prefix sums is all it takes to query the updated values of the array quickly.

Of course, a similar idea holds for dimensions $k>2$, but a single update then takes $O(2^k)$ time, which stops being practical as $k$ grows.
