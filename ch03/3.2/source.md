# Queues and circular buffers

<!-- block queue · source ods · ods:intro#the-queue-stack-and-deque-interfaces, the opening paragraph and its list, the FIFO paragraph and fig. queue (to “…called enqueue(x) and dequeue(), respectively.”) -->

## The Queue Interface

The Queue interface represents a collection of elements to which we can add elements and remove the next element. More precisely, the operations supported by the Queue interface are

- $\mathrm{add}(x)$: add the value $x$ to the Queue
- $\mathrm{remove}()$: remove the next (previously added) value, $y$, from the Queue and return $y$

Notice that the $\mathrm{remove}()$ operation takes no argument. The Queue’s *queueing discipline* decides which element should be removed. There are many possible queueing disciplines, the most common of which include FIFO, priority, and LIFO.

A *FIFO (first-in-first-out) Queue*, which is illustrated in Figure 1.1, removes items in the same order they were added, much in the same way a queue (or line-up) works when checking out at a cash register in a grocery store. This is the most common kind of Queue so the qualifier FIFO is often omitted. In other texts, the $\mathrm{add}(x)$ and $\mathrm{remove}()$ operations on a FIFO Queue are often called $\mathrm{enqueue}(x)$ and $\mathrm{dequeue}()$, respectively.

[figure queue]

<!-- block circular · source ods · ods:arrays#sec:arrayqueue, from the opening through “…does not exceed the size of a.” (the circular array) -->

## ArrayQueue: An Array-Based Queue

In this section, we present the ArrayQueue data structure, which implements a FIFO (first-in-first-out) queue; elements are removed (using the $\mathrm{remove}()$ operation) from the queue in the same order they are added (using the $\mathrm{add}(x)$ operation).

Notice that an ArrayStack is a poor choice for an implementation of a FIFO queue. It is not a good choice because we must choose one end of the list upon which to add elements and then remove elements from the other end. One of the two operations must work on the head of the list, which involves calling $\mathrm{add}(i,x)$ or $\mathrm{remove}(i)$ with a value of $i=0$. This gives a running time proportional to $n$.

To obtain an efficient array-based implementation of a queue, we first notice that the problem would be easy if we had an infinite array $a$. We could maintain one index $j$ that keeps track of the next element to remove and an integer $n$ that counts the number of elements in the queue. The queue elements would always be stored in

$$a[j],a[j+1],\ldots,a[j+n-1] \enspace .$$

Initially, both $j$ and $n$ would be set to 0. To add an element, we would place it in $a[j+n]$ and increment $n$. To remove an element, we would remove it from $a[j]$, increment $j$, and decrement $n$.

Of course, the problem with this solution is that it requires an infinite array. An ArrayQueue simulates this by using a finite array $a$ and *modular arithmetic*. This is the kind of arithmetic used when we are talking about the time of day. For example 10:00 plus five hours gives 3:00. Formally, we say that

$$10 + 5 = 15 \equiv 3 \pmod{12} \enspace .$$

We read the latter part of this equation as “15 is congruent to 3 modulo 12.” We can also treat $\bmod$ as a binary operator, so that

$$15 \bmod 12 = 3 \enspace .$$

More generally, for an integer $a$ and positive integer $m$, $a \bmod m$ is the unique integer $r\in\{0,\ldots,m-1\}$ such that $a = r + km$ for some integer $k$. Less formally, the value $r$ is the remainder we get when we divide $a$ by $m$. In many programming languages, including C, C++, and Java, the mod operate is represented using the % symbol.

Modular arithmetic is useful for simulating an infinite array, since $i\bmod \mathrm{length}(a)$ always gives a value in the range $0,\ldots,\mathrm{length}(a)-1$. Using modular arithmetic we can store the queue elements at array locations

$$a[j\bmod \mathrm{length}(a)],a[(j+1)\bmod \mathrm{length}(a)],\ldots,a[(j+n-1)\bmod \mathrm{length}(a)] \enspace.$$

This treats the array $a$ like a *circular array* in which array indices larger than $\mathrm{length}(a)-1$ “wrap around” to the beginning of the array.

The only remaining thing to worry about is taking care that the number of elements in the ArrayQueue does not exceed the size of $a$.

<!-- block arrayqueue · source ods · ods:arrays#sec:arrayqueue, from the first code import (ArrayQueue.a.j.n) to the end of “Summary” -->

## ArrayQueue’s add(x), remove() and resize()

[code codeimport ods/ArrayQueue.a.j.n]

A sequence of $\mathrm{add}(x)$ and $\mathrm{remove}()$ operations on an ArrayQueue is illustrated in Figure 2.2. To implement $\mathrm{add}(x)$, we first check if $a$ is full and, if necessary, call $\mathrm{resize}()$ to increase the size of $a$. Next, we store $x$ in $a[(j+n)\bmod \mathrm{length}(a)]$ and increment $n$.

[figure arrayqueue]

[code codeimport ods/ArrayQueue.add(x)]

To implement $\mathrm{remove}()$, we first store $a[j]$ so that we can return it later. Next, we decrement $n$ and increment $j$ (modulo $\mathrm{length}(a)$) by setting $j=(j+1)\bmod \mathrm{length}(a)$. Finally, we return the stored value of $a[j]$. If necessary, we may call $\mathrm{resize}()$ to decrease the size of $a$.

[code codeimport ods/ArrayQueue.remove()]

Finally, the $\mathrm{resize}()$ operation is very similar to the $\mathrm{resize}()$ operation of ArrayStack. It allocates a new array, $b$, of size $2n$ and copies

$$a[j],a[(j+1)\bmod \mathrm{length}(a)],\ldots,a[(j+n-1)\bmod \mathrm{length}(a)]$$

onto

$$b[0],b[1],\ldots,b[n-1]$$

and sets $j=0$.

[code codeimport ods/ArrayQueue.resize()]

### Summary

The following theorem summarizes the performance of the ArrayQueue data structure:

> **Theorem.** An ArrayQueue implements the (FIFO) Queue interface. Ignoring the cost of calls to $\mathrm{resize}()$, an ArrayQueue supports the operations $\mathrm{add}(x)$ and $\mathrm{remove}()$ in $O(1)$ time per operation. Furthermore, beginning with an empty ArrayQueue, any sequence of $m$ $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ operations results in a total of $O(m)$ time spent during all calls to $\mathrm{resize}()$.

<!-- block linked-queue · source ods · ods:linkedlists#sec:sllist, “Queue Operations” and the paragraph after thm:sllist (“An SLList nearly implements the full set of Deque operations…”) -->

## Queue Operations

An SLList can also implement the FIFO queue operations $\mathrm{add}(x)$ and $\mathrm{remove}()$ in constant time. Removals are done from the head of the list, and are identical to the $\mathrm{pop}()$ operation:

[code codeimport ods/SLList.remove()]

Additions, on the other hand, are done at the tail of the list. In most cases, this is done by setting $\mathit{tail}.\mathit{next}=u$, where $u$ is the newly created node that contains $x$. However, a special case occurs when $n=0$, in which case $\mathit{tail}=\mathit{head}=\mathit{nil}$. In this case, both $\mathit{tail}$ and $\mathit{head}$ are set to $u$.

[code codeimport ods/SLList.add(x)]

Clearly, both $\mathrm{add}(x)$ and $\mathrm{remove}()$ take constant time.

An SLList nearly implements the full set of Deque operations. The only missing operation is removing from the tail of an SLList. Removing from the tail of an SLList is difficult because it requires updating the value of $\mathit{tail}$ so that it points to the node $w$ that precedes $\mathit{tail}$ in the SLList; this is the node $w$ such that $\mathit{w}.\mathit{next}=\mathit{tail}$. Unfortunately, the only way to get to $w$ is by traversing the SLList starting at $\mathit{head}$ and taking $n-2$ steps.

## Footnotes


