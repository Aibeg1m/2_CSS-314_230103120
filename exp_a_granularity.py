
import time
from multiprocessing import Pool


def collatz_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def run_granularity(workers, total_items=1_000_000, chunk_size=1):
    numbers = range(1, total_items + 1)

    t0 = time.perf_counter()

    with Pool(processes=workers) as pool:
        results = pool.map(
            collatz_steps,
            numbers,
            chunksize=chunk_size
        )

    elapsed = time.perf_counter() - t0
    return elapsed, sum(results)


def karp_flatt(t1, tp, p):
    return ((p * tp / t1) - 1) / (p - 1)


if __name__ == "__main__":
    worker_counts = [1, 2, 4, 8]
    chunk_sizes = [1, 10_000]

    for chunk_size in chunk_sizes:
        print(f"\n===== CHUNKSIZE = {chunk_size} =====")

        runtimes = {}

        for p in worker_counts:
            elapsed, total_steps = run_granularity(
                workers=p,
                chunk_size=chunk_size
            )

            runtimes[p] = elapsed

            print(
                f"P={p} | Time={elapsed:.3f}s | "
                f"Total steps={total_steps}"
            )

        t1 = runtimes[1]

        print("\n--- Performance Analysis ---")

        for p in [2, 4, 8]:
            tp = runtimes[p]
            speedup = t1 / tp
            efficiency = speedup / p * 100
            e = karp_flatt(t1, tp, p)

            print(
                f"P={p} | Speedup={speedup:.2f}x | "
                f"Efficiency={efficiency:.2f}% | "
                f"Karp-Flatt={e:.4f}"
            )
