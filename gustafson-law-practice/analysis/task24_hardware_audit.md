# Task 24: Hardware Audit and Scaling Analysis

## 1. Objective

This task compares empirical weak-scaling performance with theoretical predictions from Gustafson's Law and Amdahl's Law.

The benchmark was executed using Python multiprocessing on a Windows 11 computer.

## 2. Hardware Configuration

| Component | Specification |
|---|---|
| Operating System | Windows 11 (Build 26200) |
| CPU Model | 12th Gen Intel Core i7-1255U |
| Physical CPU Cores | 10 |
| Logical Processors | 12 |
| L2 Cache | 6,656 KB |
| L3 Cache | 12,288 KB (12 MB) |
| Installed RAM | 8 GiB |
| Usable Physical RAM | Approximately 7.73 GiB |
| Memory Speed | 3200 MT/s (reported value: 3200) |
| RAM Manufacturer | Micron Technology |
| RAM Part Number | MT40A1G16TB-062E:F |
| Memory Channels | Not verified |
| NUMA Configuration | Not verified |

## 3. Experimental Method

The benchmark uses numerical integration with Python multiprocessing.

The workload per worker remains constant, while total work increases with the number of workers.

The tested process counts were:

\[
P=\{1,2,3,4,5,6,7,8,9,10,11,12\}
\]

Empirical scaled speedup is calculated using:

\[
S_{\text{empirical}}(P)=\frac{P\bar T(1)}{\bar T(P)}
\]

The fitted Gustafson model is:

\[
S_G(P)=P-\alpha(P-1)
\]

## 4. Experimental Results

The least-squares regression produced:

\[
\boxed{\alpha_{\text{observed}}=0.77958497}
\]

As a percentage:

\[
\boxed{\alpha_{\text{observed}}\approx77.96\%}
\]

The fitted Gustafson model is:

\[
S_G(P)=P-0.77958497(P-1)
\]

Simplifying:

\[
\boxed{S_G(P)=0.22041503P+0.77958497}
\]

The fitted model predicts limited scaling efficiency compared with ideal linear speedup.

For 12 processes:

\[
S_G(12)=12-0.77958497(11)
\]

\[
\boxed{S_G(12)\approx3.4246}
\]

The corresponding theoretical efficiency is:

\[
E_G(12)=\frac{3.4246}{12}
\]

\[
\boxed{E_G(12)\approx28.54\%}
\]

These values are predictions based on the regression fit, not the directly measured speedup at 12 processes.

## 5. Performance Analysis

The regression result suggests a substantial deviation from ideal weak scaling.

The fitted effective serial fraction of approximately 77.96% indicates that the simple Gustafson model does not describe near-linear scaling for this benchmark.

Possible reasons include:

- Python multiprocessing scheduling overhead.
- Interprocess communication and synchronization.
- Competition for CPU execution resources.
- Memory bandwidth limitations.
- Differences between physical and logical processors.
- CPU frequency changes under sustained workloads.
- Background operating-system processes.

The Intel Core i7-1255U has 10 physical cores and 12 logical processors.

Using more logical processors does not necessarily produce proportional performance improvement.

The processor has heterogeneous core types, which may also influence task scheduling and parallel performance.

Thermal throttling and NUMA effects were not directly measured and therefore cannot be confirmed as causes of performance degradation.

The fitted serial fraction should be interpreted as an **effective model parameter**, not a direct measurement showing that 77.96% of the program is sequential.

## 6. Generated Plots

The following files were generated successfully:

- `plots/scaling_comparison.png`
- `plots/scaling_comparison.pdf`

The graphs include:

1. Ideal linear speedup.
2. Fitted Gustafson speedup.
3. Empirical scaled speedup with standard error bars.
4. Amdahl's speedup using the same numerical serial-fraction parameter.

The Amdahl and Gustafson curves are compared for illustration. Their serial fractions normally use different measurement reference frames.

## 7. Conclusion

The experiment was performed on an Intel Core i7-1255U processor with 10 physical cores, 12 logical processors, and 8 GiB of installed RAM.

The observed regression parameter was:

\[
\boxed{\alpha_{\text{observed}}\approx0.7796}
\]

The fitted Gustafson model predicts approximately 3.42 scaled speedup at 12 processes, substantially below ideal linear speedup.

This result indicates that overhead and practical hardware limitations may affect weak-scaling performance.

Further investigation of individual runtimes, CPU utilization, and system behavior would be necessary to identify the dominant bottlenecks.

The experiment demonstrates the importance of evaluating theoretical scaling laws using actual benchmark measurements.