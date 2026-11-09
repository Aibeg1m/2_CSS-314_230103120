
import argparse
import csv
import math
import os
import platform
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


def integrate_chunk(task):
    """Numerical integration with a fixed number of steps per worker."""
    worker_id, workers, steps_per_worker = task

    total_steps = workers * steps_per_worker
    width = 1.0 / total_steps
    start = worker_id * steps_per_worker

    subtotal = 0.0

    for i in range(start, start + steps_per_worker):
        x = (i + 0.5) * width
        subtotal += 4.0 / (1.0 + x * x)

    return subtotal


def measure(pool, workers, work):
    tasks = [(i, workers, work) for i in range(workers)]

    start = time.perf_counter()
    partial_sums = list(pool.map(integrate_chunk, tasks))
    elapsed = time.perf_counter() - start

    pi_estimate = math.fsum(partial_sums) / (workers * work)
    return elapsed, pi_estimate


def parse_worker_counts(value):
    if value.lower() == "auto":
        cpu_count = os.cpu_count() or 1
        return list(range(1, cpu_count + 1))

    try:
        values = sorted(set(int(x) for x in value.split(",")))
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Use auto or comma-separated integers"
        )

    if not values or values[0] < 1:
        raise argparse.ArgumentTypeError(
            "Worker counts must be positive"
        )

    return values


def main():
    parser = argparse.ArgumentParser(
        description="Task 22: Empirical Weak-Scaling Benchmark"
    )

    parser.add_argument(
        "--workers",
        type=parse_worker_counts,
        default=parse_worker_counts("auto"),
        help="Worker counts, e.g. 1,2,4,6,8, or auto"
    )

    parser.add_argument(
        "--runs",
        type=int,
        default=5,
        help="Measured runs per configuration"
    )

    parser.add_argument(
        "--work",
        type=int,
        default=1_500_000,
        help="Integration steps per worker"
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results.csv",
        help="Output CSV path"
    )

    args = parser.parse_args()

    if args.runs < 1 or args.work < 1:
        parser.error("--runs and --work must be positive")

    available_cpus = os.cpu_count() or 1

    if max(args.workers) > available_cpus:
        parser.error(
            f"Requested workers exceed {available_cpus} logical CPUs"
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("TASK 22 - WEAK SCALING BENCHMARK")
    print("=" * 60)
    print("CPU:", platform.processor() or "Unknown")
    print("OS:", platform.platform())
    print("Logical CPUs:", available_cpus)
    print("Worker counts:", args.workers)
    print("Work per worker:", args.work)
    print("Runs per configuration:", args.runs)
    print("=" * 60)

    fieldnames = [
        "workers",
        "run",
        "steps_per_worker",
        "total_steps",
        "runtime_seconds",
        "pi_estimate",
        "absolute_error",
        "logical_cpus"
    ]

    with args.output.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file, fieldnames=fieldnames
        )
        writer.writeheader()

        for workers in args.workers:
            print(f"\n--- Workers: {workers} ---")

            # Create processes before measuring computation.
            with ProcessPoolExecutor(
                max_workers=workers
            ) as pool:

                # Warm up the worker pool.
                warmup_work = min(args.work, 100_000)
                measure(pool, workers, warmup_work)

                for run in range(1, args.runs + 1):
                    elapsed, pi_value = measure(
                        pool, workers, args.work
                    )

                    error = abs(pi_value - math.pi)

                    writer.writerow({
                        "workers": workers,
                        "run": run,
                        "steps_per_worker": args.work,
                        "total_steps": workers * args.work,
                        "runtime_seconds": elapsed,
                        "pi_estimate": pi_value,
                        "absolute_error": error,
                        "logical_cpus": available_cpus
                    })

                    file.flush()

                    print(
                        f"Run {run}: "
                        f"{elapsed:.4f} s | "
                        f"Pi = {pi_value:.10f}"
                    )

    print("\nBenchmark completed!")
    print("Results saved to:", args.output)


if __name__ == "__main__":
    main()
