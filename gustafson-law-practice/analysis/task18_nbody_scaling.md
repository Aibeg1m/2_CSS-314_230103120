# Task 18: N-Body Gravitational Problem Scaling

## 1. Introduction

The N-body gravitational problem simulates interactions between particles under gravitational forces.

Two common algorithms are:

- **Direct all-pairs:** \(O(N^2)\)
- **Barnes–Hut tree-code:** \(O(N\log N)\)

The objective is to determine how particle count \(N\) must increase with processor count \(P\) to maintain approximately constant parallel execution time and analyze changes in the serial-to-parallel ratio.

## 2. Direct All-Pairs Algorithm

Every particle interacts with every other particle.

The number of interactions is:

\[
\frac{N(N-1)}{2}
\]

Therefore:

\[
W_{\text{direct}}(N)=\Theta(N^2)
\]

Assuming ideal parallel execution:

\[
T_P(N)=\frac{cN^2}{P}
\]

For constant runtime:

\[
\frac{N^2}{P}=k
\]

Therefore:

\[
N^2\propto P
\]

\[
\boxed{N(P)\propto P^{1/2}}
\]

Using a reference particle count \(N_0\):

\[
\boxed{N(P)=N_0\sqrt P}
\]

Thus, increasing processors by a factor of four allows the particle count to double under ideal fixed-time scaling.

## 3. Barnes–Hut Algorithm

Barnes–Hut approximates distant particle groups using a hierarchical spatial tree.

Its typical computational complexity is:

\[
W_{\text{BH}}(N)=O(N\log N)
\]

Assume ideal parallel execution with work proportional to \(N\log N\):

\[
T_P(N)=\frac{cN\log N}{P}
\]

For constant runtime:

\[
\frac{N\log N}{P}=k
\]

Therefore:

\[
\boxed{N\log N\propto P}
\]

Unlike the direct method, this equation cannot be solved using a simple power law.

Let:

\[
N\ln N=kP
\]

Using the Lambert W function:

\[
\boxed{N(P)=\frac{kP}{W_0(kP)}}
\]

where \(W_0\) is the principal branch of the Lambert W function.

For large \(P\):

\[
\boxed{N(P)=\Theta\left(\frac{P}{\log P}\right)}
\]

Thus, Barnes–Hut supports approximately linear particle-count growth, with a logarithmic correction.

## 4. Numerical Scaling Comparison

Assume:

\[
N_0=1000
\]

For the direct method:

\[
N_{\text{direct}}(P)=1000\sqrt P
\]

For Barnes–Hut, preserve the baseline work per processor:

\[
N(P)\ln N(P)=1000\ln(1000)\,P
\]

The approximate results are:

| Processors \(P\) | Direct All-Pairs \(N\) | Barnes–Hut \(N\) |
|---:|---:|---:|
| 1 | 1,000 | 1,000 |
| 4 | 2,000 | 3,374 |
| 16 | 4,000 | 11,597 |
| 64 | 8,000 | 40,506 |
| 256 | 16,000 | 143,465 |

The values are theoretical scaling targets, not measured benchmark results.

Barnes–Hut permits a larger particle-count increase because it has lower asymptotic computational complexity.

## 5. Serial-to-Parallel Ratio Analysis

Let:

- \(T_s(N,P)\) = serial or coordination time.
- \(T_{\text{parallel}}(N,P)\) = useful parallel computation time.

Define:

\[
\boxed{R(P)=\frac{T_s(N,P)}{T_{\text{parallel}}(N,P)}}
\]

### Direct All-Pairs

Assume serial setup takes:

\[
T_s(N)=aN
\]

and parallel computation takes:

\[
T_{\text{parallel}}=\frac{bN^2}{P}
\]

Then:

\[
R_{\text{direct}}(P)=\frac{aN}{bN^2/P}
\]

\[
\boxed{R_{\text{direct}}(P)=\frac{aP}{bN}}
\]

Under ideal fixed-time scaling:

\[
N\propto P^{1/2}
\]

Therefore:

\[
\boxed{R_{\text{direct}}(P)=\Theta(P^{1/2})}
\]

Under this serial-setup assumption, the serial-to-parallel ratio increases as processor count grows.

### Barnes–Hut

Assume tree construction and coordination require a serial cost proportional to:

\[
T_s(N)=aN\log N
\]

Useful parallel computation requires:

\[
T_{\text{parallel}}=\frac{bN\log N}{P}
\]

Therefore:

\[
R_{\text{BH}}(P)=
\frac{aN\log N}{bN\log N/P}
\]

\[
\boxed{R_{\text{BH}}(P)=\frac{a}{b}P}
\]

Thus:

\[
\boxed{R_{\text{BH}}(P)=\Theta(P)}
\]

Under this fully serial tree-construction assumption, serial overhead becomes increasingly important.

However, practical Barnes–Hut implementations can parallelize tree construction and use distributed trees, reducing this bottleneck.

These ratios are conditional on the stated serial-cost models, not universal properties of the algorithms.

## 6. Practical Limitations

The previous scaling relationships assume perfect parallelization of the dominant computational work.

Real N-body applications may experience:

- Particle communication between processors.
- Load imbalance caused by nonuniform particle distributions.
- Tree construction and traversal overhead.
- Synchronization delays.
- Network bandwidth limitations.
- Memory and cache constraints.

Direct all-pairs methods have predictable computation but potentially expensive particle-data communication.

Barnes–Hut reduces arithmetic complexity but introduces irregular tree structures and communication.

If serial and communication overhead grow, the actual runtime may exceed the ideal constant-time target.

## 7. Conclusion

The ideal particle-count scaling relationships are:

**Direct all-pairs:**

\[
\boxed{N(P)=\Theta(P^{1/2})}
\]

**Barnes–Hut:**

\[
\boxed{N(P)=\Theta\left(\frac{P}{\log P}\right)}
\]

For the illustrative serial-overhead assumptions:

\[
\boxed{R_{\text{direct}}(P)=\Theta(P^{1/2})}
\]

\[
\boxed{R_{\text{BH}}(P)=\Theta(P)}
\]

Barnes–Hut enables substantially larger particle-count growth than direct all-pairs computation under ideal fixed-time scaling.

However, both algorithms require careful management of serial work, communication, and load balancing to approach Gustafson-style weak scaling.