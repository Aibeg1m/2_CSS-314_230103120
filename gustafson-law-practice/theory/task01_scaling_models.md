# Task 01: Strong Scaling vs. Weak Scaling

## 1. Introduction

Amdahl's Law and Gustafson's Law are two important
models in parallel computing. Both describe how
parallel processors improve program performance,
but they use different assumptions.

## 2. Amdahl's Law

Amdahl's Law uses strong scaling.

The total problem size remains constant when the
number of processors increases.

Formula:

S(P) = 1 / (s + (1-s)/P)

Where:
- P = number of processors
- s = serial fraction
- S(P) = speedup

As P approaches infinity, the problem size
remains fixed.

The maximum speedup approaches 1/s when s > 0.

## 3. Gustafson's Law

Gustafson's Law uses weak scaling.

The workload increases with the number of
processors while the parallel execution time
is assumed to remain constant.

Formula:

S(P) = P - alpha(P-1)

Where:
- P = number of processors
- alpha = serial fraction of parallel runtime

As P approaches infinity, the problem size
can increase proportionally with P.

## 4. Main Difference

Amdahl's Law focuses on completing the same
problem faster using more processors.

Gustafson's Law focuses on solving larger
problems within approximately the same time.

## 5. Conclusion

Amdahl's Law is useful for fixed-size problems.

Gustafson's Law is useful for large scientific
applications where workloads can grow with
available computing resources.

Both models are important for understanding
parallel computing performance.