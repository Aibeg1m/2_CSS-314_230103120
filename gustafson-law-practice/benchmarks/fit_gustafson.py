
import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
INPUT = BASE / "results.csv"
SUMMARY = BASE / "task23_summary.csv"
FIT_OUTPUT = BASE / "task23_fit.json"


def read_results():
    if not INPUT.exists():
        raise FileNotFoundError(
            "results.csv not found. Run Task 22 first."
        )

    groups = defaultdict(list)
    workloads = set()

    with INPUT.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required = {
            "workers", "run", "steps_per_worker",
            "runtime_seconds"
        }

        if not required.issubset(reader.fieldnames or []):
            raise ValueError("Incorrect results.csv columns")

        seen = set()

        for row in reader:
            p = int(row["workers"])
            run = int(row["run"])
            k = int(row["steps_per_worker"])
            runtime = float(row["runtime_seconds"])

            if p < 1 or k < 1:
                raise ValueError("Invalid processor/workload value")

            if not math.isfinite(runtime) or runtime <= 0:
                raise ValueError("Invalid runtime")

            if (p, run) in seen:
                raise ValueError("Duplicate worker/run combination")

            seen.add((p, run))
            groups[p].append(runtime)
            workloads.add(k)

    if len(workloads) != 1:
        raise ValueError(
            "Work per worker must be constant for weak scaling"
        )

    if 1 not in groups:
        raise ValueError("Baseline with 1 worker is required")

    if len(groups) < 5:
        raise ValueError(
            "At least 5 distinct worker counts are required"
        )

    for p, times in groups.items():
        if len(times) < 5:
            raise ValueError(
                f"Workers={p}: at least 5 runs required"
            )

    return groups, workloads.pop()


def main():
    groups, work = read_results()

    baseline_times = groups[1]
    baseline_mean = statistics.mean(baseline_times)
    baseline_sd = statistics.stdev(baseline_times)
    baseline_sem = baseline_sd / math.sqrt(
        len(baseline_times)
    )

    summary = []

    print("\nTASK 23: EMPIRICAL WEAK-SCALING ANALYSIS")
    print("Work per worker:", work)
    print("-" * 78)
    print(
        f"{'P':>4} {'Mean(s)':>12} {'SD(s)':>12}"
        f" {'SEM(s)':>12} {'Speedup':>12}"
        f" {'Efficiency':>12}"
    )

    for p in sorted(groups):
        times = groups[p]
        n = len(times)

        mean = statistics.mean(times)
        sd = statistics.stdev(times)
        sem = sd / math.sqrt(n)

        # Scaled speedup: relative throughput increase
        speedup = p * baseline_mean / mean
        efficiency = speedup / p

        # Approximate propagation of measurement uncertainty.
        # The p=1 speedup is defined as exactly 1.
        if p == 1:
            speedup_se = 0.0
        else:
            speedup_se = speedup * math.sqrt(
                (baseline_sem / baseline_mean) ** 2
                + (sem / mean) ** 2
            )

        item = {
            "workers": p,
            "runs": n,
            "steps_per_worker": work,
            "mean_seconds": mean,
            "std_seconds": sd,
            "sem_seconds": sem,
            "scaled_speedup": speedup,
            "speedup_se": speedup_se,
            "efficiency": efficiency,
        }

        summary.append(item)

        print(
            f"{p:>4} {mean:>12.6f} {sd:>12.6f}"
            f" {sem:>12.6f} {speedup:>12.4f}"
            f" {efficiency:>12.4f}"
        )

    # Gustafson model:
    # S(P) = P - alpha * (P - 1)
    #
    # Least squares with zero intercept for:
    # P - S(P) = alpha * (P - 1)

    numerator = 0.0
    denominator = 0.0

    for item in summary:
        p = item["workers"]

        if p == 1:
            continue

        x = p - 1
        y = p - item["scaled_speedup"]

        numerator += x * y
        denominator += x * x

    alpha = numerator / denominator

    residuals = []

    for item in summary:
        p = item["workers"]
        predicted = p - alpha * (p - 1)
        residuals.append(
            (item["scaled_speedup"] - predicted) ** 2
        )

    rmse = math.sqrt(sum(residuals) / len(residuals))

    with SUMMARY.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file, fieldnames=list(summary[0].keys())
        )
        writer.writeheader()
        writer.writerows(summary)

    fit = {
        "model": "Gustafson constrained least squares",
        "alpha_observed": alpha,
        "alpha_percent": alpha * 100,
        "rmse_speedup": rmse,
        "baseline_mean_seconds": baseline_mean,
        "steps_per_worker": work,
        "worker_counts": sorted(groups),
        "runs_per_configuration": {
            str(p): len(times)
            for p, times in groups.items()
        },
        "alpha_physically_valid": 0 <= alpha <= 1
    }

    with FIT_OUTPUT.open(
        "w", encoding="utf-8"
    ) as file:
        json.dump(fit, file, indent=2)

    print("\nREGRESSION RESULTS")
    print(f"Observed alpha: {alpha:.8f}")
    print(f"Serial fraction: {alpha * 100:.4f}%")
    print(f"Regression RMSE: {rmse:.6f}")
    print(f"Physical alpha range: {0 <= alpha <= 1}")
    print("\nSaved:", SUMMARY)
    print("Saved:", FIT_OUTPUT)

    if not 0 <= alpha <= 1:
        print(
            "WARNING: Fitted alpha is outside [0,1]. "
            "This may indicate superlinear effects, "
            "measurement noise, or model mismatch."
        )


if __name__ == "__main__":
    main()
