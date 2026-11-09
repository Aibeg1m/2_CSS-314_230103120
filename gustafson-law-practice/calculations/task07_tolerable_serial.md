# Task 07: Reverse Engineering Maximum Tolerable Serial Overhead

## 1. Introduction

Gustafson's Law describes scaled speedup in a parallel computing system when the workload increases with the number of processors.

In this task, we calculate the maximum serial fraction that a supercomputing cluster can tolerate while satisfying a required minimum scaled speedup.

## 2. Given Parameters

The supercomputing cluster has:

\[
P=8192
\]

The required minimum scaled speedup is:

\[
S(P)\geq7500
\]

We must determine:

\[
\alpha_{\max}=?
\]

Where:

- \(P\) = number of processing cores
- \(S(P)\) = scaled speedup
- \(\alpha\) = serial fraction measured during parallel execution

## 3. Gustafson's Law

The scaled speedup formula is:

\[
S(P)=P-\alpha(P-1)
\]

Substitute the given processor count:

\[
S(8192)=8192-\alpha(8192-1)
\]

Simplify:

\[
S(8192)=8192-8191\alpha
\]

The speedup must be at least 7500:

\[
8192-8191\alpha\geq7500
\]

## 4. Step-by-Step Algebraic Derivation

Start with:

\[
8192-8191\alpha\geq7500
\]

Subtract 8192 from both sides:

\[
-8191\alpha\geq7500-8192
\]

\[
-8191\alpha\geq-692
\]

Divide both sides by \(-8191\).

Since we divide by a negative number, the inequality sign must reverse:

\[
\alpha\leq\frac{692}{8191}
\]

Therefore:

\[
\boxed{\alpha_{\max}=\frac{692}{8191}}
\]

This is the exact maximum allowable serial fraction.

Converting to a decimal:

\[
\alpha_{\max}\approx0.0844829691
\]

Converting to a percentage:

\[
\boxed{\alpha_{\max}\approx8.4483\%}
\]

## 5. Numerical Verification

Substitute the exact maximum serial fraction into Gustafson's Law:

\[
S(8192)=8192-\frac{692}{8191}(8191)
\]

Cancel the denominator:

\[
S(8192)=8192-692
\]

Therefore:

\[
\boxed{S(8192)=7500}
\]

The result satisfies the required minimum speedup exactly.

### Testing a Lower Serial Fraction

Suppose:

\[
\alpha=0.08
\]

Then:

\[
S(8192)=8192-0.08(8191)
\]

\[
S(8192)=8192-655.28
\]

\[
\boxed{S(8192)=7536.72}
\]

Since:

\[
7536.72\geq7500
\]

The requirement is satisfied.

### Testing a Higher Serial Fraction

Suppose:

\[
\alpha=0.09
\]

Then:

\[
S(8192)=8192-0.09(8191)
\]

\[
S(8192)=8192-737.19
\]

\[
\boxed{S(8192)=7454.81}
\]

Since:

\[
7454.81<7500
\]

The requirement is not satisfied.

## 6. Required Parallel Efficiency

Parallel efficiency is:

\[
E(P)=\frac{S(P)}{P}
\]

At the required speedup:

\[
E(8192)=\frac{7500}{8192}
\]

Therefore:

\[
E(8192)=0.91552734375
\]

\[
\boxed{E(8192)\approx91.55\%}
\]

The cluster must achieve at least approximately 91.55% scaled parallel efficiency.

## 7. General Formula

Starting from Gustafson's Law:

\[
S(P)=P-\alpha(P-1)
\]

For a required minimum speedup \(S_{\min}\):

\[
P-\alpha(P-1)\geq S_{\min}
\]

Rearrange:

\[
\alpha(P-1)\leq P-S_{\min}
\]

For \(P>1\), divide by \(P-1\):

\[
\boxed{\alpha_{\max}=\frac{P-S_{\min}}{P-1}}
\]

This formula is valid when:

\[
1\leq S_{\min}\leq P
\]

It allows engineers to calculate the maximum tolerable serial overhead for a given processor count and required scaled speedup.

## 8. Interpretation

The result shows that the application can tolerate a maximum serial fraction of approximately 8.4483% under Gustafson's idealized scaling model.

If the serial fraction is lower than this limit, the predicted scaled speedup exceeds 7500.

If the serial fraction is greater than this limit, the predicted scaled speedup falls below the required performance baseline.

In practical computing systems, communication, synchronization, memory access, and load imbalance may influence the observed serial fraction.

Therefore, software engineers should monitor these overheads and maintain sufficient performance margins.

## 9. Conclusion

For a supercomputing cluster with 8192 cores and a minimum required scaled speedup of 7500, the maximum allowable serial fraction is:

\[
\boxed{\alpha_{\max}=\frac{692}{8191}\approx0.0844829691}
\]

Expressed as a percentage:

\[
\boxed{\alpha_{\max}\approx8.4483\%}
\]

The corresponding minimum scaled parallel efficiency is:

\[
\boxed{E_{\min}\approx91.55\%}
\]

Thus, the serial fraction must not exceed approximately 8.4483% to satisfy the required performance target under Gustafson's Law.