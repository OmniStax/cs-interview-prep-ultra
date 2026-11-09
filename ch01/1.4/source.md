# Analysing running time and space

<!-- block word-ram · source ods · ods:intro#sec:model, to “occupies one word of memory”, before the last paragraph, which the pseudocode edition prints cut short -->

## The Model of Computation

In this book, we will analyze the theoretical running times of operations on the data structures we study. To do this precisely, we need a mathematical model of computation. For this, we use the *$w$-bit word-RAM* model. RAM stands for Random Access Machine. In this model, we have access to a random access memory consisting of *cells*, each of which stores a $w$-bit *word*. This implies that a memory cell can represent, for example, any integer in the set $\{0,\ldots,2^{w}-1\}$.

In the word-RAM model, basic operations on words take constant time. This includes arithmetic operations ($+$, $-$, $\cdot$, $/$, $\bmod$), comparisons ($<$, $>$, $=$, $\le$, $\ge$), and bitwise boolean operations (bitwise-AND, OR, and exclusive-OR).

Any cell can be read or written in constant time. A computer’s memory is managed by a memory management system from which we can allocate or deallocate a block of memory of any size we would like. Allocating a block of memory of size $k$ takes $O(k)$ time and returns a reference (a pointer) to the newly-allocated memory block. This reference is small enough to be represented by a single word.

The word-size $w$ is a very important parameter of this model. The only assumption we will make about $w$ is the lower-bound $w \ge \log n$, where $n$ is the number of elements stored in any of our data structures. This is a fairly modest assumption, since otherwise a word is not even big enough to count the number of elements stored in the data structure.

Space is measured in words, so that when we talk about the amount of space used by a data structure, we are referring to the number of words of memory used by the structure. All of our data structures store values of a generic type T, and we assume an element of type T occupies one word of memory.

<!-- block running-time · source jeffe · jeffe:0.6, from “Running Time” to the end of 0.6 -->

## Running Time

The most common way of ranking different algorithms for the same problem is by how quickly they run. Ideally, we want the fastest possible algorithm for any particular problem. In many application settings, it is acceptable for programs to run efficiently most of the time, on all “reasonable” inputs. Not in this book; we require algorithms that *always* run efficiently, even in the worst case.

But how do we measure running time? As a specific example, how long does it take to sing the song BottlesOfBeer(*n*)? This is obviously a function of the input value *n*, but it also depends on how quickly you can sing. Some singers might take ten seconds to sing a verse; others might take twenty. Technology widens the possibilities even further. Dictating the song over a telegraph using Morse code might take a full minute per verse. Downloading an mp3 over the Web might take a tenth of a second per verse. Duplicating the mp3 in a computer’s main memory might take only a few microseconds per verse.

What’s important here is how the singing time changes as *n* grows. Singing BottlesOfBeer(2*n*) requires about twice much time as singing BottlesOfBeer(*n*), no matter what technology is being used. This is reflected in the asymptotic singing time Θ(*n*).

We can measure time by counting how many times the algorithm executes a certain instruction or reaches a certain milestone in the “code”. For example, we might notice that the word “beer” is sung three times in every verse of BottlesOfBeer, so the number of times you sing “beer” is a good indication of the total singing time. For this question, we can give an exact answer: BottlesOfBeer(*n*) mentions beer exactly 3*n* + 3 times.

Incidentally, there are *lots* of songs with quadratic singing time. This one is probably familiar to most English-speakers:

```
NDaysOfChristmas(gifts[2 .. n]):
  for i ← 1 to n
      Sing “On the ith day of Christmas, my true love gave to me”
      for j ← i down to 2
          Sing “j gifts[j],”
      if i > 1
          Sing “and”
      Sing “a partridge in a pear tree.”
```

[sim-song-count]

The input to NDaysOfChristmas is a list of *n* − 1 gifts, represented here as an array. It’s quite easy to show that the singing time is Θ(*n*^2^); in particular, the singer mentions the name of a gift $\sum_{i=1}^{n} i = n(n+1)/2$ times (counting the partridge in the pear tree). It’s also easy to see that during the first *n* days of Christmas, my true love gave to me exactly $\sum_{i=1}^{n}\sum_{j=1}^{i} j = n(n+1)(n+2)/6 = \Theta(n^3)$ gifts.

Other quadratic-time songs include “Old MacDonald Had a Farm”, “There Was an Old Lady Who Swallowed a Fly”, “Hole in the Bottom of the Sea”, “Green Grow the Rushes O”, “The Rattlin’ Bog”, “The Court Of King Caractacus”,“The Barley-Mow”, “If I Were Not Upon the Stage”, “Star Trekkin’ ”,“Ist das nicht ein Schnitzelbank?”,[^22]“Il Pulcino Pio”, “Minkurinn í hænsnakofanum”, “Echad Mi Yodea”, and “Το κοκοράκι”. For more examples, consult your favorite preschooler.

```
Alouette(lapart[1 .. n]):
  Chantez « Alouette, gentille alouette, alouette, je te plumerai. »
  pour tout i de 1 à n
      Chantez « Je te plumerai lapart[i]. Je te plumerai lapart[i]. »
      pour tout j de i à 1 ⟨⟨à rebours⟩⟩
          Chantez « Et lapart[j] ! Et lapart[j] ! »
      Chantez « Alouette! Alouette! Aaaaaa. . . »
      Chantez « . . . alouette, gentille allouette, alouette, je te plumerai. »
```

[alouette-code]

A few songs have even more bizarre singing times. A fairly modern example is “The TELNET Song” by Guy Steele, which actually takes Θ(2^*n*^) time to sing the first *n* verses; Steele recommended *n* = 4. Finally, there are some songs that *never* end.[^23]

Except for “The TELNET Song”, all of these songs are most naturally expressed as a small set of nested loops, so their <s>running</s> singing times can be computed using nested summations. The running time of a *recursive* algorithm is more easily expressed as a recurrence. For example, the peasant multiplication algorithm can be expressed recursively as follows:

$$x\cdot y = \begin{cases} 0 & \text{if } x = 0\\ \lfloor x/2\rfloor\cdot(y+y) & \text{if } x \text{ is even}\\ \lfloor x/2\rfloor\cdot(y+y)+y & \text{if } x \text{ is odd} \end{cases}$$

Let *T*(*x*, *y*) denote the number of parity, addition, and mediation operations required to compute *x* · *y*. This function satisfies the recursive inequality *T*(*x*, *y*) ≤ *T*(⌊*x*/2⌋, 2*y*) + 2 with base case *T*(0, *y*) = 0. Techniques described in the next chapter imply the upper bound *T*(*x*, *y*) = *O*(log *x*).

Sometimes the running time of an algorithm depends on a particular implementation of some underlying data structure of subroutine. For example, the Huntington-Hill apportionment algorithm ApportionCongress runs in *O*(*N* + *RI* + (*R* − *n*)*E*) time, where *N* denotes the running time of NewPriorityQueue, *I* denotes the running time of Insert, and *E* denotes the running time of ExtractMax. Under the reasonable assumption that *R* ≥ 2*n* (on average, each state gets at least two representatives), we can simplify this bound to *O*(*N* + *R*(*I* + *E*)). The precise running time depends on the implementation of the underlying priority queue. The Census Bureau implements the priority queue as an unsorted array, which gives us *N* = *I* = Θ(1) and *E* = Θ(*n*), so the Census Bureau’s implementation of ApportionCongress runs in ***O*****(*****Rn*****)** ***time***. However, if we implement the priority queue as a binary heap or a heap-ordered array, we have *N* = Θ(1) and *I* = *E* = *O*(log *n*), so the overall algorithm runs in ***O*****(*****R*** **log*****n*****)** time.

Finally, sometimes we are interested in computational resources other than time, such as space, number of coin flips, number of cache or page faults, number of inter-process messages, or the number of gifts my true love gave to me. These resources can be analyzed using the same techniques used to analyze running time. For example, lattice multiplication of two *n*-digit numbers requires *O*(*n*^2^) space if we write down all the partial products before adding them, but only *O*(*n*) space if we add them on the fly.

<!-- block guarantees · source ods · ods:intro#correctness-time-complexity-and-space-complexity -->

## Correctness, Time Complexity, and Space Complexity

When studying the performance of a data structure, there are three things that matter most:

- **Correctness:** The data structure should correctly implement its interface.

- **Time complexity:** The running times of operations on the data structure should be as small as possible.

- **Space complexity:** The data structure should use as little memory as possible.

In this introductory text, we will take correctness as a given; we won’t consider data structures that give incorrect answers to queries or don’t perform updates properly. We will, however, see data structures that make an extra effort to keep space usage to a minimum. This won’t usually affect the (asymptotic) running times of operations, but can make the data structures a little slower in practice.

When studying running times in the context of data structures we tend to come across three different kinds of running time guarantees:

- **Worst-case running times:** These are the strongest kind of running time guarantees. If a data structure operation has a worst-case running time of $f(n)$, then one of these operations *never* takes longer than $f(n)$ time.

- **Amortized running times:** If we say that the amortized running time of an operation in a data structure is $f(n)$, then this means that the cost of a typical operation is at most $f(n)$. More precisely, if a data structure has an amortized running time of $f(n)$, then a sequence of $m$ operations takes at most $mf(n)$ time. Some individual operations may take more than $f(n)$ time but the average, over the entire sequence of operations, is at most $f(n)$.

- **Expected running times:** If we say that the expected running time of an operation on a data structure is $f(n)$, this means that the actual running time is a random variable (see Section 1.6) and the expected value of this random variable is at most $f(n)$. The randomization here is with respect to random choices made by the data structure.

To understand the difference between worst-case, amortized, and expected running times, it helps to consider a financial example. Consider the cost of buying a house:

**Worst-case versus amortized cost:** Suppose that a home costs $120 000. In order to buy this home, we might get a 120 month (10 year) mortgage with monthly payments of $1 200 per month. In this case, the worst-case monthly cost of paying this mortgage is $1 200 per month.

If we have enough cash on hand, we might choose to buy the house outright, with one payment of $120 000. In this case, over a period of 10 years, the amortized monthly cost of buying this house is

$$\text{\textdollar}120\,000 / 120\text{ months} = \text{\textdollar}1\,000\text{ per month} \enspace .$$

This is much less than the $1 200 per month we would have to pay if we took out a mortgage.

**Worst-case versus expected cost:** Next, consider the issue of fire insurance on our $120 000 home. By studying hundreds of thousands of cases, insurance companies have determined that the expected amount of fire damage caused to a home like ours is $10 per month. This is a very small number, since most homes never have fires, a few homes may have some small fires that cause a bit of smoke damage, and a tiny number of homes burn right to their foundations. Based on this information, the insurance company charges $15 per month for fire insurance.

Now it’s decision time. Should we pay the $15 worst-case monthly cost for fire insurance, or should we gamble and self-insure at an expected cost of $10 per month? Clearly, the $10 per month costs less *in expectation*, but we have to be able to accept the possibility that the *actual cost* may be much higher. In the unlikely event that the entire house burns down, the actual cost will be $120 000.

These financial examples also offer insight into why we sometimes settle for an amortized or expected running time over a worst-case running time. It is often possible to get a lower expected or amortized running time than a worst-case running time. At the very least, it is very often possible to get a much simpler data structure if one is willing to settle for amortized or expected running times.

## Footnotes

[^22]: Ja, das ist Otto von Schnitzelpusskrankengescheitmeyer!

[^23]: They just go on and on, my friend.
