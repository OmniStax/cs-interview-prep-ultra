# Logarithms, factorials and harmonic numbers

<!-- block logarithms · source ods · ods:intro#exponentials-and-logarithms -->

## Exponentials and Logarithms

The expression $b^x$ denotes the number $b$ raised to the power of $x$. If $x$ is a positive integer, then this is just the value of $b$ multiplied by itself $x-1$ times:

$$b^x = \underbrace{b\times b\times \cdots \times b}_{x} \enspace .$$

When $x$ is a negative integer, $b^{-x}=1/b^{x}$. When $x=0$, $b^x=1$. When $b$ is not an integer, we can still define exponentiation in terms of the exponential function $e^x$ (see below), which is itself defined in terms of the exponential series, but this is best left to a calculus text.

In this book, the expression $\log_b k$ denotes the *base-$b$ logarithm* of $k$. That is, the unique value $x$ that satisfies

$$b^{x} = k \enspace .$$

Most of the logarithms in this book are base 2 (*binary logarithms*). For these, we omit the base, so that $\log k$ is shorthand for $\log_2 k$.

An informal, but useful, way to think about logarithms is to think of $\log_b k$ as the number of times we have to divide $k$ by $b$ before the result is less than or equal to 1. For example, when one does binary search, each comparison reduces the number of possible answers by a factor of 2. This is repeated until there is at most one possible answer. Therefore, the number of comparison done by binary search when there are initially at most $n+1$ possible answers is at most $\lceil\log_2(n+1)\rceil$.

Another logarithm that comes up several times in this book is the *natural logarithm*. Here we use the notation $\ln k$ to denote $\log_e k$, where $e$ --- *Euler’s constant* --- is given by

$$e = \lim_{n\rightarrow\infty} \left(1+\frac{1}{n}\right)^n \approx 2.71828 \enspace .$$

The natural logarithm comes up frequently because it is the value of a particularly common integral:

$$\int_{1}^{k} 1/x\,\mathrm{d}x = \ln k \enspace .$$

Two of the most common manipulations we do with logarithms are removing them from an exponent:

$$b^{\log_b k} = k$$

and changing the base of a logarithm:

$$\log_b k = \frac{\log_a k}{\log_a b} \enspace .$$

For example, we can use these two manipulations to compare the natural and binary logarithms

$$\ln k = \frac{\log k}{\log e} = \frac{\log k}{(\ln e)/(\ln 2)} = (\ln 2)(\log k) \approx 0.693147\log k \enspace .$$

<!-- block factorials · source ods · ods:intro#sec:factorials -->

## Factorials

In one or two places in this book, the *factorial* function is used. For a non-negative integer $n$, the notation $n!$ (pronounced “$n$ factorial”) is defined to mean

$$n! = 1\cdot2\cdot3\cdot\cdots\cdot n \enspace .$$

Factorials appear because $n!$ counts the number of distinct permutations, i.e., orderings, of $n$ distinct elements. For the special case $n=0$, $0!$ is defined as 1.

The quantity $n!$ can be approximated using *Stirling’s Approximation*:

$$n! = \sqrt{2\pi n}\left(\frac{n}{e}\right)^{n}e^{\alpha(n)} \enspace ,$$

where

$$\frac{1}{12n+1} < \alpha(n) < \frac{1}{12n} \enspace .$$

Stirling’s Approximation also approximates $\ln(n!)$:

$$\ln(n!) = n\ln n - n + \frac{1}{2}\ln(2\pi n) + \alpha(n)$$

(In fact, Stirling’s Approximation is most easily proven by approximating $\ln(n!)=\ln 1 + \ln 2 + \cdots + \ln n$ by the integral $\int_1^n \ln n\,\mathrm{d}n = n\ln n - n +1$.)

Related to the factorial function are the *binomial coefficients*. For a non-negative integer $n$ and an integer $k\in\{0,\ldots,n\}$, the notation $\binom{n}{k}$ denotes:

$$\binom{n}{k} = \frac{n!}{k!(n-k)!} \enspace .$$

The binomial coefficient $\binom{n}{k}$ (pronounced “$n$ choose $k$”) counts the number of subsets of an $n$ element set that have size $k$, i.e., the number of ways of choosing $k$ distinct integers from the set $\{1,\ldots,n\}$.

<!-- block harmonic · source ods · ods:rbs#sec:rbst, the digression on harmonic numbers, from “Before we can present our main result” to the end of its figure -->

## Harmonic Numbers

Before we can present our main result about random binary search trees, we must take some time for a short digression to discuss a type of number that comes up frequently when studying randomized structures. For a non-negative integer, $k$, the $k$-th *harmonic number*, denoted $H_k$, is defined as

$$H_k = 1 + 1/2 + 1/3 + \cdots + 1/k \enspace .$$

The harmonic number $H_k$ has no simple closed form, but it is very closely related to the natural logarithm of $k$. In particular,

$$\ln k < H_k \le \ln k + 1 \enspace .$$

Readers who have studied calculus might notice that this is because the integral $\int_1^k\! (1/x)\, \mathrm{d}x = \ln k$. Keeping in mind that an integral can be interpreted as the area between a curve and the $x$-axis, the value of $H_k$ can be lower-bounded by the integral $\int_1^k\! (1/x)\, \mathrm{d}x$ and upper-bounded by $1+ \int_1^k\! (1/x)\, \mathrm{d}x$. (See Figure 7.2 for a graphical explanation.)

## Footnotes


