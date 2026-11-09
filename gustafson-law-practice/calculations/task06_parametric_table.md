# Task 06: Parametric Speedup Across Processor Densities

## 1. Introduction

Gustafson's Law describes how parallel computing performance improves when the workload increases proportionally with the number of processors.

In this task, we calculate the theoretical scaled speedup and parallel efficiency for different processor counts.

The serial fraction is fixed at 4%.

## 2. Given Parameters

The serial fraction is:

\[
\alpha = 0.04
\]

The processor counts are:

\[
P \in \{16,64,256,1024,4096,16384\}
\]

We need to calculate:

1. Scaled speedup \(S(P)\)
2. Parallel efficiency \(E(P)\)

## 3. Mathematical Formulas

Gustafson's Law:

\[
S(P)=P-\alpha(P-1)
\]

Substituting \(\alpha=0.04\):

\[
S(P)=P-0.04(P-1)
\]

Expanding:

\[
S(P)=P-0.04P+0.04
\]

Therefore:

\[
\boxed{S(P)=0.96P+0.04}
\]

Parallel efficiency is defined as:

\[
E(P)=\frac{S(P)}{P}
\]

Substituting the speedup formula:

\[
E(P)=\frac{0.96P+0.04}{P}
\]

Therefore:

\[
\boxed{E(P)=0.96+\frac{0.04}{P}}
\]

## 4. Step-by-Step Calculations

### Case 1: P = 16

\[
S(16)=16-0.04(16-1)
\]

\[
S(16)=16-0.6
\]

\[
\boxed{S(16)=15.40}
\]

Efficiency:

\[
E(16)=\frac{15.40}{16}=0.9625
\]

\[
\boxed{E(16)=96.25\%}
\]

### Case 2: P = 64

\[
S(64)=64-0.04(63)
\]

\[
S(64)=64-2.52
\]

\[
\boxed{S(64)=61.48}
\]

Efficiency:

\[
E(64)=\frac{61.48}{64}=0.960625
\]

\[
\boxed{E(64)=96.0625\%}
\]

### Case 3: P = 256

\[
S(256)=256-0.04(255)
\]

\[
S(256)=256-10.20
\]

\[
\boxed{S(256)=245.80}
\]

Efficiency:

\[
E(256)=\frac{245.80}{256}=0.96015625
\]

\[
\boxed{E(256)=96.015625\%}
\]

### Case 4: P = 1024

\[
S(1024)=1024-0.04(1023)
\]

\[
S(1024)=1024-40.92
\]

\[
\boxed{S(1024)=983.08}
\]

Efficiency:

\[
E(1024)=\frac{983.08}{1024}=0.9600390625
\]

\[
\boxed{E(1024)=96.00390625\%}
\]

### Case 5: P = 4096

\[
S(4096)=4096-0.04(4095)
\]

\[
S(4096)=4096-163.80
\]

\[
\boxed{S(4096)=3932.20}
\]

Efficiency:

\[
E(4096)=\frac{3932.20}{4096}=0.960009765625
\]

\[
\boxed{E(4096)=96.0009765625\%}
\]

### Case 6: P = 16384

\[
S(16384)=16384-0.04(16383)
\]

\[
S(16384)=16384-655.32
\]

\[
\boxed{S(16384)=15728.68}
\]

Efficiency:

\[
E(16384)=\frac{15728.68}{16384}=0.96000244140625
\]

\[
\boxed{E(16384)=96.000244140625\%}
\]

## 5. Complete Results Table

| Processors (P) | Scaled Speedup S(P) | Efficiency (%) |
|---:|---:|---:|
| 16 | 15.40 | 96.250000 |
| 64 | 61.48 | 96.062500 |
| 256 | 245.80 | 96.015625 |
| 1024 | 983.08 | 96.003906 |
| 4096 | 3932.20 | 96.000977 |
| 16384 | 15728.68 | 96.000244 |

## 6. Analysis of Efficiency Degradation

The results show that scaled speedup increases almost linearly with the number of processors.

When the processor count increases from 16 to 16384, the predicted speedup increases from 15.40 to 15728.68.

However, parallel efficiency decreases slightly:

\[
E(16)=96.25\%
\]

\[
E(16384)\approx96.000244\%
\]

The total decrease is approximately:

\[
96.25-96.000244=0.249756
\]

This represents a decrease of approximately 0.25 percentage points.

The decrease becomes progressively smaller as the processor count grows.

This behavior occurs because:

\[
E(P)=1-\alpha+\frac{\alpha}{P}
\]

As \(P\) increases, the term \(\alpha/P\) approaches zero.

Therefore:

\[
\lim_{P\to\infty}E(P)=1-\alpha
\]

Substituting \(\alpha=0.04\):

\[
\boxed{\lim_{P\to\infty}E(P)=0.96=96\%}
\]

Thus, the theoretical efficiency approaches 96% rather than zero.

## 7. Interpretation

The results demonstrate three important properties of Gustafson's Law.

**First**, increasing the number of processors allows proportionally larger workloads to be processed in approximately constant execution time.

**Second**, a small serial fraction permits scaled speedup close to ideal linear speedup.

**Third**, when the serial fraction remains constant, efficiency approaches a positive limit.

However, these predictions assume ideal weak scaling with a constant serial fraction.

In real parallel systems, communication overhead, synchronization, memory limitations, and load imbalance can reduce actual efficiency.

Therefore, theoretical scaled speedup is not guaranteed to match measured performance.

## 8. Conclusion

Using Gustafson's Law with a constant serial fraction of 4%, we calculated scaled speedup and parallel efficiency for six processor configurations.

The results show that speedup grows almost proportionally with processor count, while efficiency decreases only slightly and approaches 96%.

The final formulas are:

\[
\boxed{S(P)=0.96P+0.04}
\]

\[
\boxed{E(P)=0.96+\frac{0.04}{P}}
\]

These findings demonstrate the potential scalability of parallel applications when their workloads can grow with available processing resources.