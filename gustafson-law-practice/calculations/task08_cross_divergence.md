# Task 08: Cross-Over Point Determination (Amdahl vs. Gustafson)

## 1. Introduction

Amdahl's Law and Gustafson's Law are two important mathematical models used to evaluate parallel computing performance.

Amdahl's Law describes strong scaling, where the total problem size remains constant.

Gustafson's Law describes scaled speedup, where the workload grows with the available processing resources.

The objective of this task is to calculate the speedup predicted by both models for 128 processors and compare the results.

## 2. Given Parameters

The number of processors is:

\[
P=128
\]

The serial fraction for Amdahl's Law is:

\[
s=0.08
\]

The serial fraction for Gustafson's Law is:

\[
\alpha=0.08
\]

Therefore, the parallel fraction is:

\[
1-0.08=0.92
\]

We need to calculate:

1. Amdahl's predicted speedup.
2. Gustafson's predicted scaled speedup.
3. Absolute and percentage discrepancy.
4. Reasons for the difference between the models.

## 3. Amdahl's Law Calculation

Amdahl's Law is defined as:

\[
S_A(P)=\frac{1}{s+\frac{1-s}{P}}
\]

Substitute the given values:

\[
S_A(128)=\frac{1}{0.08+\frac{0.92}{128}}
\]

Calculate the parallel component:

\[
\frac{0.92}{128}=0.0071875
\]

Add the serial component:

\[
0.08+0.0071875=0.0871875
\]

Therefore:

\[
S_A(128)=\frac{1}{0.0871875}
\]

The predicted speedup is:

\[
\boxed{S_A(128)\approx11.4695}
\]

Thus, Amdahl's Law predicts approximately 11.47 times faster execution on 128 processors for the fixed-size workload.

### Amdahl's Parallel Efficiency

Parallel efficiency is:

\[
E_A(P)=\frac{S_A(P)}{P}
\]

Therefore:

\[
E_A(128)=\frac{11.469534}{128}
\]

\[
\boxed{E_A(128)\approx0.089606}
\]

Expressed as a percentage:

\[
\boxed{E_A(128)\approx8.96\%}
\]

## 4. Gustafson's Law Calculation

Gustafson's scaled speedup formula is:

\[
S_G(P)=P-\alpha(P-1)
\]

Substitute the given values:

\[
S_G(128)=128-0.08(128-1)
\]

Simplify:

\[
S_G(128)=128-0.08(127)
\]

Calculate:

\[
0.08\times127=10.16
\]

Therefore:

\[
S_G(128)=128-10.16
\]

The predicted scaled speedup is:

\[
\boxed{S_G(128)=117.84}
\]

Thus, Gustafson's Law predicts a scaled speedup of 117.84.

### Gustafson's Parallel Efficiency

Parallel efficiency is:

\[
E_G(P)=\frac{S_G(P)}{P}
\]

Therefore:

\[
E_G(128)=\frac{117.84}{128}
\]

\[
\boxed{E_G(128)=0.920625}
\]

Expressed as a percentage:

\[
\boxed{E_G(128)=92.0625\%}
\]

## 5. Absolute Discrepancy

The absolute difference between the two predictions is:

\[
\Delta S=S_G(P)-S_A(P)
\]

Substitute:

\[
\Delta S=117.84-11.469534
\]

Therefore:

\[
\boxed{\Delta S\approx106.3705}
\]

Gustafson's predicted scaled speedup exceeds Amdahl's fixed-size prediction by approximately 106.37.

## 6. Percentage Discrepancy

We calculate the percentage discrepancy relative to Amdahl's predicted speedup.

The formula is:

\[
D=\frac{|S_G(P)-S_A(P)|}{S_A(P)}\times100\%
\]

Substitute the values:

\[
D=\frac{|117.84-11.469534|}{11.469534}\times100\%
\]

Simplify:

\[
D=\frac{106.370466}{11.469534}\times100\%
\]

Therefore:

\[
\boxed{D=927.4175\%}
\]

The Gustafson prediction is approximately 927.42% higher than the Amdahl prediction.

The percentage discrepancy depends on the chosen reference denominator. In this task, Amdahl's speedup is explicitly used as the reference value.

The ratio of the two predictions is:

\[
R=\frac{117.84}{11.469534}
\]

\[
\boxed{R\approx10.2742}
\]

Therefore, Gustafson's predicted speedup is approximately 10.27 times Amdahl's predicted speedup under the stated parameter assumptions.

## 7. Comparison Table

| Metric | Amdahl's Law | Gustafson's Law |
|---|---:|---:|
| Processors | 128 | 128 |
| Numerical serial fraction | 8% | 8% |
| Scaling model | Strong scaling | Scaled/weak scaling |
| Workload size | Fixed | Increasing |
| Predicted speedup | 11.4695 | 117.8400 |
| Parallel efficiency | 8.96% | 92.06% |

Additional comparison:

| Metric | Result |
|---|---:|
| Absolute speedup difference | 106.3705 |
| Percentage discrepancy relative to Amdahl | 927.4175% |
| Gustafson-to-Amdahl speedup ratio | 10.2742 |

## 8. Why the Models Diverge

The difference between the results comes from their underlying assumptions.

### Amdahl's Law

Amdahl's Law assumes a fixed total workload.

As more processors are introduced, the parallel part executes faster, but the sequential part remains unchanged.

For a fixed serial fraction \(s>0\), the maximum theoretical speedup is:

\[
S_{A,\max}=\frac{1}{s}
\]

For:

\[
s=0.08
\]

The maximum speedup is:

\[
S_{A,\max}=\frac{1}{0.08}
\]

\[
\boxed{S_{A,\max}=12.5}
\]

Thus, adding more processors cannot produce unlimited speedup for this fixed-size workload.

### Gustafson's Law

Gustafson's Law assumes that the workload can increase with processor count while execution time remains approximately constant.

Its scaled speedup is:

\[
S_G(P)=P-\alpha(P-1)
\]

Rearranging:

\[
S_G(P)=\alpha+(1-\alpha)P
\]

For:

\[
\alpha=0.08
\]

We obtain:

\[
S_G(P)=0.08+0.92P
\]

Therefore, scaled speedup grows approximately linearly with processor count.

For \(P=128\), it reaches 117.84.

## 9. Important Difference in Serial Fraction Measurement

Although this task uses:

\[
s=\alpha=0.08
\]

the two fractions have different definitions.

In Amdahl's Law, \(s\) is measured relative to the equivalent single-processor execution time.

In Gustafson's Law, \(\alpha\) is measured relative to the parallel execution time.

For the same workload under ideal parallel execution, these fractions are related by:

\[
s=\frac{\alpha}{P-\alpha(P-1)}
\]

For:

\[
P=128,\qquad\alpha=0.08
\]

The corresponding Amdahl serial fraction would be:

\[
s=\frac{0.08}{117.84}
\]

\[
\boxed{s\approx0.00067889}
\]

Using this consistent fraction in Amdahl's Law gives:

\[
\boxed{S_A(128)=117.84}
\]

Therefore, the large discrepancy obtained earlier is not a mathematical contradiction.

It results from using the same numerical value for two differently defined serial fractions under different workload assumptions.

## 10. Conclusion

For 128 processors and a numerical serial fraction of 8%, the calculated predictions are:

**Amdahl's Law:**

\[
\boxed{S_A(128)\approx11.4695}
\]

**Gustafson's Law:**

\[
\boxed{S_G(128)=117.84}
\]

**Percentage discrepancy relative to Amdahl's prediction:**

\[
\boxed{D\approx927.42\%}
\]

The models produce significantly different predictions because Amdahl's Law considers fixed-size workloads, while Gustafson's Law considers scaled workloads.

This comparison demonstrates the importance of choosing the correct scaling model and consistently defining the serial fraction when evaluating parallel computing performance.