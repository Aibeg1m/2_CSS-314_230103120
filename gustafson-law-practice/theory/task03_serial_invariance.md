# Task 03: The Serial Fraction Invariance Paradox

## 1. Introduction

Amdahl's Law and Gustafson's Law use different approaches to measure the serial fraction of a parallel program.

Amdahl's Law considers the serial fraction measured on a single processor for a fixed workload.

Gustafson's Law considers the serial fraction observed during parallel execution on multiple processors.

This difference explains why the two laws can predict significantly different speedups.

## 2. Serial Fraction in Amdahl's Law

Amdahl's Law assumes that the total problem size remains constant.

The speedup formula is:

\[
S_A(P)=\frac{1}{s_A+\frac{1-s_A}{P}}
\]

Where:

- \(P\) is the number of processors.
- \(s_A\) is the serial fraction measured relative to single-processor execution time.

The maximum theoretical speedup is:

\[
\lim_{P\to\infty}S_A(P)=\frac{1}{s_A}
\]

For example, if:

\[
s_A=0.05
\]

Then:

\[
S_{max}=\frac{1}{0.05}=20
\]

Therefore, the speedup cannot exceed 20 for that fixed-size workload under the ideal Amdahl model.

## 3. Serial Fraction in Gustafson's Law

Gustafson's Law assumes that problem size increases with the number of processors.

The execution time on the parallel machine is normalized:

\[
T_P=s+p=1
\]

Where:

- \(s\) is the serial execution time.
- \(p\) is the parallel execution time.

The serial fraction observed on the parallel machine is:

\[
\alpha=\frac{s}{s+p}
\]

Since \(s+p=1\):

\[
\alpha=s
\]

Gustafson's scaled speedup formula is:

\[
S_G(P)=P-\alpha(P-1)
\]

Unlike Amdahl's Law, this formulation evaluates the equivalent single-processor execution time of the expanded workload.

## 4. Analytical Comparison

Consider a workload with serial execution time \(t_s\) and parallel work equivalent to \(t_w\) units of single-processor execution time.

For the same workload:

\[
T_1=t_s+t_w
\]

Assuming ideal parallel execution:

\[
T_P=t_s+\frac{t_w}{P}
\]

The serial fraction measured on one processor is:

\[
s_A=\frac{t_s}{t_s+t_w}
\]

The serial fraction measured on the parallel machine is:

\[
\alpha=\frac{t_s}{t_s+t_w/P}
\]

Therefore, the two fractions are generally different.

Their relationship is:

\[
\alpha=\frac{Ps_A}{1+(P-1)s_A}
\]

Solving for the single-processor fraction gives:

\[
s_A=\frac{\alpha}{P-\alpha(P-1)}
\]

This demonstrates that the serial fraction depends on the measurement reference.

## 5. Numerical Example

Assume:

\[
P=128,\qquad \alpha=0.05
\]

Using Gustafson's Law:

\[
S_G(128)=128-0.05(127)
\]

\[
S_G(128)=128-6.35
\]

\[
\boxed{S_G(128)=121.65}
\]

Now calculate the corresponding single-processor serial fraction for this same workload:

\[
s_A=\frac{0.05}{121.65}
\]

\[
s_A\approx0.000411
\]

Using Amdahl's Law with this corresponding fraction:

\[
S_A(128)=\frac{1}{0.000411+\frac{1-0.000411}{128}}
\]

Using the unrounded fraction gives:

\[
\boxed{S_A(128)=121.65}
\]

Thus, when the same workload and consistent serial fractions are used, both formulas produce the same speedup.

The apparent contradiction occurs when a serial fraction measured in one reference frame is incorrectly treated as the fraction measured in another.

## 6. Why Massive Scaling Is Possible

In weak scaling, increasing the number of processors makes it possible to process a larger workload in approximately the same execution time.

If serial execution time remains small while the parallel workload grows, the equivalent sequential execution time becomes much larger.

As a result, scaled speedup can approach the number of processors.

However, real systems may experience additional communication, synchronization, memory, and scheduling overhead.

Therefore, the serial fraction is not guaranteed to remain constant as processor count increases.

## 7. Critical Discussion

Amdahl's Law is not mathematically incorrect or universally pessimistic. It answers a different performance question.

Amdahl's Law asks:

How much faster can a fixed workload run on multiple processors?

Gustafson's Law asks:

How much larger a workload can be processed in approximately the same execution time?

The two models are compatible when the workload and measurement reference are defined consistently.

Gustafson's approach highlights the practical importance of scaling problem size rather than considering only fixed-size acceleration.

## 8. Conclusion

The Serial Fraction Invariance Paradox results from comparing serial fractions measured relative to different execution times.

Amdahl's Law measures the serial fraction using the single-processor baseline, while Gustafson's Law measures it using the parallel execution time.

The analytical relationship is:

\[
\boxed{\alpha=\frac{Ps_A}{1+(P-1)s_A}}
\]

This explains why a small serial fraction measured on a parallel machine can correspond to an even smaller serial fraction relative to the equivalent single-processor runtime.

The two laws do not contradict each other. They describe different scaling assumptions and use different reference frames.