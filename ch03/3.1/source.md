# Stacks and bracket matching

<!-- block stack · source wikipedia · wikipedia:Stack_(abstract_data_type) lead + #Non-essential operations -->

{{short description|Abstract data type}}
{{About|the abstract concept|some concrete uses of the term in computing|Stack (disambiguation)#Computing}}
{{Use dmy dates|date=October 2022|cs1-dates=y}}
{{Use list-defined references|date=October 2022}}
[[File:Tallrik - Ystad-2018.jpg|thumb|Similarly to a stack of plates, adding or removing is only practical at the top.]]
[[File:Lifo stack.svg|thumb|350px|right|Simple representation of a stack runtime with ''push'' and ''pop'' operations]]

In [[computer science]], a '''stack''' is an [[abstract data type]] that serves as a [[collection (abstract data type)|collection]] of elements with two main operations:
* '''Push''', which adds an element to the collection, and
* '''Pop''', which removes the most recently added element.
Additionally, a [[peek (data type operation)|peek]] operation can, without modifying the stack, return the value of the last element added (the item at the top of the stack). The name ''stack'' is an [[analogy]] to a set of physical items stacked one atop another, such as a stack of plates.

The order in which elements are added to or removed from a stack is described as '''last in, first out''', referred to by the acronym '''LIFO'''.<ref group="nb" name="NB1" /> As with a stack of physical objects, this structure makes it easy to take an item off the top of the stack, but accessing a [[Data|datum]] deeper in the stack typically requires removing multiple other items first.<ref name="clrs" />

Considered a sequential collection, a stack has one end which is the only position at which the push and pop operations may occur, the ''top'' of the stack, and is fixed at the other end, the ''bottom''. A stack may be implemented as, for example, a [[singly linked list]] with a pointer to the top element.

A stack may be implemented to have a bounded capacity. If the stack is full and does not contain enough space to accept another element, the stack is in a state of [[stack overflow]].

== Non-essential operations ==
In many implementations, a stack has more operations than the essential "push" and "pop" operations. An example of a non-essential operation is "top of stack", or "peek", which observes the top element without removing it from the stack.<ref name="Horowitz_1984"/> Since this can be broken down into a "pop" followed by a "push" to return the same data to the stack, it is not considered an essential operation. If the stack is empty, an underflow condition will occur upon execution of either the "peek" or "pop" operation. Additionally, many implementations include convenience operations that handle common tasks, such as checking if the stack is empty or returning its size.

<!-- block stack-implementation · source wikipedia · wikipedia:Stack_(abstract_data_type)#Implementation, with ====Array==== and ====Linked list==== -->

== Implementation ==
A stack can be easily implemented either through an [[Array data structure|array]] or a [[linked list]], as it is merely a special case of a list.<ref>{{Cite journal |last=Pandey |first=Shreesham |year=2020 |title=Data Structures in a Nutshell |url=https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4145204 |journal=Dev Genius |volume=2020|ssrn=4145204 }}</ref> In either case, what identifies the data structure as a stack is not the implementation but the interface: the user is only allowed to pop or push items onto the array or linked list, with few other helper operations. The following will demonstrate both implementations using [[pseudocode]].

====Array====
An array can be used to implement a (bounded) stack, as follows. The first element, usually at the [[zero offset]], is the bottom, resulting in <code>array[0]</code> being the first element pushed onto the stack and the last element popped off. The program must keep track of the size (length) of the stack, using a variable ''top'' that records the number of items pushed so far, therefore pointing to the place in the array where the next element is to be inserted (assuming a zero-based index convention). Thus, the stack itself can be effectively implemented as a three-element structure:

 '''structure''' stack:
     maxsize: integer
     top: integer
     items: array of item

 '''procedure''' initialize(stk: stack, size: integer):
     stk.items ← new array of ''size'' items, initially empty
     stk.maxsize ← size
     stk.top ← 0

The ''push'' operation adds an element and increments the ''top'' index, after checking for overflow:
[[file:Stack Push operation-en.gif|thumb|200px|Animated push operation on an array-based stack from underflow to overflow]]
 '''procedure''' push(stk: stack, x: item):
     '''if''' stk.top = stk.maxsize:
         report overflow error
     '''else''':
         stk.items[stk.top] ← x
         stk.top ← stk.top + 1

Similarly, ''pop'' decrements the ''top'' index after checking for underflow, and returns the item that was previously the top one:
[[file:Stack Pop Operation-en.gif|thumb|200px|Animated pop operation on an array-based stack from the full-stack state to the underflow]]
 '''procedure''' pop(stk: stack):
     '''if''' stk.top = 0:
         report underflow error
     '''else''':
         stk.top ← stk.top − 1
         r ← stk.items[stk.top]
         '''return''' r

Using a [[dynamic array]], it is possible to implement a stack that can grow or shrink as much as needed. The size of the stack is simply the size of the dynamic array, which is a very efficient implementation of a stack since adding items to or removing items from the end of a dynamic array requires amortized O(1) time.

====Linked list====
Another option for implementing stacks is to use a [[singly linked list]]. A stack is then a pointer to the "head" of the list, with perhaps a counter to keep track of the size of the list:

 '''structure''' frame:
     data: item
     next: frame or nil

 '''structure''' stack:
     head: frame or nil
     size: integer

 '''procedure''' initialize(stk: stack):
     stk.head ← nil
     stk.size ← 0

Pushing and popping items happens at the head of the list; overflow is not possible in this implementation (unless memory is exhausted):
[[file:Linked-list-based Stack Push operation-en.gif|thumb|200px|Animated push operation on an Linked-List-based stack.]]
 '''procedure''' push(stk: stack, x: item):
     newhead ← new frame
     newhead.data ← x
     newhead.next ← stk.head
     stk.head ← newhead
     stk.size ← stk.size + 1
[[file:Linked-list-based Stack Pop Operation-en.gif|thumb|200px|Animated pop operation on an Linked-List-based stack.]]
 '''procedure''' pop(stk: stack):
     '''if''' stk.head = nil:
         report underflow error
     '''else''':
         r ← stk.head.data
         stk.head ← stk.head.next
         stk.size ← stk.size - 1
         '''return''' r

<!-- block balanced · source cpa · cpa:combinatorics/bracket_sequences#balanced-bracket-sequences, to “…in a similar fashion.”, before the article’s list of its problems -->

# Balanced bracket sequences

A **balanced bracket sequence** is a string consisting of only brackets, such that this sequence, when inserted certain numbers and mathematical operations, gives a valid mathematical expression.
Formally you can define balanced bracket sequence with:

- $e$ (the empty string) is a balanced bracket sequence.
- if $s$ is a balanced bracket sequence, then so is $(s)$.
- if $s$ and $t$ are balanced bracket sequences, then so is $s t$.

For instance $(())()$ is a balanced bracket sequence, but $())($ is not.

Of course you can define other bracket sequences also with multiple bracket types in a similar fashion.

<!-- block validation · source cpa · cpa:combinatorics/bracket_sequences#balance-validation -->

## Balance validation

We want to check if a given string is balanced or not.

At first suppose there is only one type of bracket.
For this case there exists a very simple algorithm.
Let $\text{depth}$ be the current number of open brackets.
Initially $\text{depth} = 0$.
We iterate over all character of the string, if the current bracket character is an opening bracket, then we increment $\text{depth}$, otherwise we decrement it.
If at any time the variable $\text{depth}$ gets negative, or at the end it is different from $0$, then the string is not a balanced sequence.
Otherwise it is.

If there are several bracket types involved, then the algorithm needs to be changed.
Instead of a counter $\text{depth}$ we create a stack, in which we will store all opening brackets that we meet.
If the current bracket character is an opening one, we put it onto the stack.
If it is a closing one, then we check if the stack is non-empty, and if the top element of the stack is of the same type as the current closing bracket.
If both conditions are fulfilled, then we remove the opening bracket from the stack.
If at any time one of the conditions is not fulfilled, or at the end the stack is not empty, then the string is not balanced.
Otherwise it is.
