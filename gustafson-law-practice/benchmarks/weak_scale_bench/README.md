# Task 22: Empirical Weak-Scaling Benchmark Suite

## Objective

Measure weak-scaling performance using Python multiprocessing.

The program performs numerical integration to estimate π.

## Methodology

- Every worker performs the same number of integration steps.
- Total workload grows with the number of workers.
- Processor counts range from 1 to the available logical CPU count.
- Each configuration is executed five times.
- A warm-up run is performed before measurement.
- Execution times are measured using `time.perf_counter()`.

The total workload is:

\[
W(P)=P\cdot k
\]

where \(k\) is the fixed workload per worker.

Under ideal weak scaling:

\[
T(P)\approx T(1)
\]

## Execution

From the `gustafson-law-practice` directory:

```powershell
python benchmarks/weak_scale_bench/benchmark.py --workers auto --runs 5 --work 1500000
```

For selected worker counts:

```powershell
python benchmarks/weak_scale_bench/benchmark.py --workers 1,2,4,6,8 --runs 5 --work 1500000
```

Use only worker counts supported by the local machine.

## Output

Results are saved to:

`benchmarks/results.csv`

The file includes processor counts, run numbers, workload sizes, runtimes, numerical results, and absolute integration errors.

These measurements are used for Tasks 23 and 24.

## Limitations

The benchmark measures multiprocessing performance, including task dispatch and result collection.

Results can be affected by CPU scheduling, process startup during warm-up, memory contention, power management, and background applications.

Physical core count may differ from the number of logical processors.