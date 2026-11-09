# Task 10: Memory Growth Rate vs. Scaled Speedup

## 1. Introduction

Weak scaling is an important concept in parallel computing. It describes a situation where the total problem size increases proportionally with the number of processors while the workload per processor remains approximately constant.

Gustafson's Law assumes that larger problems can be processed using additional computing resources without significantly increasing execution time.

However, physical memory limits the maximum problem size that can be stored and processed.

The objective of this task is to analyze memory growth and calculate the maximum dimension of a three-dimensional computational grid across 64 and 512 computing nodes.

## 2. Given Parameters

Under pure weak scaling, the total workload grows proportionally with processor count:

\[
W(P)=P\cdot W(1)
\]

The total memory requirement follows:

\[
M(P)=cP
\]

Where:

- \(P\) = number of computing nodes
- \(W(P)\) = total workload
- \(M(P)\) = total memory consumption
- \(c\) = memory required per node

Each computing node has a maximum memory capacity of:

\[
M_{\text{node}}=32\text{ GB}
\]

The cluster configurations are:

\[
P_1=64
\]

\[
P_2=512
\]

The grid is three-dimensional:

\[
N\times N\times N
\]

Therefore, the total number of grid cells is:

\[
N_{\text{cells}}=N^3
\]

The memory complexity is:

\[
M(N)=O(N^3)
\]

Our goal is to determine the maximum possible grid dimension \(N\).

## 3. Total Cluster Memory

The total memory available across \(P\) nodes is:

\[
M_{\text{total}}(P)=P\cdot M_{\text{node}}
\]

Since each node has 32 GB:

\[
\boxed{M_{\text{total}}(P)=32P\text{ GB}}
\]

### Case 1: 64 Nodes

\[
M_{\text{total}}(64)=64\times32
\]

\[
\boxed{M_{\text{total}}(64)=2048\text{ GB}}
\]

This is equivalent to approximately 2 TB in decimal units.

### Case 2: 512 Nodes

\[
M_{\text{total}}(512)=512\times32
\]

\[
\boxed{M_{\text{total}}(512)=16384\text{ GB}}
\]

This is equivalent to approximately 16 TB in decimal units.

The second cluster has eight times the total memory capacity:

\[
\frac{16384}{2048}=8
\]

## 4. Memory Requirements for a 3D Grid

A cubic grid contains:

\[
N^3
\]

computational cells.

Let \(b\) represent the memory required to store one grid cell, measured in bytes.

Then the total memory requirement is:

\[
M(N)=bN^3
\]

The grid must fit within the available cluster memory:

\[
bN^3\leq M_{\text{total}}(P)
\]

Substituting:

\[
bN^3\leq P\cdot M_{\text{node}}
\]

Divide by \(b\):

\[
N^3\leq\frac{P\cdot M_{\text{node}}}{b}
\]

Take the cube root:

\[
N\leq\sqrt[3]{\frac{P\cdot M_{\text{node}}}{b}}
\]

Therefore, the general maximum grid dimension is:

\[
\boxed{N_{\max}=\left\lfloor\sqrt[3]{\frac{P\cdot M_{\text{node}}}{b}}\right\rfloor}
\]

This formula assumes that memory is distributed across the nodes, with sufficiently balanced grid partitions.

It also assumes that all available memory can be used for storing grid cells.

## 5. Assumption About Memory per Grid Cell

The assignment specifies the memory available per node but does not specify how many bytes are required per grid cell.

Therefore, a unique numerical value of \(N\) cannot be determined without an additional assumption.

For this worked example, assume each grid cell stores one double-precision floating-point value.

A double-precision value requires:

\[
b=8\text{ bytes}
\]

We will also interpret the 32 GB per-node memory limit as 32 GiB for the numerical example.

Thus:

\[
M_{\text{node}}=32\times2^{30}\text{ bytes}
\]

\[
\boxed{M_{\text{node}}=34,359,738,368\text{ bytes}}
\]

This is an illustrative assumption. Actual memory requirements depend on the solver's data structures, number of stored variables, and temporary arrays.

## 6. Maximum Grid Dimension for 64 Nodes

Given:

\[
P=64
\]

The total available memory is:

\[
M_{\text{total}}=64\times32\times2^{30}
\]

\[
M_{\text{total}}=2,199,023,255,552\text{ bytes}
\]

Each grid cell requires 8 bytes.

The maximum number of cells is:

\[
N^3\leq\frac{2,199,023,255,552}{8}
\]

\[
N^3\leq274,877,906,944
\]

Take the cube root:

\[
N\leq\sqrt[3]{274,877,906,944}
\]

\[
N\leq6501.9947
\]

Because the number of cells along each dimension must be an integer:

\[
\boxed{N_{\max}(64)=6501}
\]

Therefore, the largest theoretical cubic grid that fits within the total capacity has dimensions:

\[
\boxed{6501\times6501\times6501}
\]

This is an aggregate memory ceiling, assuming ideal distribution and no additional memory overhead.

## 7. Maximum Grid Dimension for 512 Nodes

Given:

\[
P=512
\]

The total available memory is:

\[
M_{\text{total}}=512\times32\times2^{30}
\]

\[
M_{\text{total}}=17,592,186,044,416\text{ bytes}
\]

The number of possible grid cells is:

\[
N^3\leq\frac{17,592,186,044,416}{8}
\]

\[
N^3\leq2,199,023,255,552
\]

Take the cube root:

\[
N\leq\sqrt[3]{2,199,023,255,552}
\]

\[
N\leq13003.9894
\]

Taking the integer floor:

\[
\boxed{N_{\max}(512)=13003}
\]

Therefore, the largest theoretical cubic grid that fits within the total capacity has dimensions:

\[
\boxed{13003\times13003\times13003}
\]

Again, this is an ideal aggregate capacity bound.

## 8. Comparison of Results

| Parameter | 64 Nodes | 512 Nodes |
|---|---:|---:|
| Memory per node | 32 GiB | 32 GiB |
| Total cluster memory | 2048 GiB | 16384 GiB |
| Bytes per grid cell | 8 | 8 |
| Maximum grid cells | 274,877,906,944 | 2,199,023,255,552 |
| Maximum cubic dimension \(N\) | 6501 | 13003 |
| Maximum grid dimensions | 6501³ | 13003³ |

The number of nodes increases by a factor of:

\[
\frac{512}{64}=8
\]

The total memory capacity also increases by a factor of eight.

The linear grid dimension increases approximately by:

\[
\frac{13003}{6501}\approx2
\]

Therefore:

\[
\boxed{N(512)\approx2N(64)}
\]

This occurs because the memory requirement grows with the cube of the grid dimension.

## 9. Weak Scaling Relationship

Under ideal weak scaling:

\[
W(P)\propto P
\]

For a 3D computational grid:

\[
W(P)\propto N^3
\]

Combining these relationships:

\[
N^3\propto P
\]

Taking the cube root gives:

\[
\boxed{N\propto P^{1/3}}
\]

Therefore, increasing the number of computing nodes by a factor of eight increases the maximum linear grid dimension by a factor of two.

In general:

\[
\boxed{\frac{N_2}{N_1}=\left(\frac{P_2}{P_1}\right)^{1/3}}
\]

For 64 and 512 nodes:

\[
\frac{N_2}{N_1}=\left(\frac{512}{64}\right)^{1/3}
\]

\[
=\sqrt[3]{8}
\]

\[
\boxed{\frac{N_2}{N_1}=2}
\]

This exact factor applies to the continuous scaling model. Integer grid dimensions introduce small rounding differences.

## 10. Relationship with Gustafson's Law

Gustafson's Law is defined as:

\[
S(P)=P-\alpha(P-1)
\]

The law assumes that problem size can increase with available parallel computing resources.

For a memory-bound 3D grid application, increasing the number of nodes allows the total number of grid cells to increase proportionally with \(P\), provided the per-cell storage requirement remains constant.

However, increasing memory capacity does not automatically guarantee constant execution time.

Actual weak scaling also depends on computational complexity, communication overhead, memory bandwidth, and load balancing.

For example, boundary communication between subdomains may introduce additional execution time even when the number of cells per node remains fixed.

Thus, Gustafson's Law describes a theoretical performance model, while the memory calculation determines the maximum workload that can physically fit within the cluster.

## 11. Practical Memory Limitations

The calculated grid dimensions represent theoretical upper bounds.

Real scientific applications require additional memory for:

- Operating system processes.
- Input and output buffers.
- Temporary arrays.
- Communication buffers.
- Grid boundary and halo cells.
- Multiple variables per grid cell.
- Solver metadata and auxiliary data structures.

For example, if each cell requires 64 bytes instead of 8 bytes, the maximum linear grid dimension decreases by:

\[
\left(\frac{8}{64}\right)^{1/3}
\]

\[
=\frac{1}{2}
\]

Therefore, an application using 64 bytes per cell can support only approximately half the linear grid dimension of the 8-byte-per-cell example.

In addition, the global memory bound may not be attainable with a particular domain decomposition if nodes have unequal memory demands or additional halo storage.

## 12. Conclusion

Under pure weak scaling, total memory capacity grows linearly with the number of nodes:

\[
\boxed{M(P)=cP}
\]

For a three-dimensional grid:

\[
\boxed{N_{\max}=\left\lfloor\sqrt[3]{\frac{PM_{\text{node}}}{b}}\right\rfloor}
\]

Using an illustrative assumption of 8 bytes per cell and 32 GiB per node:

For 64 nodes:

\[
\boxed{N_{\max}=6501}
\]

For 512 nodes:

\[
\boxed{N_{\max}=13003}
\]

The key scaling relationship is:

\[
\boxed{N\propto P^{1/3}}
\]

This demonstrates that increasing the number of computing nodes increases total grid capacity proportionally, but the linear dimension of a 3D grid grows only with the cube root of processor count.

Memory capacity establishes the theoretical maximum problem size, while achieving Gustafson-style weak scaling additionally requires efficient computation and communication.