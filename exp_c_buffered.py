
import time
from multiprocessing import Process, Queue


def buffered_worker(out_queue, items_per_worker, batch_size=10_000):
    buffer = []

    for i in range(items_per_worker):
        buffer.append(i % 7)

        if len(buffer) >= batch_size:
            out_queue.put(sum(buffer))
            buffer.clear()

    if buffer:
        out_queue.put(sum(buffer))

    out_queue.put(None)


def run_buffered(p, total_items=10_000_000):
    q = Queue()
    items_per_worker = total_items // p

    workers = [
        Process(
            target=buffered_worker,
            args=(q, items_per_worker)
        )
        for _ in range(p)
    ]

    t0 = time.perf_counter()

    for w in workers:
        w.start()

    total_sum = 0
    active = p

    while active > 0:
        val = q.get()

        if val is None:
            active -= 1
        else:
            total_sum += val

    for w in workers:
        w.join()

    return time.perf_counter() - t0, total_sum


if __name__ == "__main__":
    cores = [1, 2, 4, 8]
    runtimes = {}

    for p in cores:
        elapsed, total_sum = run_buffered(p)
        runtimes[p] = elapsed

        print(
            f"P={p} | Time={elapsed:.3f}s | Total Sum={total_sum}"
        )

    t1 = runtimes[1]

    print("\n--- Buffered Queue Performance Analysis ---")

    for p in [2, 4, 8]:
        tp = runtimes[p]

        speedup = t1 / tp
        efficiency = speedup / p * 100
        e = ((p * tp / t1) - 1.0) / (p - 1.0)

        print(
            f"P={p} | "
            f"Speedup={speedup:.2f}x | "
            f"Efficiency={efficiency:.2f}% | "
            f"Karp-Flatt e={e:.4f}"
        )
