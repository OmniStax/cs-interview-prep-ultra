# Arrays and the list interface

<!-- block array · source wikipedia · wikipedia:Array_(data_structure), the lead -->

## Arrays

In computer science, an **array** is a data structure consisting of a collection of *elements* (values or variables), of the same memory size, each identified by at least one *array index* or *key*, the collection of which may be a tuple, known as an index tuple. In general, an array is a mutable and linear collection of elements with the same data type. An array is stored such that the position (memory address) of each element can be computed from its index tuple by a mathematical formula.[^1][^2][^3] The simplest type of data structure is a linear array, also called a one-dimensional array.

For example, an array of ten 32-bit (4-byte) integer variables, with indices 0 through 9, may be stored as ten words at memory addresses 2000, 2004, 2008, ..., 2036, (in hexadecimal: `0x7D0`, `0x7D4`, `0x7D8`, ..., `0x7F4`) so that the element with index *i* has the address 2000 + (*i* × 4).[^4] The memory address of the first element of an array is called first address, foundation address, or base address.

Because the mathematical concept of a matrix can be represented as a two-dimensional grid, two-dimensional arrays are also sometimes called "matrices". In some cases the term "vector" is used in computing to refer to an array, although tuples rather than vectors are the more mathematically correct equivalent. Tables are often implemented in the form of arrays, especially lookup tables; the word "table" is sometimes used as a synonym of array.

Arrays are among the oldest and most important data structures, and are used by almost every program. They are also used to implement many other data structures, such as lists and strings. They effectively exploit the addressing logic of computers. In most modern computers and many external storage devices, the memory is a one-dimensional array of words, whose indices are their addresses. Processors, especially vector processors, are often optimized for array operations.

Arrays are useful mostly because the element indices can be computed at run time. Among other things, this feature allows a single iterative statement to process arbitrarily many elements of an array. For that reason, the elements of an array data structure are required to have the same size and should use the same data representation. The set of valid index tuples and the addresses of the elements (and hence the element addressing formula) are usually,[^2][^5] but not always,[^2] fixed while the array is in use.

The term "array" may also refer to an array data type, a kind of data type provided by most high-level programming languages that consists of a collection of values or variables that can be selected by one or more indices computed at run-time. Array types are often implemented by array structures; however, in some languages they may be implemented by hash tables, linked lists, search trees, or other data structures.

The term is also used, especially in the description of algorithms, to mean associative array or "abstract array", a theoretical computer science model (an abstract data type or ADT) intended to capture the essential properties of arrays.

<!-- block addressing · source wikipedia · wikipedia:Array_(data_structure)#Element identifier and addressing formulas, its opening with “One-dimensional arrays” and “Multidimensional arrays”, before “Dope vectors” -->

## Element identifier and addressing formulas

When data objects are stored in an array, individual objects are selected by an index that is usually a non-negative scalar integer. Indexes are also called subscripts. An index *maps* the array value to a stored object.

There are three ways in which the elements of an array can be indexed:

- **0 (*zero-based indexing*)** The first element of the array is indexed by subscript of 0.[^8]
- **1 (*one-based indexing*)** The first element of the array is indexed by subscript of 1.
- **n (*n-based indexing*)** The base index of an array can be freely chosen. Usually programming languages allowing *n-based indexing* also allow negative index values and other scalar data types like enumerations, or characters may be used as an array index.

Using zero based indexing is the design choice of many influential programming languages, including C, Java and Lisp. This leads to simpler implementation where the subscript refers to an offset from the starting position of an array, so the first element has an offset of zero.

Arrays can have multiple dimensions, thus it is not uncommon to access an array using multiple indices. For example, a two-dimensional array `A` with three rows and four columns might provide access to the element at the 2nd row and 4th column by the expression `A[1][3]` in the case of a zero-based indexing system. Thus two indices are used for a two-dimensional array, three for a three-dimensional array, and *n* for an *n*-dimensional array.

The number of indices needed to specify an element is called the dimension, dimensionality, or rank of the array.

In standard arrays, each index is restricted to a certain range of consecutive integers (or consecutive values of some enumerated type), and the address of an element is computed by a "linear" formula on the indices.

### One-dimensional arrays

A one-dimensional array (or single dimension array) is a type of linear array. Accessing its elements involves a single subscript which can either represent a row or column index.

As an example consider the C declaration `int a[10];` which declares a one-dimensional array named `a` of ten integers. Here, the array can store ten elements of type `int` . This array has indices starting from zero through nine. For example, the expressions `a[0]` and `a[9]` are the first and last elements respectively.

For a vector with linear addressing, the element with index *i* is located at the address *B* + *c* · *i*, where *B* is a fixed *base address* and *c* a fixed constant, sometimes called the *address increment* or *stride*.

If the valid element indices begin at 0, the constant *B* is simply the address of the first element of the array. For this reason, the C programming language specifies that array indices always begin at 0; and many programmers will call that element "zeroth" rather than "first".

However, one can choose the index of the first element by an appropriate choice of the base address *B*. For example, if the array has five elements, indexed 1 through 5, and the base address *B* is replaced by *B* + 30*c*, then the indices of those same elements will be 31 to 35. If the numbering does not start at 0, the constant *B* may not be the address of any element.

### Multidimensional arrays

For a multidimensional array, the element with indices *i*,*j* would have address *B* + *c* · *i* + *d* · *j*, where the coefficients *c* and *d* are the *row* and *column address increments*, respectively.

More generally, in a *k*-dimensional array, the address of an element with indices *i*~1~, *i*~2~, ..., *i*~*k*~ is

$$B + c_1 \cdot i_1 + c_2 \cdot i_2 + \dots + c_k \cdot i_k.$$

For example: int a[2][3];

This means that array a has 2 rows and 3 columns, and the array is of integer type. Here we can store 6 elements they will be stored linearly but starting from first row linear then continuing with second row. The above array will be stored as a~11~, a~12~, a~13~, a~21~, a~22~, a~23~.

This formula requires only *k* multiplications and *k* additions, for any array that can fit in memory. Moreover, if any coefficient is a fixed power of 2, the multiplication can be replaced by bit shifting.

The coefficients *c*~*k*~ must be chosen so that every valid index tuple maps to the address of a distinct element.

If the minimum legal value for every index is 0, then *B* is the address of the element whose indices are all zero. As in the one-dimensional case, the element indices may be changed by changing the base address *B*. Thus, if a two-dimensional array has rows and columns indexed from 1 to 10 and 1 to 20, respectively, then replacing *B* by *B* + *c*~1~ − 3*c*~2~ will cause them to be renumbered from 0 through 9 and 4 through 23, respectively. Taking advantage of this feature, some languages (like FORTRAN 77) specify that array indices begin at 1, as in mathematical tradition while other languages (like Fortran 90, Pascal and Algol) let the user choose the minimum value for each index.

<!-- block efficiency · source wikipedia · wikipedia:Array_(data_structure)#Efficiency, its opening, before “Comparison with other data structures” -->

## Efficiency

Both *store* and *select* take (deterministic worst case) constant time. Arrays take linear (O(*n*)) space in the number of elements *n* that they hold.

In an array with element size *k* and on a machine with a cache line size of B bytes, iterating through an array of *n* elements requires the minimum of ceiling(*nk*/B) cache misses, because its elements occupy contiguous memory locations. This is roughly a factor of B/*k* better than the number of cache misses needed to access *n* elements at random memory locations. As a consequence, sequential iteration over an array is noticeably faster in practice than iteration over many other data structures, a property called locality of reference (this does *not* mean however, that using a perfect hash or trivial hash within the same (local) array, will not be even faster – and achievable in constant time). Libraries provide low-level optimized facilities for copying ranges of memory (such as memcpy) which can be used to move contiguous blocks of array elements significantly faster than can be achieved through individual element access. The speedup of such optimized routines varies by array element size, architecture, and implementation.

Memory-wise, arrays are compact data structures with no per-element overhead. There may be a per-array overhead (e.g., to store index bounds) but this is language-dependent. It can also happen that elements stored in an array require *less* memory than the same elements stored in individual variables, because several array elements can be stored in a single word; such arrays are often called *packed* arrays. An extreme (but commonly used) case is the bit array, where every bit represents a single element. A single octet can thus hold up to 256 different combinations of up to 8 different conditions, in the most compact form.

Array accesses with statically predictable access patterns are a major source of data parallelism.

<!-- block iliffe · source wikipedia · wikipedia:Array_(data_structure)#Comparison with other data structures, the Iliffe-vector paragraph and its image -->

## Iliffe vectors

[photo-iliffe]

An Iliffe vector is an alternative to a multidimensional array structure. It uses a one-dimensional array of references to arrays of one dimension less. For two dimensions, in particular, this alternative structure would be a vector of pointers to vectors, one for each row(pointer on c or c++). Thus an element in row *i* and column *j* of an array *A* would be accessed by double indexing (*A*[*i*][*j*] in typical notation). This alternative structure allows jagged arrays, where each row may have a different size—or, in general, where the valid range of each index depends on the values of all preceding indices. It also saves one multiplication (by the column address increment) replacing it by a bit shift (to index the vector of row pointers) and one extra memory access (fetching the row address), which may be worthwhile in some architectures.

<!-- block c-arrays · source wikipedia · wikipedia:Pointer_(computer_programming)#C arrays -->

## C arrays

In C, array indexing is formally defined in terms of pointer arithmetic; that is, the language specification requires that `a[i]` be equivalent to `*(a + i)`,[^12] because, if `a` is the name of an array, in most contexts the expression `a` evaluates to a pointer to the first element of `a`,[^13] so the syntax for accessing arrays is identical for that which can be used to dereference pointers. For example, an array `a` can be declared and used in the following manner:

```
int a[5]; // Declares 5 contiguous integers
int *ptr = a; // Array names in expressions evaluate to pointers in most cases
ptr[0] = 1; // Pointers can be indexed with array syntax
*(a + 1) = 2; // Arrays can be indexed with pointer syntax
*(1 + a) = 2; // Pointer addition is commutative
2[a] = 4; // Subscript operator is commutative (perhaps unusual)
```

This allocates a block of five integers and names the block `a`; the expression `a` evaluates, in most contexts, as a pointer to the first element of the block. Another common use of pointers is to point to dynamically allocated memory from malloc which returns a consecutive block of memory of no less than the requested size that can be used as an array. The form `i[a]` (where `i` is the index) is declared obsolescent as of C29, in favour of the more common form `a[i]`.

While, when used as an operand for most operators, an array evaluates as a pointer to the first element of the array, this is not the case for the `sizeof` operator. In this example, `sizeof(a)` will evaluate to `5 * sizeof(int)` (the size of the array), while `sizeof(ptr)` will evaluate to `sizeof(int *)`, the size of the pointer itself.

Default values of an array can be declared like:

```
int a[5] = {2, 4, 3, 1, 5};
```

If `a` is located in memory starting at address `0x1000` on a 32-bit little-endian machine then memory will contain the following (values are in hexadecimal, like the addresses):

|  | 0 | 1 | 2 | 3 |
| 1000 | 2 | 0 | 0 | 0 |
| 1004 | 4 | 0 | 0 | 0 |
| 1008 | 3 | 0 | 0 | 0 |
| 100C | 1 | 0 | 0 | 0 |
| 1010 | 5 | 0 | 0 | 0 |

Represented here are five integers: 2, 4, 3, 1, and 5. These five integers occupy 32 bits (4 bytes) each with the least-significant byte stored first (this is a little-endian CPU architecture) and are stored consecutively starting at address `0x1000`.

The syntax for C with pointers is:

- `a` means `0x1000`;
- `a + 1` means `0x1004`: the "+ 1" means to add the size of 1 `int`, which is 4 bytes;
- `*a` means to dereference the contents of `a`. Considering the contents as a memory address (`0x1000`), look up the value at that location (`0x0002`);
- `a[i]` means element number `i`, 0-based, of `a` which is translated into `*(a + i)`.

The last example is how to access the contents of `a`. Breaking it down:

- `a + i` is the memory location of the `i`^th^ element of `a`, starting at `i = 0`;
- `*(a + i)` takes that memory address and dereferences it to access the value.

<!-- block list-interface · source ods · ods:intro#the-list-interface-linear-sequences -->

## The List Interface: Linear Sequences

This book will talk very little about the FIFO Queue, Stack, or Deque interfaces. This is because these interfaces are subsumed by the List interface. A List, illustrated in Figure 1.4, represents a sequence, $x_0,\ldots,x_{n-1}$, of values. The List interface includes the following operations:

1. $\mathrm{size}()$: return $n$, the length of the list
1. $\mathrm{get}(i)$: return the value $x_{i}$
1. $\mathrm{set}(i,x)$: set the value of $x_{i}$ equal to $x$
1. $\mathrm{add}(i,x)$: add $x$ at position $i$, displacing $x_{i},\ldots,x_{n-1}$;   
 Set $x_{j+1}=x_j$, for all $j\in\{n-1,\ldots,i\}$, increment $n$, and set $x_i=x$
1. $\mathrm{remove}(i)$ remove the value $x_{i}$, displacing $x_{i+1},\ldots,x_{n-1}$;   
 Set $x_{j}=x_{j+1}$, for all $j\in\{i,\ldots,n-2\}$ and decrement $n$

Notice that these operations are easily sufficient to implement the Deque interface:

$$\begin{aligned}\mathrm{addFirst}(x) &\Rightarrow \mathrm{add}(0,x) \\ \mathrm{removeFirst}() &\Rightarrow \mathrm{remove}(0) \\ \mathrm{addLast}(x) &\Rightarrow \mathrm{add}(\mathrm{size}(),x) \\ \mathrm{removeLast}() &\Rightarrow \mathrm{remove}(\mathrm{size}()-1)\end{aligned}$$

[figure list]

Although we will normally not discuss the Stack, Deque and FIFO Queue interfaces in subsequent chapters, the terms Stack and Deque are sometimes used in the names of data structures that implement the List interface. When this happens, it highlights the fact that these data structures can be used to implement the Stack or Deque interface very efficiently. For example, the ArrayDeque class is an implementation of the List interface that implements all the Deque operations in constant time per operation.

## Footnotes

[^1]: Black, Paul E. (13 November 2008). “array”. Dictionary of Algorithms and Data Structures. National Institute of Standards and Technology. Retrieved 22 August 2010.

[^2]: Andres, Bjoern; Koethe, Ullrich; Kroeger, Thorben; Hamprecht (2010). “Runtime-Flexible Multi-dimensional Arrays and Views for C++98 and C++0x”. arXiv:1008.2909 [cs.DS].

[^3]: Garcia, Ronald; Lumsdaine, Andrew (2005). “MultiArray: a C++ library for generic programming with arrays”. Software: Practice and Experience. 35 (2): 159–188. doi:10.1002/spe.630. ISSN 0038-0644. S2CID 10890293.

[^4]: David R. Richardson (2002), The Book on Data Structures. iUniverse, 1112 pages. ISBN 0-595-24039-9, ISBN 978-0-595-24039-5.

[^3]: Garcia, Ronald; Lumsdaine, Andrew (2005). “MultiArray: a C++ library for generic programming with arrays”. Software: Practice and Experience. 35 (2): 159–188. doi:10.1002/spe.630. ISSN 0038-0644. S2CID 10890293.

[^5]: Veldhuizen, Todd L. (December 1998). Arrays in Blitz++. Computing in Object-Oriented Parallel Environments. Lecture Notes in Computer Science. Vol. 1505. Berlin: Springer. pp. 223–230. doi:10.1007/3-540-49372-7_24. ISBN 978-3-540-65387-5. [dead link]

[^2]: Andres, Bjoern; Koethe, Ullrich; Kroeger, Thorben; Hamprecht (2010). “Runtime-Flexible Multi-dimensional Arrays and Views for C++98 and C++0x”. arXiv:1008.2909 [cs.DS].

[^8]: “Array Code Examples - PHP Array Functions - PHP code”. Computer Programming Web programming Tips. Archived from the original on 13 April 2011. Retrieved 8 April 2011. “In most computer languages array index (counting) starts from 0, not from 1. Index of the first element of the array is 0, index of the second element of the array is 1, and so on. In array of names below you can see indexes and values.”

[^12]: Plauger, P J; Brodie, Jim (1992). ANSI and ISO Standard C Programmer's Reference. Redmond, WA: Microsoft Press. p. 108. ISBN 978-1-55615-359-4.

[^13]: WG14-N3096: Draft for C23: ISO/IEC 9899:2023. April 1, 2023. ISO/IEC. § 6.3.2.1: Lvalues, arrays, and function designators. p. 48. Archived on April 2, 2023.
