# Space-efficient lists

<!-- block rootish · source ods · ods:arrays#sec:rootisharraystack, from the opening through “Analysis of Growing and Shrinking” -->

## RootishArrayStack: A Space-Efficient Array Stack

One of the drawbacks of all previous data structures in this chapter is that, because they store their data in one or two arrays and they avoid resizing these arrays too often, the arrays frequently are not very full. For example, immediately after a $\mathrm{resize}()$ operation on an ArrayStack, the backing array $a$ is only half full. Even worse, there are times when only one third of $a$ contains data.

In this section, we discuss the RootishArrayStack data structure, that addresses the problem of wasted space. The RootishArrayStack stores $n$ elements using $O(\sqrt{n})$ arrays. In these arrays, at most $O(\sqrt{n})$ array locations are unused at any time. All remaining array locations are used to store data. Therefore, these data structures waste at most $O(\sqrt{n})$ space when storing $n$ elements.

A RootishArrayStack stores its elements in a list of $r$ arrays called *blocks* that are numbered $0,1,\ldots,r-1$. See Figure 2.5. Block $b$ contains $b+1$ elements. Therefore, all $r$ blocks contain a total of

$$1+ 2+ 3+\cdots +r = r(r+1)/2$$

elements. The above formula can be obtained as shown in Figure 2.6.

[figure rootisharraystack]

[code codeimport ods/RootishArrayStack.blocks.n]

[figure gauss]

As we might expect, the elements of the list are laid out in order within the blocks. The list element with index 0 is stored in block 0, elements with list indices 1 and 2 are stored in block 1, elements with list indices 3, 4, and 5 are stored in block 2, and so on. The main problem we have to address is that of determining, given an index $i$, which block contains $i$ as well as the index corresponding to $i$ within that block.

Determining the index of $i$ within its block turns out to be easy. If index $i$ is in block $b$, then the number of elements in blocks $0,\ldots,b-1$ is $b(b+1)/2$. Therefore, $i$ is stored at location

$$j = i - b(b+1)/2$$

within block $b$. Somewhat more challenging is the problem of determining the value of $b$. The number of elements that have indices less than or equal to $i$ is $i+1$. On the other hand, the number of elements in blocks $0,\ldots,b$ is $(b+1)(b+2)/2$. Therefore, $b$ is the smallest integer such that

$$(b+1)(b+2)/2 \ge i+1 \enspace .$$

We can rewrite this equation as

$$b^2 + 3b - 2i \ge 0 \enspace .$$

The corresponding quadratic equation $b^2 + 3b - 2i = 0$ has two solutions: $b=(-3 + \sqrt{9+8i}) / 2$ and $b=(-3 - \sqrt{9+8i}) / 2$. The second solution makes no sense in our application since it always gives a negative value. Therefore, we obtain the solution $b = (-3 + \sqrt{9+8i}) / 2$. In general, this solution is not an integer, but going back to our inequality, we want the smallest integer $b$ such that $b \ge (-3 + \sqrt{9+8i}) / 2$. This is simply

$$b = \left\lceil(-3 + \sqrt{9+8i}) / 2\right\rceil \enspace .$$

[code codeimport ods/RootishArrayStack.i2b(i)]

With this out of the way, the $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ methods are straightforward. We first compute the appropriate block $b$ and the appropriate index $j$ within the block and then perform the appropriate operation:

[code codeimport ods/RootishArrayStack.get(i).set(i,x)]

If we use any of the data structures in this chapter for representing the $\mathit{blocks}$ list, then $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ will each run in constant time.

The $\mathrm{add}(i,x)$ method will, by now, look familiar. We first check to see if our data structure is full, by checking if the number of blocks, $r$, is such that $r(r+1)/2 = n$. If so, we call $\mathrm{grow}()$ to add another block. With this done, we shift elements with indices $i,\ldots,n-1$ to the right by one position to make room for the new element with index $i$:

[code codeimport ods/RootishArrayStack.add(i,x)]

The $\mathrm{grow}()$ method does what we expect. It adds a new block:

[code codeimport ods/RootishArrayStack.grow()]

Ignoring the cost of the $\mathrm{grow}()$ operation, the cost of an $\mathrm{add}(i,x)$ operation is dominated by the cost of shifting and is therefore $O(1+n-i)$, just like an ArrayStack.

The $\mathrm{remove}(i)$ operation is similar to $\mathrm{add}(i,x)$. It shifts the elements with indices $i+1,\ldots,n$ left by one position and then, if there is more than one empty block, it calls the $\mathrm{shrink}()$ method to remove all but one of the unused blocks:

[code codeimport ods/RootishArrayStack.remove(i)]

[code codeimport ods/RootishArrayStack.shrink()]

Once again, ignoring the cost of the $\mathrm{shrink}()$ operation, the cost of a $\mathrm{remove}(i)$ operation is dominated by the cost of shifting and is therefore $O(n-i)$.

### Analysis of Growing and Shrinking

The above analysis of $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ does not account for the cost of $\mathrm{grow}()$ and $\mathrm{shrink}()$. Note that, unlike the $\mathrm{ArrayStack.resize}()$ operation, $\mathrm{grow}()$ and $\mathrm{shrink}()$ do not copy any data. They only allocate or free an array of size $r$. In some environments, this takes only constant time, while in others, it may require time proportional to $r$.

We note that, immediately after a call to $\mathrm{grow}()$ or $\mathrm{shrink}()$, the situation is clear. The final block is completely empty, and all other blocks are completely full. Another call to $\mathrm{grow}()$ or $\mathrm{shrink}()$ will not happen until at least $r-1$ elements have been added or removed. Therefore, even if $\mathrm{grow}()$ and $\mathrm{shrink}()$ take $O(r)$ time, this cost can be amortized over at least $r-1$ $\mathrm{add}(i,x)$ or $\mathrm{remove}(i)$ operations, so that the amortized cost of $\mathrm{grow}()$ and $\mathrm{shrink}()$ is $O(1)$ per operation.

<!-- block sqrt-lower-bound · source ods · ods:arrays#sec:rootishspaceusage -->

## Space Usage

Next, we analyze the amount of extra space used by a RootishArrayStack. In particular, we want to count any space used by a RootishArrayStack that is not an array element currently used to hold a list element. We call all such space *wasted space*.

The $\mathrm{remove}(i)$ operation ensures that a RootishArrayStack never has more than two blocks that are not completely full. The number of blocks, $r$, used by a RootishArrayStack that stores $n$ elements therefore satisfies

[drv-rootish-blocks]

Again, using the quadratic equation on this gives

The last two blocks have sizes $r$ and $r-1$, so the space wasted by these two blocks is at most $2r-1 = O(\sqrt{n})$. If we store the blocks in (for example) an ArrayStack, then the amount of space wasted by the List that stores those $r$ blocks is also $O(r)=O(\sqrt{n})$. The other space needed for storing $n$ and other accounting information is $O(1)$. Therefore, the total amount of wasted space in a RootishArrayStack is $O(\sqrt{n})$.

Next, we argue that this space usage is optimal for any data structure that starts out empty and can support the addition of one item at a time. More precisely, we will show that, at some point during the addition of $n$ items, the data structure is wasting at least in $\sqrt{n}$ space (though it may be only wasted for a moment).

Suppose we start with an empty data structure and we add $n$ items one at a time. At the end of this process, all $n$ items are stored in the structure and distributed among a collection of $r$ memory blocks. If $r\ge \sqrt{n}$, then the data structure must be using $r$ pointers (or references) to keep track of these $r$ blocks, and these pointers are wasted space. On the other hand, if $r  \sqrt{n}$. Consider the moment at which this block was first allocated. Immediately after it was allocated, this block was empty, and was therefore wasting $\sqrt{n}$ space. Therefore, at some point in time during the insertion of $n$ elements, the data structure was wasting $\sqrt{n}$ space.

<!-- block rootish-summary · source ods · ods:arrays#sec:rootisharraystack, the subsection “Summary” (thm:rootisharraystack) -->

## RootishArrayStack: Summary

The following theorem summarizes our discussion of the RootishArrayStack data structure:

> **Theorem.** A RootishArrayStack implements the List interface. Ignoring the cost of calls to $\mathrm{grow}()$ and $\mathrm{shrink}()$, a RootishArrayStack supports the operations
> - $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ in $O(1)$ time per operation; and
- $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ in $O(1+n-i)$ time per operation.
> Furthermore, beginning with an empty RootishArrayStack, any sequence of $m$ $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ operations results in a total of $O(m)$ time spent during all calls to $\mathrm{grow}()$ and $\mathrm{shrink}()$.
> The space (measured in words)[^3] used by a RootishArrayStack that stores $n$ elements is $n +O(\sqrt{n})$.

<!-- block rootish-sqrt · source ods · ods:arrays#sec:rootisharraystack, the subsection “Computing Square Roots” (lem:root), printed in the Java and C++ editions -->

## Computing Square Roots

A reader who has had some exposure to models of computation may notice that the RootishArrayStack, as described above, does not fit into the usual word-RAM model of computation (Section 1.4) because it requires taking square roots. The square root operation is generally not considered a basic operation and is therefore not usually part of the word-RAM model.

In this section, we show that the square root operation can be implemented efficiently. In particular, we show that for any integer $x\in\{0,\ldots,n\}$, $\lfloor\sqrt{x}\rfloor$ can be computed in constant-time, after $O(\sqrt{n})$ preprocessing that creates two arrays of length $O(\sqrt{n})$. The following lemma shows that we can reduce the problem of computing the square root of $x$ to the square root of a related value $x'$.

> **Lemma.** Let $x\ge 1$ and let $x'=x-a$, where $0\le a\le\sqrt{x}$. Then $\sqrt{x'} \ge \sqrt{x}-1$.

*Proof.* It suffices to show that

[drv-root]

Square both sides of this inequality to get

and gather terms to get

which is clearly true for any $x\ge 1$.

Start by restricting the problem a little, and assume that $2^{r} \le x Lemma 2.3, so $\sqrt{x}-\sqrt{x'} \le 1$. Furthermore, $x'$ has all of its lower-order $\lfloor r/2\rfloor$ bits equal to 0, so there are only

$$2^{r+1-\lfloor r/2\rfloor} \le 4\cdot2^{r/2} \le 4\sqrt{x}$$

possible values of $x'$. This means that we can use an array, $\mathit{sqrttab}$, that stores the value of $\lfloor\sqrt{x'}\rfloor$ for each possible value of $x'$. A little more precisely, we have

$$sqrttab[i] = \left\lfloor \sqrt{i 2^{\lfloor r/2\rfloor}} \right\rfloor \enspace .$$

In this way, $sqrttab[i]$ is within 2 of $\sqrt{x}$ for all $x\in\{i2^{\lfloor r/2\rfloor},\ldots,(i+1)2^{\lfloor r/2\rfloor}-1\}$. Stated another way, the array entry $s=sqrttab[x>>\lfloor r/2\rfloor]$ is either equal to $\lfloor\sqrt{x}\rfloor$, $\lfloor\sqrt{x}\rfloor-1$, or $\lfloor\sqrt{x}\rfloor-2$. From $s$ we can determine the value of $\lfloor\sqrt{x}\rfloor$ by incrementing $s$ until $(s+1)^2 > x$.

[code javaimport ods/FastSqrt.sqrt(x,r)]

Now, this only works for $x\in\{2^{r},\ldots,2^{r+1}-1\}$ and $\mathit{sqrttab}$ is a special table that only works for a particular value of $r=\lfloor\log x\rfloor$. To overcome this, we could compute $\lfloor\log n\rfloor$ different $\mathit{sqrttab}$ arrays, one for each possible value of $\lfloor\log x\rfloor$. The sizes of these tables form an exponential sequence whose largest value is at most $4\sqrt{n}$, so the total size of all tables is $O(\sqrt{n})$.

However, it turns out that more than one $\mathit{sqrttab}$ array is unnecessary; we only need one $\mathit{sqrttab}$ array for the value $r=\lfloor\log n\rfloor$. Any value $x$ with $\log x=r'<r$ can be *upgraded* by multiplying $x$ by $2^{r-r'}$ and using the equation

$$\sqrt{2^{r-r'}x} = 2^{(r-r')/2}\sqrt{x} \enspace .$$

The quantity $2^{r-r'}x$ is in the range $\{2^{r},\ldots,2^{r+1}-1\}$ so we can look up its square root in $\mathit{sqrttab}$. The following code implements this idea to compute $\lfloor\sqrt{x}\rfloor$ for all non-negative integers $x$ in the range $\{0,\ldots,2^{30}-1\}$ using an array, $\mathit{sqrttab}$, of size $2^{16}$.

[code javaimport ods/FastSqrt.sqrt(x)]

Something we have taken for granted thus far is the question of how to compute $r'=\lfloor\log x\rfloor$. Again, this is a problem that can be solved with an array, $\mathit{logtab}$, of size $2^{r/2}$. In this case, the code is particularly simple, since $\lfloor\log x\rfloor$ is just the index of the most significant 1 bit in the binary representation of $x$. This means that, for $x>2^{r/2}$, we can right-shift the bits of $x$ by $r/2$ positions before using it as an index into $\mathit{logtab}$. The following code does this using an array $\mathit{logtab}$ of size $2^{16}$ to compute $\lfloor\log x\rfloor$ for all $x$ in the range $\{1,\ldots,2^{32}-1\}$.

[code javaimport ods/FastSqrt.log(x)]

Finally, for completeness, we include the following code that initializes $\mathit{logtab}$ and $\mathit{sqrttab}$:

[code javaimport ods/FastSqrt.inittabs()]

To summarize, the computations done by the $\mathrm{i2b}(i)$ method can be implemented in constant time on the word-RAM using $O(\sqrt{n})$ extra memory to store the $\mathit{sqrttab}$ and $\mathit{logtab}$ arrays. These arrays can be rebuilt when $n$ increases or decreases by a factor of two, and the cost of this rebuilding can be amortized over the number of $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ operations that caused the change in $n$ in the same way that the cost of $\mathrm{resize}()$ is analyzed in the ArrayStack implementation.

<!-- block selist · source ods · ods:linkedlists#sec:selist, from the opening through “Removing an Element” -->

## SEList: A Space-Efficient Linked List

One of the drawbacks of linked lists (besides the time it takes to access elements that are deep within the list) is their space usage. Each node in a DLList requires an additional two references to the next and previous nodes in the list. Two of the fields in a Node are dedicated to maintaining the list, and only one of the fields is for storing data!

An SEList (space-efficient list) reduces this wasted space using a simple idea: Rather than store individual elements in a DLList, we store a block (array) containing several items. More precisely, an SEList is parameterized by a *block size* $b$. Each individual node in an SEList stores a block that can hold up to $b+1$ elements.

For reasons that will become clear later, it will be helpful if we can do Deque operations on each block. The data structure that we choose for this is a BDeque (bounded deque), derived from the ArrayDeque structure described in Section 3.3. The BDeque differs from the ArrayDeque in one small way: When a new BDeque is created, the size of the backing array $a$ is fixed at $b+1$ and never grows or shrinks. The important property of a BDeque is that it allows for the addition or removal of elements at either the front or back in constant time. This will be useful as elements are shifted from one block to another.

An SEList is just a doubly-linked list of blocks. In addition to $\mathit{next}$ and $\mathit{prev}$ pointers, each node $u$ in an SEList contains a BDeque, $\mathit{u}.\mathit{d}$.

### Space Requirements

An SEList places very tight restrictions on the number of elements in a block: Unless a block is the last block, then that block contains at least $b-1$ and at most $b+1$ elements. This means that, if an SEList contains $n$ elements, then it has at most

$$n/(b-1) + 1 = O(n/b)$$

blocks. The BDeque for each block contains an array of length $b+1$ but, for every block except the last, at most a constant amount of space is wasted in this array. The remaining memory used by a block is also constant. This means that the wasted space in an SEList is only $O(b+n/b)$. By choosing a value of $b$ within a constant factor of $\sqrt{n}$, we can make the space-overhead of an SEList approach the $\sqrt{n}$ lower bound given in Section 3.6.

### Finding Elements

The first challenge we face with an SEList is finding the list item with a given index $i$. Note that the location of an element consists of two parts:

1. The node $u$ that contains the block that contains the element with index $i$; and
1. the index $j$ of the element within its block.

To find the block that contains a particular element, we proceed the same way as we do in a DLList. We either start at the front of the list and traverse in the forward direction, or at the back of the list and traverse backwards until we reach the node we want. The only difference is that, each time we move from one node to the next, we skip over a whole block of elements.

[code pcodeimport ods/SEList.get_location(i)]

Remember that, with the exception of at most one block, each block contains at least $b-1$ elements, so each step in our search gets us $b-1$ elements closer to the element we are looking for. If we are searching forward, this means that we reach the node we want after $O(1+i/b)$ steps. If we search backwards, then we reach the node we want after $O(1+(n-i)/b)$ steps. The algorithm takes the smaller of these two quantities depending on the value of $i$, so the time to locate the item with index $i$ is $O(1+\min\{i,n-i\}/b)$.

Once we know how to locate the item with index $i$, the $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ operations translate into getting or setting a particular index in the correct block:

[code codeimport ods/SEList.get(i).set(i,x)]

The running times of these operations are dominated by the time it takes to locate the item, so they also run in $O(1+\min\{i,n-i\}/b)$ time.

### Adding an Element

Adding elements to an SEList is a little more complicated. Before considering the general case, we consider the easier operation, $\mathrm{add}(x)$, in which $x$ is added to the end of the list. If the last block is full (or does not exist because there are no blocks yet), then we first allocate a new block and append it to the list of blocks. Now that we are sure that the last block exists and is not full, we append $x$ to the last block.

[code pcodeimport ods/SEList.append(x)]

Things get more complicated when we add to the interior of the list using $\mathrm{add}(i,x)$. We first locate $i$ to get the node $u$ whose block contains the $i$th list item. The problem is that we want to insert $x$ into $u$’s block, but we have to be prepared for the case where $u$’s block already contains $b+1$ elements, so that it is full and there is no room for $x$.

Let $u_0,u_1,u_2,\ldots$ denote $u$, $\mathit{u}.\mathit{next}$, $\mathit{u}.\mathit{next}.next$, and so on. We explore $u_0,u_1,u_2,\ldots$ looking for a node that can provide space for $x$. Three cases can occur during our space exploration (see Figure 3.4):

[figure selist-add]

1. We quickly (in $r+1\le b$ steps) find a node $u_r$ whose block is not full. In this case, we perform $r$ shifts of an element from one block into the next, so that the free space in $u_r$ becomes a free space in $u_0$. We can then insert $x$ into $u_0$’s block.
1. We quickly (in $r+1\le b$ steps) run off the end of the list of blocks. In this case, we add a new empty block to the end of the list of blocks and proceed as in the first case.
1. After $b$ steps we do not find any block that is not full. In this case, $u_0,\ldots,u_{b-1}$ is a sequence of $b$ blocks that each contain $b+1$ elements. We insert a new block $u_{b}$ at the end of this sequence and *spread* the original $b(b+1)$ elements so that each block of $u_0,\ldots,u_{b}$ contains exactly $b$ elements. Now $u_0$’s block contains only $b$ elements so it has room for us to insert $x$.

[code codeimport ods/SEList.add(i,x)]

The running time of the $\mathrm{add}(i,x)$ operation depends on which of the three cases above occurs. Cases 1 and 2 involve examining and shifting elements through at most $b$ blocks and take $O(b)$ time. Case 3 involves calling the $\mathrm{spread}(u)$ method, which moves $b(b+1)$ elements and takes $O(b^2)$ time. If we ignore the cost of Case 3 (which we will account for later with amortization) this means that the total running time to locate $i$ and perform the insertion of $x$ is $O(b+\min\{i,n-i\}/b)$.

### Removing an Element

Removing an element from an SEList is similar to adding an element. We first locate the node $u$ that contains the element with index $i$. Now, we have to be prepared for the case where we cannot remove an element from $u$ without causing $u$’s block to become smaller than $b-1$.

Again, let $u_0,u_1,u_2,\ldots$ denote $u$, $\mathit{u}.\mathit{next}$, $\mathit{u}.\mathit{next}.next$, and so on. We examine $u_0,u_1,u_2,\ldots$ in order to look for a node from which we can borrow an element to make the size of $u_0$’s block at least $b-1$. There are three cases to consider (see Figure 3.5):

[figure selist-remove]

1. We quickly (in $r+1\le b$ steps) find a node whose block contains more than $b-1$ elements. In this case, we perform $r$ shifts of an element from one block into the previous one, so that the extra element in $u_r$ becomes an extra element in $u_0$. We can then remove the appropriate element from $u_0$’s block.
1. We quickly (in $r+1\le b$ steps) run off the end of the list of blocks. In this case, $u_r$ is the last block, and there is no need for $u_r$’s block to contain at least $b-1$ elements. Therefore, we proceed as above, borrowing an element from $u_r$ to make an extra element in $u_0$. If this causes $u_r$’s block to become empty, then we remove it.
1. After $b$ steps, we do not find any block containing more than $b-1$ elements. In this case, $u_0,\ldots,u_{b-1}$ is a sequence of $b$ blocks that each contain $b-1$ elements. We *gather* these $b(b-1)$ elements into $u_0,\ldots,u_{b-2}$ so that each of these $b-1$ blocks contains exactly $b$ elements and we remove $u_{b-1}$, which is now empty. Now $u_0$’s block contains $b$ elements and we can then remove the appropriate element from it.

[code codeimport ods/SEList.remove(i)]

Like the $\mathrm{add}(i,x)$ operation, the running time of the $\mathrm{remove}(i)$ operation is $O(b+\min\{i,n-i\}/b)$ if we ignore the cost of the $\mathrm{gather}(u)$ method that occurs in Case 3.

<!-- block selist-amortized · source ods · ods:linkedlists#lem:selist-amortized, the subsection “Amortized Analysis of Spreading and Gathering” -->

## Amortized Analysis of Spreading and Gathering

Next, we consider the cost of the $\mathrm{gather}(u)$ and $\mathrm{spread}(u)$ methods that may be executed by the $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ methods. For the sake of completeness, here they are:

[code codeimport ods/SEList.spread(u)]

[code codeimport ods/SEList.gather(u)]

The running time of each of these methods is dominated by the two nested loops. Both the inner and outer loops execute at most $b+1$ times, so the total running time of each of these methods is $O((b+1)^2)=O(b^2)$. However, the following lemma shows that these methods execute on at most one out of every $b$ calls to $\mathrm{add}(i,x)$ or $\mathrm{remove}(i)$.

> **Lemma.** If an empty SEList is created and any sequence of $m\ge 1$ calls to $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ is performed, then the total time spent during all calls to $\mathrm{spread}()$ and $\mathrm{gather}()$ is $O(bm)$.

*Proof.* We will use the potential method of amortized analysis. We say that a node $u$ is *fragile* if $u$’s block does not contain $b$ elements (so that $u$ is either the last node, or contains $b-1$ or $b+1$ elements). Any node whose block contains $b$ elements is *rugged*. Define the *potential* of an SEList as the number of fragile nodes it contains. We will consider only the $\mathrm{add}(i,x)$ operation and its relation to the number of calls to $\mathrm{spread}(u)$. The analysis of $\mathrm{remove}(i)$ and $\mathrm{gather}(u)$ is identical.

Notice that, if Case 1 occurs during the $\mathrm{add}(i,x)$ method, then only one node, $u_r$ has the size of its block changed. Therefore, at most one node, namely $u_r$, goes from being rugged to being fragile. If Case 2 occurs, then a new node is created, and this node is fragile, but no other node changes size, so the number of fragile nodes increases by one. Thus, in either Case 1 or Case 2 the potential of the SEList increases by at most one.

Finally, if Case 3 occurs, it is because $u_0,\ldots,u_{b-1}$ are all fragile nodes. Then $\mathrm{spread}(u_0)$ is called and these $b$ fragile nodes are replaced with $b+1$ rugged nodes. Finally, $x$ is added to $u_0$’s block, making $u_0$ fragile. In total the potential decreases by $b-1$.

In summary, the potential starts at 0 (there are no nodes in the list). Each time Case 1 or Case 2 occurs, the potential increases by at most 1. Each time Case 3 occurs, the potential decreases by $b-1$. The potential (which counts the number of fragile nodes) is never less than 0. We conclude that, for every occurrence of Case 3, there are at least $b-1$ occurrences of Case 1 or Case 2. Thus, for every call to $\mathrm{spread}(u)$ there are at least $b$ calls to $\mathrm{add}(i,x)$. This completes the proof.

<!-- block selist-summary · source ods · ods:linkedlists#sec:selist, the subsection “Summary” (thm:selist and the closing paragraph) -->

## SEList: Summary

The following theorem summarizes the performance of the SEList data structure:

> **Theorem.** An SEList implements the List interface. Ignoring the cost of calls to $\mathrm{spread}(u)$ and $\mathrm{gather}(u)$, an SEList with block size $b$ supports the operations
> - $\mathrm{get}(i)$ and $\mathrm{set}(i,x)$ in $O(1+\min\{i,n-i\}/b)$ time per operation; and
- $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ in $O(b+\min\{i,n-i\}/b)$ time per operation.
> Furthermore, beginning with an empty SEList, any sequence of $m$ $\mathrm{add}(i,x)$ and $\mathrm{remove}(i)$ operations results in a total of $O(bm)$ time spent during all calls to $\mathrm{spread}(u)$ and $\mathrm{gather}(u)$.
> The space (measured in words)[^1] used by an SEList that stores $n$ elements is $n +O(b + n/b)$.

The SEList is a trade-off between an ArrayList and a DLList where the relative mix of these two structures depends on the block size $b$. At the extreme $b=2$, each SEList node stores at most three values, which is not much different than a DLList. At the other extreme, $b>n$, all the elements are stored in a single array, just like in an ArrayList. In between these two extremes lies a trade-off between the time it takes to add or remove a list item and the time it takes to locate a particular list item.

## Footnotes

[^3]: Recall Section 1.4 for a discussion of how memory is measured.

[^1]: Recall Section 1.4 for a discussion of how memory is measured.
