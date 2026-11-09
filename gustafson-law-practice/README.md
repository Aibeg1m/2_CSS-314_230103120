# Gustafson's Law & Weak Scaling — Practice Tasks

**Course:** Parallel & Distributed Computing Architecture  
**Student ID:** 230103120  
**Instructor:** Sufyan bin Uzayr  
**Tasks:** 01–25

## 1. Project Overview

This repository contains theoretical explanations, mathematical derivations, numerical calculations, algorithmic analyses, and empirical benchmarking related to Gustafson's Law and parallel computing.

The project compares strong scaling and weak scaling, investigates communication overhead, and evaluates performance using real multiprocessing benchmarks.

## 2. Mathematical Foundations

### Amdahl's Law

Amdahl's Law describes speedup for a fixed-size workload:

\[
S_A(P)=\frac{1}{s+(1-s)/P}
\]

### Gustafson's Law

Gustafson's Law describes scaled speedup:

\[
S_G(P)=P-\alpha(P-1)
\]

### Parallel Efficiency

\[
E(P)=\frac{S(P)}{P}
\]

### Isoefficiency

The isoefficiency relationship is:

\[
W=KT_o(W,P)
\]

These mathematical models explain how processor count, workload size, and serial overhead influence parallel computing performance.

## 3. Project Structure

```text
gustafson-law-practice/
├── README.md
├── theory/
│   ├── task01_scaling_models.md
│   ├── task02_derivation.md
│   ├── task03_serial_invariance.md
│   ├── task04_asymptotic_limits.md
│   ├── task05_historical_ncube.md
│   ├── task11_sun_ni_comparison.md
│   ├── task12_communication_penalty.md
│   ├── task13_failure_cases.md
│   ├── task14_isoefficiency.md
│   └── task15_energy_scaling.md
├── calculations/
│   ├── task06_parametric_table.md
│   ├── task07_tolerable_serial.md
│   ├── task08_cross_divergence.md
│   ├── task09_multicomponent.md
│   ├── task10_memory_growth.md
│   ├── task16_gemm_scaling.md
│   └── task17_stencil_scaling.md
├── analysis/
│   ├── task18_nbody_scaling.md
│   ├── task19_monte_carlo.md
│   ├── task20_graph_processing.md
│   └── task24_hardware_audit.md
├── benchmarks/
│   ├── simulator.py
│   ├── task21_simulation.csv
│   ├── weak_scale_bench/
│   │   ├── benchmark.py
│   │   └── README.md
│   ├── results.csv
│   ├── fit_gustafson.py
│   ├── task23_summary.csv
│   ├── task23_fit.json
│   └── plot_scaling.py
└── plots/
    ├── task21_comparison.png
    ├── scaling_comparison.png
    └── scaling_comparison.pdf
```

## 4. Task Index

| Task | Topic | File |
|---|---|---|
| 01 | Strong vs. Weak Scaling | [Task 01](theory/task01_scaling_models.md) |
| 02 | Gustafson's Law Derivation | [Task 02](theory/task02_derivation.md) |
| 03 | Serial Fraction Invariance | [Task 03](theory/task03_serial_invariance.md) |
| 04 | Asymptotic Efficiency | [Task 04](theory/task04_asymptotic_limits.md) |
| 05 | Historical nCUBE Experiment | [Task 05](theory/task05_historical_ncube.md) |
| 06 | Parametric Speedup | [Task 06](calculations/task06_parametric_table.md) |
| 07 | Maximum Serial Overhead | [Task 07](calculations/task07_tolerable_serial.md) |
| 08 | Amdahl vs. Gustafson | [Task 08](calculations/task08_cross_divergence.md) |
| 09 | Multi-Component Workload | [Task 09](calculations/task09_multicomponent.md) |
| 10 | Memory Growth | [Task 10](calculations/task10_memory_growth.md) |
| 11 | Sun–Ni Model | [Task 11](theory/task11_sun_ni_comparison.md) |
| 12 | Communication Overhead | [Task 12](theory/task12_communication_penalty.md) |
| 13 | Weak-Scaling Failure Cases | [Task 13](theory/task13_failure_cases.md) |
| 14 | Isoefficiency | [Task 14](theory/task14_isoefficiency.md) |
| 15 | Energy Scaling | [Task 15](theory/task15_energy_scaling.md) |
| 16 | GEMM Scaling | [Task 16](calculations/task16_gemm_scaling.md) |
| 17 | 3D Stencil Scaling | [Task 17](calculations/task17_stencil_scaling.md) |
| 18 | N-Body Scaling | [Task 18](analysis/task18_nbody_scaling.md) |
| 19 | Monte Carlo Scaling | [Task 19](analysis/task19_monte_carlo.md) |
| 20 | Graph Processing | [Task 20](analysis/task20_graph_processing.md) |
| 21 | Speedup Simulator | [simulator.py](benchmarks/simulator.py) |
| 22 | Weak-Scaling Benchmark | [benchmark.py](benchmarks/weak_scale_bench/benchmark.py) |
| 23 | Experimental Regression | [fit_gustafson.py](benchmarks/fit_gustafson.py) |
| 24 | Hardware Audit and Plots | [Task 24](analysis/task24_hardware_audit.md) |

## 5. Installation

Requirements:

- Python 3.10 or newer
- Matplotlib
- A computer supporting Python multiprocessing

Install dependencies:

```powershell
python -m pip install matplotlib
```

All commands below must be executed from the `gustafson-law-practice` directory.

## 6. Run Task 21 — Speedup Simulator

```powershell
python benchmarks/simulator.py
```

To use specific parameters:

```powershell
python benchmarks/simulator.py --processors 1,2,4,8,16,32,64,128,256,512,1024 --alphas 0.001,0.04,0.08,0.20
```

Output:

- `benchmarks/task21_simulation.csv`
- `plots/task21_comparison.png`

## 7. Run Task 22 — Weak-Scaling Benchmark

```powershell
python benchmarks/weak_scale_bench/benchmark.py --workers auto --runs 5 --work 1500000
```

The benchmark performs numerical integration using Python multiprocessing.

Each worker executes a constant number of integration steps.

Total workload grows according to:

\[
W(P)=Pk
\]

Output:

`benchmarks/results.csv`

## 8. Run Task 23 — Experimental Regression

```powershell
python benchmarks/fit_gustafson.py
```

The script calculates:

- Mean execution time
- Sample standard deviation
- Standard error
- Empirical scaled speedup
- Parallel efficiency
- Least-squares estimate of the serial fraction

Outputs:

- `benchmarks/task23_summary.csv`
- `benchmarks/task23_fit.json`

## 9. Run Task 24 — Comparison Plots

```powershell
python benchmarks/plot_scaling.py
```

The script generates:

- `plots/scaling_comparison.png`
- `plots/scaling_comparison.pdf`

The graph compares ideal linear speedup, fitted Gustafson speedup, empirical speedup with standard error bars, and Amdahl's Law.

## 10. Experimental Hardware

The experiments were performed using:

| Component | Specification |
|---|---|
| CPU | Intel Core i7-1255U |
| Physical Cores | 10 |
| Logical Processors | 12 |
| Operating System | Windows 11 |
| L2 Cache | 6,656 KB |
| L3 Cache | 12,288 KB |
| Installed RAM | 8 GiB |
| Memory Speed | Reported 3200 |

Further hardware details are available in [Task 24](analysis/task24_hardware_audit.md).

## 11. Experimental Results

The benchmark tested processor counts from 1 to 12.

The estimated serial fraction from least-squares regression was:

\[
\boxed{\alpha_{\text{observed}}=0.77958497}
\]

The fitted theoretical Gustafson speedup at 12 processes is:

\[
S_G(12)=12-0.77958497(11)
\]

\[
\boxed{S_G(12)\approx3.4246}
\]

The predicted efficiency is approximately:

\[
\boxed{E_G(12)\approx28.54\%}
\]

These values are based on the fitted model and should not be confused with directly measured speedup.

The fitted serial fraction is an effective parameter that includes the influence of practical overhead.

## 12. Engineering Guidelines

Gustafson-style weak scaling is most suitable when:

1. Problem size can grow with available processors.
2. Parallel work dominates serial computation.
3. Communication overhead remains controlled.
4. Workload distribution is balanced.
5. Memory capacity is sufficient for expanded problems.

Amdahl's Law is useful for evaluating fixed-size workloads.

Sun–Ni's model is useful when memory capacity limits problem expansion.

Isoefficiency analysis determines how quickly workload size must increase to maintain parallel efficiency.

Actual benchmarks remain necessary because theoretical models cannot capture all hardware and operating-system effects.

## 13. Limitations

The empirical benchmark uses Python multiprocessing and a synthetic numerical integration workload.

The results may be influenced by:

- Operating-system scheduling
- Process-management overhead
- CPU frequency variation
- Hardware resource contention
- Physical versus logical processor differences

Thermal throttling and NUMA effects were not directly confirmed.

The model parameters and experimental results are specific to the tested machine and benchmark implementation.

## 14. Conclusion

This project analyzed 25 practice tasks covering Gustafson's Law, strong and weak scaling, serial overhead, memory constraints, communication costs, numerical algorithms, and empirical performance.

The theoretical analysis demonstrates that increasing problem size can allow parallel systems to achieve near-linear scaled speedup.

However, real benchmark results may differ significantly from ideal predictions because of communication, synchronization, scheduling, and hardware limitations.

The experiments highlight the importance of combining mathematical scaling models with actual measurements when evaluating parallel software performance.