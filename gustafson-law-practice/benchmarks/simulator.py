
import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt


def amdahl_speedup(p, s):
    return 1 / (s + (1 - s) / p)


def gustafson_speedup(p, alpha):
    return p - alpha * (p - 1)


def parse_processors(value):
    try:
        numbers = [int(x) for x in value.split(",")]
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid processor counts")

    if not numbers or any(p < 1 or p > 65536 for p in numbers):
        raise argparse.ArgumentTypeError(
            "Processor counts must be between 1 and 65536"
        )

    return sorted(set(numbers))


def parse_alphas(value):
    try:
        values = [float(x) for x in value.split(",")]
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid serial fractions")

    if not values or any(not 0.001 <= a <= 0.20 for a in values):
        raise argparse.ArgumentTypeError(
            "Serial fractions must be between 0.001 and 0.20"
        )

    return sorted(set(values))


def main():
    parser = argparse.ArgumentParser(
        description="Amdahl and Gustafson Speedup Simulator"
    )

    parser.add_argument(
        "--processors",
        type=parse_processors,
        default=parse_processors("1,2,4,8,16,32,64,128,256,512,1024")
    )

    parser.add_argument(
        "--alphas",
        type=parse_alphas,
        default=parse_alphas("0.001,0.04,0.08,0.20")
    )

    args = parser.parse_args()

    processors = args.processors
    alphas = args.alphas

    # Project directory
    root = Path(__file__).resolve().parent.parent

    csv_path = root / "benchmarks" / "task21_simulation.csv"
    plot_path = root / "plots" / "task21_comparison.png"

    plot_path.parent.mkdir(parents=True, exist_ok=True)

    # Calculate speedup and efficiency
    results = []

    for alpha in alphas:
        for p in processors:
            sa = amdahl_speedup(p, alpha)
            sg = gustafson_speedup(p, alpha)

            results.append([
                p,
                alpha,
                sa,
                sg,
                sa / p,
                sg / p
            ])

    # Export results to CSV
    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Processors",
            "Serial_Fraction",
            "Amdahl_Speedup",
            "Gustafson_Speedup",
            "Amdahl_Efficiency",
            "Gustafson_Efficiency"
        ])

        writer.writerows(results)

    print("CSV created:", csv_path)

    # Generate comparison plot
    plt.figure(figsize=(10, 6))

    plt.plot(
        processors,
        processors,
        "k--",
        label="Ideal Linear Speedup"
    )

    for alpha in alphas:
        amdahl = [amdahl_speedup(p, alpha) for p in processors]
        gustafson = [gustafson_speedup(p, alpha) for p in processors]

        plt.plot(
            processors,
            amdahl,
            marker="o",
            label=f"Amdahl alpha={alpha}"
        )

        plt.plot(
            processors,
            gustafson,
            marker="s",
            label=f"Gustafson alpha={alpha}"
        )

    plt.xlabel("Number of Processors")
    plt.ylabel("Speedup")
    plt.title("Amdahl vs Gustafson Speedup")

    if max(processors) / min(processors) >= 32:
        plt.xscale("log", base=2)

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(plot_path, dpi=300)
    plt.close()

    print("Plot created:", plot_path)
    print("Simulation completed successfully!")


if __name__ == "__main__":
    main()
