# Task 20: Parallel Graph Traversal & Irregular Workloads

## 1. Introduction

Parallel graph algorithms such as Breadth-First Search (BFS) and PageRank are difficult to scale efficiently on power-law graphs.

Unlike dense matrix multiplication, graph algorithms have irregular memory access, uneven workloads, and data-dependent communication.

The objective is to explain why achieving Gustafson-style weak scaling is more difficult for graph analytics than for regular dense linear algebra.

## 2. Breadth-First Search (BFS)

BFS explores a graph level by level.

Its sequential complexity is:

\[
\boxed{T_{\text{BFS}}=O(V+E)}
\]

where:

- \(V\) = number of vertices
- \(E\) = number of edges

Under weak scaling:

\[
V(P)=PV_0,\qquad E(P)=PE_0
\]

The useful work per processor remains approximately constant:

\[
\frac{V(P)+E(P)}{P}=V_0+E_0
\]

However, BFS requires synchronization between traversal levels.

A simplified parallel runtime model is:

\[
\boxed{T_{\text{BFS}}(P)=T_{\text{local}}+T_{\text{comm}}+T_{\text{sync}}+T_{\text{imbalance}}}
\]

In power-law graphs, high-degree vertices may create large frontiers and unequal workloads.

As a result, communication, synchronization, and load imbalance can prevent constant execution time.

## 3. PageRank

PageRank calculates vertex importance using iterative updates.

A simplified PageRank equation is:

\[
PR(v)=\frac{1-d}{V}+d\sum_{u\rightarrow v}\frac{PR(u)}{\deg^+(u)}
\]

where \(d\) is the damping factor and \(\deg^+(u)\) is the outgoing degree of vertex \(u\).

Each iteration typically requires:

\[
\boxed{O(V+E)}
\]

computational work.

Under ideal weak scaling, each processor handles approximately constant numbers of vertices and edges.

However, PageRank introduces:

- Communication of vertex contributions
- Synchronization between iterations
- Irregular memory access
- Unequal work distribution

If the number of iterations is \(I\):

\[
\boxed{T_{\text{PageRank}}(P)=I(P)\left(T_{\text{local}}+T_{\text{comm}}(P)+T_{\text{sync}}(P)\right)}
\]

If communication overhead or iteration count increases with processor count, execution time also increases.

Thus, ideal weak scaling may fail.

## 4. Why Power-Law Graphs Are Difficult

Power-law graphs contain many low-degree vertices and a small number of extremely high-degree vertices.

This structure creates three major problems.

**1. Load imbalance**

Some processors process high-degree vertices while others finish early.

\[
T_{\text{compute}}\propto\max_i W_i
\]

where \(W_i\) represents the workload assigned to processor \(i\).

**2. Irregular memory access**

Graph traversal follows adjacency relationships rather than predictable contiguous memory locations.

This causes cache misses and random memory access.

**3. Communication and synchronization**

Graph edges frequently connect vertices stored on different processors.

This requires remote data exchange and synchronization.

As processor count increases, these overheads may become significant.

## 5. Comparison with Dense Linear Algebra

Dense matrix multiplication has regular computational patterns.

For two \(N\times N\) matrices:

\[
\boxed{W_{\text{GEMM}}=O(N^3)}
\]

Its data is stored in predictable arrays, allowing optimized memory access and block-based computation.

| Characteristic | BFS | PageRank | Dense GEMM |
|---|---|---|---|
| Workload | Irregular | Irregular | Regular |
| Memory access | Random | Graph-dependent | Predictable |
| Load balancing | Difficult | Degree-dependent | Relatively easy |
| Synchronization | Every BFS level | Every iteration | Usually block-level |
| Communication | Frontier exchanges | Vertex contributions | Matrix-block exchanges |
| Weak scaling | Challenging | Challenging | More predictable |

Dense GEMM often achieves better scaling because computation is regular and substantial arithmetic work can be performed per communication operation.

Graph algorithms frequently have lower arithmetic intensity and less predictable data dependencies.

## 6. Gustafson's Law and Graph Scaling

Gustafson's Law states:

\[
\boxed{S_G(P)=P-\alpha(P-1)}
\]

It assumes favorable workload expansion and approximately constant parallel execution time.

For graph algorithms, an effective serial or coordination fraction may increase with processor count:

\[
\alpha=\alpha(P)
\]

A simplified model is:

\[
S(P)=P-\alpha(P)(P-1)
\]

However, this expression is only a qualitative extension when communication and runtime change; actual scaled speedup must be measured against the equivalent sequential execution time.

If communication and synchronization increase, efficiency may decrease even when the number of vertices per processor remains constant.

Therefore, Gustafson's ideal weak-scaling assumptions are harder to maintain for irregular graph workloads.

## 7. Possible Optimizations

Graph-processing scalability can be improved through:

- Degree-aware graph partitioning
- Dynamic load balancing
- Communication aggregation
- Frontier compression for BFS
- Direction-optimizing BFS
- Efficient sparse-matrix operations for PageRank
- Reducing unnecessary synchronization

These methods reduce communication and improve processor utilization.

However, performance still depends on graph structure and hardware architecture.

## 8. Conclusion

BFS and PageRank are more difficult to weak-scale than dense matrix algorithms because of irregular memory access, uneven vertex degrees, and data-dependent synchronization.

Although their useful workload per processor may remain constant, communication and coordination overhead can increase with processor count.

Dense linear algebra generally scales more predictably because of its regular data structures and higher computational intensity.

**The main conclusion is that Gustafson-style weak scaling requires not only increasing problem size, but also balanced workloads, efficient memory access, and controlled communication overhead.**