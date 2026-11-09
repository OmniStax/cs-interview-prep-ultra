# Min-stacks and monotonic queues

<!-- block min-stack · source cpa · cpa:data_structures/stack_queue_modification, its opening and #stack-modification -->

# Minimum stack / Minimum queue

In this article we will consider three problems: 
first we will modify a stack in a way that allows us to find the smallest element of the stack in $O(1)$, then we will do the same thing with a queue, and finally we will use these data structures to find the minimum in all subarrays of a fixed length in an array in $O(n)$

## Stack modification

We want to modify the stack data structure in such a way, that it is possible to find the smallest element in the stack in $O(1)$ time, while maintaining the same asymptotic behavior for adding and removing elements from the stack.
Quick reminder, on a stack we only add and remove elements on one end.

To do this, we will not only store the elements in the stack, but we will store them in pairs: the element itself and the minimum in the stack starting from this element and below.

```cpp
stack<pair<int, int>> st;
```

It is clear that finding the minimum in the whole stack consists only of looking at the value `stack.top().second`.

It is also obvious that adding or removing a new element to the stack can be done in constant time.

Implementation:

* Adding an element:
```cpp
int new_min = st.empty() ? new_elem : min(new_elem, st.top().second);
st.push({new_elem, new_min});
```

* Removing an element:
```cpp
int removed_element = st.top().first;
st.pop();
```

* Finding the minimum:
```cpp
int minimum = st.top().second;
```

<!-- block min-queue · source cpa · cpa:data_structures/stack_queue_modification#queue-modification-method-1 -->

## Queue modification (method 1)

Now we want to achieve the same operations with a queue, i.e. we want to add elements at the end and remove them from the front.

Here we consider a simple method for modifying a queue.
It has a big disadvantage though, because the modified queue will actually not store all elements.

The key idea is to only store the items in the queue that are needed to determine the minimum.
Namely we will keep the queue in nondecreasing order (i.e. the smallest value will be stored in the head), and of course not in any arbitrary way, the actual minimum has to be always contained in the queue.
This way the smallest element will always be in the head of the queue.
Before adding a new element to the queue, it is enough to make a "cut":
we will remove all trailing elements of the queue that are larger than the new element, and afterwards add the new element to the queue. 
This way we don't break the order of the queue, and we will also not lose the current element if it is at any subsequent step the minimum. 
All the elements that we removed can never be a minimum itself, so this operation is allowed.
When we want to extract an element from the head, it actually might not be there (because we removed it previously while adding a smaller element). 
Therefore when deleting an element from a queue we need to know the value of the element.
If the head of the queue has the same value, we can safely remove it, otherwise we do nothing.

Consider the implementations of the above operations:

```cpp
deque<int> q;
```

* Finding the minimum:
```cpp
int minimum = q.front();
```

* Adding an element:
```cpp
while (!q.empty() && q.back() > new_element)
    q.pop_back();
q.push_back(new_element);
```

* Removing an element:
```cpp
if (!q.empty() && q.front() == remove_element)
    q.pop_front();
```

It is clear that on average all these operation only take $O(1)$ time (because every element can only be pushed and popped once).

<!-- block min-queue-index · source cpa · cpa:data_structures/stack_queue_modification#queue-modification-method-2 -->

## Queue modification (method 2)

This is a modification of method 1.
We want to be able to remove elements without knowing which element we have to remove.
We can accomplish that by storing the index for each element in the queue.
And we also remember how many elements we already have added and removed.

```cpp
deque<pair<int, int>> q;
int cnt_added = 0;
int cnt_removed = 0;
```

* Finding the minimum:
```cpp
int minimum = q.front().first;
```

* Adding an element:
```cpp
while (!q.empty() && q.back().first > new_element)
    q.pop_back();
q.push_back({new_element, cnt_added});
cnt_added++;
```

* Removing an element:
```cpp
if (!q.empty() && q.front().second == cnt_removed) 
    q.pop_front();
cnt_removed++;
```

<!-- block two-stack-queue · source cpa · cpa:data_structures/stack_queue_modification#queue-modification-method-3 -->

## Queue modification (method 3)

Here we consider another way of modifying a queue to find the minimum in $O(1)$.
This way is somewhat more complicated to implement, but this time we actually store all elements.
And we also can remove an element from the front without knowing its value.

The idea is to reduce the problem to the problem of stacks, which was already solved by us.
So we only need to learn how to simulate a queue using two stacks.

We make two stacks, `s1` and `s2`. 
Of course these stack will be of the modified form, so that we can find the minimum in $O(1)$. 
We will add new elements to the stack `s1`, and remove elements from the stack `s2`.
If at any time the stack `s2` is empty, we move all elements from `s1` to `s2` (which essentially reverses the order of those elements).
Finally finding the minimum in a queue involves just finding the minimum of both stacks.

Thus we perform all operations in $O(1)$ on average (each element will be once added to stack `s1`, once transferred to `s2`, and once popped from `s2`)

Implementation:

```cpp
stack<pair<int, int>> s1, s2;
```

* Finding the minimum:
```cpp
if (s1.empty() || s2.empty()) 
    minimum = s1.empty() ? s2.top().second : s1.top().second;
else
    minimum = min(s1.top().second, s2.top().second);
```

* Add element:
```cpp
int minimum = s1.empty() ? new_element : min(new_element, s1.top().second);
s1.push({new_element, minimum});
```

* Removing an element:
```cpp
if (s2.empty()) {
    while (!s1.empty()) {
        int element = s1.top().first;
        s1.pop();
        int minimum = s2.empty() ? element : min(element, s2.top().second);
        s2.push({element, minimum});
    }
}
int remove_element = s2.top().first;
s2.pop();
```

<!-- block window-minimum · source cpa · cpa:data_structures/stack_queue_modification#finding-the-minimum-for-all-subarrays-of-fixed-length -->

## Finding the minimum for all subarrays of fixed length

Suppose we are given an array $A$ of length $N$ and a given $M \le N$.
We have to find the minimum of each subarray of length $M$ in this array, i.e. we have to find:

$$\min_{0 \le i \le M-1} A[i], \min_{1 \le i \le M} A[i], \min_{2 \le i \le M+1} A[i],~\dots~, \min_{N-M \le i \le N-1} A[i]$$

We have to solve this problem in linear time, i.e. $O(n)$.

We can use any of the three modified queues to solve the problem.
The solutions should be clear:
we add the first $M$ element of the array, find and output its minimum, then add the next element to the queue and remove the first element of the array, find and output its minimum, etc. 
Since all operations with the queue are performed in constant time on average, the complexity of the whole algorithm will be $O(n)$.

<!-- block nearest-smaller · source wikipedia · wikipedia:All_nearest_smaller_values lead, #Example, #Sequential algorithm -->

{{short description|Computational problem}}
In [[computer science]], the '''all nearest smaller values''' (ANSV) problem is: given an array <math>A[1..n]</math>, compute for each position <math>i</math> the index
<math>P[i] = \max\{\,j < i \mid A[j] < A[i]\,\}</math>, or determine that no such <math>j</math> exists.  The corresponding nearest-smaller ''value'' is <math>A[P[i]]</math>.  Some presentations report <math>A[P[i]]</math>, but many applications require the indices <math>P[i]</math>.

This problem can be solved efficiently both by parallel and non-parallel algorithms: {{harvtxt|Berkman|Schieber|Vishkin|1993}},  who first identified the procedure as a useful subroutine for other parallel programs, developed efficient [[parallel algorithms|algorithms]] to solve it in the [[Parallel Random Access Machine]] model; it may also be solved in [[linear time]] on a non-parallel computer using a [[Stack (data structure)|stack]]-based algorithm.{{sfnp|Berkman|Schieber|Vishkin|1993}} Later researchers have studied algorithms to solve it in other models of parallel computation.{{sfnp|Kravets|Plaxton|1996}}{{sfnp|He|Huang|2001}}

== Example ==
Suppose that the input is the following:
:0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15.
The first element of the sequence (0) has no previous value.
The nearest (only) smaller value previous to 8 and to 4 is 0. All three values previous to 12 are smaller, but the nearest one is 4. Continuing in the same way, the nearest previous smaller values for this sequence (indicating the nonexistence of a previous smaller value by a dash) are
:—, 0, 0, 4, 0, 2, 2, 6, 0, 1, 1, 5, 1, 3, 3, 7.
In most applications, the positions of the nearest smaller values, and not the values themselves, should be computed, and in many applications the same computation should be computed for the reversal of the sequence in order to find the following smaller value that is closest in the sequence.

== Sequential algorithm ==
On a sequential computer, all nearest smaller values may be found by using a [[stack (data structure)|stack data structure]]: one processes the values in sequence order, using the stack to maintain a subsequence of the values that have been processed so far and are smaller than any later value that has already been processed. In [[pseudocode]], the algorithm is as follows.
 S = new empty stack data structure
 '''for''' x in the input sequence '''do'''
     '''while''' S is nonempty and the top element of S is greater than or equal to x '''do'''
         pop S
     '''if''' S '''is''' empty '''then'''
         x has no preceding smaller value
     '''else'''
         the nearest smaller value to x is the top element of S
     push x onto S

Despite having a nested loop structure, the running time of this algorithm is linear, because every iteration of the inner loop removes an item that had been added in some previous iteration of the outer loop. It is closely related to an algorithm of [[Donald Knuth|Knuth]] for [[stack-sortable permutation|sorting with a stack]] (for inputs that can be sorted in this way).<ref>{{citation
 | last = Knuth | first = Donald | author-link = Donald Knuth
 | location = Reading, Mass.
 | publisher = Addison-Wesley
 | title = [[The Art of Computer Programming]]
 | contribution = Vol. 1: Fundamental Algorithms
 | year = 1968| volume = 34 | issue = 2 | page = 198 | doi = 10.13182/NSE68-A19548 | bibcode = 1968NSE....34..198W }}.</ref>

An even simpler linear-time sequential algorithm  does not even need a stack; it assumes that the input sequence is given as an array <code>A[1,n]</code> of size <code>n</code>, and stores the index <code>j</code> of the preceding smaller value of the <code>i</code><sup>th</sup> value <code>A[i]</code> in <code>P[i]</code>. We assume an artificial overall minimum at <code>A[0]</code>:{{sfnp|Barbay|Fischer|Navarro|2012|loc=Lemma 1}}

 '''for''' i from 1 to n:
     j = i-1
     '''while''' A[j] >= A[i]:
         j = P[j]
     P[i] = j

<!-- block zero-submatrix · source cpa · cpa:dynamic_programming/zero_matrix -->

# Finding the largest zero submatrix

You are given a matrix with `n` rows and `m` columns. Find the largest submatrix consisting of only zeros (a submatrix is a rectangular area of the matrix).

## Algorithm

Elements of the matrix will be `a[i][j]`, where `i = 0...n - 1`, `j = 0... m - 1`. For simplicity, we will consider all non-zero elements equal to 1.

### Step 1: Auxiliary dynamic

First, we calculate the following auxiliary matrix: `d[i][j]`, nearest row that has a 1 above `a[i][j]`. Formally speaking, `d[i][j]` is the largest row number (from `0` to `i - 1`), in which there is a element equal to `1` in the `j`-th column. 
While iterating from top-left to bottom-right, when we stand in row `i`, we know the values from the previous row, so, it is enough to update just the elements with value `1`. We can save the values in a simple array `d[i]`, `i = 1...m - 1`, because in the further algorithm we will process the matrix one row at a time and only need the values of the current row.

```cpp
vector<int> d(m, -1);
for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
        if (a[i][j] == 1) {
            d[j] = i;
        }
    }
}
```

### Step 2: Problem solving

We can solve the problem in $O(n m^2)$ iterating through rows, considering every possible left and right columns for a submatrix. The bottom of the rectangle will be the current row, and using `d[i][j]` we can find the top row. However, it is possible to go further and significantly improve the complexity of the solution.

It is clear that the desired zero submatrix is bounded on all four sides by some ones, which prevent it from increasing in size and improving the answer. Therefore,  we will not miss the answer if we act as follows: for every cell `j` in row `i` (the bottom row of a potential zero submatrix) we will have `d[i][j]` as the top row of the current zero submatrix. It now remains to determine the optimal left and right boundaries of the zero submatrix, i.e. maximally push this submatrix to the left and right of the `j`-th column. 

What does it mean to push the maximum to the left? It means to find an index `k1` for which `d[i][k1] > d[i][j]`, and at the same time `k1` - the closest one to the left of the index `j`. It is clear that then `k1 + 1` gives the number of the left column of the required zero submatrix. If there is no such index at all, then put `k1` = `-1`(this means that we were able to extend the current zero submatrix to the left all the way to the border of matrix `a`).

Symmetrically, you can define an index `k2` for the right border: this is the closest index to the right of `j` such that `d[i][k2] > d[i][j]` (or `m`, if there is no such index).

So, the indices `k1` and `k2`, if we learn to search for them effectively, will give us all the necessary information about the current zero submatrix. In particular, its area will be equal to `(i - d[i][j]) * (k2 - k1 - 1)`.

How to look for these indexes `k1` and `k2` effectively with fixed `i` and `j`? We can do that in $O(1)$ on average.

To achieve such complexity, you can use the stack as follows. Let's first learn how to search for an index `k1`, and save its value for each index `j` within the current row `i` in matrix `d1[i][j]`. To do this, we will look through all the columns `j` from left to right, and we will store in the stack only those columns that have `d[][]` strictly greater than `d[i][j]`. It is clear that when moving from a column `j` to the next column, it is necessary to update the content of the stack. When there is an inappropriate element at the top of the stack (i.e. `d[][] <= d[i][j]`) pop it. It is easy to understand that it is enough to remove from the stack only from its top, and from none of its other places (because the stack will contain an increasing `d` sequence of columns).

The value `d1[i][j]` for each `j` will be equal to the value lying at that moment on top of the stack.

The dynamics `d2[i][j]` for finding the indices `k2` is considered similar, only you need to view the columns from right to left.

It is clear that since there are exactly `m` pieces added to the stack on each line, there could not be more deletions either, the sum of complexities will be linear, so the final complexity of the algorithm is $O(nm)$.

It should also be noted that this algorithm consumes $O(m)$ memory (not counting the input data - the matrix `a[][]`).

### Implementation

```cpp
int zero_matrix(vector<vector<int>> a) {
    int n = a.size();
    int m = a[0].size();

    int ans = 0;
    vector<int> d(m, -1), d1(m), d2(m);
    stack<int> st;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == 1)
                d[j] = i;
        }

        for (int j = 0; j < m; ++j) {
            while (!st.empty() && d[st.top()] <= d[j])
                st.pop();
            d1[j] = st.empty() ? -1 : st.top();
            st.push(j);
        }
        while (!st.empty())
            st.pop();

        for (int j = m - 1; j >= 0; --j) {
            while (!st.empty() && d[st.top()] <= d[j])
                st.pop();
            d2[j] = st.empty() ? m : st.top();
            st.push(j);
        }
        while (!st.empty())
            st.pop();

        for (int j = 0; j < m; ++j)
            ans = max(ans, (i - d[j]) * (d2[j] - d1[j] - 1));
    }
    return ans;
}
```
