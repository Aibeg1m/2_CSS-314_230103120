# Task 09: Multi-Component Workload Partitioning

## 1. Introduction

Scientific simulations often contain several computational phases with different parallelization characteristics.

Some operations can be executed simultaneously on many processors, while others require sequential execution or synchronization.

Gustafson's Law can be used to evaluate the theoretical scaled speedup of a multi-component workload.

The objective of this task is to identify the aggregate serial fraction and calculate scaled speedup for 512 and 2048 processors.

## 2. Given Parameters

The scientific simulation consists of three computational phases.

| Phase | Description | Percentage of Parallel Runtime |
|---|---|---:|
| A | Initial disk I/O and parameter broadcast | 2% |
| B | Boundary message-passing synchronization | 6% |
| C | Core domain flux computation | 92% |
| **Total** | | **100%** |

The processor configurations are:

\[
P_1=512
\]

\[
P_2=2048
\]

We must determine:

1. Aggregate serial fraction \(\alpha\).
2. Scaled speedup for 512 processors.
3. Scaled speedup for 2048 processors.
4. Parallel efficiency.
5. The effect of communication and synchronization overhead.

## 3. Workload Phase Classification

### Phase A: Disk I/O and Parameter Broadcast

Phase A represents 2% of total parallel execution time.

It includes initialization, input operations, and parameter distribution.

For this simplified model, Phase A is treated as serial overhead.

Therefore:

\[
\alpha_A=0.02
\]

In a real system, some I/O and broadcasting activities may execute concurrently. However, the task does not specify their parallelizable portions.

### Phase B: Boundary Message-Passing Synchronization

Phase B represents 6% of total parallel execution time.

It involves communication and synchronization between processors.

These operations may cause processors to wait before continuing their computations.

For this simplified calculation, the entire synchronization phase is treated as effective serial overhead.

Therefore:

\[
\alpha_B=0.06
\]

This is a modeling assumption. Communication is not necessarily strictly sequential, but its non-overlapped waiting time can limit effective scaling.

### Phase C: Core Domain Flux Computation

Phase C represents 92% of total parallel execution time.

It consists of numerical computations that can be distributed across processors.

This phase is treated as fully parallelizable.

Therefore:

\[
p=0.92
\]

## 4. Aggregate Serial Fraction

The aggregate serial fraction is calculated by adding the serial overhead components:

\[
\alpha=\alpha_A+\alpha_B
\]

Substitute:

\[
\alpha=0.02+0.06
\]

Therefore:

\[
\boxed{\alpha=0.08}
\]

Expressed as a percentage:

\[
\boxed{\alpha=8\%}
\]

The parallel fraction is:

\[
p=1-\alpha
\]

\[
p=1-0.08
\]

\[
\boxed{p=0.92=92\%}
\]

Verification:

\[
\alpha+p=0.08+0.92=1
\]

Thus, the normalized parallel execution time is consistent with Gustafson's model.

## 5. Gustafson's Law

The scaled speedup formula is:

\[
S(P)=P-\alpha(P-1)
\]

Substitute the aggregate serial fraction:

\[
S(P)=P-0.08(P-1)
\]

Expand:

\[
S(P)=P-0.08P+0.08
\]

Therefore:

\[
\boxed{S(P)=0.92P+0.08}
\]

This formula will be used for both processor configurations.

## 6. Calculation for 512 Processors

Given:

\[
P=512
\]

Using Gustafson's Law:

\[
S(512)=512-0.08(512-1)
\]

Simplify:

\[
S(512)=512-0.08(511)
\]

Calculate the serial penalty:

\[
0.08\times511=40.88
\]

Therefore:

\[
S(512)=512-40.88
\]

The scaled speedup is:

\[
\boxed{S(512)=471.12}
\]

This means that the expanded workload has an equivalent sequential execution time 471.12 times the parallel execution time under the idealized model.

### Parallel Efficiency for 512 Processors

Parallel efficiency is:

\[
E(P)=\frac{S(P)}{P}
\]

Substitute:

\[
E(512)=\frac{471.12}{512}
\]

Therefore:

\[
E(512)=0.92015625
\]

Expressed as a percentage:

\[
\boxed{E(512)=92.015625\%}
\]

## 7. Calculation for 2048 Processors

Given:

\[
P=2048
\]

Using Gustafson's Law:

\[
S(2048)=2048-0.08(2048-1)
\]

Simplify:

\[
S(2048)=2048-0.08(2047)
\]

Calculate the serial penalty:

\[
0.08\times2047=163.76
\]

Therefore:

\[
S(2048)=2048-163.76
\]

The scaled speedup is:

\[
\boxed{S(2048)=1884.24}
\]

### Parallel Efficiency for 2048 Processors

\[
E(2048)=\frac{1884.24}{2048}
\]

Therefore:

\[
E(2048)=0.9200390625
\]

Expressed as a percentage:

\[
\boxed{E(2048)=92.00390625\%}
\]

## 8. Complete Results Table

| Metric | 512 Processors | 2048 Processors |
|---|---:|---:|
| Serial fraction | 8% | 8% |
| Parallel fraction | 92% | 92% |
| Ideal linear speedup | 512 | 2048 |
| Gustafson scaled speedup | 471.12 | 1884.24 |
| Scaled parallel efficiency | 92.015625% | 92.00390625% |
| Serial speedup penalty | 40.88 | 163.76 |

The ideal linear speedup assumes that the entire workload can execute in parallel.

The actual theoretical scaled speedup is lower because 8% of parallel execution time is modeled as serial overhead.

## 9. Comparison of the Two Processor Configurations

The processor count increases by a factor of four:

\[
\frac{2048}{512}=4
\]

The scaled speedup ratio is:

\[
R=\frac{S(2048)}{S(512)}
\]

Substitute:

\[
R=\frac{1884.24}{471.12}
\]

Therefore:

\[
\boxed{R=3.99949}
\]

The speedup increases by almost exactly four times.

This demonstrates nearly linear scaled-speedup growth under the assumption that the serial fraction remains constant.

However, efficiency decreases slightly:

\[
92.015625\%-92.00390625\%
\]

\[
\boxed{\Delta E=0.01171875\text{ percentage points}}
\]

The efficiency difference is small because the serial fraction remains fixed at 8%.

## 10. Effect of Communication and Synchronization

In real distributed systems, communication overhead may change as the number of processors increases.

For example, additional processors may introduce:

- More boundary exchanges.
- Increased network traffic.
- Higher synchronization costs.
- Communication contention.
- Load imbalance between processors.

Therefore, the effective serial fraction may depend on processor count:

\[
\alpha=\alpha(P)
\]

A simplified extended model is:

\[
S(P)=P-\alpha(P)(P-1)
\]

If the effective serial fraction increases with the number of processors, scaled speedup may become smaller than predicted by the constant-fraction model.

For example, suppose the effective serial fraction increases from 8% to 10% at 2048 processors.

Then:

\[
S(2048)=2048-0.10(2047)
\]

\[
S(2048)=2048-204.7
\]

\[
\boxed{S(2048)=1843.3}
\]

This is lower than the original prediction of 1884.24.

The example illustrates the potential impact of increasing communication overhead. It is hypothetical rather than an experimentally measured result.

## 11. Partial Parallelization of Communication

The main calculation assumes that the entire 6% synchronization phase acts as effective serial overhead.

However, some communication may overlap with useful computation.

Let \(r\) represent the fraction of Phase B that remains non-overlapped and acts as effective serial overhead, with:

\[
0\leq r\leq1
\]

The adjusted effective serial fraction is:

\[
\alpha_{\text{eff}}=0.02+0.06r
\]

If half of Phase B is effectively hidden by overlapping communication and computation:

\[
r=0.5
\]

Then:

\[
\alpha_{\text{eff}}=0.02+0.06(0.5)
\]

\[
\boxed{\alpha_{\text{eff}}=0.05}
\]

For 512 processors:

\[
S(512)=512-0.05(511)
\]

\[
\boxed{S(512)=486.45}
\]

For 2048 processors:

\[
S(2048)=2048-0.05(2047)
\]

\[
\boxed{S(2048)=1945.65}
\]

This simplified scenario assumes the newly parallelizable portion remains within the normalized runtime model.

The calculations demonstrate that reducing effective serial overhead improves predicted scaled speedup.

## 12. Interpretation

The simulation workload contains three phases with different performance characteristics.

Phase A contributes 2% serial overhead.

Phase B contributes 6% synchronization overhead under the simplifying assumption that it cannot overlap with computation.

Phase C contributes 92% parallel computation.

Combining the serial components produces an aggregate serial fraction of 8%.

Under Gustafson's Law, this results in high scaled efficiency for both processor counts.

The results also show that reducing communication and synchronization overhead can significantly improve scaled performance.

In practical scientific simulations, the actual communication fraction must be measured because its behavior may depend on network topology, decomposition strategy, processor count, and workload characteristics.

## 13. Conclusion

The aggregate serial fraction is:

\[
\boxed{\alpha=0.08=8\%}
\]

For 512 processors:

\[
\boxed{S(512)=471.12}
\]

\[
\boxed{E(512)=92.015625\%}
\]

For 2048 processors:

\[
\boxed{S(2048)=1884.24}
\]

\[
\boxed{E(2048)=92.00390625\%}
\]

The results demonstrate that Gustafson's Law predicts nearly linear scaled speedup when the serial fraction remains constant.

However, real communication and synchronization overhead can change with processor count.

Therefore, effective workload partitioning, communication overlap, and synchronization optimization are important for achieving high parallel efficiency.