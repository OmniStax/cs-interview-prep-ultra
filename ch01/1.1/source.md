# What an algorithm is

<!-- block algorithm · source jeffe · jeffe:0.1 -->

## What is an algorithm?

An algorithm is an explicit, precise, unambiguous, mechanically-executable sequence of elementary instructions, usually intended to accomplish a specific purpose. For example, here is an algorithm for singing that annoying song “99 Bottles of Beer on the Wall”, for arbitrary values of 99:

```
BottlesOfBeer(n):
  For i ← n down to 1
      Sing “i bottles of beer on the wall, i bottles of beer,”
      Sing “Take one down, pass it around, i − 1 bottles of beer on the wall.”
  Sing “No bottles of beer on the wall, no bottles of beer,”
  Sing “Go to the store, buy some more, n bottles of beer on the wall.”
```

[bottles-code]

The word “algorithm” does *not* derive, as algorithmophobic classicists might guess, from the Greek roots *arithmos* (άριθμός), meaning “number”, and *algos* (ἄλγος), meaning “pain”. Rather, it is a corruption of the name of the 9th century Persian scholar Muḥammad ibn Mūsā al-Khwārizmī.[^1] Al-Khwārizmī is perhaps best known as the writer of the treatise *Al-Kitāb al-mukhtaṣar fīhīsāb al-ğabr* *wa’l-muqābala*,[^2] from which the modern word *algebra* derives. In a different treatise, al-Khwārizmī described the modern decimal system for writing and manipulating numbers—in particular, the use of a small circle or *ṣifr* to represent a missing quantity—which had been developed in India several centuries earlier. The methods described in this latter treatise, using either written figures or counting stones, became known in English as *algorism* or *augrym*, and its figures became known in English as *ciphers*.

Although both place-value notation and al-Khwārizmī’s works were already known by some European scholars, the “Hindu-Arabic” numeric system was popularized in Europe by the medieval Italian mathematician and tradesman Leonardo of Pisa, better known as Fibonacci. Thanks in part to his 1202 book *Liber Abaci*,[^3] written figures began to replace the counting table (then known as an *abacus*) and finger arithmetic[^4] as the preferred platform for calculation[^5] in Europe in the 13th century—*not* because written decimal figures were easier to learn or use, but because they provided an audit trail. Ciphers became common in Western Europe only with the advent of movable type, and truly ubiquitous only after cheap paper became plentiful in the early 19th century.

Eventually the word *algorism* evolved into the modern *algorithm*, via folk etymology from the Greek *arithmos* (and perhaps the previously mentioned *algos*).[^6] Thus, until very recently, the word *algorithm* referred exclusively to mechanical techniques for place-value arithmetic using “Arabic” numerals. People trained in the fast and reliable execution of these procedures were called *algorists* or *computators*, or more simply, *computers*.

<!-- block lattice · source jeffe · jeffe:0.2, the preamble and “Lattice Multiplication” -->

## Lattice Multiplication

Although they have been a topic of formal academic study for only a few decades, algorithms have been with us since the dawn of civilization. Descriptions of step-by-step arithmetic computation are among the earliest examples of written human language, long predating the expositions by Fibonacci and al-Khwārizmī, or even the place-value notation they popularized.

The most familiar method for multiplying large numbers, at least for American students, is the ***lattice algorithm***. This algorithm was popularized by Fibonacci in *Liber Abaci*, who learned it from Arabic sources including al-Khwārizmī, who in turn learned it from Indian sources including Brahmagupta’s 7th-century treatise *Brāhmasphuṭasiddhānta*, who may have learned it from Chinese sources. The oldest surviving descriptions of the algorithm appear in *The Mathematical* *Classic of Sunzi*, written in China between the 3rd and 5th centuries, and in Eutocius of Ascalon’s commentaries on Archimedes’ *Measurement of the Circle*, written around 500ce, but there is evidence that the algorithm was known much earlier. Eutocius credits the method to a lost treatise of Apollonius of Perga, who lived around 300bce, entitled *Okytokion* (᾿Ωκυτόκιον).[^7] The Sumerians recorded multiplication tables on clay tablets as early as 2600bce, suggesting that they may have used the lattice algorithm.[^8]

The lattice algorithm assumes that the input numbers are represented as explicit strings of digits; I’ll assume here that we’re working in base ten, but the algorithm generalizes immediately to any other base. To simplify notation,[^9] the input consists of a pair of arrays *X*[0.. *m*− 1] and *Y*[0.. *n*− 1], representing the numbers

$$x = \sum_{i=0}^{m-1} X[i]\cdot 10^i \quad\text{and}\quad y = \sum_{j=0}^{n-1} Y[j]\cdot 10^j,$$

and similarly, the output consists of a single array *Z*[0.. *m*+ *n*−1], representing the product

$$z = x\cdot y = \sum_{k=0}^{m+n-1} Z[k]\cdot 10^k.$$

The algorithm uses addition and *single-digit* multiplication as primitive operations. Addition can be performed using a simple for-loop. In practice, single-digit multiplication is performed using a lookup table, either carved into clay tablets, painted on strips of wood or bamboo, written on paper, stored in read-only memory, or memorized by the computator. The entire lattice algorithm can be summarized by the formula

$$x\cdot y = \sum_{i=0}^{m-1}\sum_{j=0}^{n-1}\bigl(X[i]\cdot Y[j]\cdot 10^{i+j}\bigr).$$

Different variants of the lattice algorithm evaluate the partial products *X*[*i*] · *Y*[*j*] · 10^*i*^^+^^*j*^ in different orders and use different strategies for computing their sum. For example, in *Liber Abaco*, Fibonacci describes a variant that considers the *mn* partial products in increasing order of significance, as shown in modern pseudocode below.

```
FibonacciMultiply(X[0.. m − 1], Y[0.. n − 1]):
  hold ← 0
  for k ← 0 to n + m − 1
      for all i and j such that i + j = k
          hold ← hold + X[i] · Y[j]
      Z[k] ← hold mod 10
      hold ← ⌊hold/10⌋
  return Z[0.. m + n − 1]
```

[sim-lattice]

Fibonacci’s algorithm is often executed by storing all the partial products in a two-dimensional table (often called a “tableau” or “grate” or “lattice”) and then summing along the diagonals with appropriate carries, as shown on the right in Figure 0.1. American elementary-school students are taught to multiply one factor (the “multiplicand”) by each digit in the other factor (the “multiplier”), writing down all the multiplicand-by-digit products before adding them up, as shown on the left in Figure 0.1. This was also the method described by Eutocius, although he fittingly considered the multiplier digits from left to right, as shown in Figure 0.2. Both of these variants (and several others) are described and illustrated side by side in the anonymous 1458 textbook *L’Arte dell’Abbaco*, also known as the *Treviso Arithmetic*, the first *printed* mathematics book in the West.

All of these variants of the lattice algorithm—and other similar variants described by Sunzi, al-Khwārizmī, Fibonacci, *L’Arte dell’Abbaco*, and many other sources—compute the product of any *m*-digit number and any *n*-digit number in ***O*****(*****mn*****)** ***time***; the running time of every variant is dominated by the number of single-digit multiplications.

<!-- block peasant · source jeffe · jeffe:0.2, “Duplation and Mediation” -->

## Duplation and Mediation

The lattice algorithm is not the oldest multiplication algorithm for which we have direct recorded evidence. An even older and arguably simpler algorithm, which does not rely on place-value notation, is sometimes called *Russian peasant* *multiplication*, *Ethiopian peasant multiplication*, or just ***peasant multiplication***. A variant of this algorithm was copied into the Rhind papyrus by the Egyptian scribe Ahmes around 1650bce, from a document he claimed was (then) about 350 years old.[^10] This algorithm was still taught in elementary schools in Eastern Europe in the late 20th century; it was also commonly used by early digital computers that did not implement integer multiplication directly in hardware.

The peasant multiplication algorithm reduces the difficult task of multiplying arbitrary numbers to a sequence of four simpler operations: (1) determining parity (even or odd), (2) addition, (3) ***duplation*** (doubling a number), and (4) ***mediation*** (halving a number, rounding down).

The correctness of this algorithm follows by induction from the following recursive identity, which holds for all non-negative integers *x* and *y* :

$$x\cdot y = \begin{cases} 0 & \text{if } x = 0\\ \lfloor x/2\rfloor\cdot(y+y) & \text{if } x \text{ is even}\\ \lfloor x/2\rfloor\cdot(y+y)+y & \text{if } x \text{ is odd} \end{cases}$$

Arguably, this recurrence *is* the peasant multiplication algorithm. Don’t let the iterative pseudocode fool you; the algorithm is fundamentally recursive!

As stated, PeasantMultiply performs *O*(log *x*) parity, addition, and mediation operations, but we can improve this bound to *O*(log min{*x*, *y*}) by swapping the two arguments when *x > y* . Assuming the numbers are represented using any reasonable place-value notation (like binary, decimal, Babylonian hexagesimal, Egyptian duodecimal, Roman numeral, Chinese counting rods, bead positions on an abacus, and so on), each operation requires at most *O*(log(*xy*)) = *O*(log max{*x*, *y*}) single-digit operations, so the overall running time of the algorithm is *O*(log min{*x*, *y*} · log max{*x*, *y*}) = *O*(log *x* · log *y*).

In other words, this algorithm requires ***O*****(*****mn*****)** ***time*** to multiply an *m*-digit number by an *n*-digit number; up to constant factors, this is the same running time as the lattice algorithm. This algorithm requires (a constant factor!) more paperwork to execute by hand than the lattice algorithm, but the necessary primitive operations are arguably easier for humans to perform. In fact, the two algorithms are equivalent when numbers are represented in binary.

<!-- block compass · source jeffe · jeffe:0.2, “Compass and Straightedge” -->

## Compass and Straightedge

Classical Greek geometers identified numbers (or more accurately, *magnitudes*) with line segments of the appropriate length, which they manipulated using two simple mechanical tools—the compass and the straightedge—versions of which had already been in common use by surveyors, architects, and other artisans for centuries. Using *only* these two tools, these scholars reduced several complex geometric constructions to the following primitive operations, starting with one or more identified reference points.

- Draw the unique line passing through two distinct identified points.

- Draw the unique circle centered at one identified point and passing through

another.

- Identify the intersection point (if any) of two lines.

- Identify the intersection points (if any) of a line and a circle.

- Identify the intersection points (if any) of two circles.

In practice, Greek geometry students almost certainly drew their constructions on an *abax* (ἄβαξ), a table covered in dust or sand.[^11] Centuries earlier, Egyptian surveyors carried out many of the same constructions using ropes to determine straight lines and circles on the ground.[^12] However, Euclid and other Greek geometers presented compass and straightedge constructions as precise mathematical *abstractions*—points are *ideal* points; lines are *ideal* lines; and circles are *ideal* circles.

Figure 0.4 shows an algorithm, described in Euclid’s *Elements* about 2500 years ago, for multiplying or dividing two magnitudes. The input consists of four distinct points *A*, *B*, *C* , and *D*, and the goal is to construct a point *Z* such that |*AZ*| = |*AC*||*AD*|*/*|*AB*|. In particular, if we define |*AB*| to be our unit of length, then the algorithm computes the product of |*AC*| and |*AD*|.

Notice that Euclid first defines a new primitive operation RightAngle by (as modern programmers would phrase it) writing a subroutine. The correctness of the algorithm follows from the observation that triangles *ACE* and *AZF* are similar. The second and third lines of the main algorithm are ambiguous, because *α* intersects any circle centered at *A* at *two* distinct points, but the algorithm is actually correct no matter which intersection points are chosen for *E* and *F* .

Euclid’s algorithm reduces the problem of multiplying two magnitudes (lengths) to a series of primitive compass-and-straightedge operations. These operations are difficult to implement precisely on a modern digital computer, but Euclid’s algorithm wasn’t *designed* for a digital computer. It was designed for the Platonic Ideal Geometer, wielding the Platonic Ideal Compass and the Platonic Ideal Straightedge, who could execute each operation perfectly in constant time *by definition*. In this model of computation, MultiplyOrDivide runs in *O*(1) time!

<!-- block apportionment · source jeffe · jeffe:0.3 -->

## Congressional Apportionment

Here is another real-world example of an algorithm of significant political importance. Article I, Section 2 of the United States Constitution requires that

> Representatives and direct Taxes shall be apportioned among the several States which may be included within this Union, according to their respective Numbers. . . . The Number of Representatives shall not exceed one for every thirty Thousand, but each State shall have at Least one Representative. . . .

Because there are only a finite number of seats in the House of Representatives, *exact* proportional representation requires either shared or fractional representatives, neither of which are legal. As a result, over the next several decades, many different apportionment algorithms were proposed and used to round the ideal fractional solution fairly. The algorithm actually used today, called the ***Huntington-Hill method*** or the ***method of equal proportions***, was first suggested by Census Bureau statistician Joseph Hill in 1911, refined by Harvard mathematician Edward Huntington in 1920, adopted into Federal law (2 U.S.C. §2a) in 1941, and survived a Supreme Court challenge in 1992.[^13]

The Huntington-Hill method allocates representatives to states one at a time. First, in a preprocessing stage, each state is allocated one representative. Then in each iteration of the main loop, the next representative is assigned to the state with the highest *priority*. The priority of each state is defined to be $P/\sqrt{r(r+1)}$, where *P* is the state’s population and *r* is the number of representatives already allocated to that state.

The algorithm is described in pseudocode in Figure 0.5. The input consists of an array *Pop*[1.. *n*] storing the populations of the *n* states and an integer *R* equal to the total number of representatives; the algorithm assumes *R* ≥ *n*. (Currently, in the United States, *n* = 50 and *R* = 435.) The output array *Rep*[1.. *n*] records the number of representatives allocated to each state.

This implementation of Huntington-Hill uses a priority queue that supports the operations NewPriorityQueue, Insert, and ExtractMax. (The actual law doesn’t say anything about priority queues, of course.) The output of the algorithm, and therefore its correctness, does not depend *at all* on how this priority queue is implemented. The Census Bureau uses a sorted array, stored in a single column of an Excel spreadsheet, which is recalculated from scratch at every iteration. You (should have) learned a more efficient implementation in your undergraduate data structures class.

Similar apportionment algorithms are used in multi-party parliamentary elections around the world, where the number of seats allocated to each party is supposed to be proportional to the number of votes that party receives. The two most common are the *D’Hondt method*[^14] and the *Webster–Sainte-Laguë* *method*,[^15] which respectively use priorities *P/*(*r* + 1) and *P/*(2*r* + 1) in place of the square-root expression in Huntington-Hill. The Huntington-Hill method is essentially unique to the United States House of Representatives, thanks in part to the constitutional requirement that each state must be allocated at least one representative.

<!-- block underspecified · source jeffe · jeffe:0.4 -->

## A Bad Example

As a prototypical example of a sequence of instructions that is *not* actually an algorithm, consider "Martin’s algorithm”:[^16]

```
BeAMillionaireAndNeverPayTaxes():
  Get a million dollars.
  If the tax man comes to your door and says, “You have never paid taxes!”
      Say “I forgot.”
```

Pretty simple, except for that first step; it’s a doozy! A group of billionaire CEOs, Silicon Valley venture capitalists, or New York City real-estate hustlers might consider this an algorithm, because for them the first step is both unambiguous and trivial,[^17] but for the rest of us poor slobs, Martin’s procedure is too vague to be considered an actual algorithm. On the other hand, this is a perfect example of a ***reduction***—it *reduces* the problem of being a millionaire and never paying taxes to the “easier” problem of acquiring a million dollars. We’ll see reductions over and over again in this book. As hundreds of businessmen and politicians have demonstrated, if you know how to solve the easier problem, a reduction tells you how to solve the harder one.

Martin’s algorithm, like some of our previous examples, is not the kind of algorithm that computer scientists are used to thinking about, because it is phrased in terms of operations that are difficult for computers to perform. This book focuses (almost!) exclusively on algorithms that can be reasonably implemented on a standard digital computer. Each step in these algorithms is either directly supported by common programming languages (such as arithmetic, assignments, loops, or recursion) or something that you’ve already learned how to do (like sorting, binary search, tree traversal, or singing “*n* Bottles of Beer on the Wall”).

<!-- block describing · source jeffe · jeffe:0.5 -->

## Describing Algorithms

The skills required to effectively *design and analyze* algorithms are entangled with the skills required to effectively *describe* algorithms. At least in my classes, a complete description of any algorithm has four components:

- **What:** A precise specification of the problem that the algorithm solves.

- **How:** A precise description of the algorithm itself.

- **Why:** A proof that the algorithm solves the problem it is supposed to solve.

- **How fast:** An analysis of the running time of the algorithm.

It is not necessary (or even advisable) to *develop* these four components in this particular order. Problem specifications, algorithm descriptions, correctness proofs, and time analyses usually evolve simultaneously, with the development of each component informing the development of the others. For example, we may need to tweak the problem description to support a faster algorithm, or modify the algorithm to handle a tricky case in the proof of correctness. Nevertheless, *presenting* these components separately is usually clearest for the reader.

As with any writing, it’s important to aim your descriptions at the right audience; I recommend writing for a competent but skeptical programmer *who* *is not as clever as you are*. Think of yourself six months ago. As you develop any new algorithm, you will naturally build up lots of intuition about the problem and about how your algorithm solves it, and your informal reasoning will be guided by that intuition. But anyone *reading* your algorithm later, or the code you derive from it, won’t share your intuition or experience. Neither will your compiler. Neither will you six months from now. All they will have is your written description.

Even if you never have to explain your algorithms to anyone else, it’s still important to develop them with an audience in mind. Trying to communicate clearly forces you to *think* more clearly. In particular, writing for a *novice* audience, who will interpret your words *exactly* as written, forces you to work through fine details, no matter how “obvious” or “intuitive” your high-level ideas may seem at the moment. Similarly, writing for a *skeptical* audience forces you to develop robust arguments for correctness and efficiency, instead of trusting your intuition or your intelligence.[^18]

I cannot emphasize this point enough: **Your primary job as an algorithm** **designer is** ***teaching other people*** **how and why your algorithms work.** If you can’t communicate your ideas to other human beings, they may as well not exist. Producing correct and efficient executable code is an important but secondary goal. Convincing yourself, your professors, your (prospective) employers, your colleagues, or your students that you are smart is at best a distant third.

### Specifying the Problem

Before we can even start developing a new algorithm, we have to agree on what problem our algorithm is supposed to solve. Similarly, before we can even start *describing* an algorithm, we have to *describe* the problem that the algorithm is supposed to solve.

Algorithmic problems are often presented using standard English, in terms of real-world objects. It’s up to us, the algorithm designers, to restate these problems in terms of formal, abstract, *mathematical* objects—numbers, arrays, lists, graphs, trees, and so on—that we can reason about formally. We must also determine if the problem statement carries any hidden assumptions, and state those assumptions explicitly. (For example, in the song “*n* Bottles of Beer on the Wall”, *n* is always a non-negative integer.[^19])

We may need to refine our specification as we develop the algorithm. For example, our algorithm may require a particular input representation, or produce a particular output representation, that was left unspecified in the original informal problem description. Or our algorithm might actually solve a *more general* problem than we were originally asked to solve. (This is a common feature of recursive algorithms.)

The specification should include just enough detail that someone else could *use* our algorithm as a black box, without knowing how or why the algorithm actually works. In particular, we must describe the type *and meaning* of each input parameter, and exactly how the eventual output depends on the input parameters. On the other hand, our specification should *deliberately hide* any details that are *not* necessary to use the algorithm as a black box. Let that which does not matter truly slide.

For example, the lattice and duplation-and-mediation algorithms both solve the same problem: Given two non-negative integers *x* and *y* , each represented as an array of digits, compute the product *x* · *y* , also represented as an array of digits. To someone *using* these algorithms, the choice of algorithm is completely irrelevant. On the other hand, the Greek straightedge-and-compass algorithm solves a *different problem*, because the input and output values are represented by line segments instead of arrays of digits.

### Describing the Algorithm

Computer programs are concrete representations of algorithms, but algorithms are *not* programs. Rather, algorithms are abstract mechanical procedures that can be implemented in *any* programming language that supports the underlying primitive operations. The idiosyncratic syntactic details of your favorite programming language are utterly irrelevant; focusing on these will only distract you (and your readers) from what’s *really* going on.[^20] A good algorithm description is closer to what we should write in the *comments* of a real program than the code itself. Code is a poor medium for storytelling.

On the other hand, a plain English prose description is usually not a good idea either. Algorithms have lots of idiomatic structure—especially conditionals, loops, function calls, and recursion—that are far too easily hidden by unstructured prose. Colloquial English is full of ambiguities and shades of meaning, but algorithms must be described as unambiguously as possible. Prose is a poor medium for precision.

In my opinion, the clearest way to present an algorithm is using a combination of *pseudo*code and structured English. Pseudocode uses the *structure* of formal programming languages and mathematics to break algorithms into primitive steps; the primitive steps themselves can be written using mathematical notation, pure English, or an appropriate mixture of the two, *whatever is clearest*. Well-written pseudocode reveals the internal structure of the algorithm but hides irrelevant implementation details, making the algorithm easier to understand, analyze, debug, and implement.

Whenever we describe an algorithm, our description should include every detail necessary to fully specify the algorithm, prove its correctness, and analyze its running time. At the same time, it should *exclude* any details that are *not* necessary to fully specify the algorithm, prove its correctness, and analyze its running time. (Slide.) At a more practical level, our description should allow a competent but skeptical programmer *who has not read this book* to quickly and correctly implement the algorithm in *their* favorite programming language, *without understanding why it works*.

I don’t want to bore you with the rules I follow for writing pseudocode, but I must caution against one especially pernicious habit. ***Never*** describe repeated operations informally, as in “Do [this] first, then do [that] second, ***and so on***.” or “Repeat ***this process*** until [something]”. As anyone who has taken one of those frustrating “What comes next in this sequence?” tests already knows, describing the first few steps of an algorithm says little or nothing about what happens in later steps. If your algorithm has a loop, write it as a loop, and explicitly describe what happens in an *arbitrary* iteration. Similarly, if your algorithm is recursive, write it recursively, and explicitly describe the case boundaries and what happens in each case.

<!-- block correctness · source jeffe · jeffe:0.6, from its opening to the end of “Correctness” -->

## Analyzing Algorithms

It’s not enough just to write down an algorithm and say “Behold!” We must also convince our audience (and ourselves!) that the algorithm actually does what it’s supposed to do, and that it does so efficiently.

### Correctness

In some application settings, it is acceptable for programs to behave correctly most of the time, on all “reasonable” inputs. Not in this book; we require algorithms that are *always* correct, for *all possible* inputs. Moreover, we must *prove* that our algorithms are correct; trusting our instincts, or trying a few test cases, isn’t good enough. Sometimes correctness is truly obvious, especially for algorithms you’ve seen in earlier courses. On the other hand, “obvious” is all too often a synonym for “wrong”. Most of the algorithms we discuss in this course require real work to prove correct. In particular, correctness proofs usually involve induction. We *like* induction. Induction is our *friend*.[^21]

Of course, before we can formally prove that our algorithm does what it’s supposed to do, we have to formally describe what it’s supposed to do!

<!-- block efficiency · source ods · ods:intro#the-need-for-efficiency, to the end of “The solution”, before “The remainder of this chapter” -->

## The Need for Efficiency

In the next section, we look at the operations supported by the most commonly used data structures. Anyone with a bit of programming experience will see that these operations are not hard to implement correctly. We can store the data in an array or a linked list and each operation can be implemented by iterating over all the elements of the array or list and possibly adding or removing an element.

This kind of implementation is easy, but not very efficient. Does this really matter? Computers are becoming faster and faster. Maybe the obvious implementation is good enough. Let’s do some rough calculations to find out.

**Number of operations:** Imagine an application with a moderately-sized data set, say of one million ($10^6$), items. It is reasonable, in most applications, to assume that the application will want to look up each item at least once. This means we can expect to do at least one million ($10^6$) searches in this data. If each of these $10^6$ searches inspects each of the $10^6$ items, this gives a total of $10^6\times 10^6=10^{12}$ (one thousand billion) inspections.

**Processor speeds:** At the time of writing, even a very fast desktop computer can not do more than one billion ($10^9$) operations per second.[^ods] This means that this application will take at least $10^{12}/10^9 = 1000$ seconds, or roughly 16 minutes and 40 seconds. Sixteen minutes is an eon in computer time, but a person might be willing to put up with it (if he or she were headed out for a coffee break).

**Bigger data sets:** Now consider a company like Google, that indexes over 8.5 billion web pages. By our calculations, doing any kind of query over this data would take at least 8.5 seconds. We already know that this isn’t the case; web searches complete in much less than 8.5 seconds, and they do much more complicated queries than just asking if a particular page is in their list of indexed pages. At the time of writing, Google receives approximately $4,500$ queries per second, meaning that they would require at least $4,500\times 8.5=38,250$ very fast servers just to keep up.

**The solution:** These examples tell us that the obvious implementations of data structures do not scale well when the number of items, $n$, in the data structure and the number of operations, $m$, performed on the data structure are both large. In these cases, the time (measured in, say, machine instructions) is roughly $n\times m$.

The solution, of course, is to carefully organize data within the data structure so that not every operation requires every data item to be inspected. Although it sounds impossible at first, we will see data structures where a search requires looking at only two items on average, independent of the number of items stored in the data structure. In our billion instruction per second computer it takes only $0.000000002$ seconds to search in a data structure containing a billion items (or a trillion, or a quadrillion, or even a quintillion items).

We will also see implementations of data structures that keep the items in sorted order, where the number of items inspected during an operation grows very slowly as a function of the number of items in the data structure. For example, we can maintain a sorted set of one billion items while inspecting at most 60 items during any operation. In our billion instruction per second computer, these operations take $0.00000006$ seconds each.

<!-- block interfaces · source ods · ods:intro#sec:interfaces, its opening, before “The Queue, Stack, and Deque Interfaces” -->

## Interfaces

When discussing data structures, it is important to understand the difference between a data structure’s interface and its implementation. An interface describes what a data structure does, while an implementation describes how the data structure does it.

An *interface*, sometimes also called an *abstract data type*, defines the set of operations supported by a data structure and the semantics, or meaning, of those operations. An interface tells us nothing about how the data structure implements these operations; it only provides a list of supported operations along with specifications about what types of arguments each operation accepts and the value returned by each operation.

A data structure *implementation*, on the other hand, includes the internal representation of the data structure as well as the definitions of the algorithms that implement the operations supported by the data structure. Thus, there can be many implementations of a single interface. For example, in Section 2.2, we will see implementations of the List interface using arrays and in Sections 2.5–2.6 we will see implementations of the List interface using pointer-based data structures. Each implements the same interface, List, but in different ways.

## Footnotes

[^1]: “Mohammad, father of Adbdulla, son of Moses, the Kwārizmian”. Kwārizm is an ancient city, now called Khiva, in the Khorezm Province of Uzbekistan.

[^2]: “The Compendious Book on Calculation by Completion and Balancing”

[^3]: While it is tempting to translate the title *Liber Abaci* as “The Book of the Abacus”, a more accurate translation is “The Book of Calculation”. Both before and after Fibonacci, the Italian word *abaco* was used to describe anything related to numerical calculation—devices, methods, schools, books, and so on—much in the same way that “computer science” is used today in English, or as the Chinese phrase for “operations research” translates literally as “the study of using counting rods”.

[^4]: ☞ Reckoning with *digits*! ☞

[^5]: The word *calculate* derives from the Latin word *calculus*, meaning “small rock”, referring to the stones on a counting table, or as Chaucer called them, *augrym stones*. In 440bce, Herodotus wrote in his *Histories* that “The Greeks write and calculate (λογίζεσθαι ψήφοις, literally ‘reckon with pebbles’) from left to right; the Egyptians do the opposite. Yet they say that their way of writing is toward the right, and the Greek way toward the left.” (Herodotus is strangely silent on which end of the egg the Egyptians ate first.)

[^6]: Some medieval sources claim that the Greek prefix “algo-” means “art” or “introduction”. Others claim that algorithms were invented by a Greek philosopher, or a king of India, or perhaps a king of Spain, named “Algus” or “Algor” or “Argus”. A few, possibly including Dante Alighieri, even identified the inventor with the mythological Greek shipbuilder and eponymous argonaut. It’s unclear whether any of these risible claims were intended to be historically accurate, or merely mnemonic.

[^7]: Literally “medicine that promotes quick and easy childbirth”! Pappus of Alexandria reproduced several excerpts of *Okytokion* about 200 years before Eutocius, but his description of the lattice multiplication algorithm (if he gave one) is *also* lost.

[^8]: There is ample evidence that ancient Sumerians calculated accurately with extremely large numbers using their base-60 place-value numerical system, but I am not aware of any surviving record of the actual methods they used. In addition to standard multiplication and reciprocal tables, tables listing the squares of integers from 1 to 59 have been found, leading some math historians to conjecture that Babylonians multiplied using an identity like *xy* = ((*x* + *y*)^2^ − *x*^2^ − *y*^2^)*/*2. But this trick only works when *x* + *y <* 60; history is silent on how the Babylonians might have computed *x*^2^ when *x* ≥ 60.

[^9]: but at the risk of inflaming the historical enmity between Greece and Egypt, or Lilliput and Blefuscu, or Macs and PCs, or people who think zero is a natural number and people who are wrong

[^10]: The version of this algorithm actually used in ancient Egypt does not use mediation or parity, but it does use comparisons. To avoid halving, the algorithm pre-computes two tables by repeated doubling: one containing all the powers of 2 not exceeding *x* , the other containing the same powers of 2 multiplied by *y* . The powers of 2 that sum to *x* are then found by greedy subtraction, and the corresponding entries in the other table are added together to form the product.

[^11]: The written numerals 1 through 9 were known in Europe at least two centuries before Fibonacci’s *Liber Abaci* as “gobar numerals”, from the Arabic word *ghubār* meaning dust, ultimately referring to the Indian practice of performing arithmetic on tables covered with sand. The Greek word ἄβαξ is the origin of the Latin *abacus*, which also originally referred to a sand table.

[^12]: Remember what “geometry” means? Democritus would later refer to these Egyptian surveyors, somewhat derisively, as *arpedonaptai* (ἀρπεδονάπται), meaning “rope-fasteners”.

[^13]: Overruling an earlier ruling by a federal district court, the Supreme Court unanimously held that ***any*** apportionment method adopted in good faith by Congress is constitutional (*United* *States Department of Commerce v. Montana*). The current congressional apportionment algorithm is described in gruesome detail at the U.S. Census Department web site http://www.census.gov/topics/public-sector/congressional-apportionment.html. A good history of the apportionment problem can be found at http://www.thirty-thousand.org/pages/Apportionment.htm. A report by the Congressional Research Service describing various apportionment methods is available at http://www.fas.org/sgp/crs/misc/R41382.pdf.

[^14]: developed by Thomas Jefferson in 1792, used for U.S. Congressional apportionment from 1792 to 1832, rediscovered by Belgian mathematician Victor D’Hondt in 1878, and refined by Swiss physicist Eduard Hagenbach-Bischoff in 1888.

[^15]: developed by Daniel Webster in 1832, used for U.S. Congressional apportionment from 1842 to 1911, rediscovered by French mathematician André Sainte-Laguë in 1910, and rediscovered again by German physicist Hans Schepers in 1980.

[^16]: Steve Martin, “You Can Be A Millionaire”, *Saturday Night Live*, January 21, 1978. Also appears on *Comedy Is Not Pretty*, Warner Bros. Records, 1979.

[^17]: Something something secure quantum blockchain deep-learning something.

[^18]: In particular, I assume that *you* are a skeptical novice!

[^19]: I’ve never heard anyone sing “√2 Bottles of Beer on the Wall.” Occasionally I *have* heard set theorists singing “ℵ~0~ bottles of beer on the wall”, but for some reason they always gave up before the song was over.

[^20]: This is, of course, a matter of religious conviction. Armchair linguists argue incessantly over the *Sapir-Whorf hypothesis*, which states (more or less) that people think only in the categories imposed by their languages. According to an extreme formulation of this principle, some concepts in one language simply cannot be understood by speakers of other languages, not just because of technological advancement—How would you translate “jump the shark” or “Fortnite streamer” into Aramaic?—but because of inherent structural differences between languages and cultures. For a more skeptical view, see Steven Pinker’s *The Language Instinct*. There is admittedly some strength to this idea when applied to different programming paradigms. (What’s the Y combinator, again? How do templates work? What’s an Abstract Factory?) Fortunately, those differences are too subtle to have any impact on the material in *this* book. For a compelling counterexample, see Chris Okasaki’s monograph *Functional Data Structures* and its more recent descendants.

[^21]: If induction is *not* your friend, you will have a hard time with this book.

[^ods]: Computer speeds are at most a few gigahertz (billions of cycles per second), and each operation typically takes a few cycles.
