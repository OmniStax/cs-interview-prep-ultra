<!-- block two-pointers · source oiwiki · oiwiki:misc/two-pointer#引入 -->

## Introduction

Two pointers is a simple yet flexible technique and way of thinking: used on its own it easily solves certain specific problems, and combined with other algorithms it can serve many different purposes.

As the name suggests, two pointers means using two pointers at the same time: on sequences and linked lists they point at positions, on trees and graphs they point at nodes, and by moving either in the same direction or toward each other they maintain and count information.

Next, let us look at several concrete ways of using two pointers.

<!-- block sorted-pair · source oiwiki · oiwiki:misc/two-pointer#利用序列有序性 (its opening, 例题 4 as a link, and 过程) -->

## Using the order of a sequence

Much of the time, two pointers used on a sequence reach their goal correctly because of some property of the sequence, and the most common one is that the sequence is sorted.

[[lc167]]

### Procedure

This kind of problem is another classic application of two pointers; binary search is convenient too, but its time complexity carries an extra $\log{n}$, and its code is not as concise.

Next, the two-pointer approach. Since we must find two numbers, and the two cannot be at the same position, their positions must be one on the left and one on the right. Since the sum of the two numbers is fixed, the larger the smaller of the two numbers is, the smaller the larger one is. Given these properties, we may as well approach them from both ends.

First suppose the answer is 1 and n. If we find that $num[1]+num[n]\gt \mathit{target}$, we need to make one of the elements smaller, and $\mathit{num}[1]$ cannot get any smaller, so we decrease the pointer at $n$ by one, making the larger number smaller.

Likewise, if we find that $num[1]+num[n]\lt \mathit{target}$, we need to make one of the elements larger, but $\mathit{num}[n]$ cannot get any larger, so we increase the pointer at 1 by one, making the smaller number larger.

Generalising, if our two pointers are now at $l,r$, with $l\lt r$, then if $num[l]+num[r]\gt \mathit{target}$ we decrease $r$ by one, and if $num[l]+num[r]\lt \mathit{target}$ we increase $l$ by one. In this way $l$ keeps moving right and $r$ keeps moving left, until each of them has closed in on one number of the answer.

<!-- block variable-window · source oiwiki · oiwiki:misc/two-pointer#维护区间信息 (its opening, 例题 1 as a link, and its 过程) -->

## Maintaining information over a range

If two pointers are not combined with other data structures, the simplest pattern for maintaining information over a range with them is to maintain information that has a certain monotonicity and in which adding or removing one element is easy to handle, such as a sum of positive numbers or a product of positive integers.

### Example

[[lc713]]

#### Procedure

Let the two pointers be $l,r$, and keep in addition a variable $\mathit{tmp}$ that records the product of all the numbers in $[l,r]$. At the start $l,r$ are both at the far left. First move $r$ to the right until we find $\mathit{tmp}\geq k$ for the first time; then fix $r$ and move $l$ to the right until $\mathit{tmp}\lt k$. Then for each $r$, $l$ is the left boundary it can extend to, and by the monotonicity of products of positive integers, the number of ranges with right endpoint $r$ that satisfy the problem's condition is $r-l+1$.
