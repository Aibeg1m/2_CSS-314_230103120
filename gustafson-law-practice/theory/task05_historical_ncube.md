# Task 05: Deconstructing the "Amdahl's Pessimism" Fallacy

## 1. Introduction

In 1988, John L. Gustafson, Gary R. Montry, and Robert E. Benner demonstrated exceptional parallel computing performance using a 1024-processor hypercube computer at Sandia National Laboratories.

Their research challenged the pessimistic interpretation of Amdahl's Law, which suggested that small serial portions of programs severely limited the usefulness of massively parallel computers.

The experiments demonstrated that scientific workloads could achieve scaled speedups exceeding 1000 when problem size increased with the number of processors.

## 2. Historical Background

Gene Amdahl introduced his parallel computing argument in 1967.

Amdahl's Law assumes that the total problem size remains fixed.

Its mathematical expression is:

\[
S_A(P)=\frac{1}{s+\frac{1-s}{P}}
\]

Where:

- \(P\) = number of processors
- \(s\) = serial fraction of the sequential execution time
- \(S_A(P)\) = fixed-size speedup

When the processor count approaches infinity:

\[
\lim_{P\to\infty}S_A(P)=\frac{1}{s}
\]

For a workload with a serial fraction of 0.4%:

\[
s=0.004
\]

The theoretical maximum speedup is:

\[
S_{\max}=\frac{1}{0.004}=250
\]

This result seems to suggest that thousands of processors would be inefficient for applications with even a small serial portion.

However, this conclusion applies to a fixed-size workload with a fixed serial fraction.

## 3. Reconstruction of the 1988 Experiment

The researchers used a 1024-processor NCUBE/ten MIMD hypercube system.

The computer had distributed memory, and processors communicated through explicit message passing.

The researchers investigated three practical scientific applications:

1. **Wave mechanics:** simulation using explicit finite-difference methods.
2. **Fluid dynamics:** simulation using flux-corrected transport methods.
3. **Structural analysis:** finite-element calculations using the conjugate-gradient method.

The experiments compared two approaches:

**Fixed-size scaling:** The total problem size remains constant as more processors are used.

**Scaled-size scaling:** The workload grows with the number of processors, allowing each processor to handle a substantial portion of the problem.

The original journal paper reported the following results:

| Performance measure | Reported speedup |
|---|---:|
| Fixed-size parallel speedup | 502–637× |
| Scaled-size parallel speedup | 1009–1020× |

These are reported experimental ranges, not estimates calculated from the simplified formulas.

Gustafson's separate 1988 article also discussed scaled speedups of approximately 1021×, 1020×, and 1016× for three scientific applications.

The small differences reflect the figures reported in the two publications and their measurement presentations.

## 4. Amdahl's Law Calculation

Suppose:

\[
P=1024
\]

and:

\[
s=0.004
\]

Using Amdahl's Law:

\[
S_A(1024)=\frac{1}{0.004+\frac{0.996}{1024}}
\]

Calculate the parallel component:

\[
\frac{0.996}{1024}=0.00097265625
\]

Therefore:

\[
S_A(1024)=\frac{1}{0.00497265625}
\]

\[
\boxed{S_A(1024)\approx201.10}
\]

This is the ideal fixed-size prediction under the assumed serial fraction.

It is significantly smaller than the scaled speedups observed in the Sandia experiments.

However, this calculation does not represent the fixed-size serial fractions measured in the original experiments. It is an illustrative comparison based on the 0.4% value discussed in Gustafson's work.

## 5. Gustafson's Scaled Speedup Calculation

Gustafson's Law assumes that the parallel workload increases with the number of processors.

The scaled speedup formula is:

\[
S_G(P)=P-\alpha(P-1)
\]

Where:

- \(P\) = number of processors
- \(\alpha\) = serial fraction measured relative to parallel execution time

For:

\[
P=1024
\]

\[
\alpha=0.004
\]

We obtain:

\[
S_G(1024)=1024-0.004(1023)
\]

\[
S_G(1024)=1024-4.092
\]

\[
\boxed{S_G(1024)=1019.908}
\]

Therefore, the theoretical scaled speedup is approximately:

\[
\boxed{S_G(1024)\approx1020}
\]

The corresponding parallel efficiency is:

\[
E_G(1024)=\frac{1019.908}{1024}
\]

\[
\boxed{E_G(1024)\approx99.60\%}
\]

This calculation illustrates how a small serial fraction measured on the parallel system permits nearly linear scaled speedup.

The computed value is a model prediction, not an independently measured experimental result.

## 6. Why Problem Expansion Changes the Result

The key difference between Amdahl's and Gustafson's models is the behavior of the workload.

Under Amdahl's Law, a fixed amount of work is distributed across increasing numbers of processors.

Consequently, the sequential portion eventually becomes the dominant limitation.

Under Gustafson's Law, the total workload increases as more processors become available.

For example, scientific researchers can increase:

- Simulation grid resolution
- Number of computational elements
- Spatial domain size
- Number of simulated particles
- Complexity of the physical model

The parallel portion of the computation therefore becomes much larger while the serial overhead may remain relatively small.

Assume that execution time on the parallel machine is normalized:

\[
T_P=s+p=1
\]

The equivalent sequential execution time for the expanded workload is:

\[
T_1=s+Pp
\]

Thus:

\[
S_G(P)=\frac{T_1}{T_P}
\]

\[
S_G(P)=s+Pp
\]

Since:

\[
p=1-s
\]

We obtain:

\[
\boxed{S_G(P)=P-s(P-1)}
\]

The formula explains how scaled speedup can approach the number of processors.

## 7. Why Amdahl's Law Was Not Disproved

The Sandia experiments did not mathematically disprove Amdahl's Law.

Instead, they showed that applying fixed-size assumptions to growing scientific workloads can produce misleading conclusions.

Amdahl's Law answers:

How much faster can an unchanged workload execute using more processors?

Gustafson's Law answers:

How much more computational work can be completed in approximately the same time using additional processors?

These are different performance questions.

For a given workload, both models can be mathematically consistent when their serial fractions are defined relative to the appropriate execution times.

The apparent contradiction occurs when fixed-size assumptions are incorrectly applied to scaled workloads.

## 8. Practical Optimizations Used in the Experiment

The original research also demonstrated the importance of reducing parallel overhead.

The authors employed techniques including:

**Communication overlap:** Communication was scheduled to overlap with useful computation whenever possible.

**Reduced synchronization:** Unnecessary waiting between processors was minimized.

**Domain decomposition:** Large scientific problems were divided into computational subdomains.

**Load balancing:** Work was distributed to reduce differences in processor execution times.

**Communication optimization:** Local message exchanges and efficient communication patterns reduced overhead.

These improvements helped the applications achieve high efficiency on the 1024-processor architecture.

However, scaling performance was not perfect. Communication, redundant work, hardware effects, and load imbalance still introduced efficiency losses.

## 9. Critical Evaluation

The historical results demonstrate that massively parallel systems can be highly effective for scientific problems whose size can grow with available computing resources.

Nevertheless, Gustafson's Law has limitations.

Its ideal model assumes that serial overhead remains sufficiently small as the processor count increases.

In practical systems, communication costs, synchronization overhead, memory bandwidth, and load imbalance can prevent near-linear scaling.

Therefore, Gustafson's Law should be interpreted as a theoretical scaling model rather than a guarantee of unlimited performance.

The experimental findings support workload-aware performance evaluation, not the rejection of Amdahl's mathematical model.

## 10. Conclusion

The 1988 Sandia research demonstrated scaled speedups exceeding 1000 on a 1024-processor hypercube system.

The main reason was the expansion of scientific workloads as more processors became available.

Amdahl's Law predicts performance for a fixed problem size, while Gustafson's Law evaluates scaled workloads.

The fundamental lesson is that serial overhead should be analyzed together with workload size and the measurement reference frame.

The experiments challenged an overly pessimistic application of Amdahl's Law and helped establish weak scaling as an important principle in high-performance computing.

## References

1. Gustafson, J. L., Montry, G. R., and Benner, R. E. (1988). *Development of Parallel Methods for a 1024-Processor Hypercube*. SIAM Journal on Scientific and Statistical Computing, 9(4), 609–638. https://doi.org/10.1137/0909041

2. Gustafson, J. L. (1988). *Reevaluating Amdahl's Law*. Communications of the ACM, 31(5), 532–533. https://doi.org/10.1145/42411.42415