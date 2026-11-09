# Deques

<!-- block deque · source ods · ods:intro#the-queue-stack-and-deque-interfaces, the Deque paragraph (“A Deque is a generalization of both…” to “…addLast(x) and removeFirst().”) -->

## The Deque interface

A Deque is a generalization of both the FIFO Queue and LIFO Queue (Stack). A Deque represents a sequence of elements, with a front and a back. Elements can be added at the front of the sequence or the back of the sequence. The names of the Deque operations are self-explanatory: $\mathrm{add\_first}(x)$, $\mathrm{remove\_first}()$, $\mathrm{add\_last}(x)$, and $\mathrm{remove\_last}()$. It is worth noting that a Stack can be implemented using only $\mathrm{add\_first}(x)$ and $\mathrm{remove\_first}()$ while a FIFO Queue can be implemented using $\mathrm{add\_last}(x)$ and $\mathrm{remove\_first}()$.

<!-- block arraydeque · source ods · ods:arrays#sec:arraydeque, the whole section with thm:arraydeque -->

## ArrayDeque: Fast Deque Operations Using an Array

The ArrayQueue from the previous section is a data structure for representing a sequence that allows us to efficiently add to one end of the sequence and remove from the other end. The ArrayDeque data structure allows for efficient addition and removal at both ends. This structure implements the List interface by using the same circular array technique used to represent an ArrayQueue.

[code codeimport ods/ArrayDeque.a.j.n]

The $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ operations on an ArrayDeque are straightforward. They get or set the array element $a[{(j+i)\bmod \mathrm{length}(a)}]$.

[code codeimport ods/ArrayDeque.get(i).set(i,x)]

The implementation of $\mathrm{add}(i,x)$ is a little more interesting. As usual, we first check if $a$ is full and, if necessary, call $\mathrm{resize}()$ to resize $a$. Remember that we want this operation to be fast when $i$ is small (close to 0) or when $i$ is large (close to $n$). Therefore, we check if $iFigure 2.3 for an illustration of $\mathrm{add}(i,x)$ and $\mathrm{remove}(x)$ operations on an ArrayDeque.

[figure arraydeque]

By doing the shifting in this way, we guarantee that $\mathrm{add}(i,x)$ never has to shift more than $\min\{ i, n-i \}$ elements. Thus, the running time of the $\mathrm{add}(i,x)$ operation (ignoring the cost of a $\mathrm{resize}()$ operation) is $O(1+\min\{i,n-i\})$.

The implementation of the $\mathrm{remove}(i)$ operation is similar. It either shifts elements $a[0],\ldots,a[i-1]$ right by one position or shifts the elements $a[i+1],\ldots,a[n-1]$ left by one position depending on whether $i<n/2$. Again, this means that $\mathrm{remove}(i)$ never spends more than $O(1+\min\{i,n-i\})$ time to shift elements.

[code codeimport ods/ArrayDeque.remove(i)]

### Summary

The following theorem summarizes the performance of the ArrayDeque data structure:

> **Theorem.** An ArrayDeque implements the List interface. Ignoring the cost of calls to $\mathrm{resize}()$, an ArrayDeque supports the operations
> - $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ in $O(1)$ time per operation; and
- $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ in $O(1+\min\{i,n-i\})$ time per operation.
> Furthermore, beginning with an empty ArrayDeque, performing any sequence of $m$ $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ operations results in a total of $O(m)$ time spent during all calls to $\mathrm{resize}()$.

<!-- block dualarraydeque · source ods · ods:arrays#sec:dualarraydeque, the whole section with lem:dualarraydeque-amortized and thm:dualarraydeque -->

## DualArrayDeque: Building a Deque from Two Stacks

Next, we present a data structure, the DualArrayDeque that achieves the same performance bounds as an ArrayDeque by using two ArrayStacks. Although the asymptotic performance of the DualArrayDeque is no better than that of the ArrayDeque, it is still worth studying, since it offers a good example of how to make a sophisticated data structure by combining two simpler data structures.

A DualArrayDeque represents a list using two ArrayStacks. Recall that an ArrayStack is fast when the operations on it modify elements near the end. A DualArrayDeque places two ArrayStacks, called $\mathit{front}$ and $\mathit{back}$, back-to-back so that operations are fast at either end.

[code codeimport ods/DualArrayDeque.front.back]

A DualArrayDeque does not explicitly store the number, $n$, of elements it contains. It doesn’t need to, since it contains $n=\mathrm{front.size}() + \mathrm{back.size}()$ elements. Nevertheless, when analyzing the DualArrayDeque we will still use $n$ to denote the number of elements it contains.

[code codeimport ods/DualArrayDeque.size()]

The $\mathit{front}$ ArrayStack stores the list elements that whose indices are $0,\ldots,\mathrm{front.size}()-1$, but stores them in reverse order. The $\mathit{back}$ ArrayStack contains list elements with indices in $\mathrm{front.size}(),\ldots,\mathrm{size}()-1$ in the normal order. In this way, $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ translate into appropriate calls to $\mathrm{get}(i)$ or $\mathrm{set}(i,x)$ on either $\mathit{front}$ or $\mathit{back}$, which take $O(1)$ time per operation.

[code codeimport ods/DualArrayDeque.get(i).set(i,x)]

Note that if an index $i<\mathrm{front.size}()$, then it corresponds to the element of $\mathit{front}$ at position $\mathrm{front.size}()-i-1$, since the elements of $\mathit{front}$ are stored in reverse order.

Adding and removing elements from a DualArrayDeque is illustrated in Figure 2.4. The $\mathrm{add}(i,x)$ operation manipulates either $\mathit{front}$ or $\mathit{back}$, as appropriate:

[figure dualarraydeque]

The $\mathrm{add}(i,x)$ method performs rebalancing of the two ArrayStacks $\mathit{front}$ and $\mathit{back}$, by calling the $\mathrm{balance}()$ method. The implementation of $\mathrm{balance}()$ is described below, but for now it is sufficient to know that $\mathrm{balance}()$ ensures that, unless $\mathrm{size}()<2$, $\mathrm{front.size}()$ and $\mathrm{back.size}()$ do not differ by more than a factor of 3. In particular, $3\cdot\mathrm{front.size}() \ge \mathrm{back.size}()$ and $3\cdot\mathrm{back.size}() \ge \mathrm{front.size}()$.

Next we analyze the cost of $\mathrm{add}(i,x)$, ignoring the cost of calls to $\mathrm{balance}()$. If $i<\mathrm{front.size}()$, then $\mathrm{add}(i,x)$ gets implemented by the call to $\mathrm{front.add}(\mathrm{front.size}()-i-1,x)$. Since $\mathit{front}$ is an ArrayStack, the cost of this is

$$O(\mathrm{front.size}()-(\mathrm{front.size}()-i-1)+1) = O(i+1) \enspace .\tag{2.1}$$

On the other hand, if $i\ge\mathrm{front.size}()$, then $\mathrm{add}(i,x)$ gets implemented as $\mathrm{back.add}(i-\mathrm{front.size}(),x)$. The cost of this is

$$O(\mathrm{back.size}()-(i-\mathrm{front.size}())+1) = O(n-i+1) \enspace .\tag{2.2}$$

Notice that the first case (2.1) occurs when $i n/4$. Summarizing the situation, we have

$$\text{Running time of } \mathrm{add}(i,x) \le \begin{cases} O(1+ i) & \text{if $i< n/4$} \\ O(n) & \text{if $n/4 \le i < 3n/4$} \\ O(1+n-i) & \text{if $i \ge 3n/4$} \end{cases}$$

Thus, the running time of $\mathrm{add}(i,x)$, if we ignore the cost of the call to $\mathrm{balance}()$, is $O(1+\min\{i, n-i\})$.

The $\mathrm{remove}(i)$ operation and its analysis resemble the $\mathrm{add}(i,x)$ operation and analysis.

[code codeimport ods/DualArrayDeque.remove(i)]

### Balancing

Finally, we turn to the $\mathrm{balance}()$ operation performed by $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$. This operation ensures that neither $\mathit{front}$ nor $\mathit{back}$ becomes too big (or too small). It ensures that, unless there are fewer than two elements, each of $\mathit{front}$ and $\mathit{back}$ contain at least $n/4$ elements. If this is not the case, then it moves elements between them so that $\mathit{front}$ and $\mathit{back}$ contain exactly $\lfloor n/2\rfloor$ elements and $\lceil n/2\rceil$ elements, respectively.

[code codeimport ods/DualArrayDeque.balance()]

Here there is little to analyze. If the $\mathrm{balance}()$ operation does rebalancing, then it moves $O(n)$ elements and this takes $O(n)$ time. This is bad, since $\mathrm{balance}()$ is called with each call to $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$. However, the following lemma shows that, on average, $\mathrm{balance}()$ only spends a constant amount of time per operation.

> **Lemma.** If an empty DualArrayDeque is created and any sequence of $m\ge 1$ calls to $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ are performed, then the total time spent during all calls to $\mathrm{balance}()$ is $O(m)$.

*Proof.* We will show that, if $\mathrm{balance}()$ is forced to shift elements, then the number of $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ operations since the last time any elements were shifted by $\mathrm{balance}()$ is at least $n/2-1$. As in the proof of Lemma 2.1, this is sufficient to prove that the total time spent by $\mathrm{balance}()$ is $O(m)$.

We will perform our analysis using a technique knows as the *potential method*. Define the *potential*, $\Phi$, of the DualArrayDeque as the difference in size between $\mathit{front}$ and $\mathit{back}$:

$$\Phi = |\mathrm{front.size}() - \mathrm{back.size}()| \enspace .$$

The interesting thing about this potential is that a call to $\mathrm{add}(i,x)$ or $\mathrm{remove}(i)$ that does not do any balancing can increase the potential by at most 1.

Observe that, immediately after a call to $\mathrm{balance}()$ that shifts elements, the potential, $\Phi_0$, is at most 1, since

$$\Phi_0 = \left|\lfloor n/2\rfloor-\lceil n/2\rceil\right|\le 1 \enspace .$$

Consider the situation immediately before a call to $\mathrm{balance}()$ that shifts elements and suppose, without loss of generality, that $\mathrm{balance}()$ is shifting elements because $3\mathrm{front.size}() < \mathrm{back.size}()$. Notice that, in this case,

[drv-balance-potential]

Furthermore, the potential at this point in time is

Therefore, the number of calls to $\mathrm{add}(i,x)$ or $\mathrm{remove}(i)$ since the last time $\mathrm{balance}()$ shifted elements is at least $\Phi_1-\Phi_0 > n/2-1$. This completes the proof.

### Summary

The following theorem summarizes the properties of a DualArrayDeque:

> **Theorem.** A DualArrayDeque implements the List interface. Ignoring the cost of calls to $\mathrm{resize}()$ and $\mathrm{balance}()$, a DualArrayDeque supports the operations
> - $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ in $O(1)$ time per operation; and
- $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ in $O(1+\min\{i,n-i\})$ time per operation.
> Furthermore, beginning with an empty DualArrayDeque, any sequence of $m$ $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ operations results in a total of $O(m)$ time spent during all calls to $\mathrm{resize}()$ and $\mathrm{balance}()$.

## Footnotes


