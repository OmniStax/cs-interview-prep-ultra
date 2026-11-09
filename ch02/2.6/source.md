# Doubly linked lists

<!-- block dummy-node · source ods · ods:linkedlists#sec:dllist, opening through fig. dllist and the DLList() code -->

## DLList: A Doubly-Linked List

A DLList (doubly-linked list) is very similar to an SLList except that each node $u$ in a DLList has references to both the node $u.next$ that follows it and the node $u.prev$ that precedes it.

When implementing an SLList, we saw that there were always several special cases to worry about. For example, removing the last element from an SLList or adding an element to an empty SLList requires care to ensure that $head$ and $tail$ are correctly updated. In a DLList, the number of these special cases increases considerably. Perhaps the cleanest way to take care of all these special cases in a DLList is to introduce a $dummy$ node. This is a node that does not contain any data, but acts as a placeholder so that there are no special nodes; every node has both a $next$ and a $prev$, with $dummy$ acting as the node that follows the last node in the list and that precedes the first node in the list. In this way, the nodes of the list are (doubly-)linked into a cycle, as illustrated in Figure 3.2.

```python
def _initialize(self):
    self.n = 0
    self.dummy = DLList.Node(None)
    self.dummy.prev = self.dummy
    self.dummy.next = self.dummy
```

```java
int n;
Node dummy;

DLList() {
    dummy = new Node();
    dummy.next = dummy;
    dummy.prev = dummy;
    n = 0;
}
```

```cpp
Node dummy;
int n;

DLList<T>::DLList() {
    dummy.next = &dummy;
    dummy.prev = &dummy;
    n = 0;
}
```

```javascript
n;
dummy;

constructor() {
  this.dummy = new Node();
  this.dummy.next = this.dummy;
  this.dummy.prev = this.dummy;
  this.n = 0;
}
```

<!-- block dllist · source ods · ods:linkedlists#sec:dllist, from getNode(i) through “Adding and Removing” and “Summary” -->

## Operations on a DLList

Finding the node with a particular index in a DLList is easy; we can either start at the head of the list ($dummy.next$) and work forward, or start at the tail of the list ($dummy.prev$) and work backward. This allows us to reach the $i$th node in $O(1+\min\{i,n-i\})$ time:

```python
def get_node(self, i):
    if i < self.n//2:
        p = self.dummy.next
        for _ in range(i):
            p = p.next
    else:
        p = self.dummy
        for _ in range(self.n, i, -1):
            p = p.prev
    return p
```

```java
Node getNode(int i) {
    Node p = null;
    if (i < n / 2) {
        p = dummy.next;
        for (int j = 0; j < i; j++)
            p = p.next;
    } else {
        p = dummy;
        for (int j = n; j > i; j--)
            p = p.prev;
    }
    return p;
}
```

```cpp
DLList<T>::Node* DLList<T>::getNode(int i) {
    Node* p;
    if (i < n / 2) {
        p = dummy.next;
        for (int j = 0; j < i; j++)
            p = p->next;
    } else {
        p = &dummy;
        for (int j = n; j > i; j--)
            p = p->prev;
    }
    return (p);
}
```

```javascript
getNode(i) {
  let p = null;
  if (i < Math.floor(this.n / 2)) {
    p = this.dummy.next;
    for (let j = 0; j < i; j++)
      p = p.next;
  } else {
    p = this.dummy;
    for (let j = this.n; j > i; j--)
      p = p.prev;
  }
  return p;
}
```

The $get(i)$ and $set(i,x)$ operations are now also easy. We first find the $i$th node and then get or set its $x$ value:

```python
def get(self, i):
    if i < 0 or i >= self.n: raise IndexError()
    return self.get_node(i).x

def set(self, i, x): #@ReservedAssignment
    if i < 0 or i >= self.n: raise IndexError()
    u = self.get_node(i)
    y = u.x
    u.x = x
    return y
```

```java
T get(int i) {
    return getNode(i).x;
}

T set(int i, T x) {
    Node u = getNode(i);
    T y = u.x;
    u.x = x;
    return y;
}
```

```cpp
T DLList<T>::get(int i) {
    return getNode(i)->x;
}

T DLList<T>::set(int i, T x) {
    Node* u = getNode(i);
    T y = u->x;
    u->x = x;
    return y;
}
```

```javascript
get(i) {
  return this.getNode(i).x;
}

set(i, x) {
  const u = this.getNode(i);
  const y = u.x;
  u.x = x;
  return y;
}
```

The running time of these operations is dominated by the time it takes to find the $i$th node, and is therefore $O(1+\min\{i,n-i\})$.

### Adding and Removing

If we have a reference to a node $w$ in a DLList and we want to insert a node $u$ before $w$, then this is just a matter of setting $u.next=w$, $u.prev=w.prev$, and then adjusting $u.prev.next$ and $u.next.prev$. (See Figure 3.3.) Thanks to the dummy node, there is no need to worry about $w.prev$ or $w.next$ not existing.

[sim-dllist]

Now, the list operation $add(i,x)$ is trivial to implement. We find the $i$th node in the DLList and insert a new node $u$ that contains $x$ just before it.

```python
def add(self, i, x):
    if i < 0 or i > self.n:    raise IndexError()
    self.add_before(self.get_node(i), x)
```

```java
void add(int i, T x) {
    addBefore(getNode(i), x);
}
```

```cpp
void DLList<T>::add(int i, T x) {
    addBefore(getNode(i), x);
}
```

```javascript
add(i, x) {
  this.addBefore(this.getNode(i), x);
}
```

The only non-constant part of the running time of $add(i,x)$ is the time it takes to find the $i$th node (using $getNode(i)$). Thus, $add(i,x)$ runs in $O(1+\min\{i, n-i\})$ time.

Removing a node $w$ from a DLList is easy. We only need to adjust pointers at $w.next$ and $w.prev$ so that they skip over $w$. Again, the use of the dummy node eliminates the need to consider any special cases:

```python
def _remove(self, w):
    w.prev.next = w.next
    w.next.prev = w.prev
    self.n -= 1
```

```java
void remove(Node w) {
    w.prev.next = w.next;
    w.next.prev = w.prev;
    n--;
}
```

```cpp
void DLList<T>::remove(Node *w) {
    w->prev->next = w->next;
    w->next->prev = w->prev;
    delete w;
    n--;
}
```

```javascript
_remove(w) {
  w.prev.next = w.next;
  w.next.prev = w.prev;
  this.n--;
}
```

Now the $remove(i)$ operation is trivial. We find the node with index $i$ and remove it:

```python
def remove(self, i):
    if i < 0 or i >= self.n: raise IndexError()
    self._remove(self.get_node(i))
```

```java
T remove(int i) {
    Node w = getNode(i);
    remove(w);
    return w.x;
}
```

```cpp
T DLList<T>::remove(int i) {
    Node *w = getNode(i);
    T x = w->x;
    remove(w);
    return x;
}
```

```javascript
remove(i) {
  const w = this.getNode(i);
  this._remove(w);
  return w.x;
}
```

Again, the only expensive part of this operation is finding the $i$th node using $getNode(i)$, so $remove(i)$ runs in $O(1+\min\{i, n-i\})$ time.

### Summary

The following theorem summarizes the performance of a DLList:

> **Theorem.** A DLList implements the List interface. In this implementation, the $get(i)$, $set(i,x)$, $add(i,x)$ and $remove(i)$ operations run in $O(1+\min\{i,n-i\})$ time per operation.

It is worth noting that, if we ignore the cost of the $getNode(i)$ operation, then all operations on a DLList take constant time. Thus, the only expensive part of operations on a DLList is finding the relevant node. Once we have the relevant node, adding, removing, or accessing the data at that node takes only constant time.

This is in sharp contrast to the array-based List implementations of Section 2.2; in those implementations, the relevant array item can be found in constant time. However, addition or removal requires shifting elements in the array and, in general, takes non-constant time.

For this reason, linked list structures are well-suited to applications where references to list nodes can be obtained through external means.

## Footnotes


