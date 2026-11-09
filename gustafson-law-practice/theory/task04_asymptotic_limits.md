# Task 04: Asymptotic Analysis of Parallel Efficiency

## 1. Introduction

Parallel efficiency measures how effectively a parallel computing system utilizes its available processors.

It is defined as the ratio of speedup to the number of processors:

\[
E(P)=\frac{S(P)}{P}
\]

Where:

- \(E(P)\) = parallel efficiency
- \(S(P)\) = speedup
- \(P\) = number of processors
- \(\alpha\) = serial fraction measured on the parallel machine

The objective is to determine the asymptotic efficiency of Gustafson's Law and compare it with Amdahl's Law as the number of processors approaches infinity.

## 2. Gustafson's Law

Gustafson's scaled speedup is defined as:

\[
S_G(P)=P-\alpha(P-1)
\]

Substitute this expression into the parallel efficiency formula:

\[
E_G(P)=\frac{P-\alpha(P-1)}{P}
\]

Separate the terms:

\[
E_G(P)=\frac{P}{P}-\frac{\alpha(P-1)}{P}
\]

Simplify:

\[
E_G(P)=1-\alpha\left(\frac{P-1}{P}\right)
\]

Since:

\[
\frac{P-1}{P}=1-\frac{1}{P}
\]

We obtain:

\[
E_G(P)=1-\alpha\left(1-\frac{1}{P}\right)
\]

Expand the expression:

\[
\boxed{E_G(P)=1-\alpha+\frac{\alpha}{P}}
\]

This is Gustafson's parallel efficiency formula.

## 3. Asymptotic Limit of Gustafson's Efficiency

We calculate the limit as the processor count approaches infinity:

\[
\lim_{P\to\infty}E_G(P)
=\lim_{P\to\infty}\left(1-\alpha+\frac{\alpha}{P}\right)
\]

Assume that the serial fraction \(\alpha\) remains constant as \(P\) increases.

Because:

\[
\lim_{P\to\infty}\frac{\alpha}{P}=0
\]

The expression becomes:

\[
\boxed{\lim_{P\to\infty}E_G(P)=1-\alpha}
\]

This proves that Gustafson's parallel efficiency approaches a nonzero constant when \(0\leq\alpha<1\).

For example, if:

\[
\alpha=0.04
\]

Then:

\[
\lim_{P\to\infty}E_G(P)=1-0.04=0.96
\]

Therefore:

\[
\boxed{E_G(\infty)=96\%}
\]

This means the idealized model predicts that efficiency approaches 96% as the number of processors becomes very large.

## 4. Amdahl's Law

Amdahl's Law models strong scaling, where the total workload remains fixed.

Its speedup formula is:

\[
S_A(P)=\frac{1}{s+\frac{1-s}{P}}
\]

Where \(s\) represents the serial fraction measured relative to the single-processor runtime.

Parallel efficiency is:

\[
E_A(P)=\frac{S_A(P)}{P}
\]

Substitute Amdahl's speedup:

\[
E_A(P)=\frac{1}{P\left(s+\frac{1-s}{P}\right)}
\]

Multiply the denominator by \(P\):

\[
\boxed{E_A(P)=\frac{1}{Ps+(1-s)}}
\]

## 5. Asymptotic Limit of Amdahl's Efficiency

We calculate:

\[
\lim_{P\to\infty}E_A(P)
=\lim_{P\to\infty}\frac{1}{Ps+(1-s)}
\]

Assume that \(s\) is constant and:

\[
0<s\leq1
\]

As the number of processors increases:

\[
Ps\to\infty
\]

Therefore, the denominator approaches infinity:

\[
Ps+(1-s)\to\infty
\]

Hence:

\[
\boxed{\lim_{P\to\infty}E_A(P)=0}
\]

Thus, Amdahl's parallel efficiency approaches zero for any positive fixed serial fraction.

Special case:

If \(s=0\), then:

\[
S_A(P)=P
\]

And:

\[
E_A(P)=1
\]

Therefore:

\[
\boxed{\lim_{P\to\infty}E_A(P)=1,\quad s=0}
\]

## 6. Numerical Comparison

For illustration, assume that both numerical serial-fraction parameters equal 0.04.

This comparison uses the same numerical value but different scaling assumptions and measurement reference frames.

| Processors (P) | Gustafson Efficiency | Amdahl Efficiency |
|---|---:|---:|
| 1 | 100.00% | 100.00% |
| 4 | 97.00% | 89.29% |
| 16 | 96.25% | 62.50% |
| 64 | 96.06% | 28.41% |
| 256 | 96.02% | 8.93% |
| 1024 | 96.00% | 2.39% |

The results show that Gustafson's efficiency approaches 96%, while Amdahl's efficiency decreases toward zero.

## 7. Interpretation

The difference occurs because the two laws model different workload conditions.

**Gustafson's Law:**

- Assumes that the workload increases with the number of processors.
- Uses a fixed-time scaling perspective.
- Assumes the serial fraction measured on the parallel machine remains constant.
- Predicts a positive limiting efficiency of \(1-\alpha\).

**Amdahl's Law:**

- Assumes that the total workload remains constant.
- Uses a fixed-size scaling perspective.
- Assumes a constant single-processor serial fraction.
- Predicts that efficiency approaches zero whenever the serial fraction is positive.

Gustafson's Law demonstrates that large processor counts can remain useful when applications have sufficiently scalable workloads.

However, real applications may experience additional communication, synchronization, memory, and scheduling overhead.

Consequently, maintaining a constant serial fraction across arbitrarily large processor counts is an idealized assumption.

## 8. Conclusion

For Gustafson's Law:

\[
\boxed{\lim_{P\to\infty}E_G(P)=1-\alpha}
\]

For Amdahl's Law with \(s>0\):

\[
\boxed{\lim_{P\to\infty}E_A(P)=0}
\]

For Amdahl's Law with \(s=0\):

\[
\boxed{\lim_{P\to\infty}E_A(P)=1}
\]

The main conclusion is that Gustafson's Law predicts sustainable parallel efficiency under ideal weak-scaling conditions, while Amdahl's Law predicts declining efficiency for a fixed workload with a positive serial fraction.

Both laws are mathematically valid within their respective assumptions.