# Task 12: Communication Overhead Penalty Integration

## 1. Introduction

Gustafson's Law describes the theoretical speedup achievable when the computational workload increases with the number of processors.

The classical formulation assumes that the serial fraction remains constant while the parallel workload grows.

However, real distributed computing systems experience additional overhead caused by communication between processors.

Communication overhead may include:

- Network latency.
- Data transmission.
- Message-passing operations.
- Synchronization delays.
- Network contention.
- Data redistribution.

These costs often increase as more processors participate in computation.

The objective of this task is to develop an extended Gustafson model that explicitly includes communication overhead and analyze its effect on scaled speedup and parallel efficiency.

## 2. Classical Gustafson's Law

The classical scaled speedup formula is:

\[
S_G(P)=P-\alpha(P-1)
\]

Where:

- \(P\) = number of processors.
- \(\alpha\) = serial fraction measured on the parallel machine.
- \(S_G(P)\) = scaled speedup.

An equivalent expression is:

\[
S_G(P)=\alpha+(1-\alpha)P
\]

The model assumes normalized parallel execution time:

\[
T_P=s+p=1
\]

Where:

- \(s\) = serial execution time.
- \(p\) = parallel execution time.

The equivalent sequential execution time for the expanded computational workload is:

\[
T_1=s+Pp
\]

Therefore:

\[
S_G(P)=\frac{s+Pp}{s+p}
\]

Since \(s+p=1\):

\[
\boxed{S_G(P)=s+Pp}
\]

This formulation assumes ideal execution of the parallel portion and does not explicitly account for additional communication delays.

## 3. Communication Overhead in Distributed Systems

In distributed-memory parallel computing, processors exchange data through a communication network.

As processor count increases, communication becomes an important performance factor.

Let:

\[
C(P)
\]

represent the additional non-overlapped communication overhead associated with using \(P\) processors.

For the proposed model, \(C(P)\) is measured in units of the normalized useful execution time.

We assume:

\[
C(P)\geq0
\]

and:

\[
C(1)=0
\]

The second condition means that no interprocessor communication overhead exists when only one processor is used.

Communication overhead can grow according to different patterns.

Two examples from the assignment are:

\[
C(P)=O(\log P)
\]

and:

\[
C(P)=O(P^{1/2})
\]

The actual growth pattern depends on communication topology, algorithm design, message sizes, and network characteristics.

## 4. Derivation of the Modified Gustafson Model

We begin with normalized useful parallel execution time:

\[
s+p=1
\]

The equivalent sequential runtime for the expanded workload is:

\[
T_1=s+Pp
\]

Now introduce additional communication overhead:

\[
C(P)
\]

The actual parallel execution time becomes:

\[
T_P^{*}=s+p+C(P)
\]

Since:

\[
s+p=1
\]

We obtain:

\[
\boxed{T_P^{*}=1+C(P)}
\]

Scaled speedup is the ratio of equivalent sequential execution time to actual parallel execution time:

\[
S_C(P)=\frac{T_1}{T_P^{*}}
\]

Substitute the expressions:

\[
S_C(P)=\frac{s+Pp}{s+p+C(P)}
\]

Using the normalization:

\[
s+p=1
\]

We obtain:

\[
S_C(P)=\frac{s+Pp}{1+C(P)}
\]

Define the serial fraction of the useful computation as:

\[
\alpha=\frac{s}{s+p}
\]

Since \(s+p=1\):

\[
s=\alpha
\]

and:

\[
p=1-\alpha
\]

Substituting:

\[
S_C(P)=\frac{\alpha+P(1-\alpha)}{1+C(P)}
\]

Expanding:

\[
S_C(P)=\frac{P-\alpha(P-1)}{1+C(P)}
\]

Therefore, the proposed communication-aware Gustafson model is:

\[
\boxed{
S_C(P)=
\frac{P-\alpha(P-1)}
{1+C(P)}
}
\]

This equation explicitly incorporates additional communication overhead into scaled speedup.

### Modeling assumptions

This extension assumes that:

1. Useful execution time is normalized before communication overhead is added.
2. The serial fraction \(\alpha\) is measured relative to useful execution time, excluding the additional overhead \(C(P)\).
3. Communication overhead represents non-overlapped extra runtime.
4. The equivalent sequential workload remains \(s+Pp\).
5. The overhead is caused by parallel execution and is not part of the equivalent sequential computational workload.

If some communication is already included in the measured serial fraction, it must not be counted again in \(C(P)\).

The model is a proposed extension rather than the unique standard form of Gustafson's Law.

## 5. Verification of the Classical Model

If communication overhead is zero:

\[
C(P)=0
\]

Then:

\[
S_C(P)=
\frac{P-\alpha(P-1)}{1+0}
\]

Therefore:

\[
\boxed{S_C(P)=P-\alpha(P-1)}
\]

This is exactly Gustafson's original formulation.

Thus, the proposed model reduces to the classical law when communication overhead is absent.

## 6. Logarithmic Communication Overhead

Some parallel algorithms use hierarchical communication structures.

Examples include tree-based reductions and broadcasts.

In an ideal balanced binary communication tree, the number of communication stages may grow approximately as:

\[
\log_2 P
\]

We model communication overhead as:

\[
\boxed{C_{\log}(P)=\beta\log_2 P}
\]

Where:

\[
\beta>0
\]

is the additional communication-time cost per normalized tree stage.

Substitute this expression into the modified Gustafson model:

\[
S_{\log}(P)=
\frac{P-\alpha(P-1)}
{1+\beta\log_2P}
\]

Therefore:

\[
\boxed{
S_{\log}(P)=
\frac{P-\alpha(P-1)}
{1+\beta\log_2P}
}
\]

This model describes a system where communication overhead grows logarithmically with processor count.

Logarithmic growth is relatively slow compared with linear growth, but it can still reduce efficiency at very large processor counts.

## 7. Square-Root Communication Overhead

Some communication patterns involve geometrically expanding communication requirements.

For example, communication costs may grow with the dimensions of a processor grid.

A simplified square-root overhead model is:

\[
\boxed{C_{\sqrt{}}(P)=\gamma(\sqrt P-1)}
\]

Where:

\[
\gamma>0
\]

is a normalized communication coefficient.

The subtraction of one ensures:

\[
C_{\sqrt{}}(1)=0
\]

For large \(P\), the overhead grows as:

\[
C_{\sqrt{}}(P)=O(P^{1/2})
\]

Substitute the expression into the modified Gustafson model:

\[
S_{\sqrt{}}(P)=
\frac{P-\alpha(P-1)}
{1+\gamma(\sqrt P-1)}
\]

Therefore:

\[
\boxed{
S_{\sqrt{}}(P)=
\frac{P-\alpha(P-1)}
{1+\gamma(\sqrt P-1)}
}
\]

This model demonstrates how increasing communication costs can significantly reduce scaled speedup.

A square-root dependence is not universal for distributed systems; it represents a possible topology-dependent cost model.

## 8. Numerical Example

Consider a distributed computing system with:

\[
P=64
\]

and serial fraction:

\[
\alpha=0.04
\]

Assume normalized communication coefficients:

\[
\beta=0.02
\]

and:

\[
\gamma=0.02
\]

We compare three cases:

1. Classical Gustafson's Law.
2. Logarithmic communication overhead.
3. Square-root communication overhead.

### Case 1: Classical Gustafson's Law

\[
S_G(64)=64-0.04(64-1)
\]

\[
S_G(64)=64-2.52
\]

\[
\boxed{S_G(64)=61.48}
\]

The parallel efficiency is:

\[
E_G(64)=\frac{61.48}{64}
\]

\[
\boxed{E_G(64)=96.0625\%}
\]

### Case 2: Logarithmic Communication

The communication overhead is:

\[
C_{\log}(64)=0.02\log_2 64
\]

Since:

\[
\log_2 64=6
\]

We obtain:

\[
C_{\log}(64)=0.02(6)
\]

\[
\boxed{C_{\log}(64)=0.12}
\]

The modified speedup is:

\[
S_{\log}(64)=\frac{61.48}{1+0.12}
\]

\[
S_{\log}(64)=\frac{61.48}{1.12}
\]

\[
\boxed{S_{\log}(64)\approx54.8929}
\]

Parallel efficiency:

\[
E_{\log}(64)=\frac{54.8929}{64}
\]

\[
\boxed{E_{\log}(64)\approx85.77\%}
\]

### Case 3: Square-Root Communication

The communication overhead is:

\[
C_{\sqrt{}}(64)=0.02(\sqrt{64}-1)
\]

Since:

\[
\sqrt{64}=8
\]

We obtain:

\[
C_{\sqrt{}}(64)=0.02(8-1)
\]

\[
\boxed{C_{\sqrt{}}(64)=0.14}
\]

The modified speedup is:

\[
S_{\sqrt{}}(64)=\frac{61.48}{1+0.14}
\]

\[
S_{\sqrt{}}(64)=\frac{61.48}{1.14}
\]

\[
\boxed{S_{\sqrt{}}(64)\approx53.9298}
\]

Parallel efficiency:

\[
E_{\sqrt{}}(64)=\frac{53.9298}{64}
\]

\[
\boxed{E_{\sqrt{}}(64)\approx84.27\%}
\]

## 9. Comparison Table

| Model | Communication Overhead | Scaled Speedup | Efficiency |
|---|---:|---:|---:|
| Classical Gustafson | 0.00 | 61.4800 | 96.06% |
| Logarithmic communication | 0.12 | 54.8929 | 85.77% |
| Square-root communication | 0.14 | 53.9298 | 84.27% |

The results demonstrate that introducing communication overhead reduces the predicted scaled speedup.

Under the chosen coefficients, the square-root model produces a larger penalty than the logarithmic model at 64 processors.

These values are hypothetical model calculations, not experimental measurements.

## 10. Modified Parallel Efficiency

Parallel efficiency is defined as:

\[
E_C(P)=\frac{S_C(P)}{P}
\]

Substitute the modified speedup:

\[
E_C(P)=
\frac{P-\alpha(P-1)}
{P[1+C(P)]}
\]

Divide the numerator by \(P\):

\[
E_C(P)=
\frac{1-\alpha+\frac{\alpha}{P}}
{1+C(P)}
\]

Therefore:

\[
\boxed{
E_C(P)=
\frac{1-\alpha+\frac{\alpha}{P}}
{1+C(P)}
}
\]

This equation demonstrates that communication overhead directly reduces parallel efficiency.

Even if the useful-work serial fraction remains constant, a growing communication penalty can cause efficiency to decline.

## 11. Asymptotic Analysis

We analyze the behavior of the modified model as:

\[
P\to\infty
\]

Assume:

\[
0\leq\alpha<1
\]

and that \(\alpha\) remains constant relative to useful execution time.

The modified efficiency is:

\[
E_C(P)=
\frac{1-\alpha+\frac{\alpha}{P}}
{1+C(P)}
\]

### Case 1: No Communication Overhead

If:

\[
C(P)=0
\]

Then:

\[
\lim_{P\to\infty}E_C(P)=1-\alpha
\]

This is the classical Gustafson efficiency limit.

### Case 2: Logarithmically Increasing Overhead

Suppose:

\[
C(P)=\beta\log_2P
\]

with:

\[
\beta>0
\]

Then:

\[
E_{\log}(P)=
\frac{1-\alpha+\frac{\alpha}{P}}
{1+\beta\log_2P}
\]

As \(P\to\infty\):

\[
\frac{\alpha}{P}\to0
\]

and:

\[
\log_2P\to\infty
\]

Therefore:

\[
\boxed{
\lim_{P\to\infty}E_{\log}(P)=0
}
\]

The corresponding scaled speedup grows asymptotically as:

\[
\boxed{
S_{\log}(P)=\Theta\left(\frac{P}{\log P}\right)
}
\]

under the assumed constant \(\alpha<1\) and positive \(\beta\).

Thus, speedup can continue increasing while efficiency approaches zero.

### Case 3: Square-Root Communication Overhead

Suppose:

\[
C(P)=\gamma(\sqrt P-1)
\]

with:

\[
\gamma>0
\]

Then:

\[
E_{\sqrt{}}(P)=
\frac{1-\alpha+\frac{\alpha}{P}}
{1+\gamma(\sqrt P-1)}
\]

As:

\[
P\to\infty
\]

the denominator grows without bound.

Therefore:

\[
\boxed{
\lim_{P\to\infty}E_{\sqrt{}}(P)=0
}
\]

The scaled speedup grows asymptotically as:

\[
\boxed{
S_{\sqrt{}}(P)=\Theta(\sqrt P)
}
\]

under the same assumptions.

This demonstrates that increasing communication costs can prevent ideal linear scaled speedup.

## 12. Communication Overlap and Optimization

Communication overhead does not always contribute entirely to execution time.

Some applications overlap communication with useful computation.

Let:

\[
0\leq\eta\leq1
\]

represent the fraction of communication overhead that can be hidden through overlap.

The effective non-overlapped communication overhead becomes:

\[
C_{\text{eff}}(P)=(1-\eta)C(P)
\]

The corresponding speedup is:

\[
\boxed{
S_{\text{overlap}}(P)=
\frac{P-\alpha(P-1)}
{1+(1-\eta)C(P)}
}
\]

If:

\[
\eta=0
\]

there is no communication overlap.

If:

\[
\eta=1
\]

the modeled communication overhead is completely hidden.

In practice, complete overlap may not be possible because communication and computation share hardware and software resources.

Common optimization strategies include:

- Non-blocking message passing.
- Communication-computation overlap.
- Hierarchical collective operations.
- Reducing message frequency.
- Increasing computational work per communication operation.
- Improving data locality.
- Minimizing global synchronization.
- Using topology-aware processor allocation.

These methods can reduce effective communication overhead and improve scaled speedup.

## 13. Critical Analysis

The classical Gustafson model is useful for understanding the potential benefits of workload expansion.

However, distributed applications may experience additional communication costs as processor count increases.

The proposed model:

\[
S_C(P)=
\frac{P-\alpha(P-1)}
{1+C(P)}
\]

demonstrates that the achievable speedup depends on both useful computation and additional overhead.

Several important observations follow.

**First**, a small serial fraction alone does not guarantee high parallel efficiency.

**Second**, communication complexity can determine how performance changes as processor count grows.

**Third**, applications with logarithmic communication overhead may scale more effectively than applications with stronger communication growth, assuming comparable overhead coefficients.

**Fourth**, communication-aware programming techniques can improve performance by reducing effective overhead.

**Finally**, the assumed communication function must be validated through benchmarking.

The model does not guarantee that a particular distributed algorithm follows logarithmic or square-root communication growth.

It also assumes that the single-processor equivalent workload can be separated cleanly from additional parallel communication costs.

For more accurate performance predictions, engineers should measure computation, communication, synchronization, and idle time separately.

## 14. Conclusion

Gustafson's classical scaled speedup formula is:

\[
\boxed{
S_G(P)=P-\alpha(P-1)
}
\]

By introducing additional communication overhead \(C(P)\), we derived:

\[
\boxed{
S_C(P)=
\frac{P-\alpha(P-1)}
{1+C(P)}
}
\]

For logarithmic communication growth:

\[
\boxed{
S_{\log}(P)=
\frac{P-\alpha(P-1)}
{1+\beta\log_2P}
}
\]

For square-root communication growth:

\[
\boxed{
S_{\sqrt{}}(P)=
\frac{P-\alpha(P-1)}
{1+\gamma(\sqrt P-1)}
}
\]

The numerical example with 64 processors and a 4% serial fraction produced:

- Classical Gustafson speedup: 61.48.
- Logarithmic overhead speedup: approximately 54.89.
- Square-root overhead speedup: approximately 53.93.

The analysis demonstrates that additional communication overhead reduces scaled speedup and parallel efficiency.

The main conclusion is that practical weak scaling requires both a highly parallel computational workload and efficient communication between processors.

## References

1. Gustafson, J. L. (1988). *Reevaluating Amdahl's Law*. Communications of the ACM, 31(5), 532–533. https://doi.org/10.1145/42411.42415

2. Gropp, W., Lusk, E., & Skjellum, A. (2014). *Using MPI: Portable Parallel Programming with the Message-Passing Interface*. MIT Press.

3. Hockney, R. W. (1994). The communication challenge for MPP: Intel Paragon and Meiko CS-2. *Parallel Computing*, 20(3), 389–398.