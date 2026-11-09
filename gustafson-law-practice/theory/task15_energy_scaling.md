# Task 15: Energy and Power Proportionality under Scaled Speedup

## 1. Introduction

Energy efficiency is an important consideration in high-performance computing (HPC).

Parallel computing can reduce execution time or allow larger computational workloads to be processed within a fixed period.

However, increasing the number of processors also increases the power required by the computing system.

Gustafson's Law describes scaled speedup when workload size grows with processor count while execution time remains approximately constant.

The objective of this task is to develop a mathematical energy-consumption model for weak scaling and compare the energy required by a single processor with the energy consumed by a parallel system.

The analysis considers idle power, active computing power, processor count, execution time, and workload size.

## 2. Mathematical Foundations

### 2.1 Gustafson's Law

Gustafson's scaled speedup formula is:

\[
S_G(P)=P-\alpha(P-1)
\]

Where:

- \(P\) = number of processors.
- \(\alpha\) = serial fraction measured on the parallel machine.
- \(S_G(P)\) = scaled speedup.

An equivalent expression is:

\[
\boxed{S_G(P)=\alpha+(1-\alpha)P}
\]

Parallel efficiency is:

\[
E_G(P)=\frac{S_G(P)}{P}
\]

Therefore:

\[
\boxed{E_G(P)=1-\alpha+\frac{\alpha}{P}}
\]

Under ideal weak scaling, the computational workload grows with processor count while parallel execution time remains approximately constant.

### 2.2 Electrical Energy

Electrical energy consumption is defined as:

\[
E=\int_0^T\mathcal{P}(t)\,dt
\]

Where:

- \(E\) = energy consumption in joules.
- \(\mathcal{P}(t)\) = instantaneous electrical power in watts.
- \(T\) = execution time in seconds.

For constant power:

\[
\boxed{E=\mathcal{P}T}
\]

Since:

\[
1\text{ watt}=1\text{ joule/second}
\]

Energy is measured in joules:

\[
1\text{ J}=1\text{ W}\cdot1\text{ s}
\]

## 3. Processor Power Model

The task assumes each processor consumes idle and dynamic power.

Define:

\[
P_{\text{idle}}
\]

as the static power consumed by one powered-on processor when it is idle.

Define:

\[
P_{\text{active}}
\]

as the additional dynamic power consumed when that processor performs computation.

Thus, total power for one fully active processor is:

\[
\boxed{P_{\text{core}}=P_{\text{idle}}+P_{\text{active}}}
\]

In this model, \(P_{\text{active}}\) is an incremental dynamic-power contribution rather than the total active-state power.

For \(P\) powered-on processors, aggregate idle power is:

\[
\boxed{\mathcal{P}_{\text{idle,total}}=PP_{\text{idle}}}
\]

If all processors are active simultaneously:

\[
\boxed{\mathcal{P}_{\text{total}}=P(P_{\text{idle}}+P_{\text{active}})}
\]

The corresponding energy consumption over time \(T\) is:

\[
\boxed{E_P=P(P_{\text{idle}}+P_{\text{active}})T}
\]

This simplified expression assumes that every processor remains fully active during the entire execution period.

A more detailed model must distinguish serial and parallel execution phases.

## 4. Serial and Parallel Execution Phases

Gustafson's Law separates execution into serial and parallel components.

Let:

\[
T_s
\]

represent the serial execution time.

Let:

\[
T_p
\]

represent the parallel execution time.

Total execution time is:

\[
\boxed{T=T_s+T_p}
\]

The serial fraction is:

\[
\alpha=\frac{T_s}{T}
\]

Therefore:

\[
T_s=\alpha T
\]

Similarly:

\[
T_p=(1-\alpha)T
\]

During the serial phase, assume only one processor performs useful computation.

During the parallel phase, assume all \(P\) processors perform useful computation.

All processors remain powered on during both phases.

These assumptions allow the energy consumption of the two phases to be modeled separately.

## 5. Energy Consumption During the Serial Phase

During serial execution, one processor is active while the remaining \(P-1\) processors are idle.

The total power consumption is:

\[
\mathcal{P}_s=
(P_{\text{idle}}+P_{\text{active}})
+(P-1)P_{\text{idle}}
\]

Simplifying:

\[
\boxed{\mathcal{P}_s=PP_{\text{idle}}+P_{\text{active}}}
\]

The serial phase lasts:

\[
T_s=\alpha T
\]

Therefore, serial-phase energy consumption is:

\[
E_s=\mathcal{P}_sT_s
\]

Substituting:

\[
\boxed{
E_s=(PP_{\text{idle}}+P_{\text{active}})\alpha T
}
\]

This shows that idle processors can consume significant energy even when they are not performing useful computation.

## 6. Energy Consumption During the Parallel Phase

During parallel execution, all \(P\) processors are assumed to be active.

Total parallel-phase power is:

\[
\mathcal{P}_p=P(P_{\text{idle}}+P_{\text{active}})
\]

The duration of this phase is:

\[
T_p=(1-\alpha)T
\]

Therefore:

\[
E_p=\mathcal{P}_pT_p
\]

Substituting:

\[
\boxed{
E_p=P(P_{\text{idle}}+P_{\text{active}})(1-\alpha)T
}
\]

## 7. Total Energy Consumption

Total energy consumption is:

\[
E_P=E_s+E_p
\]

Substitute the serial and parallel expressions:

\[
E_P=
(PP_{\text{idle}}+P_{\text{active}})\alpha T
+
P(P_{\text{idle}}+P_{\text{active}})(1-\alpha)T
\]

Expand:

\[
E_P=
PP_{\text{idle}}\alpha T
+
P_{\text{active}}\alpha T
+
PP_{\text{idle}}(1-\alpha)T
+
PP_{\text{active}}(1-\alpha)T
\]

Group the idle-power terms:

\[
PP_{\text{idle}}\alpha T
+
PP_{\text{idle}}(1-\alpha)T
=
PP_{\text{idle}}T
\]

Group the dynamic-power terms:

\[
P_{\text{active}}\alpha T
+
PP_{\text{active}}(1-\alpha)T
=
P_{\text{active}}T[\alpha+P(1-\alpha)]
\]

Therefore:

\[
\boxed{
E_P=
T\left[
PP_{\text{idle}}
+
P_{\text{active}}\big(\alpha+P(1-\alpha)\big)
\right]
}
\]

This is the proposed phase-aware energy consumption model for a Gustafson-style weak-scaling workload.

It accounts for:

1. Processor count.
2. Idle power.
3. Dynamic computing power.
4. Serial execution time.
5. Parallel execution time.
6. Constant total wall-clock execution time.

## 8. Relationship Between Energy and Gustafson's Speedup

Recall Gustafson's Law:

\[
S_G(P)=\alpha+P(1-\alpha)
\]

Substitute this expression into the energy model:

\[
E_P=
T\left[
PP_{\text{idle}}
+
P_{\text{active}}S_G(P)
\right]
\]

Therefore:

\[
\boxed{
E_P=
T\left[
PP_{\text{idle}}+
P_{\text{active}}S_G(P)
\right]
}
\]

This equation directly relates total energy consumption to Gustafson's scaled speedup.

The first term represents static energy consumption across all processors.

The second term represents dynamic energy consumption associated with useful computation.

The equation assumes a constant power contribution per active processor and perfect utilization during the parallel phase.

## 9. Single-Processor Energy Consumption

Consider a single fully active processor operating for time \(T\).

Its power is:

\[
\mathcal{P}_1=P_{\text{idle}}+P_{\text{active}}
\]

Its energy consumption is:

\[
\boxed{
E_1=(P_{\text{idle}}+P_{\text{active}})T
}
\]

This formula can be compared directly with the energy consumption of \(P\) processors over the same wall-clock time.

However, the amount of useful work completed is different under weak scaling.

A single processor completes one processor's worth of computation during time \(T\).

A parallel system can complete a larger workload within the same time.

Therefore, comparing only total energy does not fully describe the energy efficiency of the systems.

## 10. Numerical Example

Consider a computing system with the following parameters.

| Parameter | Value |
|---|---:|
| Number of processors | 8 |
| Idle power per processor | 20 W |
| Additional dynamic power | 60 W |
| Total runtime | 100 seconds |
| Serial fraction | 10% |
| Parallel fraction | 90% |

Therefore:

\[
P=8
\]

\[
P_{\text{idle}}=20\text{ W}
\]

\[
P_{\text{active}}=60\text{ W}
\]

\[
T=100\text{ s}
\]

\[
\alpha=0.10
\]

### 10.1 Gustafson Scaled Speedup

Using Gustafson's Law:

\[
S_G(8)=8-0.10(8-1)
\]

\[
S_G(8)=8-0.7
\]

Therefore:

\[
\boxed{S_G(8)=7.3}
\]

The expanded workload has an equivalent single-processor execution time 7.3 times the parallel runtime.

### 10.2 Serial and Parallel Phase Durations

The serial phase lasts:

\[
T_s=\alpha T
\]

\[
T_s=0.10(100)
\]

\[
\boxed{T_s=10\text{ s}}
\]

The parallel phase lasts:

\[
T_p=(1-\alpha)T
\]

\[
T_p=0.90(100)
\]

\[
\boxed{T_p=90\text{ s}}
\]

### 10.3 Serial-Phase Energy

During the serial phase, one processor is active and seven are idle.

Total power:

\[
\mathcal{P}_s=8(20)+60
\]

\[
\boxed{\mathcal{P}_s=220\text{ W}}
\]

Energy:

\[
E_s=220(10)
\]

\[
\boxed{E_s=2200\text{ J}}
\]

### 10.4 Parallel-Phase Energy

During the parallel phase, all eight processors are active.

Total power:

\[
\mathcal{P}_p=8(20+60)
\]

\[
\boxed{\mathcal{P}_p=640\text{ W}}
\]

Energy:

\[
E_p=640(90)
\]

\[
\boxed{E_p=57600\text{ J}}
\]

### 10.5 Total Parallel Energy

\[
E_8=E_s+E_p
\]

\[
E_8=2200+57600
\]

Therefore:

\[
\boxed{E_8=59800\text{ J}}
\]

The eight-processor system consumes 59.8 kJ during the 100-second execution period.

## 11. Energy Consumption on One Processor

For one active processor:

\[
P_{\text{core}}=20+60
\]

\[
P_{\text{core}}=80\text{ W}
\]

For the same wall-clock runtime:

\[
T=100\text{ s}
\]

The energy consumption is:

\[
E_1=80(100)
\]

Therefore:

\[
\boxed{E_1=8000\text{ J}}
\]

The one-processor system consumes 8 kJ over the same 100 seconds.

The ratio of parallel to single-processor energy is:

\[
R_E=\frac{E_8}{E_1}
\]

\[
R_E=\frac{59800}{8000}
\]

Therefore:

\[
\boxed{R_E=7.475}
\]

Thus, the eight-processor system consumes approximately 7.475 times as much energy during the same wall-clock period.

However, it also completes a larger workload.

## 12. Comparison for the Same Expanded Workload

The previous comparison used identical execution time but different total amounts of useful work.

A fair comparison of energy required to finish the same expanded workload uses the equivalent sequential execution time.

The parallel system achieves:

\[
S_G(8)=7.3
\]

Therefore:

\[
T_1^*=S_G(8)T
\]

Substituting:

\[
T_1^*=7.3(100)
\]

\[
\boxed{T_1^*=730\text{ s}}
\]

One processor would require 730 seconds to complete the same expanded workload under the ideal model.

The corresponding sequential energy consumption is:

\[
E_1^*=(P_{\text{idle}}+P_{\text{active}})T_1^*
\]

\[
E_1^*=80(730)
\]

Therefore:

\[
\boxed{E_1^*=58400\text{ J}}
\]

The parallel system consumes:

\[
E_8=59800\text{ J}
\]

The energy ratio becomes:

\[
R_{\text{same work}}=\frac{59800}{58400}
\]

\[
\boxed{R_{\text{same work}}\approx1.024}
\]

The parallel system consumes approximately 2.4% more energy than one processor for the same expanded workload under the stated model.

However, the parallel system completes that workload in 100 seconds instead of 730 seconds.

This is a tradeoff between execution time, available processing resources, and total energy consumption.

## 13. Numerical Comparison Table

| Metric | One Processor, 100 s | Eight Processors, 100 s | One Processor, Same Expanded Workload |
|---|---:|---:|---:|
| Processor count | 1 | 8 | 1 |
| Execution time | 100 s | 100 s | 730 s |
| Active processor power | 80 W | 80 W per active processor | 80 W |
| Total energy | 8,000 J | 59,800 J | 58,400 J |
| Equivalent useful work | 100 processor-seconds | 730 processor-seconds | 730 processor-seconds |
| Completes expanded workload | No | Yes | Yes |

The first two columns compare identical execution time.

The last two columns compare identical amounts of useful computational work.

The distinction is necessary because weak scaling intentionally increases problem size.

## 14. Energy Efficiency Per Unit of Work

An important measure is the amount of energy required to complete one unit of computational work.

Define:

\[
\varepsilon=\frac{E}{W}
\]

Where:

- \(\varepsilon\) = energy per unit of useful work.
- \(E\) = total energy.
- \(W\) = computational work.

For the single-processor system:

\[
\varepsilon_1=\frac{8000}{100}
\]

\[
\boxed{\varepsilon_1=80\text{ J per equivalent processor-second}}
\]

For the eight-processor system:

\[
\varepsilon_8=\frac{59800}{730}
\]

\[
\boxed{\varepsilon_8\approx81.92\text{ J per equivalent processor-second}}
\]

Thus, the eight-processor configuration has a slightly higher energy cost per unit of useful work in this example.

This difference arises from the idle power consumed by processors during serial execution.

However, it provides substantially higher useful throughput.

## 15. General Energy Ratio for Identical Runtime

For one processor over runtime \(T\):

\[
E_1=T(P_{\text{idle}}+P_{\text{active}})
\]

For \(P\) processors:

\[
E_P=
T\left[
PP_{\text{idle}}+
P_{\text{active}}S_G(P)
\right]
\]

Divide:

\[
\frac{E_P}{E_1}
=
\frac{
T[PP_{\text{idle}}+P_{\text{active}}S_G(P)]
}{
T(P_{\text{idle}}+P_{\text{active}})
}
\]

Cancel \(T\):

\[
\boxed{
\frac{E_P}{E_1}
=
\frac{
PP_{\text{idle}}+P_{\text{active}}S_G(P)
}{
P_{\text{idle}}+P_{\text{active}}
}
}
\]

This formula compares energy consumed by one processor and \(P\) processors over identical wall-clock runtime.

The workloads are not identical under weak scaling.

For a fixed serial fraction:

\[
S_G(P)=\alpha+(1-\alpha)P
\]

As \(P\) increases, total energy consumption generally increases approximately linearly under the assumed power model.

## 16. Energy Ratio for Identical Workload

For the same expanded workload, the sequential execution time is:

\[
T_1^*=S_G(P)T
\]

Sequential energy is:

\[
E_1^*=
(P_{\text{idle}}+P_{\text{active}})S_G(P)T
\]

Parallel energy is:

\[
E_P=
T[
PP_{\text{idle}}+
P_{\text{active}}S_G(P)
]
\]

Therefore:

\[
\frac{E_P}{E_1^*}
=
\frac{
PP_{\text{idle}}+
P_{\text{active}}S_G(P)
}{
(P_{\text{idle}}+P_{\text{active}})S_G(P)
}
\]

Rearranging:

\[
\boxed{
\frac{E_P}{E_1^*}
=
1+
\frac{P_{\text{idle}}[P-S_G(P)]}
{(P_{\text{idle}}+P_{\text{active}})S_G(P)}
}
\]

Using Gustafson's Law:

\[
P-S_G(P)=\alpha(P-1)
\]

We obtain:

\[
\boxed{
\frac{E_P}{E_1^*}
=
1+
\frac{\alpha(P-1)P_{\text{idle}}}
{(P_{\text{idle}}+P_{\text{active}})[P-\alpha(P-1)]}
}
\]

This equation shows that idle power and serial execution increase the parallel system's energy consumption relative to one processor for the same workload.

Under the assumptions of this model, if:

\[
P_{\text{idle}}>0,\quad\alpha>0,\quad P>1
\]

then:

\[
E_P>E_1^*
\]

The model does not account for dynamic voltage and frequency scaling, different processor architectures, cooling, network power, or other system-level effects that may change practical results.

## 17. Energy and Performance Tradeoffs

Parallel computing introduces several important tradeoffs.

### 17.1 Higher Power Consumption

Adding processors usually increases instantaneous power consumption.

Even idle processors consume energy.

Therefore, total power can rise approximately proportionally with processor count.

### 17.2 Higher Computational Throughput

Under ideal weak scaling, increasing processor count allows the system to complete a larger workload in approximately constant time.

Thus, parallel computing increases computational throughput.

### 17.3 Energy Efficiency

Higher throughput does not necessarily mean lower energy consumption.

Energy efficiency depends on:

- Static and dynamic processor power.
- Serial overhead.
- Processor utilization.
- Execution time.
- Communication activity.
- Hardware power-management capabilities.

### 17.4 Power Management

Energy consumption can be reduced using:

- Dynamic voltage and frequency scaling.
- Processor sleep states.
- Power-aware scheduling.
- Efficient workload distribution.
- Reducing unnecessary synchronization.
- Communication-computation overlap.
- Turning off unused resources.

These techniques may improve real energy efficiency, although their effects must be validated experimentally.

## 18. Limitations of the Model

The proposed energy model uses several simplifying assumptions.

First, each processor is assumed to have constant idle power and constant additional dynamic power.

Second, all processors remain powered on throughout execution.

Third, the parallel phase is assumed to utilize all available processors.

Fourth, the serial phase is assumed to use only one active processor.

Fifth, execution time is assumed to remain constant under weak scaling.

Sixth, network, memory, storage, cooling, and other system-level power costs are excluded.

In real HPC systems, these assumptions may not hold.

For example, processors can have varying power consumption depending on workload, clock frequency, temperature, and memory activity.

Communication-intensive applications may also consume substantial network energy.

Therefore, the equations provide a theoretical framework rather than a complete hardware-level energy prediction.

## 19. Critical Discussion

Gustafson's Law demonstrates that increasing processor count can enable larger computational problems to be solved in approximately constant time.

However, it does not guarantee energy savings.

The developed model shows that total energy consumption depends on both processor count and the distribution of serial and parallel computation.

For identical wall-clock runtime, a parallel system usually consumes more total energy because more processors remain powered on.

Nevertheless, it also completes more computational work.

For identical useful workload, parallel execution can significantly reduce completion time, but its energy advantage depends on hardware and power-management characteristics.

In the numerical example, the eight-processor system consumed approximately 2.4% more energy for the same expanded workload while completing it 7.3 times faster.

This illustrates why both performance and energy consumption should be considered when designing parallel software.

## 20. Conclusion

The general energy consumption equation is:

\[
\boxed{E=\mathcal{P}T}
\]

For one fully active processor:

\[
\boxed{
E_1=(P_{\text{idle}}+P_{\text{active}})T
}
\]

For \(P\) processors under the proposed phase-aware weak-scaling model:

\[
\boxed{
E_P=
T\left[
PP_{\text{idle}}+
P_{\text{active}}(\alpha+P(1-\alpha))
\right]
}
\]

Using Gustafson's scaled speedup:

\[
\boxed{
E_P=
T[PP_{\text{idle}}+P_{\text{active}}S_G(P)]
}
\]

The numerical example demonstrated:

- Eight-processor scaled speedup: 7.3.
- Single-processor energy over 100 seconds: 8,000 J.
- Eight-processor energy over 100 seconds: 59,800 J.
- Single-processor energy for the same expanded workload: 58,400 J.
- Parallel energy overhead for identical work: approximately 2.4%.

The main conclusion is that Gustafson-style weak scaling can increase computational throughput substantially, but it does not automatically reduce total energy consumption.

Efficient parallel computing requires a balance between execution speed, processor utilization, static power, dynamic power, and overall energy efficiency.

## References

1. Gustafson, J. L. (1988). *Reevaluating Amdahl's Law*. Communications of the ACM, 31(5), 532–533. https://doi.org/10.1145/42411.42415

2. Hennessy, J. L., & Patterson, D. A. (2019). *Computer Architecture: A Quantitative Approach*, 6th Edition. Morgan Kaufmann.

3. Grama, A., Gupta, A., Karypis, G., & Kumar, V. (2003). *Introduction to Parallel Computing*, 2nd Edition. Addison-Wesley.