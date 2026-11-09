# Task 19: Monte Carlo Path Simulation — The Ideal Weak Scaling Model

## 1. Introduction

Monte Carlo simulation uses random samples to estimate numerical results. Since samples can be computed independently, Monte Carlo is an example of an *embarrassingly parallel* workload.

However, large-scale implementations still experience overhead from:

- Pseudo-random number generator (PRNG) initialization.
- Random seed management.
- Global reduction operations.
- Output serialization and data collection.

The objective is to analyze these overheads and determine how tree-based reductions influence Gustafson's scaled speedup.

## 2. Ideal Weak Scaling

Let:

- \(P\) = number of processors.
- \(k\) = number of samples per processor.
- \(N\) = total number of samples.

Under weak scaling:

\[
\boxed{N=kP}
\]

If each sample requires \(t\) seconds, computation time per processor is:

\[
\boxed{T_{\text{compute}}=kt}
\]

Since \(k\) remains constant, ideal parallel runtime is independent of processor count.

Gustafson's Law predicts:

\[
\boxed{S_G(P)=P-\alpha(P-1)}
\]

where \(\alpha\) is the serial fraction measured during parallel execution.

For nearly zero serial overhead:

\[
\alpha\approx0
\]

Therefore:

\[
\boxed{S_G(P)\approx P}
\]

This explains why Monte Carlo methods are well suited to weak scaling.

## 3. Sources of Serial Overhead

### PRNG Seed Management

Each processor needs an independent or properly partitioned pseudo-random sequence.

Seed distribution and generator initialization can introduce serial or coordination overhead.

If a central process initializes every worker sequentially, setup cost may increase as:

\[
T_{\text{seed}}(P)=O(P)
\]

Independent counter-based generators or deterministic per-worker stream initialization can reduce this overhead.

### Output Serialization

If every processor sends all generated samples to one process, output costs may grow with \(P\).

A better approach is to compute local statistics and communicate only partial results.

For example, each processor can return a local sum and sample count instead of sending all samples.

### Reduction Operations

Monte Carlo integration requires combining partial results.

For example:

\[
\hat I=\frac{1}{N}\sum_{i=1}^{N}f(X_i)
\]

Each processor calculates a local sum:

\[
L_j=\sum_{i=1}^{k}f(X_{j,i})
\]

The final result is:

\[
\boxed{\hat I=\frac{1}{kP}\sum_{j=1}^{P}L_j}
\]

Combining the local sums requires a reduction operation.

## 4. Tree-Based Reduction Analysis

A sequential reduction of \(P\) partial results requires:

\[
O(P)
\]

combination steps on one processor.

A balanced binary reduction tree combines values in parallel.

At each stage, the number of participating values is approximately halved.

The number of stages is:

\[
\boxed{L(P)=\lceil\log_2P\rceil}
\]

Assuming each reduction stage requires a fixed time \(\lambda\):

\[
\boxed{T_{\text{reduction}}(P)=\lambda\lceil\log_2P\rceil}
\]

For powers of two:

| Processors | Reduction Stages |
|---:|---:|
| 2 | 1 |
| 4 | 2 |
| 8 | 3 |
| 16 | 4 |
| 64 | 6 |
| 256 | 8 |
| 1024 | 10 |

Tree reductions significantly reduce communication depth compared with sequential aggregation.

However, reduction overhead still grows logarithmically.

## 5. Communication-Aware Scaled Speedup

Let the useful computation consist of:

- Serial time \(s\).
- Parallel time \(p\).

Normalize:

\[
s+p=1
\]

The equivalent sequential execution time is:

\[
T_1=s+Pp
\]

Assume that tree-reduction overhead is additional and is not already included in \(s\) or \(p\).

Define normalized overhead:

\[
C(P)=\beta\log_2P
\]

where \(\beta\) represents the reduction-stage cost relative to normalized useful runtime.

The modified parallel execution time is:

\[
T_P=1+C(P)
\]

Therefore:

\[
S(P)=\frac{s+Pp}{1+C(P)}
\]

Using:

\[
s=\alpha,\qquad p=1-\alpha
\]

we obtain:

\[
\boxed{
S(P)=\frac{P-\alpha(P-1)}{1+\beta\log_2P}
}
\]

This is a simplified communication-aware extension of Gustafson's Law.

It assumes that the equivalent sequential workload excludes additional parallel reduction overhead.

## 6. Numerical Example

Assume:

\[
P=256
\]

\[
\alpha=0.01
\]

\[
\beta=0.005
\]

First, calculate ideal Gustafson speedup:

\[
S_G(256)=256-0.01(255)
\]

\[
\boxed{S_G(256)=253.45}
\]

Now calculate reduction overhead:

\[
C(256)=0.005\log_2(256)
\]

\[
C(256)=0.005(8)
\]

\[
\boxed{C(256)=0.04}
\]

Communication-aware speedup:

\[
S(256)=\frac{253.45}{1.04}
\]

\[
\boxed{S(256)=243.70}
\]

Parallel efficiency:

\[
E(256)=\frac{243.70}{256}
\]

\[
\boxed{E(256)\approx95.20\%}
\]

Without the additional reduction penalty, Gustafson efficiency would be:

\[
E_G(256)=\frac{253.45}{256}
\]

\[
\boxed{E_G(256)\approx99.00\%}
\]

Thus, the modeled tree-reduction overhead reduces scaled speedup from 253.45 to approximately 243.70.

These are theoretical calculations, not measured benchmark results.

## 7. Asymptotic Behavior

For nearly perfect parallel computation, let:

\[
\alpha=0
\]

Then:

\[
S(P)=\frac{P}{1+\beta\log_2P}
\]

For a fixed positive \(\beta\), as \(P\) becomes large:

\[
\boxed{S(P)=\Theta\left(\frac{P}{\log P}\right)}
\]

Efficiency becomes:

\[
E(P)=\frac{1}{1+\beta\log_2P}
\]

Therefore:

\[
\boxed{\lim_{P\to\infty}E(P)=0}
\]

This result shows that logarithmically growing reduction overhead eventually decreases efficiency, even for an otherwise highly parallel workload.

In practice, large sample counts per processor can make reduction time relatively small.

## 8. Optimization Strategies

Monte Carlo scalability can be improved by:

1. Using independent or counter-based PRNG streams.
2. Initializing seeds without centralized sequential bottlenecks.
3. Aggregating results locally before communication.
4. Using balanced tree-based reductions.
5. Avoiding unnecessary sample output.
6. Overlapping communication with computation when possible.

These strategies reduce the effective serial fraction and communication overhead.

## 9. Conclusion

Monte Carlo simulation is well suited to weak scaling because samples can be evaluated independently.

Under ideal conditions:

\[
\boxed{S_G(P)\approx P}
\]

However, PRNG initialization, output serialization, and global reductions introduce non-zero overhead.

A balanced reduction tree requires:

\[
\boxed{O(\log P)}
\]

communication stages.

A simplified communication-aware speedup model is:

\[
\boxed{
S(P)=\frac{P-\alpha(P-1)}{1+\beta\log_2P}
}
\]

The main conclusion is that Monte Carlo methods can achieve near-linear scaled speedup when computation dominates communication and reduction overhead is minimized.