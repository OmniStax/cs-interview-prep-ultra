# Singly linked lists

<!-- block singly-linked-list · source wikipedia · wikipedia:Linked_list lead + #Basic concepts and nomenclature + ===Singly linked list=== -->

{{Short description|Data structure with nodes pointing to the next node}}
{{Redirect|Dynamic list|text=For the Wikipedia guideline which describes list articles which may never be completed, see [[Wikipedia:WikiProject Lists]].}}
{{More footnotes needed|date=March 2012}}
[[File:Singly-linked-list.svg|frame|A linked list is a sequence of nodes that contain two fields: data (an integer value here as an example) and a link to the next node. The last node is linked to a terminator used to signify the end of the list.]]
In [[computer science]], a '''linked list''' is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element [[pointer (computer programming)|points]] to the next. It is a [[data structure]] consisting of a collection of [[node (computer science)|node]]s which together represent a [[sequence]]. In its most basic form, each node contains [[Data (computing)|data]], and a [[reference (computer science)|reference]] (in other words, a ''link'') to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions. A drawback of linked lists is that data access time is [[Time complexity|linear]] with respect to the number of nodes in the list. Because nodes are serially linked, accessing any node requires that the prior node be accessed beforehand (which introduces difficulties in [[instruction pipelining|pipelining]]). Faster access, such as [[random access]] (direct access), is not possible. [[Array data structure|Arrays]] have better [[locality of reference|cache locality]] compared to linked lists.

Linked lists are among the simplest and most common data structures. They can be used to implement several other common [[abstract data type]]s, including [[List (abstract data type)|lists]], [[Stack (abstract data type)|stacks]], [[Queue (abstract data type)|queues]], [[associative array]]s, and [[S-expression]]s, though it is not uncommon to implement those data structures directly without using a linked list as the basis.

The principal benefit of a linked list over a conventional [[array data structure|array]] is that the list elements can be easily inserted or removed without reallocation or reorganization of the entire structure because the data items do not need to be stored [[wikt:contiguous|contiguously]] in memory or on disk, while restructuring an array at [[Run time (program lifecycle phase)|run-time]] is a much more expensive operation. In an array, data is stored contiguously in memory; each element is located in an adjacent location to the previous one. But in a linked list, data is not stored in contiguous memory locations; instead, the node holding the reference to other node's memory address is in sequential order. Linked lists allow insertion and removal of nodes at any point in the list, and allow doing so with a constant number of operations by keeping the link previous to the link being added or removed in memory during list traversal.

On the other hand, since simple linked lists by themselves do not allow random access to the data or any form of efficient indexing, many basic operations—such as obtaining the last node of the list, finding a node that contains a given datum, or locating the place where a new node should be inserted—may require iterating through most or all of the list elements.

==Basic concepts and nomenclature==
Each record of a linked list is often called an 'element' or '[[node (computer science)|node]]'.

The field of each node that contains the address of the next node is usually called the 'next link' or 'next pointer'. The remaining fields are known as the 'data', 'information', 'value', 'cargo', or 'payload' fields.

The 'head' of a list is its first node. The 'tail' of a list may refer either to the rest of the list after the head, or to the last node in the list. In [[Lisp (programming language)|Lisp]] and some derived languages, the next node may be called the '[[CAR and CDR|cdr]]' (pronounced {{IPA|/'kʊd.əɹ/}}) of the list, while the payload of the head node may be called the 'car'.

===Singly linked list===
Singly linked lists contain nodes which have a 'value' field as well as 'next' field, which points to the next node in line of nodes. Operations that can be performed on singly linked lists include insertion, deletion and traversal.

[[Image:Singly-linked-list.svg|frame|center|A singly linked list whose nodes contain two fields: an integer value (data) and a link to the next node]]

The following C language code demonstrates how to add a new node with the "value" to the end of a singly linked list:
<syntaxhighlight lang="c" line="">
#include <stdlib.h>

// Each node in a linked list is a structure. The head node is the first node in the list.

typedef struct Node {
    int value;
    struct Node* next;
} Node;

Node* addNodeToTail(Node* head, int value) {
    // declare Node pointer and initialize to point to the new Node (i.e., it will have the new Node's memory address) being added to the end of the list.
    Node* temp = (Node*)malloc(sizeof *temp); /// 'malloc' in stdlib.
    temp->value = value; // Add data to the value field of the new Node.
    temp->next = NULL; // initialize invalid links to nil.
    
    if (!head) {
        head = temp;     // If the linked list is empty (i.e., the head node pointer is a null pointer), then have the head node pointer point to the new Node.
    } else {
        Node* p = head;   // Assign the head node pointer to the Node pointer 'p'.
        while (p->next) {
            p = p->next;    // Traverse the list until p is the last Node. The last Node always points to NULL.
        }
        p->next = temp; // Make the previously last Node point to the new Node.
    }
    
    return head;    // Return the head node pointer.
}
</syntaxhighlight>

<!-- block pointer-to-pointer · source wikipedia · wikipedia:Pointer_(computer_programming)#Multiple indirection, to “…the address of the new item.”, before the argv paragraph -->

====Multiple indirection====
In some languages, a pointer can reference another pointer, requiring multiple dereference operations to get to the original value. While each level of indirection may add a performance cost, it is sometimes necessary in order to provide correct behavior for complex [[data structures]]. For example, in C it is typical to define a [[linked list]] in terms of an element that contains a pointer to the next element of the list:

<syntaxhighlight lang="C">
typedef struct LinkedList {
    int value;
    struct LinkedList *next;
} LinkedList;

LinkedList *head = NULL;
</syntaxhighlight>

This implementation uses a pointer to the first element in the list as a surrogate for the entire list. If a new value is added to the beginning of the list, <code>head</code> has to be changed to point to the new element. Since C arguments are always passed by value, using double indirection allows the insertion to be implemented correctly, and has the desirable side-effect of eliminating special case code to deal with insertions at the front of the list:

<syntaxhighlight lang="C">
// Given a sorted list at *head, insert the element item at the first
// location where all earlier elements have lesser or equal value.
void insert(LinkedList **head, LinkedList *item) {
    // p points to a pointer to an element
    LinkedList **p = head;
    while (*p && (*p)->value < item->value) {
        p = &(*p)->next;
    }
    item->next = *p;
    *p = item;
}

// Caller does this:
insert(&head, item);
</syntaxhighlight>

In this case, if the value of <code>item</code> is less than that of <code>head</code>, the caller's <code>head</code> is properly updated to the address of the new item.

<!-- block list-operations · source wikipedia · wikipedia:Linked_list#Linked list operations (its opening) + ====Singly linked lists==== -->

==Linked list operations==
When manipulating linked lists in-place, care must be taken to not use values that have been invalidated in previous assignments. This makes algorithms for inserting or deleting linked list nodes somewhat subtle. This section gives [[pseudocode]] for adding or removing nodes from singly, doubly, and circularly linked lists in-place. Throughout, ''null'' is used to refer to an end-of-list marker or [[sentinel value|sentinel]], which may be implemented in a number of ways.

===Linearly linked lists===

====Singly linked lists====
The node data structure will have two fields. There is also a variable, ''firstNode'' which always points to the first node in the list, or is ''null'' for an empty list.

 '''record''' ''Node''
 {
     data; ''// The data being stored in the node''
     ''Node'' next ''// A [[reference (computer science)|reference]]''<ref name=":0" /> to the next node, null for last node
 }

 '''record''' ''List''
 {
     ''Node'' firstNode ''// points to first node of list; null for empty list''
 }

Traversal of a singly linked list is simple, beginning at the first node and following each ''next'' link until reaching the end:

 node := list.firstNode
 '''while''' node not null
     ''(do something with node.data)''
     node := node.next

The following code inserts a node after an existing node in a singly linked list. The diagram shows how it works. Inserting a node before an existing one cannot be done directly; instead, one must keep track of the previous node and insert a node after it.

  [[File:CPT-LinkedLists-addingnode.svg|frame|center|Diagram of inserting a node into a singly linked list]]

 '''function''' insertAfter(''Node'' node, ''Node'' newNode) ''// insert newNode after node''
     newNode.next := node.next
     node.next    := newNode

Inserting at the beginning of the list requires a separate function. This requires updating ''firstNode''.

 '''function''' insertBeginning(''List'' list, ''Node'' newNode) ''// insert node before current first node''
     newNode.next   := list.firstNode
     list.firstNode := newNode

Similarly, there are functions for removing the node ''after'' a given node, and for removing a node from the beginning of the list. The diagram demonstrates the former. To find and remove a particular node, one must again keep track of the previous element.

[[File:CPT-LinkedLists-deletingnode.svg|frame|center|Diagram of deleting a node from a singly linked list]]

 '''function''' removeAfter(''Node'' node) ''// remove node past this one''
     obsoleteNode := node.next
     node.next := node.next.next
     destroy obsoleteNode

 '''function''' removeBeginning(''List'' list) ''// remove first node''
     obsoleteNode := list.firstNode
     list.firstNode := list.firstNode.next ''// point past deleted node''
     destroy obsoleteNode

Notice that <code>removeBeginning()</code> sets <code>list.firstNode</code> to <code>null</code> when removing the last node in the list.

Since it is not possible to iterate backwards, efficient <code>insertBefore</code> or <code>removeBefore</code> operations are not possible. Inserting to a list before a specific node requires traversing the list, which would have a worst case running time of O(n).

Appending one linked list to another can be inefficient unless a reference to the tail is kept as part of the List structure, because it is needed to traverse the entire first list in order to find the tail, and then append the second list to this. Thus, if two linearly linked lists are each of length <math>n</math>, list appending has [[asymptotic time complexity]] of <math>O(n)</math>. In the Lisp family of languages, list appending is provided by the <code>[[append]]</code> procedure.

Many of the special cases of linked list operations can be eliminated by including a dummy element at the front of the list. This ensures that there are no special cases for the beginning of the list and renders both <code>insertBeginning()</code> and <code>removeBeginning()</code> unnecessary, i.e., every element or node is next to another node (even the first node is next to the dummy node). In this case, the first useful data in the list will be found at <code>list.'''firstNode'''.next</code>.

<!-- block lists-vs-arrays · source wikipedia · wikipedia:Linked_list#Linked lists vs. dynamic arrays, without its comparison table (a template) -->

===Linked lists vs. dynamic arrays===
{{List data structure comparison}}
A ''[[dynamic array]]'' is a data structure that allocates all elements contiguously in memory, and keeps a count of the current number of elements. If the space reserved for the dynamic array is exceeded, it is reallocated and (possibly) copied, which is an expensive operation.

Linked lists have several advantages over dynamic arrays. Insertion or deletion of an element at a specific point of a list, assuming that a pointer is indexed to the node (before the one to be removed, or before the insertion point) already, is a constant-time operation (otherwise without this reference it is O(n)), whereas insertion in a dynamic array at random locations will require moving half of the elements on average, and all the elements in the worst case. While one can "delete" an element from an array in constant time by somehow marking its slot as "vacant", this causes [[fragmentation (computer)|fragmentation]] that impedes the performance of iteration.

Moreover, arbitrarily many elements may be inserted into a linked list, limited only by the total memory available; while a dynamic array will eventually fill up its underlying array data structure and will have to reallocate—an expensive operation, one that may not even be possible if memory is fragmented, although the cost of reallocation can be averaged over insertions, and the cost of an insertion due to reallocation would still be [[Amortized analysis|amortized]] O(1). This helps with appending elements at the array's end, but inserting into (or removing from) middle positions still carries prohibitive costs due to data moving to maintain contiguity. An array from which many elements are removed may also have to be resized in order to avoid wasting too much space.

On the other hand, dynamic arrays (as well as fixed-size [[array data structure]]s) allow constant-time [[random access]], while linked lists allow only [[sequential access]] to elements. Singly linked lists, in fact, can be easily traversed in only one direction. This makes linked lists unsuitable for applications where it's useful to look up an element by its index quickly, such as [[heapsort]]. Sequential access on arrays and dynamic arrays is also faster than on linked lists on many machines, because they have optimal [[locality of reference]] and thus make good use of data caching.

Another disadvantage of linked lists is the extra storage needed for references, which often makes them impractical for lists of small data items such as [[character (computing)|characters]] or [[Boolean value]]s, because the storage overhead for the links may exceed by a factor of two or more the size of the data. In contrast, a dynamic array requires only the space for the data itself (and a very small amount of control data).<ref group="note">The amount of control data required for a dynamic array is usually of the form <math>K+Bn</math>, where <math>K</math> is a per-array constant, <math>B</math> is a per-dimension constant, and <math>n</math> is the number of dimensions. <math>K</math> and <math>B</math> are typically on the order of 10 bytes.</ref> It can also be slow, and with a naïve allocator, wasteful, to allocate memory separately for each new element, a problem generally solved using [[memory pool]]s.

Some hybrid solutions try to combine the advantages of the two representations. [[Unrolled linked list]]s store several elements in each list node, increasing cache performance while decreasing memory overhead for references. [[CDR coding]] does both these as well, by replacing references with the actual data referenced, which extends off the end of the referencing record.

A good example that highlights the pros and cons of using dynamic arrays vs. linked lists is by implementing a program that resolves the [[Josephus problem]]. The Josephus problem is an election method that works by having a group of people stand in a circle. Starting at a predetermined person, one may count around the circle ''n'' times. Once the ''n''th person is reached, one should remove them from the circle and have the members close the circle. The process is repeated until only one person is left. That person wins the election. This shows the strengths and weaknesses of a linked list vs. a dynamic array, because if the people are viewed as connected nodes in a circular linked list, then it shows how easily the linked list is able to delete nodes (as it only has to rearrange the links to the different nodes). However, the linked list will be poor at finding the next person to remove and will need to search through the list until it finds that person. A dynamic array, on the other hand, will be poor at deleting nodes (or elements) as it cannot remove one node without individually shifting all the elements up the list by one. However, it is exceptionally easy to find the ''n''th person in the circle by directly referencing them by their position in the array.

The [[list ranking]] problem concerns the efficient conversion of a linked list representation into an array. Although trivial for a conventional computer, solving this problem by a [[parallel algorithm]] is complicated and has been the subject of much research.

A [[self-balancing binary search tree|balanced tree]] has similar memory access patterns and space overhead to a linked list while permitting much more efficient indexing, taking O(log n) time instead of O(n) for a random access. However, insertion and deletion operations are more expensive due to the overhead of tree manipulations to maintain balance. Schemes exist for trees to automatically maintain themselves in a balanced state: [[AVL tree]]s or [[red–black tree]]s.
