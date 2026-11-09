
import csv
import json
import math
import platform
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
BENCHMARKS = ROOT / "benchmarks"
PLOTS = ROOT / "plots"

SUMMARY = BENCHMARKS / "task23_summary.csv"
FIT = BENCHMARKS / "task23_fit.json"

OUTPUT_PNG = PLOTS / "scaling_comparison.png"
OUTPUT_PDF = PLOTS / "scaling_comparison.pdf"


def amdahl(p, alpha):
    denominator = alpha + (1 - alpha) / p
    return 1 / denominator if denominator > 0 else float("nan")


def gustafson(p, alpha):
    return p - alpha * (p - 1)


def load_data():
    if not SUMMARY.exists() or not FIT.exists():
        raise FileNotFoundError(
            "Run Task 23 first. Summary CSV or fit JSON is missing."
        )

    with FIT.open("r", encoding="utf-8") as file:
        fit = json.load(file)

    alpha = float(fit["alpha_observed"])

    if not math.isfinite(alpha):
        raise ValueError("Invalid fitted alpha")

    rows = []

    with SUMMARY.open(
        "r", newline="", encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append({
                "p": int(row["workers"]),
                "speedup": float(row["scaled_speedup"]),
                "error": float(row["speedup_se"]),
            })

    if not rows:
        raise ValueError("No benchmark data found")

    rows.sort(key=lambda r: r["p"])

    for row in rows:
        if (
            row["p"] < 1
            or not math.isfinite(row["speedup"])
            or not math.isfinite(row["error"])
            or row["error"] < 0
        ):
            raise ValueError("Invalid measured data")

    return alpha, rows


def main():
    alpha, rows = load_data()

    processors = [row["p"] for row in rows]
    empirical = [row["speedup"] for row in rows]
    errors = [row["error"] for row in rows]

    ideal = processors
    gustafson_values = [
        gustafson(p, alpha) for p in processors
    ]
    amdahl_values = [
        amdahl(p, alpha) for p in processors
    ]

    PLOTS.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(11, 7))

    ax.plot(
        processors,
        ideal,
        "k--",
        linewidth=2,
        label="Ideal Linear Speedup"
    )

    ax.plot(
        processors,
        gustafson_values,
        marker="s",
        linewidth=2,
        label=f"Gustafson (alpha={alpha:.5f})"
    )

    ax.plot(
        processors,
        amdahl_values,
        marker="^",
        linewidth=2,
        label="Amdahl (same fitted alpha)"
    )

    ax.errorbar(
        processors,
        empirical,
        yerr=errors,
        fmt="o",
        capsize=5,
        markersize=7,
        label="Measured Speedup ± SE"
    )

    ax.set_title(
        "Empirical vs Theoretical Parallel Scaling"
    )
    ax.set_xlabel("Number of Processes (P)")
    ax.set_ylabel("Scaled Speedup")
    ax.set_xticks(processors)
    ax.grid(True, alpha=0.3)
    ax.legend()

    if alpha < 0 or alpha > 1:
        ax.text(
            0.02, 0.98,
            "Warning: fitted alpha outside physical range",
            transform=ax.transAxes,
            va="top",
            fontsize=9
        )

    fig.tight_layout()

    fig.savefig(OUTPUT_PNG, dpi=300)
    fig.savefig(OUTPUT_PDF)
    plt.close(fig)

    print("=" * 55)
    print("TASK 24 - SCALING COMPARISON")
    print("=" * 55)
    print(f"Fitted alpha: {alpha:.8f}")
    print(f"Processor counts: {processors}")
    print(f"CPU: {platform.processor() or 'Unknown'}")
    print(f"OS: {platform.platform()}")
    print("PNG:", OUTPUT_PNG)
    print("PDF:", OUTPUT_PDF)
    print("Task 24 plotting completed!")


if __name__ == "__main__":
    main()
