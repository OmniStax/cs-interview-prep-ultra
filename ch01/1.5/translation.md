<!-- block amortized · source oiwiki · oiwiki:basic/amortized-analysis#引入, #内容 (its heading dropped) and #聚合分析 -->

## Introduction

Amortized analysis is a technique for analysing the performance of algorithms and dynamic data structures. It looks not only at the cost of a single operation but, by evaluating the average cost of a sequence of operations, gives a more accurate assessment of overall performance. Amortized analysis involves no probability, and it can only guarantee the average time per operation of worst-case performance; it cannot establish the average performance of the system. In the worst case, amortized analysis spreads the overhead of expensive operations over cheap operations, ensuring that the average cost of the operations as a whole stays within a reasonable range.

Amortized analysis usually uses three main methods of analysis: aggregate analysis, the accounting method and the potential method. Each of these methods has its own emphasis and suits different situations, but they share a common goal: by balancing the costs of operations, to optimise the overall worst-case performance of a data structure.

Consider a growable array, such as `vector` in C++, whose initial capacity is $m = 1$. Each time a new element is inserted, if the array is full, the size of the array must be doubled, then the elements of the original array are copied into the new array, and finally the new element is inserted.

Next, taking the insert operation of the dynamic array as the example, its amortized cost is analysed by the three methods of aggregate analysis, the accounting method and the potential method.

### Aggregate analysis

Aggregate analysis computes the total cost of a sequence of operations and averages it over each operation, which gives the amortized time complexity of each operation.

Taking the dynamic array as the example, first, two key costs of the insert operation can be obtained:

-   If the array is not full, the cost of the insert operation is $O(1)$.
-   If the array is full, the insert operation must resize, and the cost of copying the elements after the resize is $O(m)$, where $m$ is the current size of the array.

So, to compute the total cost of $n$ insert operations, it can be split into two parts:

1.  **The cost of the insert operations**: the direct cost of inserting each new element is constant time $O(1)$; for $n$ operations, the total cost is $O(n)$;
2.  **The cost of resizing the array**: each resize involves copying the elements of the original array into the new array. These operations happen when the size of the array is a power of $2$. The total number of elements copied in resizes is the sum of all the powers of two strictly less than $n$; when $n\ge1$, the total copying cost is $\sum_{i=0}^{\lceil\log_2 n\rceil - 1}2^i=2^{\lceil\log_2 n\rceil}-1<2n$, and the total cost is $O(n)$.

Therefore, the total insertion cost of the array is $O(n)$, and the cost amortized to each operation is $O(1)$. Even in the worst case, the average cost of each insert operation is still constant time.

<!-- block accounting · source oiwiki · oiwiki:basic/amortized-analysis#记账分析 -->

### The accounting method

The accounting method assigns each operation a fixed amortized cost in advance, to ensure that the total cost of all the operations does not exceed the sum of these preassigned costs. The accounting method resembles a mechanism of **paying in advance**, in which operations of lower cost store part of their credit to pay for expensive operations in the future.

Taking the dynamic array as the example, each insert operation can be assigned a fixed amortized cost, to ensure that enough credit has already been set aside when a resize is needed.

1.  **Assigning credit**:
    -   Suppose the actual cost of each insert operation is $1$, and its amortized cost is set to $3$.
    -   Of this, $1$ is used for the current insert operation and $2$ for a possible future resize.

2.  **Spending credit**:
    -   When the array is full, a resize must be performed, with actual cost $O(m)$, where $m$ is the current size of the array.
    -   Suppose the array holds $n$ elements before the resize; since the $n/2$ elements of the latter half of the original array prestored $n$ units of amortized cost in all when they were inserted, this is exactly enough to pay for the cost of the resize.

Here is a concrete example:

[[sim-pay-for-doubling]]

The process above shows that the amortized cost stored by each insert operation is enough to pay for future resizes, which ensures that the amortized cost of each operation stays at $O(1)$.

<!-- block potential · source oiwiki · oiwiki:basic/amortized-analysis#势能分析, with #原理 and #示例：动态数组的扩容分析 -->

### The potential method

The potential method defines a potential function (usually written $\Phi$) that measures the **potential energy** of a data structure, that is, the resources reserved in the state of the system, which can be used to pay for expensive operations in the future. The changes of the potential are used to balance the total cost of a sequence of operations, which ensures that the amortized cost of the whole algorithm stays within a reasonable range.

#### Principle

First, define a **state** $S$ as the state of the data structure at some moment; the state may include the number of elements, the capacity, pointers and other information, and the initial state is defined as $S_0$, the state before any operation has been performed.

Next, define a potential function $\Phi(S)$ that measures the potential of the data structure in state $S$; with the initial state $S_0$, the potential of every reachable state $S$ must satisfy $\Phi(S) \geq \Phi(S_0)$[^clemson][^uci][^stanford]; some sources additionally require $\Phi(S_0)=0$[^cornell], which is in fact unnecessary.

For each operation, its amortized cost $\hat{c}$ is defined as:

$$
\hat{c} = c + \Phi(S') - \Phi(S)
$$

where $c$ is the actual cost of the operation, and $S$ and $S'$ are the states of the data structure before and after the operation. The formula shows that the amortized cost equals the actual cost plus the change in potential. If an operation increases the potential (that is, $\Phi(S') > \Phi(S)$), the amortized cost goes up; if an operation uses up potential (that is, $\Phi(S') < \Phi(S)$), the amortized cost goes down.

We can analyse the total cost of a sequence of operations through the potential function. Let $S_1, S_2, \dots, S_m$ be the sequence of states produced by $m$ operations starting from the initial state $S_0$, and $c_i$ the actual cost of the $i$-th operation; then the amortized cost $p_i$ of the $i$-th operation is:

$$
p_i = c_i + \Phi(S_i) - \Phi(S_{i-1})
$$

Therefore, the total time cost of the $m$ operations is:

$$
\sum_{i=1}^m c_i = \sum_{i=1}^m p_i + \Phi(S_0) - \Phi(S_m)
$$

Since $\Phi(S) \geq \Phi(S_0)$, an upper bound on the total time cost is:

$$
\sum_{i=1}^m p_i \geq \sum_{i=1}^m c_i
$$

Therefore, if $p_i = O(T(n))$, then $O(T(n))$ is an upper bound on the amortized complexity.

#### Example: analysing the resizing of a dynamic array

Taking the insert operation of the dynamic array `vector` as the example, write the initial state as $h_0$ and define the following potential function $\Phi(h)$:

$$
\Phi(h) = 2n - m
$$

where $n$ is the number of elements in the array and $m$ is the current capacity of the array. The changes of this potential function reflect the rise and fall of the prestored credit used to pay for future resizes. In the initial state, the empty array of capacity $1$, $\Phi(h_0)=-1$; in the non-empty reachable states where elements are only inserted and the array doubles when full, $m\leq 2n$, so $\Phi(h)\geq 0>\Phi(h_0)$.

1.  **Insert (no resize needed)**:
    -   **Operation cost**: $O(1)$, since only one element is inserted.
    -   **Change in potential**: after the insert, the number of elements increases by 1 and the potential increases by $2$.
        -   $\Phi(h') - \Phi(h) = 2(n + 1) - m - (2n - m) = 2$.
    -   **Amortized cost**: $1 + 2 = 3$.

2.  **Insert (triggers a resize)**:
    -   Suppose the current capacity is $m = n$; inserting a new element triggers a resize, and the new capacity becomes $2n$.
    -   **Operation cost**: $O(n)$, since all the elements must be copied into the new array and the new element inserted.
    -   **Change in potential**: the change in potential after the resize and the insert is $2-n$, which is a decrease only when $n>2$.
        -   $\Phi(h') - \Phi(h) = 2(n + 1) - 2n - (2n - n) = 2 - n$.
    -   **Amortized cost**: $n + 1 + (2 - n) = 3$.

The analysis above shows that, although the actual cost of a resize is high, thanks to the design of the potential function the overall amortized cost still stays at the constant level $O(1)$.

<!-- block stack-example · source oiwiki · oiwiki:basic/amortized-analysis#扩展示例：堆栈操作 (its opening and table), #聚合分析法 and #记账分析法 -->

## Extended example: stack operations

Stack operations are one of the classic applications of amortized analysis. Suppose we start from an empty stack and `pop` is used only on a non-empty stack; the stack `S` supports the following three operations:

| Operation        | Description             | Actual cost $c_i$           |
| ---------------- | ----------------------- | --------------------------- |
| `S.push(x)`      | Push element $x$ onto the stack | $1$                 |
| `S.pop()`        | Pop the element at the top of the stack | $1$         |
| `S.multi-pop(k)` | Pop at most $k$ elements from the top of the stack | $O(\min(\lvert S\rvert,k))$ |

We will analyse the amortized cost of these stack operations by the three methods of aggregate analysis, the accounting method and the potential method.

### The aggregate method

Aggregate analysis computes the total cost of all the operations and spreads it evenly over each operation, which gives the amortized cost.

1.  For $n_{\text{push}}$ `push(x)` operations, each costs $O(1)$, so the total cost is $O(n_{\text{push}})$;
2.  For $n_{\text{pop}}$ `pop()` operations, each costs $O(1)$, and the total cost is $O(n_{\text{pop}})$;
3.  For $n_{\text{multi-pop}}$ `multi-pop(k)` operations, although the actual cost of each is $O(\min(\lvert S \rvert, k))$, the number of elements these operations pop cannot exceed the number of elements pushed before by `push(x)`, so the total cost is still bounded by $n_{\text{push}}$.

The total number of operations is $n=n_{\text{push}}+n_{\text{pop}}+n_{\text{multi-pop}}$, and $n_{\text{push}}\le n$. Each element is pushed and popped at most once each, so the total cost charged per element is $O(n_{\text{push}})=O(n)$; even counting separately a constant checking overhead for each call, the total cost is still $O(n)$, amortized to $O(1)$.

### The accounting method

The accounting method sets aside part of the credit at each `push(x)` operation, to pay for possible future `pop()` or `multi-pop(k)` operations.

1.  **`S.push(x)`**: suppose the amortized cost of each `push(x)` operation is $2$, of which $1$ unit is used for the current operation and the other $1$ unit is stored as credit, to pay for a future `pop()` or `multi-pop(k)` operation;
2.  **`S.pop()`**: the actual cost is $1$, but since an earlier `push(x)` operation has already prestored $1$ unit of credit for it, the amortized cost is $0$;
3.  **`S.multi-pop(k)`**: the actual cost of each popped element is $1$, which can be paid by the credit prestored by that element's earlier `push(x)` operation, so the amortized cost is $0$.

From the analysis above, the credit prestored by push operations is enough to pay for the future pop operations of those elements, so the amortized cost of each operation is $O(1)$.

<!-- block stack-potential · source oiwiki · oiwiki:basic/amortized-analysis#扩展示例：堆栈操作, its #势能分析法 -->

### The potential method

The potential method defines a potential function to measure the state of the stack, and uses the changes of the potential to balance the costs of operations.

1.  **Potential function**: let $\Phi(h)$ be the number of elements in the stack, that is, $\Phi(h) = \lvert S \rvert$. Each element contributes $1$ unit of potential;
2.  **`S.push(x)`**: each `push(x)` operation increases the number of elements in the stack, and the potential increases by $1$, so the amortized cost is $1 + 1 = 2$;
3.  **`S.pop()`**: each `pop()` operation decreases the number of elements in the stack, and the potential decreases by $1$, so the amortized cost is $1 - 1 = 0$;
4.  **`S.multi-pop(k)`**: let $t=\min(\lvert S\rvert,k)$; `multi-pop(k)` actually pops $t$ elements and the potential decreases by $t$, so the amortized cost charged per element is $t-t=0$; counting the call overhead, it is $O(1)$.

With the potential function designed as above, the amortized cost of the `push(x)` operation is $2$, while the amortized cost of the `pop()` and `multi-pop(k)` operations is $0$. Therefore, the amortized cost of every stack operation is $O(1)$.
