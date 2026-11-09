# Task 11: The Sun and Ni Memory-Bounded Speedup Comparison

## 1. Introduction

Parallel computing performance depends on the number of processors, the serial portion of the program, and how the workload grows as more computing resources become available.

Three important parallel speedup models are:

1. Amdahl's Law — fixed-size scaling.
2. Gustafson's Law — fixed-time scaling.
3. Sun–Ni's Law — memory-bounded scaling.

In 1993, Xian-He Sun and Lionel M. Ni introduced a memory-bounded speedup model in their research paper *Scalable Problems and Memory-Bounded Speedup*.

Their model generalizes the fixed-size and fixed-time approaches by considering how problem size grows with available memory.

The objective of this task is to compare Gustafson's Law with the Sun–Ni model, derive their mathematical relationships, and identify conditions under which Gustafson's Law overestimates or underestimates practical performance.

## 2. Amdahl's Law: Fixed-Size Scaling

Amdahl's Law assumes that the total problem size remains constant as processor count increases.

The formula is:

\[
S_A(P)=\frac{1}{s+\frac{1-s}{P}}
\]

Where:

- \(P\) = number of processors.
- \(s\) = serial fraction of the original sequential execution time.
- \(1-s\) = parallelizable fraction.
- \(S_A(P)\) = fixed-size speedup.

For a positive serial fraction:

\[
\lim_{P\to\infty}S_A(P)=\frac{1}{s}
\]

Therefore, fixed-size speedup has a theoretical upper bound when \(s>0\).

Amdahl's Law is appropriate when the application processes the same workload using different processor counts.

## 3. Gustafson's Law: Fixed-Time Scaling

Gustafson's Law assumes that the workload grows as the number of processors increases while parallel execution time remains approximately constant.

The scaled speedup formula is:

\[
S_G(P)=P-\alpha(P-1)
\]

Where:

- \(P\) = number of processors.
- \(\alpha\) = serial fraction measured on the parallel machine.
- \(S_G(P)\) = scaled speedup.

The formula can also be written as:

\[
S_G(P)=\alpha+(1-\alpha)P
\]

Parallel efficiency is:

\[
E_G(P)=\frac{S_G(P)}{P}
\]

Therefore:

\[
\boxed{E_G(P)=1-\alpha+\frac{\alpha}{P}}
\]

Assuming a constant serial fraction:

\[
\boxed{\lim_{P\to\infty}E_G(P)=1-\alpha}
\]

This model demonstrates that high efficiency can be maintained when larger workloads contain a sufficiently large parallel component.

However, it does not explicitly model restrictions imposed by memory capacity or communication overhead.

## 4. Sun–Ni's Memory-Bounded Speedup Model

Sun and Ni proposed a model in which workload growth is constrained by available memory.

The main idea is that increasing the number of processors often increases total system memory.

This additional memory can support larger scientific datasets and more complex computational problems.

However, the relationship between workload growth and memory growth is application-dependent.

Let:

- \(P\) = number of processors.
- \(k\) = serial fraction of the original baseline workload.
- \(1-k\) = parallel fraction of the baseline workload.
- \(G(P)\) = growth factor of the parallel workload allowed by memory expansion.
- \(S_{MB}(P)\) = memory-bounded speedup.

Assume the original sequential workload is normalized to one unit.

Its serial component is:

\[
W_s=k
\]

Its parallelizable component is:

\[
W_p=1-k
\]

If increased memory allows the parallel workload to grow by a factor \(G(P)\), the equivalent sequential execution time for the expanded workload is:

\[
T_1^*=k+(1-k)G(P)
\]

Assuming ideal distribution of parallel work, execution time on \(P\) processors is:

\[
T_P^*=k+\frac{(1-k)G(P)}{P}
\]

Speedup is defined as:

\[
S_{MB}(P)=\frac{T_1^*}{T_P^*}
\]

Substituting the expressions gives:

\[
\boxed{
S_{MB}(P)=
\frac{k+(1-k)G(P)}
{k+\frac{(1-k)G(P)}{P}}
}
\]

This is the simplified Sun–Ni memory-bounded speedup model.

The equation assumes ideal parallel work distribution, a fixed serial workload component, and no additional communication overhead.

The original research also discusses more general formulations that account for uneven workload allocation and communication costs.

## 5. Mathematical Relationship Between the Three Models

An important property of Sun–Ni's model is that it includes Amdahl's Law and Gustafson's Law as special cases.

### Case 1: No Workload Growth

Suppose the available memory does not increase the workload:

\[
G(P)=1
\]

Substitute into Sun–Ni's formula:

\[
S_{MB}(P)=
\frac{k+(1-k)}
{k+\frac{1-k}{P}}
\]

Since:

\[
k+(1-k)=1
\]

We obtain:

\[
\boxed{
S_{MB}(P)=
\frac{1}{k+\frac{1-k}{P}}
}
\]

This is exactly Amdahl's Law with:

\[
s=k
\]

Therefore:

\[
\boxed{G(P)=1\Rightarrow\text{Amdahl's Law}}
\]

### Case 2: Linear Workload Growth

Suppose the parallel workload increases proportionally with processor count:

\[
G(P)=P
\]

Substitute into Sun–Ni's formula:

\[
S_{MB}(P)=
\frac{k+(1-k)P}
{k+\frac{(1-k)P}{P}}
\]

Simplify the denominator:

\[
k+(1-k)=1
\]

Therefore:

\[
S_{MB}(P)=k+(1-k)P
\]

Rearranging:

\[
S_{MB}(P)=P-k(P-1)
\]

Thus:

\[
\boxed{S_{MB}(P)=P-k(P-1)}
\]

This is Gustafson's scaled speedup formula.

In this special case, \(k\) also equals the serial fraction of the normalized parallel runtime because the parallel execution time equals one unit.

Therefore:

\[
\boxed{G(P)=P\Rightarrow\text{Gustafson's Law}}
\]

These relationships demonstrate that the memory-bounded model generalizes both traditional scaling models.

## 6. Relationship Between Memory and Workload Growth

Assume that the total memory capacity increases linearly with the number of processors:

\[
M(P)=PM_1
\]

Where \(M_1\) is the memory capacity of one processor.

Let the amount of computational work depend on memory size:

\[
W(M)=cM^\beta
\]

Where:

- \(c\) = proportionality constant.
- \(\beta\) = workload-growth exponent.

The workload growth factor is:

\[
G(P)=\frac{W(PM_1)}{W(M_1)}
\]

Substituting:

\[
G(P)=\frac{c(PM_1)^\beta}{cM_1^\beta}
\]

Simplifying:

\[
\boxed{G(P)=P^\beta}
\]

Therefore, Sun–Ni's simplified model becomes:

\[
\boxed{
S_{MB}(P)=
\frac{k+(1-k)P^\beta}
{k+(1-k)P^{\beta-1}}
}
\]

Three important cases arise:

**Case A: \(\beta=0\)**

The workload remains fixed:

\[
G(P)=1
\]

The model becomes Amdahl's Law.

**Case B: \(\beta=1\)**

The workload grows linearly with memory and processor count:

\[
G(P)=P
\]

The model becomes Gustafson's Law.

**Case C: \(\beta>1\)**

Computational work grows faster than memory capacity.

The memory-bounded model can predict a greater speedup than the corresponding linear-growth model, although execution time may increase.

## 7. Numerical Comparison

Consider an application with:

\[
P=16
\]

and original baseline serial fraction:

\[
k=0.10
\]

Therefore:

\[
1-k=0.90
\]

We compare three workload-growth scenarios.

### Scenario 1: Fixed-Size Workload

Assume:

\[
G(P)=1
\]

Using Amdahl's Law:

\[
S_A(16)=\frac{1}{0.10+\frac{0.90}{16}}
\]

\[
S_A(16)=\frac{1}{0.15625}
\]

Therefore:

\[
\boxed{S_A(16)=6.40}
\]

### Scenario 2: Linear Workload Growth

Assume:

\[
G(P)=16
\]

Using Gustafson's Law:

\[
S_G(16)=16-0.10(16-1)
\]

\[
S_G(16)=16-1.5
\]

Therefore:

\[
\boxed{S_G(16)=14.50}
\]

### Scenario 3: Memory-Bounded Workload Growth

Assume memory capacity allows the parallel workload to increase by a factor of four:

\[
G(P)=4
\]

Using Sun–Ni's Law:

\[
S_{MB}(16)=
\frac{0.10+0.90(4)}
{0.10+\frac{0.90(4)}{16}}
\]

Calculate the numerator:

\[
0.10+3.60=3.70
\]

Calculate the denominator:

\[
0.10+\frac{3.60}{16}=0.325
\]

Therefore:

\[
S_{MB}(16)=\frac{3.70}{0.325}
\]

\[
\boxed{S_{MB}(16)\approx11.3846}
\]

The memory-bounded prediction lies between the fixed-size and linear-growth predictions.

## 8. Comparison Table

| Model | Workload Growth Factor | Predicted Speedup | Efficiency |
|---|---:|---:|---:|
| Amdahl | 1 | 6.4000 | 40.00% |
| Sun–Ni | 4 | 11.3846 | 71.15% |
| Gustafson | 16 | 14.5000 | 90.63% |

The comparison demonstrates that predicted speedup depends strongly on how much the workload can increase.

For the same baseline serial fraction, Sun–Ni's model produces a continuum between the fixed-size and fixed-time cases.

## 9. When Gustafson's Law Overestimates Performance

Gustafson's Law may overestimate achievable performance when the application cannot maintain its assumed workload and runtime scaling behavior.

### 9.1 Insufficient Workload Growth

Suppose available memory limits the workload growth factor to:

\[
G(P)<P
\]

The application cannot increase its parallel workload as much as the ideal linear-growth assumption requires.

Under the simplified model with the same baseline serial fraction, this produces a lower memory-bounded speedup than the linear-growth Gustafson case.

For example:

\[
S_{MB}(16)\approx11.38<14.50=S_G(16)
\]

### 9.2 Communication Overhead

Distributed-memory systems require processors to exchange data.

As processor count increases, communication costs may become significant.

Examples include:

- Network latency.
- Message-passing overhead.
- Global synchronization.
- Communication contention.
- Data redistribution.

If these overheads increase with processor count, parallel execution time may no longer remain constant.

### 9.3 Load Imbalance

Some processors may receive more work than others.

The parallel execution time is then determined by the slowest processors.

This reduces real speedup compared with an ideal model assuming balanced work distribution.

### 9.4 Memory Bandwidth Limitations

Increasing memory capacity does not necessarily increase memory bandwidth proportionally.

Applications with irregular access patterns or heavy memory traffic may become bandwidth-bound.

Consequently, additional processors and memory may not produce the expected performance improvement.

## 10. When Gustafson's Law Underestimates Performance

Gustafson's linear-workload formulation can underestimate memory-bounded speedup when increased memory enables computational work to grow faster than processor count.

Consider dense matrix multiplication.

The computational complexity is:

\[
W(N)=O(N^3)
\]

The memory requirement is:

\[
M(N)=O(N^2)
\]

Thus:

\[
N\propto M^{1/2}
\]

Substituting into the computational complexity:

\[
W(M)\propto(M^{1/2})^3
\]

Therefore:

\[
\boxed{W(M)\propto M^{3/2}}
\]

If memory capacity increases by a factor of \(P\):

\[
\boxed{G(P)=P^{3/2}}
\]

Since:

\[
P^{3/2}>P\qquad(P>1)
\]

the computational workload grows faster than the processor count.

For the simplified Sun–Ni model, take:

\[
P=16,\qquad k=0.10
\]

Then:

\[
G(16)=16^{3/2}=64
\]

The memory-bounded speedup is:

\[
S_{MB}(16)=
\frac{0.10+0.90(64)}
{0.10+\frac{0.90(64)}{16}}
\]

Simplifying:

\[
S_{MB}(16)=\frac{57.70}{3.70}
\]

\[
\boxed{S_{MB}(16)\approx15.5946}
\]

This exceeds the linear-growth Gustafson prediction:

\[
S_G(16)=14.50
\]

Therefore:

\[
\boxed{S_{MB}(16)>S_G(16)}
\]

This comparison must be interpreted carefully.

The larger memory-bounded speedup does not imply that the expanded workload finishes in constant time.

In this example, the parallel execution time is:

\[
T_P^*=3.70
\]

rather than one normalized time unit.

The higher speedup reflects a larger amount of computational work and a smaller serial proportion relative to the expanded workload.

It is not evidence of superlinear efficiency, since the speedup remains below the processor count.

## 11. Critical Analysis

Gustafson's Law and Sun–Ni's Law describe different resource constraints.

Gustafson's Law emphasizes the relationship between workload expansion, processor count, and approximately constant execution time.

Sun–Ni's Law emphasizes the relationship between workload expansion and available memory capacity.

These models are mathematically related, but their practical predictions depend on application characteristics.

| Feature | Gustafson's Law | Sun–Ni's Law |
|---|---|---|
| Main constraint | Approximately fixed execution time | Available memory |
| Workload growth | Linear-growth special case | Application-dependent |
| Memory capacity | Not explicit | Explicitly influences workload |
| Serial fraction | Measured in parallel runtime | Baseline fraction in simplified formulation |
| Communication overhead | Not explicit in classical formula | Considered in more general formulations |
| Suitable applications | Efficiently scalable parallel workloads | Memory-limited scientific computations |
| Main limitation | Assumes favorable weak scaling | Requires an accurate workload-memory model |

The most important observation is that memory growth and workload growth are not necessarily identical.

An application may have:

\[
G(P)<P
\]

when memory constraints or application characteristics limit workload expansion.

Alternatively:

\[
G(P)>P
\]

when computational complexity grows faster than the memory footprint.

Thus, Sun–Ni's formulation provides a more flexible framework for analyzing memory-dependent applications.

Nevertheless, both simplified models rely on ideal assumptions.

Actual performance must also consider communication, synchronization, memory bandwidth, load imbalance, and processor overhead.

## 12. Engineering Implications

When selecting a scaling model, parallel software engineers should consider the application's primary resource constraint.

Amdahl's Law is appropriate when the problem size is fixed.

Gustafson's Law is appropriate when larger workloads can be solved in approximately constant time.

Sun–Ni's model is appropriate when the maximum problem size depends on available memory.

For scientific simulations, engineers should estimate:

1. Available aggregate memory.
2. Memory required per computational element.
3. Computational complexity as a function of problem size.
4. Expected workload growth with memory capacity.
5. Communication and synchronization costs.
6. Actual parallel execution time.

These measurements help determine whether a simplified theoretical scaling prediction is realistic.

## 13. Conclusion

Sun–Ni's memory-bounded speedup model generalizes Amdahl's and Gustafson's laws by introducing an application-dependent workload-growth factor.

The simplified model is:

\[
\boxed{
S_{MB}(P)=
\frac{k+(1-k)G(P)}
{k+\frac{(1-k)G(P)}{P}}
}
\]

When:

\[
G(P)=1
\]

the model becomes Amdahl's Law.

When:

\[
G(P)=P
\]

the model becomes Gustafson's Law.

When:

\[
G(P)=P^\beta
\]

the model captures different relationships between memory capacity and computational workload.

Gustafson's Law may overestimate performance when memory constraints limit useful workload growth or when communication overhead prevents ideal weak scaling.

It may underestimate memory-bounded speedup when computational work grows faster than memory capacity, although such workloads may require longer execution time.

The main conclusion is that memory capacity, workload complexity, and communication overhead must be considered together when evaluating practical parallel scalability.

## References

1. Sun, X.-H., & Ni, L. M. (1993). *Scalable Problems and Memory-Bounded Speedup*. Journal of Parallel and Distributed Computing, 19(1), 27–37. https://doi.org/10.1006/jpdc.1993.1087

2. Gustafson, J. L. (1988). *Reevaluating Amdahl's Law*. Communications of the ACM, 31(5), 532–533. https://doi.org/10.1145/42411.42415

3. Sun, X.-H., & Ni, L. M. (1992). *Scalable Problems and Memory-Bounded Speedup*. NASA Technical Report NASA-CR-189726. https://ntrs.nasa.gov/citations/19930007365