# CS482 — Parallel Computing Performance
## Practice Lab — Variant B

**Student ID:** 230103120

**Topic:** Scalability Diagnostics: Granularity & IPC Contention

## 1. Objective

The goal of this lab is to test the performance of parallel Python programs. We use 1, 2, 4, and 8 processes. We compare execution time, speedup, efficiency, and the Karp–Flatt metric.

## 2. Experiment A — Granularity Trap

We tested two chunk sizes: 1 and 10,000.

| Processes | Micro (k=1), Time (s) | Coarse (k=10000), Time (s) |
|---|---|---|
| 1 | TODO | TODO |
| 2 | TODO | TODO |
| 4 | TODO | TODO |
| 8 | TODO | TODO |

**Result:** Small tasks can create high scheduling overhead. Larger chunks reduce the number of tasks sent to workers.

## 3. Experiment B — Queue Contention

We used multiprocessing.Queue to send 400,000 items.

| Processes | Time (s) |
|---|---|
| 1 | TODO |
| 2 | TODO |
| 4 | TODO |
| 8 | TODO |

**Result:** Sending many small messages can make the program slow. More processes can increase queue contention.

## 4. Experiment C — Buffered Queue

We used local buffers with a batch size of 10,000. The program processed 10,000,000 items.

| Processes | Time (s) |
|---|---|
| 1 | TODO |
| 2 | TODO |
| 4 | TODO |
| 8 | TODO |

**Result:** Buffered aggregation reduces communication overhead. Workers send batch sums instead of individual items.

## 5. Performance Comparison

| Configuration | T1 (s) | T2 (s) | T4 (s) | T8 (s) | S8 | e(2) | e(8) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A: Micro (k=1) | TODO | TODO | TODO | TODO | TODO | TODO | TODO | High dispatch overhead |
| A: Coarse (k=10000) | TODO | TODO | TODO | TODO | TODO | TODO | TODO | Reduced dispatch overhead |
| B: Queue Choke | TODO | TODO | TODO | TODO | TODO | TODO | TODO | IPC contention |
| C: Buffered Batch | TODO | TODO | TODO | TODO | TODO | TODO | TODO | Reduced IPC overhead |

## 6. Formulas

Speedup: S(p) = T1 / Tp

Efficiency: E(p) = S(p) / p × 100%

Karp–Flatt: e(p) = ((p × Tp / T1) − 1) / (p − 1)

## 7. Conclusion

In this lab, we tested three parallel computing methods. Experiment A shows how chunk size affects performance. Experiment B tests communication through a shared Queue. Experiment C uses local buffers to reduce communication.

The experiments help us understand that more processes do not always make a program faster. Task size and communication overhead are important for parallel performance.