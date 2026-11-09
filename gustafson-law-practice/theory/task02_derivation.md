# Task 02: Formal Derivation of Gustafson's Scaled Speedup

## 1. Introduction

Gustafson's Law explains how parallel computing performance improves when the workload increases with the number of processors.

Unlike Amdahl's Law, Gustafson's Law assumes that the parallel execution time remains constant while the problem size grows.

The goal is to derive:

\[
S(P) = s + pP
\]

and prove:

\[
S(P) = P - \alpha(P-1)
\]

## 2. Define the Variables

Let:

- \(P\) = number of processors
- \(s\) = serial execution time
- \(p\) = parallel execution time on \(P\) processors
- \(\alpha\) = serial fraction of the normalized parallel runtime
- \(S(P)\) = scaled speedup

We normalize the total execution time on \(P\) processors:

\[
T_P = s+p=1
\]

This means the serial and parallel phases together take one unit of time.

## 3. Equivalent Execution Time on One Processor

The serial portion of the program cannot be accelerated by additional processors.

Therefore, its execution time remains:

\[
T_{serial}=s
\]

The parallel portion takes \(p\) units of time when executed using \(P\) processors.

Assuming ideal parallel execution, the equivalent time required by one processor for the same workload is:

\[
T_{parallel,1}=Pp
\]

Therefore, the total equivalent single-processor execution time is:

\[
T_1=s+Pp
\]

## 4. Derivation of Scaled Speedup

Speedup is defined as the ratio between the equivalent single-processor runtime and the parallel runtime:

\[
S(P)=\frac{T_1}{T_P}
\]

Substitute the expressions:

\[
S(P)=\frac{s+Pp}{s+p}
\]

Since the parallel execution time is normalized:

\[
s+p=1
\]

We obtain:

\[
\boxed{S(P)=s+pP}
\]

This is the first form of Gustafson's Law.

## 5. Derivation Using the Serial Fraction

From the normalization condition:

\[
s+p=1
\]

Therefore:

\[
p=1-s
\]

Substitute into the speedup formula:

\[
S(P)=s+P(1-s)
\]

Expand the brackets:

\[
S(P)=s+P-Ps
\]

Rearrange:

\[
S(P)=P-s(P-1)
\]

Since the normalized serial fraction is:

\[
\alpha=\frac{s}{s+p}=s
\]

We obtain:

\[
\boxed{S(P)=P-\alpha(P-1)}
\]

This is Gustafson's scaled speedup formula.

## 6. Numerical Example

Suppose:

\[
P=8
\]

and:

\[
\alpha=0.05
\]

This means 5% of parallel execution time is serial.

Using Gustafson's Law:

\[
S(8)=8-0.05(8-1)
\]

\[
S(8)=8-0.35
\]

\[
\boxed{S(8)=7.65}
\]

The theoretical scaled speedup is 7.65.

Parallel efficiency is:

\[
E(P)=\frac{S(P)}{P}
\]

Therefore:

\[
E(8)=\frac{7.65}{8}
\]

\[
\boxed{E(8)=0.95625=95.625\%}
\]

## 7. Interpretation

The result demonstrates that a parallel system can achieve speedup close to the number of processors when the serial fraction is small.

Gustafson's Law assumes that the workload can grow with the number of processors while the total parallel execution time stays constant.

The formula describes an idealized scaling model. Real systems may experience additional communication, synchronization, and memory overhead.

## 8. Conclusion

Starting from the normalized parallel runtime:

\[
s+p=1
\]

We derived:

\[
\boxed{S(P)=s+pP}
\]

Then, by replacing the parallel fraction with \(1-\alpha\), we proved:

\[
\boxed{S(P)=P-\alpha(P-1)}
\]

Gustafson's Law shows that increasing the number of processors allows larger computational problems to be solved in approximately constant time, provided the workload scales efficiently.