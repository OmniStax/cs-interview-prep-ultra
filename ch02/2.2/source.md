# Dynamic arrays

<!-- block arrays-intro · source ods · ods:arrays#chap:arrays, the chapter opening (the table, the three points and the amortized paragraph) -->

## Array-Based Lists

In this chapter, we will study implementations of the List and Queue interfaces where the underlying data is stored in an array, called the *backing array*. The following table summarizes the running times of operations for the data structures presented in this chapter:

|  | $\mathrm{get}(i)$/$\mathrm{set}(i,x)$ | $\mathrm{add}(i,x)$/$\mathrm{remove}(i)$ |
|---|---|---|
| ArrayStack | $O(1)$ | $O(n-i)$ |
| ArrayDeque | $O(1)$ | $O(\min\{i,n-i\})$ |
| DualArrayDeque | $O(1)$ | $O(\min\{i,n-i\})$ |
| RootishArrayStack | $O(1)$ | $O(n-i)$ |

Data structures that work by storing data in a single array have many advantages and limitations in common:

- Arrays offer constant time access to any value in the array. This is what allows $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ to run in constant time.
- Arrays are not very dynamic. Adding or removing an element near the middle of a list means that a large number of elements in the array need to be shifted to make room for the newly added element or to fill in the gap created by the deleted element. This is why the operations $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ have running times that depend on $n$ and $i$.
- Arrays cannot expand or shrink. When the number of elements in the data structure exceeds the size of the backing array, a new array needs to be allocated and the data from the old array needs to be copied into the new array. This is an expensive operation.

The third point is important. The running times cited in the table above do not include the cost associated with growing and shrinking the backing array. We will see that, if carefully managed, the cost of growing and shrinking the backing array does not add much to the cost of an *average* operation. More precisely, if we start with an empty data structure, and perform any sequence of $m$ $\mathrm{add}(i,x)$ or $\mathrm{remove}(i)$ operations, then the total cost of growing and shrinking the backing array, over the entire sequence of $m$ operations is $O(m)$. Although some individual operations are more expensive, the amortized cost, when amortized over all $m$ operations, is only $O(1)$ per operation.

<!-- block arraystack · source ods · ods:arrays#sec:arraystack, the opening and The Basics -->

## ArrayStack: Fast Stack Operations Using an Array

An ArrayStack implements the list interface using an array $a$, called the *backing array*. The list element with index $i$ is stored in $a[i]$. At most times, $a$ is larger than strictly necessary, so an integer $n$ is used to keep track of the number of elements actually stored in $a$. In this way, the list elements are stored in $a[0]$,…,$a[n-1]$ and, at all times, $\mathrm{length}(a) \ge n$.

[code codeimport ods/ArrayStack.a.n.size()]

### The Basics

Accessing and modifying the elements of an ArrayStack using $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ is trivial. After performing any necessary bounds-checking we simply return or set, respectively, $a[i]$.

[code codeimport ods/ArrayStack.get(i).set(i,x)]

The operations of adding and removing elements from an ArrayStack are illustrated in Figure 2.1. To implement the $\mathrm{add}(i,x)$ operation, we first check if $a$ is already full. If so, we call the method $\mathrm{resize}()$ to increase the size of $a$. How $\mathrm{resize}()$ is implemented will be discussed later. For now, it is sufficient to know that, after a call to $\mathrm{resize}()$, we can be sure that $\mathrm{length}(a) > n$. With this out of the way, we now shift the elements $a[i],\ldots,a[n-1]$ right by one position to make room for $x$, set $a[i]$ equal to $x$, and increment $n$.

[figure arraystack]

[code codeimport ods/ArrayStack.add(i,x)]

If we ignore the cost of the potential call to $\mathrm{resize}()$, then the cost of the $\mathrm{add}(i,x)$ operation is proportional to the number of elements we have to shift to make room for $x$. Therefore the cost of this operation (ignoring the cost of resizing $a$) is $O(n-i)$.

Implementing the $\mathrm{remove}(i)$ operation is similar. We shift the elements $a[i+1],\ldots,a[n-1]$ left by one position (overwriting $a[i]$) and decrease the value of $n$. After doing this, we check if $n$ is getting much smaller than $\mathrm{length}(a)$ by checking if $\mathrm{length}(a) \ge 3n$. If so, then we call $\mathrm{resize}()$ to reduce the size of $a$.

[code codeimport ods/ArrayStack.remove(i)]

If we ignore the cost of the $\mathrm{resize}()$ method, the cost of a $\mathrm{remove}(i)$ operation is proportional to the number of elements we shift, which is $O(n-i)$.

<!-- block resize · source ods · ods:arrays#growing-and-shrinking, the first two paragraphs and resize() -->

## Growing and Shrinking

The $\mathrm{resize}()$ method is fairly straightforward; it allocates a new array $b$ whose size is $2n$ and copies the $n$ elements of $a$ into the first $n$ positions in $b$, and then sets $a$ to $b$. Thus, after a call to $\mathrm{resize}()$, $\mathrm{length}(a) = 2n$.

[code codeimport ods/ArrayStack.resize()]

Analyzing the actual cost of the $\mathrm{resize}()$ operation is easy. It allocates an array $b$ of size $2n$ and copies the $n$ elements of $a$ into $b$. This takes $O(n)$ time.

<!-- block arraystack-cost · source ods · ods:arrays#growing-and-shrinking, from “The running time analysis from the previous section ignored…” to the end of the section: lem:arraystack-amortized with its proof, and the Summary (thm:arraystack and the push/pop paragraph) -->

## Amortized cost of resizing

The running time analysis from the previous section ignored the cost of calls to $\mathrm{resize}()$. In this section we analyze this cost using a technique known as *amortized analysis*. This technique does not try to determine the cost of resizing during each individual $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ operation. Instead, it considers the cost of all calls to $\mathrm{resize}()$ during a sequence of $m$ calls to $\mathrm{add}(i,x)$ or $\mathrm{remove}(i)$. In particular, we will show:

> **Lemma.** If an empty ArrayStack is created and any sequence of $m\ge 1$ calls to $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ are performed, then the total time spent during all calls to $\mathrm{resize}()$ is $O(m)$.

*Proof.* We will show that any time $\mathrm{resize}()$ is called, the number of calls to $\mathit{add}$ or $\mathit{remove}$ since the last call to $\mathrm{resize}()$ is at least $n/2-1$. Therefore, if $n_i$ denotes the value of $n$ during the $i$th call to $\mathrm{resize}()$ and $r$ denotes the number of calls to $\mathrm{resize}()$, then the total number of calls to $\mathrm{add}(i,x)$ or $\mathrm{remove}(i)$ is at least

[drv-arraystack-sum]

which is equivalent to

On the other hand, the total time spent during all calls to $\mathrm{resize}()$ is

since $r$ is not more than $m$. All that remains is to show that the number of calls to $\mathrm{add}(i,x)$ or $\mathrm{remove}(i)$ between the $(i-1)$th and the $i$th call to $\mathrm{resize}()$ is at least $n_i/2$.

There are two cases to consider. In the first case, $\mathrm{resize}()$ is being called by $\mathrm{add}(i,x)$ because the backing array $a$ is full, i.e., $\mathrm{length}(a) = n=n_i$. Consider the previous call to $\mathrm{resize}()$: after this previous call, the size of $a$ was $\mathrm{length}(a)$, but the number of elements stored in $a$ was at most $\mathrm{length}(a)/2=n_i/2$. But now the number of elements stored in $a$ is $n_i=\mathrm{length}(a)$, so there must have been at least $n_i/2$ calls to $\mathrm{add}(i,x)$ since the previous call to $\mathrm{resize}()$.

The second case occurs when $\mathrm{resize}()$ is being called by $\mathrm{remove}(i)$ because $\mathrm{length}(a) \ge 3n=3n_i$. Again, after the previous call to $\mathrm{resize}()$ the number of elements stored in $a$ was at least $\mathrm{length}(a)/2-1$.[^1] Now there are $n_i\le\mathrm{length}(a)/3$ elements stored in $a$. Therefore, the number of $\mathrm{remove}(i)$ operations since the last call to $\mathrm{resize}()$ is at least

[drv-shrink-case]

In either case, the number of calls to $\mathrm{add}(i,x)$ or $\mathrm{remove}(i)$ that occur between the $(i-1)$th call to $\mathrm{resize}()$ and the $i$th call to $\mathrm{resize}()$ is at least $n_i/2-1$, as required to complete the proof.

### Summary

The following theorem summarizes the performance of an ArrayStack:

> **Theorem.** An ArrayStack implements the List interface. Ignoring the cost of calls to $\mathrm{resize}()$, an ArrayStack supports the operations
> - $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ in $O(1)$ time per operation; and
- $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ in $O(1+n-i)$ time per operation.
> Furthermore, beginning with an empty ArrayStack and performing any sequence of $m$ $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ operations results in a total of $O(m)$ time spent during all calls to $\mathrm{resize}()$.

The ArrayStack is an efficient way to implement a Stack. In particular, we can implement $\mathrm{push}(x)$ as $\mathrm{add}(n,x)$ and $\mathrm{pop}()$ as $\mathrm{remove}(n-1)$, in which case these operations will run in $O(1)$ amortized time.

<!-- block fastarraystack · source ods · ods:arrays#sec:fastarraystack -->

## FastArrayStack: An Optimized ArrayStack

Much of the work done by an ArrayStack involves shifting (by $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$) and copying (by $\mathrm{resize}()$) of data. In a naive implementation, this would be done using $\textbf{for}$ loops. It turns out that many programming environments have specific functions that are very efficient at copying and moving blocks of data. In the C programming language, there are the $\mathrm{memcpy}(d,s,n)$ and $\mathrm{memmove}(d,s,n)$ functions. In the C++ language there is the $\mathrm{std{:}{:}copy}(a_0,a_1,b)$ algorithm. In Java there is the $\mathrm{System.arraycopy}(s,i,d,j,n)$ method.

[code javaimport ods/FastArrayStack.add(i,x).remove(i).resize()]

These functions are usually highly optimized and may even use special machine instructions that can do this copying much faster than we could by using a $\textbf{for}$ loop. Although using these functions does not asymptotically decrease the running times, it can still be a worthwhile optimization.

In our C++ and Java implementations, the use of fast array copying functions resulted in speedups of a factor between 2 and 3, depending on the types of operations performed. Your mileage may vary.

## Footnotes

[^1]: The ${}-1$ in this formula accounts for the special case that occurs when $n=0$ and $\mathrm{length}(a) = 1$.
