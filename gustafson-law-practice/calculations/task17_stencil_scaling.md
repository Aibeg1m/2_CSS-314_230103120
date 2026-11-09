# Task 17: 3D Stencil Hydrodynamics Simulation

## 1. Introduction

A 7-point 3D stencil computes each grid cell using its own value and six neighboring cells.

For a cubic grid of size \(N\times N\times N\):

- Computational work: \(O(N^3)\)
- Boundary communication: \(O(N^2)\)

The objective is to analyze the communication-to-computation ratio under Gustafson's weak-scaling assumptions.

## 2. Surface-to-Volume Ratio

The computational volume is:

\[
V=N^3
\]

For a cubic subdomain, the total boundary surface area is approximately:

\[
A=6N^2
\]

Therefore, the communication-to-computation ratio is:

\[
R(N)=\frac{6N^2}{N^3}
\]

Simplifying:

\[
\boxed{R(N)=\frac{6}{N}}
\]

Thus:

\[
\boxed{R(N)=O(N^{-1})}
\]

As the local grid dimension increases, the ratio decreases because volume grows faster than surface area.

## 3. Weak-Scaling Derivation

Under ideal weak scaling, total grid volume grows proportionally with processor count:

\[
N_{\text{global}}^3=PN_0^3
\]

Therefore:

\[
\boxed{N_{\text{global}}=N_0P^{1/3}}
\]

where \(N_0\) is the local cubic grid dimension per processor.

Each processor handles:

\[
V_{\text{local}}=N_0^3
\]

Its boundary communication is approximately:

\[
A_{\text{local}}=6N_0^2
\]

Therefore:

\[
R_{\text{local}}=\frac{6N_0^2}{N_0^3}
\]

\[
\boxed{R_{\text{local}}=\frac{6}{N_0}}
\]

Since \(N_0\) remains constant:

\[
\boxed{R_{\text{local}}=O(1)}
\]

Thus, the local communication-to-computation ratio remains approximately constant under ideal weak scaling.

## 4. Global vs. Local Scaling

The global surface-to-volume ratio is:

\[
R_{\text{global}}=\frac{6}{N_{\text{global}}}
\]

Substituting:

\[
N_{\text{global}}=N_0P^{1/3}
\]

gives:

\[
\boxed{R_{\text{global}}=\frac{6}{N_0P^{1/3}}}
\]

Therefore:

\[
\boxed{R_{\text{global}}\propto P^{-1/3}}
\]

The global exterior surface-to-volume ratio improves as the domain grows.

However, this does not mean interprocessor communication decreases. Internal subdomain boundaries still require halo exchanges.

For constant local subdomain size, communication per processor remains approximately constant, although network contention and synchronization can increase.

## 5. Numerical Example

Assume:

\[
N_0=64
\]

The local computation is:

\[
V_{\text{local}}=64^3=262144
\]

The local boundary area is:

\[
A_{\text{local}}=6(64^2)=24576
\]

Therefore:

\[
R_{\text{local}}=\frac{24576}{262144}
\]

\[
\boxed{R_{\text{local}}=0.09375}
\]

Consider different processor counts:

| Processors \(P\) | Global Grid Dimension | Local Grid Dimension | Local Surface/Volume Ratio |
|---:|---:|---:|---:|
| 1 | 64 | 64 | 0.09375 |
| 8 | 128 | 64 | 0.09375 |
| 64 | 256 | 64 | 0.09375 |
| 512 | 512 | 64 | 0.09375 |
| 4096 | 1024 | 64 | 0.09375 |

The total problem grows while the workload and approximate boundary exchange per processor remain constant.

The boundary area used here is a geometric approximation; actual communication depends on the number of neighboring subdomains and halo layers.

## 6. Communication and Runtime Model

A simplified parallel runtime is:

\[
T(P)=T_{\text{compute}}+T_{\text{communication}}
\]

For one local cubic domain:

\[
T_{\text{compute}}\approx aN_0^3
\]

A simple latency-bandwidth communication model is:

\[
T_{\text{communication}}\approx6\lambda+6bN_0^2
\]

where:

- \(a\) = computation time per cell
- \(\lambda\) = message startup latency
- \(b\) = communication time per boundary cell

Therefore:

\[
\boxed{T(P)\approx aN_0^3+6\lambda+6bN_0^2}
\]

Under ideal weak scaling, \(N_0\) remains constant, so this runtime can remain approximately constant.

In real systems, growing network congestion, synchronization, and load imbalance may increase communication time.

## 7. Conclusion

The surface-to-volume ratio of a cubic 3D stencil is:

\[
\boxed{R(N)=\frac{6}{N}}
\]

Under ideal weak scaling:

\[
\boxed{N_{\text{global}}\propto P^{1/3}}
\]

The global exterior surface-to-volume ratio decreases as \(P^{-1/3}\), while the local communication-to-computation ratio remains approximately constant.

Therefore, a 3D stencil can achieve favorable weak scaling when local grid dimensions remain fixed and communication overhead is efficiently managed.