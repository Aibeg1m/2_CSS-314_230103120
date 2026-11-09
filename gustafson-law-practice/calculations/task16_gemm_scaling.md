# Task 16: Dense Matrix Multiplication Scaling (GEMM)

## 1. Introduction

Dense matrix multiplication calculates:

\[
C=A\times B
\]

where \(A\), \(B\), and \(C\) are \(N\times N\) matrices.

The computational complexity is:

\[
W(N)=O(N^3)
\]

The memory complexity is:

\[
M(N)=O(N^2)
\]

The objective is to determine how matrix dimension \(N\) must grow with processor count \(P\) under Gustafson's fixed-time scaling assumption.

## 2. Mathematical Derivation

Under ideal parallel execution:

\[
T_P(N)\propto\frac{N^3}{P}
\]

Gustafson's fixed-time assumption requires:

\[
T_P(N)=\text{constant}
\]

Therefore:

\[
\frac{N^3}{P}=k
\]

where \(k\) is constant.

Rearranging:

\[
N^3=kP
\]

Taking the cube root:

\[
\boxed{N\propto P^{1/3}}
\]

For a reference matrix dimension \(N_0\) on one processor:

\[
\boxed{N(P)=N_0P^{1/3}}
\]

Thus, increasing the processor count by a factor of eight doubles the matrix dimension.

## 3. Numerical Scaling Table

Assume the initial matrix dimension is:

\[
N_0=1024
\]

| Processors \(P\) | Dimension \(N\) | Matrix Size | Work Growth |
|---:|---:|---|---:|
| 1 | 1024 | 1024 × 1024 | 1× |
| 8 | 2048 | 2048 × 2048 | 8× |
| 64 | 4096 | 4096 × 4096 | 64× |
| 512 | 8192 | 8192 × 8192 | 512× |
| 4096 | 16384 | 16384 × 16384 | 4096× |

The computational work per processor remains constant:

\[
\frac{N(P)^3}{P}=N_0^3
\]

This demonstrates ideal weak scaling.

## 4. Memory Scaling Analysis

Memory consumption grows as:

\[
M(N)\propto N^2
\]

Substitute:

\[
N(P)=N_0P^{1/3}
\]

Then:

\[
M(P)\propto(N_0P^{1/3})^2
\]

Therefore:

\[
\boxed{M(P)\propto P^{2/3}}
\]

Memory required per processor is:

\[
M_{\text{per processor}}\propto\frac{P^{2/3}}{P}
\]

\[
\boxed{M_{\text{per processor}}\propto P^{-1/3}}
\]

For example, increasing processor count from 1 to 8 doubles \(N\), increases total memory fourfold, and reduces memory per processor by half under ideal distribution.

If three dense double-precision matrices are stored:

\[
M(N)\approx3(8N^2)=24N^2\text{ bytes}
\]

This excludes temporary buffers and other implementation overhead.

## 5. Practical Limitations

The ideal model assumes perfect workload distribution.

Real GEMM performance may be affected by:

- Communication between processors.
- Memory bandwidth limitations.
- Data distribution and synchronization.
- Cache efficiency and load balancing.

Therefore, constant runtime is an ideal theoretical prediction rather than a guarantee.

## 6. Conclusion

For dense matrix multiplication:

\[
\boxed{N(P)=N_0P^{1/3}}
\]

The scaling relationships are:

\[
\boxed{W(P)\propto P}
\]

\[
\boxed{M(P)\propto P^{2/3}}
\]

\[
\boxed{M_{\text{per processor}}\propto P^{-1/3}}
\]

Thus, matrix dimension must increase with the cube root of processor count to maintain constant ideal computation time. This is consistent with Gustafson's weak-scaling principle.