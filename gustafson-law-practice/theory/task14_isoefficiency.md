# Task 14: Isoefficiency Relation with Gustafson Scaling

## 1. Introduction

Parallel computing scalability describes how effectively an application uses increasing numbers of processors.

Gustafson's Law demonstrates that large speedups are possible when computational workloads increase with processor count.

However, increasing the workload does not automatically guarantee that parallel efficiency remains constant.

The isoefficiency concept, associated with the work of Vipin Kumar and Ananth Grama, describes how quickly problem size must increase as processor count grows to maintain a specified level of parallel efficiency.

The objective of this task is to derive the isoefficiency function, analyze its relationship with Gustafson's Law, and determine the conditions under which a weak-scaling program maintains constant efficiency.

## 2. Mathematical Foundations

### 2.1 Parallel Speedup

Parallel speedup is defined as:

\[
S(P)=\frac{T_1(W)}{T_P(W)}
\]

Where:

- \(P\) = number of processors.
- \(W\) = total computational work.
- \(T_1(W)\) = sequential execution time.
- \(T_P(W)\) = parallel execution time.
- \(S(P)\) = parallel speedup.

Assuming one unit of work requires one unit of sequential execution time:

\[
T_1(W)=W
\]

Therefore:

\[
S(P)=\frac{W}{T_P(W)}
\]

### 2.2 Parallel Efficiency

Parallel efficiency measures processor utilization:

\[
E(P)=\frac{S(P)}{P}
\]

Substituting the speedup expression:

\[
E(P)=\frac{W}{PT_P(W)}
\]

Thus:

\[
\boxed{E(P)=\frac{W}{PT_P(W)}}
\]

The ideal efficiency is:

\[
E(P)=1
\]

This represents perfect linear speedup.

In real applications:

\[
0<E(P)\leq1
\]

for conventional speedup without superlinear effects.

## 3. The Parallel Overhead Function

Parallel execution includes useful computation and overhead.

The overhead function is defined as:

\[
\boxed{T_o(W,P)=PT_P(W)-W}
\]

Where \(T_o\) represents total excess processor-time consumption relative to ideal execution.

It may include:

- Communication overhead.
- Synchronization delays.
- Processor idle time.
- Load imbalance.
- Sequential execution penalties.
- Parallel scheduling costs.

Rearrange:

\[
PT_P(W)=W+T_o(W,P)
\]

Substitute into the efficiency formula:

\[
E(P)=\frac{W}{W+T_o(W,P)}
\]

Therefore:

\[
\boxed{E(P)=\frac{1}{1+\frac{T_o(W,P)}{W}}}
\]

This equation establishes a direct relationship between parallel efficiency, useful work, and overhead.

Efficiency remains constant when the ratio of overhead to useful work remains constant.

## 4. Formal Derivation of the Isoefficiency Function

Suppose the required efficiency is a fixed target:

\[
E(P)=E_0
\]

Where:

\[
0<E_0<1
\]

Starting from:

\[
E_0=\frac{W}{W+T_o(W,P)}
\]

Multiply both sides:

\[
E_0(W+T_o)=W
\]

Expand:

\[
E_0W+E_0T_o=W
\]

Move \(E_0W\) to the right:

\[
E_0T_o=W-E_0W
\]

Factor:

\[
E_0T_o=W(1-E_0)
\]

Divide by \(1-E_0\):

\[
W=\frac{E_0}{1-E_0}T_o(W,P)
\]

Define:

\[
K=\frac{E_0}{1-E_0}
\]

Therefore:

\[
\boxed{W=KT_o(W,P)}
\]

This is the fundamental isoefficiency relationship.

Because the overhead function may depend on both \(W\) and \(P\), the equation may be implicit and must be solved for workload growth.

The resulting workload requirement is called the isoefficiency function.

## 5. Interpretation of Isoefficiency

Isoefficiency describes how problem size must grow with processor count to preserve a target efficiency.

A program has favorable scalability when the required workload grows relatively slowly.

For example:

If:

\[
W(P)=\Theta(P)
\]

the workload needs to increase linearly with the number of processors.

If:

\[
W(P)=\Theta(P\log P)
\]

the workload must grow slightly faster than linearly.

If:

\[
W(P)=\Theta(P^2)
\]

the workload must increase quadratically.

Higher workload-growth requirements indicate that more work is necessary to compensate for increasing parallel overhead.

Therefore, the isoefficiency function provides a way to compare parallel algorithms independently of a single processor configuration.

## 6. Gustafson's Law and Weak Scaling

Gustafson's Law assumes that workload size increases with processor count while execution time remains approximately constant.

The scaled speedup formula is:

\[
S_G(P)=P-\alpha(P-1)
\]

Where \(\alpha\) is the serial fraction measured on the parallel machine.

An equivalent form is:

\[
S_G(P)=\alpha+(1-\alpha)P
\]

Parallel efficiency is:

\[
E_G(P)=\frac{S_G(P)}{P}
\]

Substituting:

\[
E_G(P)=\frac{\alpha+(1-\alpha)P}{P}
\]

Therefore:

\[
\boxed{E_G(P)=1-\alpha+\frac{\alpha}{P}}
\]

Assuming a constant serial fraction:

\[
\lim_{P\to\infty}E_G(P)=1-\alpha
\]

Thus:

\[
\boxed{\lim_{P\to\infty}E_G(P)=1-\alpha}
\]

This result predicts asymptotically constant parallel efficiency.

However, this conclusion depends on maintaining the assumed serial fraction and favorable workload scaling.

## 7. Derivation for an Ideal Gustafson-Compliant Program

Consider a parallel application consisting of:

- A fixed sequential component \(s\).
- A parallelizable workload \(w\).

The equivalent sequential execution time is:

\[
T_1=s+w
\]

Assuming perfect distribution of parallel work, the parallel execution time is:

\[
T_P=s+\frac{w}{P}
\]

The total useful sequential work is:

\[
W=s+w
\]

### 7.1 Deriving the Overhead

The parallel overhead function is:

\[
T_o(W,P)=PT_P-W
\]

Substitute:

\[
T_o=P\left(s+\frac{w}{P}\right)-(s+w)
\]

Expand:

\[
T_o=Ps+w-s-w
\]

Simplify:

\[
\boxed{T_o=s(P-1)}
\]

This is the processor-time overhead caused by the fixed serial portion.

It increases linearly with the number of processors when \(s>0\).

### 7.2 Substituting into Isoefficiency

The isoefficiency relationship is:

\[
W=KT_o(W,P)
\]

Substitute:

\[
W=Ks(P-1)
\]

Therefore:

\[
\boxed{W(P)=Ks(P-1)}
\]

For a constant serial workload \(s>0\) and fixed target efficiency \(E_0\):

\[
K=\frac{E_0}{1-E_0}
\]

Thus:

\[
\boxed{
W(P)=\frac{E_0}{1-E_0}s(P-1)
}
\]

For sufficiently large \(P\):

\[
P-1=\Theta(P)
\]

Therefore:

\[
\boxed{W(P)=\Theta(P)}
\]

This is the isoefficiency function of the idealized Gustafson-compliant program with a fixed positive serial workload and no additional parallel overhead.

### 7.3 Interpretation

The result demonstrates that total useful work must grow linearly with processor count to maintain a fixed efficiency strictly between zero and one.

This is consistent with the traditional weak-scaling assumption:

\[
W(P)\propto P
\]

Thus, under these assumptions, Gustafson-style weak scaling and linear isoefficiency are compatible.

## 8. Formal Proof of Constant Efficiency Under Weak Scaling

Assume the serial execution time is fixed:

\[
s>0
\]

Suppose each processor receives a constant parallelizable workload \(q\).

The total parallelizable workload becomes:

\[
w(P)=Pq
\]

Therefore, total useful work is:

\[
W(P)=s+Pq
\]

The parallel runtime is:

\[
T_P=s+\frac{Pq}{P}
\]

Simplify:

\[
\boxed{T_P=s+q}
\]

The parallel execution time is constant.

Now calculate speedup:

\[
S(P)=\frac{s+Pq}{s+q}
\]

Parallel efficiency becomes:

\[
E(P)=\frac{s+Pq}{P(s+q)}
\]

Separate the terms:

\[
E(P)=\frac{s}{P(s+q)}+\frac{q}{s+q}
\]

Therefore:

\[
\boxed{
E(P)=\frac{q}{s+q}+\frac{s}{P(s+q)}
}
\]

Take the limit:

\[
\lim_{P\to\infty}E(P)
=
\frac{q}{s+q}
\]

Define the serial fraction measured on the parallel machine:

\[
\alpha=\frac{s}{s+q}
\]

Therefore:

\[
1-\alpha=\frac{q}{s+q}
\]

We obtain:

\[
\boxed{
\lim_{P\to\infty}E(P)=1-\alpha
}
\]

This is exactly Gustafson's asymptotic efficiency result.

Hence, a fixed serial workload combined with constant parallel work per processor produces constant parallel runtime and asymptotically constant efficiency.

This completes the proof.

## 9. Special Case: Zero Serial Overhead

Suppose the application is perfectly parallelizable:

\[
s=0
\]

Then:

\[
T_P=\frac{W}{P}
\]

The overhead function becomes:

\[
T_o=PT_P-W
\]

\[
T_o=P\frac{W}{P}-W
\]

Therefore:

\[
\boxed{T_o=0}
\]

Parallel efficiency is:

\[
E(P)=\frac{W}{W+0}
\]

\[
\boxed{E(P)=1}
\]

Thus, perfect efficiency is maintained for any positive workload in the ideal model, provided sufficient parallelism exists.

In this special case, the isoefficiency requirement imposes no minimum workload-growth rate based on overhead.

However, choosing constant work per processor still produces:

\[
W(P)=\Theta(P)
\]

This is a weak-scaling choice rather than a mathematical requirement for maintaining efficiency.

Therefore, the statement that every Gustafson-compliant program necessarily has linear isoefficiency requires an explicit assumption of positive fixed serial overhead.

## 10. Numerical Example

Consider an ideal parallel application with a fixed serial execution time:

\[
s=1
\]

Suppose the required efficiency is:

\[
E_0=0.90
\]

Then:

\[
K=\frac{E_0}{1-E_0}
\]

\[
K=\frac{0.90}{0.10}
\]

\[
\boxed{K=9}
\]

The isoefficiency relationship becomes:

\[
W(P)=Ks(P-1)
\]

Substitute:

\[
W(P)=9(1)(P-1)
\]

Therefore:

\[
\boxed{W(P)=9(P-1)}
\]

### Case 1: 16 Processors

\[
W(16)=9(16-1)
\]

\[
\boxed{W(16)=135}
\]

The parallelizable work is:

\[
w=135-1=134
\]

Parallel execution time:

\[
T_{16}=1+\frac{134}{16}
\]

\[
T_{16}=9.375
\]

Efficiency:

\[
E(16)=\frac{135}{16(9.375)}
\]

\[
\boxed{E(16)=90\%}
\]

### Case 2: 64 Processors

\[
W(64)=9(64-1)
\]

\[
\boxed{W(64)=567}
\]

The parallelizable work is:

\[
w=567-1=566
\]

Parallel execution time:

\[
T_{64}=1+\frac{566}{64}
\]

\[
T_{64}=9.84375
\]

Efficiency:

\[
E(64)=\frac{567}{64(9.84375)}
\]

\[
\boxed{E(64)=90\%}
\]

### Case 3: 256 Processors

\[
W(256)=9(256-1)
\]

\[
\boxed{W(256)=2295}
\]

The parallelizable work is:

\[
w=2295-1=2294
\]

Parallel execution time:

\[
T_{256}=1+\frac{2294}{256}
\]

\[
T_{256}=9.9609375
\]

Efficiency:

\[
E(256)=\frac{2295}{256(9.9609375)}
\]

\[
\boxed{E(256)=90\%}
\]

### Complete Results Table

| Processors | Required Workload | Parallel Runtime | Efficiency |
|---:|---:|---:|---:|
| 16 | 135 | 9.375000 | 90% |
| 64 | 567 | 9.843750 | 90% |
| 256 | 2295 | 9.960938 | 90% |

The results demonstrate that maintaining 90% efficiency requires increasing workload approximately proportionally with processor count.

The parallel runtime approaches a constant value of 10 time units.

This example uses exact isoefficiency targets, rather than requiring identical runtime at every finite processor count.

## 11. Realistic Communication Overhead

The previous derivation assumed that the only overhead was the fixed sequential component.

Real parallel applications experience additional communication and synchronization costs.

Let:

\[
C(P)
\]

represent additional non-overlapped runtime overhead.

Then:

\[
T_P=s+\frac{w}{P}+C(P)
\]

The total processor-time overhead becomes:

\[
T_o=PT_P-W
\]

Substituting:

\[
T_o=P\left(s+\frac{w}{P}+C(P)\right)-(s+w)
\]

Simplify:

\[
\boxed{T_o=s(P-1)+PC(P)}
\]

Therefore, the general isoefficiency relationship is:

\[
\boxed{
W=K[s(P-1)+PC(P)]
}
\]

This expression demonstrates that increasing communication overhead may require faster workload growth to maintain constant efficiency.

## 12. Logarithmic Communication Example

Suppose communication overhead grows logarithmically with processor count:

\[
C(P)=c\log_2P
\]

Where:

\[
c>0
\]

The total overhead is:

\[
T_o=s(P-1)+Pc\log_2P
\]

For sufficiently large \(P\), the logarithmic communication term dominates the fixed serial contribution.

Therefore:

\[
T_o=\Theta(P\log P)
\]

Using the isoefficiency relationship:

\[
W=KT_o
\]

We obtain:

\[
\boxed{W(P)=\Theta(P\log P)}
\]

under the stated overhead model and a constant efficiency target.

Thus, workload must grow faster than linearly to compensate for logarithmically increasing communication time.

If a program increases workload only as:

\[
W(P)=\Theta(P)
\]

then its overhead-to-work ratio grows approximately as:

\[
\frac{T_o}{W}=\Theta(\log P)
\]

Consequently:

\[
E(P)=\frac{1}{1+T_o/W}
\]

decreases toward zero.

This explains why ideal Gustafson weak scaling may fail when communication overhead increases with processor count.

## 13. Square-Root Communication Example

Suppose the additional runtime overhead is:

\[
C(P)=c(\sqrt P-1)
\]

Where:

\[
c>0
\]

Then:

\[
T_o=s(P-1)+Pc(\sqrt P-1)
\]

For large \(P\):

\[
Pc\sqrt P=cP^{3/2}
\]

Therefore:

\[
T_o=\Theta(P^{3/2})
\]

The isoefficiency relation gives:

\[
W=KT_o
\]

Thus:

\[
\boxed{W(P)=\Theta(P^{3/2})}
\]

This means that maintaining constant efficiency requires workload growth faster than linear.

The application must increase total useful work approximately as \(P^{3/2}\) to compensate for the modeled communication overhead.

These logarithmic and square-root cases are hypothetical performance models. The actual overhead depends on the algorithm and hardware architecture.

## 14. Comparison of Isoefficiency Functions

| Parallel Program Model | Dominant Overhead | Isoefficiency Function |
|---|---|---|
| Perfectly parallel program | 0 | No overhead-driven growth requirement |
| Fixed positive serial work | \(\Theta(P)\) | \(\Theta(P)\) |
| Logarithmic communication time | \(\Theta(P\log P)\) | \(\Theta(P\log P)\) |
| Square-root communication time | \(\Theta(P^{3/2})\) | \(\Theta(P^{3/2})\) |

The table shows that the workload-growth requirement depends on the overhead function.

The ideal Gustafson model has favorable linear isoefficiency when serial work is fixed and positive.

Real distributed algorithms may require larger workloads to maintain the same efficiency.

## 15. Critical Analysis

Isoefficiency and Gustafson's Law are complementary rather than contradictory.

Gustafson's Law evaluates the potential benefits of increasing the workload with processor count.

Isoefficiency evaluates how much workload growth is required to maintain a chosen efficiency target.

The two concepts answer different questions.

**Gustafson's Law asks:**

How much larger a workload can be processed in approximately constant time using additional processors?

**Isoefficiency asks:**

How quickly must workload size increase with processor count to maintain a specified parallel efficiency?

An important limitation is that constant efficiency and constant runtime are not equivalent.

From:

\[
E(P)=\frac{W(P)}{PT_P(P)}
\]

If efficiency is constant:

\[
T_P(P)=\frac{W(P)}{PE_0}
\]

Therefore, constant runtime additionally requires:

\[
W(P)=\Theta(P)
\]

If the workload grows faster than linearly to compensate for increasing overhead, runtime may increase even though efficiency remains constant.

For example, if:

\[
W(P)=\Theta(P\log P)
\]

and efficiency is fixed:

\[
T_P(P)=\Theta(\log P)
\]

Thus, the system maintains efficiency but no longer satisfies the classical fixed-time weak-scaling premise.

This distinction is important when evaluating practical HPC applications.

## 16. Engineering Implications

The isoefficiency concept helps engineers evaluate the scalability of parallel software.

A favorable isoefficiency function indicates that the application can efficiently use more processors without requiring excessive workload expansion.

For example:

- Linear isoefficiency is favorable for large-scale parallel computation.
- \(P\log P\) isoefficiency requires moderate additional workload growth.
- Polynomial functions with larger exponents require substantially larger workloads.

However, the necessary problem size must also fit within available memory and satisfy application requirements.

An algorithm may have good theoretical isoefficiency but still perform poorly because of:

- Insufficient memory capacity.
- Network congestion.
- Load imbalance.
- Synchronization bottlenecks.
- Limited problem parallelism.
- Increasing communication latency.

Therefore, practical scalability analysis should combine Gustafson's Law, isoefficiency functions, and empirical benchmarking.

## 17. Conclusion

The isoefficiency relationship is:

\[
\boxed{
W=KT_o(W,P)
}
\]

Where:

\[
K=\frac{E_0}{1-E_0}
\]

For an ideal Gustafson-compliant program with fixed positive serial work \(s\) and no additional overhead:

\[
T_o=s(P-1)
\]

Therefore:

\[
W(P)=Ks(P-1)
\]

And the isoefficiency function is:

\[
\boxed{W(P)=\Theta(P)}
\]

This proves that linear workload growth is sufficient to maintain constant parallel efficiency under the stated ideal assumptions.

For a perfectly parallel program with zero overhead, no workload growth is required solely to preserve efficiency.

For applications with increasing communication overhead, the isoefficiency requirement may increase to:

\[
\boxed{W(P)=\Theta(P\log P)}
\]

or:

\[
\boxed{W(P)=\Theta(P^{3/2})}
\]

depending on the overhead model.

The main conclusion is that Gustafson's ideal weak-scaling behavior corresponds to favorable isoefficiency only when serial work and communication overhead remain sufficiently controlled.

Isoefficiency provides a mathematical framework for determining whether an application can maintain its parallel efficiency as computing resources increase.

## References

1. Grama, A., Gupta, A., Karypis, G., & Kumar, V. (2003). *Introduction to Parallel Computing*, 2nd Edition. Addison-Wesley.

2. Gustafson, J. L. (1988). *Reevaluating Amdahl's Law*. Communications of the ACM, 31(5), 532–533. https://doi.org/10.1145/42411.42415

3. University of Illinois Chicago. *Parallel FFT and Isoefficiency*. https://homepages.math.uic.edu/~jan/mcs572f16/mcs572notes/lec14.html

4. Cornell University. *Performance Basics — Numerical Methods for Data Science*. https://www.cs.cornell.edu/~bindel/nmds/00-Background/02-Performance.html