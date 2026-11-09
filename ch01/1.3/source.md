# Asymptotic notation

<!-- block big-o · source ods · ods:intro#asymptotic-notation, up to (not including) “In a few cases, we will use asymptotic notation on functions with more than one variable” -->

## Asymptotic Notation

When analyzing data structures in this book, we want to talk about the running times of various operations. The exact running times will, of course, vary from computer to computer and even from run to run on an individual computer. When we talk about the running time of an operation we are referring to the number of computer instructions performed during the operation. Even for simple code, this quantity can be difficult to compute exactly. Therefore, instead of analyzing running times exactly, we will use the so-called *big-Oh notation*: For a function $f(n)$, $O(f(n))$ denotes a set of functions,

$$O(f(n)) = \left\{ \begin{array}{l} g(n):\mbox{there exists $c>0$, and $n_0$ such that} \\ \quad\mbox{$g(n) \le c\cdot f(n)$ for all $n\ge n_0$} \end{array} \right\} \enspace .$$

Thinking graphically, this set consists of the functions $g(n)$ where $c\cdot f(n)$ starts to dominate $g(n)$ when $n$ is sufficiently large.

We generally use asymptotic notation to simplify functions. For example, in place of $5n\log n + 8n - 200$ we can write $O(n\log n)$. This is proven as follows:

$$\begin{aligned} 5n\log n + 8n - 200 & \le 5n\log n + 8n \\ & \le 5n\log n + 8n\log n & \mbox{ for $n\ge 2$ (so that $\log n \ge 1$)} \\ & \le 13n\log n \enspace . \end{aligned}$$

This demonstrates that the function $f(n)=5n\log n + 8n - 200$ is in the set $O(n\log n)$ using the constants $c=13$ and $n_0 = 2$.

A number of useful shortcuts can be applied when using asymptotic notation. First:

$$O(n^{c_1}) \subset O(n^{c_2}) \enspace ,$$

for any $c_1 < c_2$. Second: For any constants $a,b,c > 0$,

$$O(a) \subset O(\log n) \subset O(n^{b}) \subset O({c}^n) \enspace .$$

These inclusion relations can be multiplied by any positive value, and they still hold. For example, multiplying by $n$ yields:

$$O(n) \subset O(n\log n) \subset O(n^{1+b}) \subset O(n{c}^n) \enspace .$$

Continuing in a long and distinguished tradition, we will abuse this notation by writing things like $f_1(n) = O(f(n))$ when what we really mean is $f_1(n) \in O(f(n))$. We will also make statements like “the running time of this operation is $O(f(n))$” when this statement should be “the running time of this operation is *a member of* $O(f(n))$.” These shortcuts are mainly to avoid awkward language and to make it easier to use asymptotic notation within strings of equations.

A particularly strange example of this occurs when we write statements like

$$T(n) = 2\log n + O(1) \enspace .$$

Again, this would be more correctly written as

$$T(n) \le 2\log n + [\mbox{some member of $O(1)$]} \enspace .$$

The expression $O(1)$ also brings up another issue. Since there is no variable in this expression, it may not be clear which variable is getting arbitrarily large. Without context, there is no way to tell. In the example above, since the only variable in the rest of the equation is $n$, we can assume that this should be read as $T(n) = 2\log n + O(f(n))$, where $f(n) = 1$.

Big-Oh notation is not new or unique to computer science. It was used by the number theorist Paul Bachmann as early as 1894, and is immensely useful for describing the running times of computer algorithms. Consider the following piece of code:

One execution of this method involves

- $1$ assignment ($int\, i\,\gets\, 0$),

- $n+1$ comparisons ($i < n$),

- $n$ increments ($i++$),

- $n$ array offset calculations ($a[i]$), and

- $n$ indirect assignments ($a[i]\gets i$).

So we could write this running time as

$$T(n)=a + b(n+1) + cn + dn + en \enspace ,$$

where $a$, $b$, $c$, $d$, and $e$ are constants that depend on the machine running the code and represent the time to perform assignments, comparisons, increment operations, array offset calculations, and indirect assignments, respectively. However, if this expression represents the running time of two lines of code, then clearly this kind of analysis will not be tractable to complicated code or algorithms. Using big-Oh notation, the running time can be simplified to

$$T(n)= O(n) \enspace .$$

Not only is this more compact, but it also gives nearly as much information. The fact that the running time depends on the constants $a$, $b$, $c$, $d$, and $e$ in the above example means that, in general, it will not be possible to compare two running times to know which is faster without knowing the values of these constants. Even if we make the effort to determine these constants (say, through timing tests), then our conclusion will only be valid for the machine we run our tests on.

Big-Oh notation allows us to reason at a much higher level, making it possible to analyze more complicated functions. If two algorithms have the same big-Oh running time, then we won’t know which is faster, and there may not be a clear winner. One may be faster on one machine, and the other may be faster on a different machine. However, if the two algorithms have demonstrably different big-Oh running times, then we can be certain that the one with the smaller running time will be faster *for large enough values of $n$*.

An example of how big-Oh notation allows us to compare two different functions is shown in Figure 1.5, which compares the rate of growth of $f_1(n)=15n$ versus $f_2(n)=2n\log n$. It might be that $f_1(n)$ is the running time of a complicated linear time algorithm while $f_2(n)$ is the running time of a considerably simpler algorithm based on the divide-and-conquer paradigm. This illustrates that, although $f_1(n)$ is greater than $f_2(n)$ for small values of $n$, the opposite is true for large values of $n$. Eventually $f_1(n)$ wins out, by an increasingly wide margin. Analysis using big-Oh notation told us that this would happen, since $O(n)\subset O(n\log n)$.

<!-- block omega-theta · source opendsa · opendsa:AlgAnal/AnalLower (Lower Bounds, Theta Notation, Classifying Functions) -->

## Lower Bounds and Θ Notation

### Lower Bounds

Big-Oh notation describes an upper bound. In other words, big-Oh notation states a claim about the greatest amount of some resource (usually time) that is required by an algorithm for some class of inputs of size $n$ (typically the worst such input, the average of all possible inputs, or the best such input).

Similar notation is used to describe the least amount of a resource that an algorithm needs for some class of input. Like big-Oh notation, this is a measure of the algorithm’s growth rate. Like big-Oh notation, it works for any resource, but we most often measure the least amount of time required. And again, like big-Oh notation, we are measuring the resource required for some particular class of inputs: the worst-, average-, or best-case input of size $n$.

The lower bound for an algorithm (or a problem, as explained later) is denoted by the symbol $\Omega$, pronounced “big-Omega” or just “Omega”. The following definition for $\Omega$ is symmetric with the definition of big-Oh.

> For $\mathbf{T}(n)$ a non-negatively valued function, $\mathbf{T}(n)$ is in set $\Omega(g(n))$ if there exist two positive constants $c$ and $n_0$ such that $\mathbf{T}(n) \geq c g(n)$ for all $n > n_0$.[^1]

**Example**

Assume $\mathbf{T}(n) = c_1 n^2 + c_2 n$ for $c_1$ and $c_2 > 0$. Then,

$$c_1 n^2 + c_2 n \geq c_1 n^2$$

for all $n > 1$. So, $\mathbf{T}(n) \geq c n^2$ for $c = c_1$ and $n_0 = 1$. Therefore, $\mathbf{T}(n)$ is in $\Omega(n^2)$ by the definition.

It is also true that the equation of the example above is in $\Omega(n)$. However, as with big-Oh notation, we wish to get the “tightest” (for $\Omega$ notation, the largest) bound possible. Thus, we prefer to say that this running time is in $\Omega(n^2)$.

Recall the sequential search algorithm to find a value $K$ within an array of integers. In the average and worst cases this algorithm is in $\Omega(n)$, because in both the average and worst cases we must examine *at least* $cn$ values (where $c$ is 1/2 in the average case and 1 in the worst case).

### Theta Notation

The definitions for big-Oh and $\Omega$ give us ways to describe the upper bound for an algorithm (if we can find an equation for the maximum cost of a particular class of inputs of size $n$) and the lower bound for an algorithm (if we can find an equation for the minimum cost for a particular class of inputs of size $n$). When the upper and lower bounds are the same within a constant factor, we indicate this by using $\Theta$ (big-Theta) notation. An algorithm is said to be $\Theta(h(n))$ if it is in $O(h(n))$ *and* it is in $\Omega(h(n))$. Note that we drop the word “in” for $\Theta$ notation, because there is a strict equality for two equations with the same $\Theta$. In other words, if $f(n)$ is $\Theta(g(n))$, then $g(n)$ is $\Theta(f(n))$.

Because the sequential search algorithm is both in $O(n)$ and in $\Omega(n)$ in the average case, we say it is $\Theta(n)$ in the average case.

Given an algebraic equation describing the time requirement for an algorithm, the upper and lower bounds always meet. That is because in some sense we have a perfect analysis for the algorithm, embodied by the running-time equation. For many algorithms (or their instantiations as programs), it is easy to come up with the equation that defines their runtime behavior. The analysis for most commonly used algorithms is well understood and we can almost always give a $\Theta$ analysis for them. However, the class of NP-Complete problems all have no definitive $\Theta$ analysis, just some unsatisfying big-Oh and $\Omega$ analyses. Even some “simple” programs are hard to analyze. Nobody currently knows the true upper or lower bounds for the following code fragment.

```java
while (n > 1)
  if (ODD(n))
    n = 3 * n + 1;
   else
     n = n / 2;
```

While some textbooks and programmers will casually say that an algorithm is “order of” or “big-Oh” of some cost function, it is generally better to use $\Theta$ notation rather than big-Oh notation whenever we have sufficient knowledge about an algorithm to be sure that the upper and lower bounds indeed match. OpenDSA modules use $\Theta$ notation in preference to big-Oh notation whenever our state of knowledge makes that possible. Limitations on our ability to analyze certain algorithms may require use of big-Oh or $\Omega$ notations. In rare occasions when the discussion is explicitly about the upper or lower bound of a problem or algorithm, the corresponding notation will be used in preference to $\Theta$ notation.

### Classifying Functions

Given functions $f(n)$ and $g(n)$ whose growth rates are expressed as algebraic equations, we might like to determine if one grows faster than the other. The best way to do this is to take the limit of the two functions as $n$ grows towards infinity,

$$\lim_{n \rightarrow \infty} \frac{f(n)}{g(n)}.$$

If the limit goes to $\infty$, then $f(n)$ is in $\Omega(g(n))$ because $f(n)$ grows faster. If the limit goes to zero, then $f(n)$ is in $O(g(n))$ because $g(n)$ grows faster. If the limit goes to some constant other than zero, then $f(n) = \Theta(g(n))$ because both grow at the same rate.

**Example**

If $f(n) = n^2$ and $g(n) = 2n\log n$, is $f(n)$ in $O(g(n))$, $\Omega(g(n))$, or $\Theta(g(n))$? Since

$$\frac{n^2}{2n\log n} = \frac{n}{2\log n},$$

we easily see that

$$\lim_{n \rightarrow \infty} \frac{n^2}{2n\log n} = \infty$$

because $n$ grows faster than $2\log n$. Thus, $n^2$ is in $\Omega(2n\log n)$.

[sim-limit-test]

<!-- block multivariate · source opendsa · opendsa:AlgAnal/AnalMultiple -->

## Multiple Parameters

Sometimes the proper analysis for an algorithm requires multiple parameters to describe the cost. To illustrate the concept, consider an algorithm to compute the rank ordering for counts of all pixel values in a picture. Pictures are often represented by a two-dimensional array, and a pixel is one cell in the array. The value of a pixel is either the code value for the color, or a value for the intensity of the picture at that pixel. Assume that each pixel can take any integer value in the range 0 to $C - 1$. The problem is to find the number of pixels of each color value and then sort the color values with respect to the number of times each value appears in the picture. Assume that the picture is a rectangle with $P$ pixels. A pseudocode algorithm to solve the problem follows.

```java
for (i=0; i<C; i++) {   // Initialize count
   count[i] = 0;
}
for (i=0; i<P; i++) {   // Look at all of the pixels
   count[value(i)]++; // Increment a pixel value count
}
sort(count);          // Sort pixel value counts
```

In this example, `count` is an array of size `C` that stores the number of pixels for each color value. Function `value(i)` returns the color value for pixel $i$.

The time for the first `for` loop (which initializes `count`) is based on the number of colors, $C$. The time for the second loop (which determines the number of pixels with each color) is $\Theta(P)$. The time for the final line, the call to `sort`, depends on the cost of the sorting algorithm used. We will assume that the sorting algorithm has cost $\Theta(P \log P)$ if $P$ items are sorted, thus yielding $\Theta(P \log P)$ as the total algorithm cost.

Is this a good representation for the cost of this algorithm? What is actually being sorted? It is not the pixels, but rather the colors. What if $C$ is much smaller than $P$? Then the estimate of $\Theta(P \log P)$ is pessimistic, because much fewer than $P$ items are being sorted. Instead, we should use $P$ as our analysis variable for steps that look at each pixel, and $C$ as our analysis variable for steps that look at colors. Then we get $\Theta(C)$ for the initialization loop, $\Theta(P)$ for the pixel count loop, and $\Theta(C \log C)$ for the sorting operation. This yields a total cost of $\Theta(P + C \log C)$.

Why can we not simply use the value of $C$ for input size and say that the cost of the algorithm is $\Theta(C \log C)$? Because, $C$ is typically much less than $P$. For example, a picture might have 1000 $\times$ 1000 pixels and a range of 256 possible colors. So, $P$ is one million, which is much larger than $C \log C$. But, if $P$ is smaller, or $C$ larger (even if it is still less than $P$), then $C \log C$ can become the larger quantity. Thus, neither variable should be ignored.

## Footnotes

[^1]: An alternate (non-equivalent) definition for $\Omega$ is

> $\mathbf{T}(n)$ is in the set $\Omega(g(n))$ if there exists a positive constant $c$ such that $\mathbf{T}(n) \geq c g(n)$ for an infinite number of values for $n$.

This definition says that for an “interesting” number of cases, the algorithm takes at least $c g(n)$ time. Note that this definition is *not* symmetric with the definition of big-Oh. For $g(n)$ to be a lower bound, this definition *does not* require that $\mathbf{T}(n) \geq c g(n)$ for all values of $n$ greater than some constant. It only requires that this happen often enough, in particular that it happen for an infinite number of values for $n$. Motivation for this alternate definition can be found in the following example.

Assume a particular algorithm has the following behavior:

$$\mathbf{T}(n) = \left\{ \begin{array}{ll}
n  & \mbox{for all odd}\ n \geq 1\\
n^2/100 & \mbox{for all even}\ n \geq 0
\end{array}
\right.$$

From this definition, $n^2/100 \geq \frac{1}{100} n^2$ for all even $n \geq 0$. So, $\mathbf{T}(n) \geq c n^2$ for an infinite number of values of $n$ (i.e., for all even $n$) for $c = 1/100$. Therefore, $\mathbf{T}(n)$ is in $\Omega(n^2)$ by the definition.

For this equation for $\mathbf{T}(n)$, it is true that all inputs of size $n$ take at least $cn$ time. But an infinite number of inputs of size $n$ take $cn^2$ time, so we would like to say that the algorithm is in $\Omega(n^2)$. Unfortunately, using our first definition will yield a lower bound of $\Omega(n)$ because it is not possible to pick constants $c$ and $n_0$ such that $\mathbf{T}(n) \geq c n^2$ for all $n>n_0$. The alternative definition does result in a lower bound of $\Omega(n^2)$ for this algorithm, which seems to fit common sense more closely. Fortunately, few real algorithms or computer programs display the pathological behavior of this example. Our first definition for $\Omega$ generally yields the expected result.

As you can see from this discussion, asymptotic bounds notation is not a law of nature. It is merely a powerful modeling tool used to describe the behavior of algorithms.
