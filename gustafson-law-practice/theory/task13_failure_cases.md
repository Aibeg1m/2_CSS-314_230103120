# Task 13: Boundary Case — When Gustafson Fails

## 1. Introduction

Gustafson's Law describes the potential speedup of parallel applications when the workload increases with the number of processors.

The formula is:

\[
S_G(P)=P-\alpha(P-1)
\]

Where:

- \(P\) = number of processors.
- \(\alpha\) = serial fraction measured during parallel execution.
- \(S_G(P)\) = scaled speedup.

The key assumption behind ideal weak scaling is that the workload per processor remains approximately constant while the total parallel execution time remains nearly constant.

However, some algorithms cannot maintain constant execution time as processor count increases.

This may occur because of:

- Communication overhead.
- Global synchronization.
- Load imbalance.
- Increasing computational complexity.
- Memory access contention.
- Sequential dependencies.

This report analyzes two concrete algorithms where ideal weak scaling fails:

1. Parallel Breadth-First Search (BFS) on irregular graphs.
2. Parallel dense Gaussian elimination with partial pivoting.

The analysis demonstrates why Gustafson's constant-runtime premise can break down for these workloads.

## 2. Mathematical Foundation

For an ideally weak-scaling application, the total amount of work increases proportionally with processor count:

\[
W(P)=PW(1)
\]

If the parallel workload is distributed evenly:

\[
T_{\text{compute}}(P)=\frac{W(P)}{P}
\]

Substitute:

\[
T_{\text{compute}}(P)=\frac{PW(1)}{P}
\]

Therefore:

\[
\boxed{T_{\text{compute}}(P)=W(1)}
\]

The useful computational time remains constant.

However, practical parallel runtime also includes overhead:

\[
T_P=T_{\text{compute}}(P)+T_{\text{comm}}(P)+T_{\text{sync}}(P)+T_{\text{imbalance}}(P)
\]

Where:

- \(T_{\text{comm}}\) = communication time.
- \(T_{\text{sync}}\) = synchronization time.
- \(T_{\text{imbalance}}\) = additional time caused by unequal work distribution.

Even when useful computational time remains constant, total runtime can increase if overhead grows with processor count.

The constant-runtime premise fails when:

\[
\boxed{T_P(P)\not\approx\text{constant}}
\]

for increasing \(P\).

## 3. Failure Case 1: Parallel Breadth-First Search (BFS)

### 3.1 Algorithm Description

Breadth-First Search is a graph traversal algorithm that explores vertices level by level.

Starting from a source vertex, BFS visits its immediate neighbors before exploring vertices at greater distances.

BFS is widely used in:

- Social network analysis.
- Shortest-path problems in unweighted graphs.
- Web graph processing.
- Network connectivity analysis.
- Distributed graph analytics.

The sequential computational complexity of BFS using adjacency lists is:

\[
\boxed{T_{\text{seq}}=O(V+E)}
\]

Where:

- \(V\) = number of vertices.
- \(E\) = number of edges.

Although BFS contains parallelizable operations, dependencies between traversal levels create synchronization requirements.

### 3.2 Parallel BFS Execution

A common parallel BFS implementation follows these steps:

1. Initialize the source vertex.
2. Identify the current frontier.
3. Distribute frontier vertices among processors.
4. Explore neighboring vertices in parallel.
5. Exchange discovered vertices between processors.
6. Synchronize processors.
7. Construct the next frontier.
8. Repeat until the traversal finishes.

The next BFS level cannot be completed before the current frontier has been processed.

Therefore, the algorithm contains global coordination requirements.

### 3.3 Weak-Scaling Assumption

Assume a sparse graph with a constant average degree.

Under weak scaling:

\[
V(P)=PV_0
\]

Where \(V_0\) is the number of vertices per processor.

If the average number of edges per vertex remains constant:

\[
E(P)=O(V(P))
\]

Therefore:

\[
E(P)=O(PV_0)
\]

The useful work per processor is approximately:

\[
\frac{V(P)+E(P)}{P}=O(V_0)
\]

This suggests constant useful computation per processor.

However, constant useful work does not guarantee constant total execution time.

### 3.4 Synchronization Overhead

BFS processes graph vertices in levels.

Let:

\[
L(P)
\]

represent the number of BFS levels or the maximum source eccentricity reached during traversal.

Suppose each level requires a global coordination operation with latency:

\[
t_{\text{sync}}(P)
\]

The total synchronization cost is approximately:

\[
T_{\text{sync}}(P)=L(P)t_{\text{sync}}(P)
\]

For a simplified tree-based collective operation:

\[
t_{\text{sync}}(P)=c\log_2P
\]

Where \(c\) is the synchronization latency coefficient.

Therefore:

\[
\boxed{T_{\text{sync}}(P)=cL(P)\log_2P}
\]

If the number of BFS levels remains constant, synchronization overhead still increases logarithmically under this assumed communication model.

If the graph diameter also increases, the synchronization cost can grow faster.

For example, for a family of sparse path-like graphs:

\[
L(P)=\Theta(V(P))
\]

With:

\[
V(P)=PV_0
\]

We obtain:

\[
L(P)=\Theta(P)
\]

Thus, using the simplified tree-synchronization model:

\[
\boxed{T_{\text{sync}}(P)=\Theta(P\log P)}
\]

This is a particularly unfavorable weak-scaling case.

The exact behavior depends on graph topology and the BFS implementation.

### 3.5 Load Imbalance

Graph workloads often contain irregular vertex degrees.

Some vertices may have only a few neighbors, while others may have thousands or millions.

If vertices are distributed without considering degree, processors receive unequal amounts of work.

Let:

\[
W_i
\]

represent the amount of work assigned to processor \(i\).

The parallel computation time is constrained by the slowest processor:

\[
T_{\text{compute}}(P)\propto\max_i W_i
\]

Even when average work is constant:

\[
\frac{1}{P}\sum_{i=1}^{P}W_i=W_0
\]

it does not follow that:

\[
\max_iW_i=W_0
\]

A high-degree vertex can create a large imbalance.

Therefore, average workload per processor may remain constant while actual runtime increases.

### 3.6 Communication Overhead

Distributed BFS requires processors to exchange information about newly discovered vertices.

If a vertex and its neighbor are stored on different processors, the discovery may require communication.

Total communication depends on:

- Graph partitioning.
- Number of cut edges.
- Frontier size.
- Network topology.
- Message aggregation.
- Vertex-degree distribution.

An approximate performance model is:

\[
T_{\text{BFS}}(P)=
T_{\text{local}}(P)
+T_{\text{messages}}(P)
+T_{\text{sync}}(P)
+T_{\text{imbalance}}(P)
\]

Even if:

\[
T_{\text{local}}(P)=O(1)
\]

the remaining terms may grow with \(P\).

Therefore:

\[
\boxed{T_{\text{BFS}}(P)\not\approx\text{constant}}
\]

### 3.7 Why Gustafson's Assumption Fails

Parallel BFS can fail to achieve ideal weak scaling because:

1. Traversal levels introduce sequential dependencies.
2. Global synchronization may become more expensive.
3. Irregular vertex degrees cause load imbalance.
4. Distributed frontiers generate communication overhead.
5. Graph structure can change as the workload expands.

Consequently, increasing the number of processors does not necessarily preserve constant execution time.

**Conclusion for BFS:** Irregular graph structure and level-by-level dependencies can prevent ideal Gustafson-style weak scaling.

## 4. Failure Case 2: Parallel Gaussian Elimination with Partial Pivoting

### 4.1 Algorithm Description

Gaussian elimination solves systems of linear equations:

\[
Ax=b
\]

Where:

- \(A\) is an \(N\times N\) matrix.
- \(x\) is the unknown vector.
- \(b\) is the right-hand-side vector.

The algorithm transforms the matrix into an upper triangular form.

Partial pivoting improves numerical stability by selecting a suitable pivot row.

Dense Gaussian elimination requires approximately:

\[
\boxed{W(N)=O(N^3)}
\]

arithmetic operations.

Its dense matrix storage requirement is:

\[
\boxed{M(N)=O(N^2)}
\]

The algorithm can parallelize matrix updates, but pivot selection and panel factorization introduce dependencies.

### 4.2 Parallel Execution

A simplified parallel implementation performs:

1. Pivot selection.
2. Possible row exchange.
3. Panel factorization.
4. Pivot and panel data distribution.
5. Parallel trailing-matrix updates.
6. Repetition for subsequent elimination steps.

The trailing-matrix update contains substantial parallel work.

However, the next elimination stage depends on results from earlier stages.

This creates a sequence of dependent computational phases.

### 4.3 Weak-Scaling Problem

For a constant amount of arithmetic work per processor, assume:

\[
\frac{N^3}{P}=\text{constant}
\]

Therefore:

\[
N^3\propto P
\]

Taking the cube root:

\[
\boxed{N(P)\propto P^{1/3}}
\]

Thus, the matrix dimension must grow approximately with the cube root of processor count under this fixed-arithmetic-work condition.

The number of elimination stages is proportional to matrix dimension:

\[
L(N)=\Theta(N)
\]

Substituting the scaling relationship:

\[
L(P)=\Theta(P^{1/3})
\]

Therefore, the number of sequentially dependent stages increases as the processor count grows.

Even when total arithmetic work per processor remains constant, the algorithm requires more dependent stages.

### 4.4 Pivot Selection Overhead

Partial pivoting requires choosing a pivot row based on numerical values.

In a distributed-memory implementation, pivot selection can require reductions and communication.

Assume each pivot-selection operation requires:

\[
t_{\text{pivot}}(P)=c\log_2P
\]

under an idealized tree-based collective communication model.

Since there are approximately \(N\) pivot stages:

\[
T_{\text{pivot}}(P)=\Theta(N\log P)
\]

Using:

\[
N\propto P^{1/3}
\]

We obtain:

\[
\boxed{T_{\text{pivot}}(P)=\Theta(P^{1/3}\log P)}
\]

This growing overhead can violate the constant-runtime assumption.

The expression is an illustrative model. Actual implementations use blocked algorithms, hierarchical collectives, and other optimizations that can change communication costs.

### 4.5 Communication and Row Exchanges

Pivoting may require exchanging matrix rows between processors.

Parallel factorization also requires distributing panel and pivot information.

Communication time can be modeled as:

\[
T_{\text{comm}}(P)
=
T_{\text{latency}}(P)
+
T_{\text{transfer}}(P)
\]

A simple latency-bandwidth model for a message is:

\[
T_{\text{message}}=\lambda+\frac{m}{B}
\]

Where:

- \(\lambda\) = message startup latency.
- \(m\) = message size.
- \(B\) = effective network bandwidth.

As processor count and matrix dimension increase, the number of communication stages and message patterns may change.

These effects can increase total execution time even when arithmetic work per processor is held constant.

### 4.6 Dependency and Parallelism Limits

Gaussian elimination contains a dependency chain across elimination stages.

The next stage requires information produced by the preceding stage.

Let:

\[
T_{\text{critical}}(N)
\]

represent the critical-path execution time.

Even with unlimited processors:

\[
T_P(N)\geq T_{\text{critical}}(N)
\]

For a simplified algorithm with at least one positive-latency dependent operation per elimination stage:

\[
T_{\text{critical}}(N)=\Omega(N)
\]

Under arithmetic weak scaling:

\[
N\propto P^{1/3}
\]

Therefore:

\[
\boxed{T_{\text{critical}}(P)=\Omega(P^{1/3})}
\]

This simplified dependency lower bound shows why constant execution time cannot be guaranteed as the matrix grows.

Optimized blocked and communication-avoiding factorizations can reduce practical overhead, but they do not eliminate all dependencies.

### 4.7 Overall Runtime Model

A simplified parallel runtime model is:

\[
T_{\text{GE}}(P)=
T_{\text{arithmetic}}(P)
+
T_{\text{pivot}}(P)
+
T_{\text{communication}}(P)
+
T_{\text{dependency}}(P)
\]

Under arithmetic weak scaling:

\[
T_{\text{arithmetic}}(P)\approx\text{constant}
\]

However, pivoting, communication, and dependency costs may increase.

Therefore:

\[
\boxed{T_{\text{GE}}(P)\not\approx\text{constant}}
\]

This demonstrates a failure mode of ideal weak scaling.

### 4.8 Why Gustafson's Assumption Fails

Gaussian elimination with partial pivoting can fail to achieve ideal weak scaling because:

1. The number of elimination stages grows with matrix dimension.
2. Pivot selection introduces global coordination.
3. Row exchanges require communication.
4. Panel factorizations contain sequential dependencies.
5. Communication and synchronization costs may grow with processor count.

**Conclusion for Gaussian elimination:** Increasing matrix size introduces additional dependent stages and communication requirements, preventing guaranteed constant execution time.

## 5. Comparison of the Two Algorithms

| Characteristic | Parallel BFS | Gaussian Elimination |
|---|---|---|
| Problem type | Graph traversal | Dense linear algebra |
| Sequential complexity | \(O(V+E)\) | \(O(N^3)\) |
| Main parallel operation | Frontier exploration | Matrix updates |
| Main bottleneck | Irregular frontier and synchronization | Pivoting and panel dependencies |
| Communication pattern | Irregular vertex messages | Matrix panels, pivots, and row exchanges |
| Load imbalance | Often significant | Usually more predictable |
| Sequential dependency | BFS levels | Elimination stages |
| Weak-scaling difficulty | Graph structure and coordination | Growing critical path and communication |

Both algorithms demonstrate that constant work per processor does not automatically imply constant execution time.

However, the reasons differ.

BFS is limited mainly by irregular workload distribution and level-based synchronization.

Gaussian elimination is limited by sequential dependencies, pivot selection, and communication.

## 6. Numerical Illustration

Consider an idealized application with:

\[
T_{\text{compute}}=1\text{ second}
\]

Assume the communication and synchronization overhead is:

\[
T_{\text{overhead}}(P)=0.02\log_2P
\]

Then:

\[
T_P=1+0.02\log_2P
\]

The predicted runtimes are:

| Processors | Useful Computation | Overhead | Total Runtime |
|---:|---:|---:|---:|
| 1 | 1.00 s | 0.00 s | 1.00 s |
| 4 | 1.00 s | 0.04 s | 1.04 s |
| 16 | 1.00 s | 0.08 s | 1.08 s |
| 64 | 1.00 s | 0.12 s | 1.12 s |
| 256 | 1.00 s | 0.16 s | 1.16 s |
| 1024 | 1.00 s | 0.20 s | 1.20 s |

Although useful computation remains constant, total execution time increases.

This example is hypothetical and illustrates the effect of growing communication overhead.

It is not measured performance data for BFS or Gaussian elimination.

## 7. Impact on Parallel Efficiency

Classical Gustafson efficiency is:

\[
E_G(P)=1-\alpha+\frac{\alpha}{P}
\]

With a constant serial fraction, the efficiency approaches:

\[
\lim_{P\to\infty}E_G(P)=1-\alpha
\]

However, when additional non-overlapped communication overhead is introduced, an illustrative extended model is:

\[
S_C(P)=\frac{P-\alpha(P-1)}{1+C(P)}
\]

Where \(C(P)\) is additional overhead normalized relative to useful execution time.

Parallel efficiency becomes:

\[
E_C(P)=
\frac{1-\alpha+\frac{\alpha}{P}}
{1+C(P)}
\]

If:

\[
C(P)\to\infty
\]

then for a fixed \(\alpha\):

\[
\boxed{\lim_{P\to\infty}E_C(P)=0}
\]

Therefore, even when the serial fraction of useful work remains constant, growing communication overhead can cause efficiency to decline toward zero.

This demonstrates that Gustafson's ideal efficiency prediction is not guaranteed for algorithms with significant communication and synchronization costs.

## 8. Potential Optimization Strategies

### 8.1 Optimizing Parallel BFS

Weak-scaling performance can be improved through:

- Degree-aware graph partitioning.
- Dynamic load balancing.
- Frontier compression.
- Message aggregation.
- Direction-optimizing BFS.
- Reducing remote memory access.
- Avoiding unnecessary global synchronization.

These methods can reduce communication and improve processor utilization.

However, they do not guarantee ideal weak scaling for every graph family.

### 8.2 Optimizing Gaussian Elimination

Parallel Gaussian elimination can be improved through:

- Blocked matrix algorithms.
- Communication-avoiding factorization.
- Efficient collective operations.
- Overlapping communication and computation.
- Load-balanced matrix distribution.
- Optimized BLAS routines.
- Hierarchical pivot selection.

These techniques reduce overhead and improve scalability.

Nevertheless, numerical dependencies and communication requirements remain important constraints.

## 9. Critical Discussion

Gustafson's Law is a useful theoretical model for understanding the benefits of increasing workload size with processor count.

However, it should not be interpreted as a universal guarantee of scalable performance.

The model is most applicable when:

1. The workload can increase with processor count.
2. Useful work can be distributed efficiently.
3. Serial overhead remains sufficiently small.
4. Communication does not grow excessively.
5. Processor workloads remain balanced.

Parallel BFS and Gaussian elimination violate some of these conditions in challenging scaling regimes.

BFS may experience increasing synchronization, irregular communication, and load imbalance.

Gaussian elimination may experience a growing dependency chain and additional pivot-related communication.

Therefore, both algorithms can fail to maintain constant runtime under weak scaling.

The extent of failure depends on the workload, processor architecture, data distribution, and implementation.

Neither algorithm is guaranteed to fail under every finite processor configuration, but both provide clear examples where ideal weak-scaling assumptions become unrealistic.

## 10. Conclusion

This task analyzed two concrete parallel algorithms where Gustafson's ideal weak-scaling assumptions may fail.

**Algorithm 1: Parallel Breadth-First Search**

Its main limitations are:

- Level-by-level synchronization.
- Irregular memory access.
- Communication overhead.
- Load imbalance.
- Graph-dependent traversal depth.

**Algorithm 2: Parallel Gaussian Elimination with Partial Pivoting**

Its main limitations are:

- Sequential elimination stages.
- Pivot-selection communication.
- Row exchanges.
- Growing critical-path requirements.
- Synchronization overhead.

The general parallel runtime model is:

\[
\boxed{
T_P=T_{\text{compute}}
+T_{\text{comm}}
+T_{\text{sync}}
+T_{\text{imbalance}}
}
\]

Even if useful computation per processor remains constant, total execution time may increase because of the additional overhead terms.

The main conclusion is that ideal weak scaling requires more than constant work per processor.

Successful scaling also requires low communication overhead, efficient synchronization, balanced workloads, and sufficiently independent parallel computation.

## References

1. Gustafson, J. L. (1988). *Reevaluating Amdahl's Law*. Communications of the ACM, 31(5), 532–533. https://doi.org/10.1145/42411.42415

2. Beamer, S., Asanović, K., & Patterson, D. (2012). *Direction-Optimizing Breadth-First Search*. Proceedings of SC12. https://doi.org/10.1109/SC.2012.50

3. Demmel, J., Grigori, L., Hoemmen, M., & Langou, J. (2012). *Communication-Optimal Parallel and Sequential QR and LU Factorizations*. SIAM Journal on Scientific Computing, 34(1), A206–A239. https://doi.org/10.1137/080731992