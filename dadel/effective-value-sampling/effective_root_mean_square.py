from typing import Callable, Tuple

import numpy as np
import matplotlib.pyplot as plt

def rms_grid(f: Callable[[float], float], a: float, b: float, n: int) -> Tuple[float, float]:
    """Calculates RMS using a uniform grid of points."""
    x = np.linspace(a, b, n)
    f_squared = f(x) ** 2
    return np.sqrt(np.mean(f_squared)), x

def rms_monte_carlo(f: Callable[[float], float], a: float, b: float, n: float) -> Tuple[float, float]:
    """Calculates RMS using Monte Carlo random sampling."""
    # Generate n random points uniformly distributed between a and b
    x = np.random.uniform(a, b, n)
    f_squared = f(x) ** 2
    return np.sqrt(np.mean(f_squared)), x


def main() -> None:
    # Example function: f(x) = x (e.g., linearly increasing ramp signal)
    def f(x: float) -> float:
        return np.sin(x)

    a, b = 0.0, 100
    n: int = 100000  # Number of sample points

    # Compute using both methods
    val_grid, x_grid = rms_grid(f, a, b, n)
    val_mc, x_mc = rms_monte_carlo(f, a, b, n)

    print(f"Interval: [{a}, {b}] with n={n} samples")
    print(f"Grid Sampling RMS: {val_grid:.5f}")
    print(f"Random Sampling RMS: {val_mc:.5f}")

    # Visualization comparison
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(x_grid, f(x_grid), alpha=0.5, color='blue', s=10)
    plt.title(f"Grid Sampling (n={n})\nRMS: {val_grid:.4f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.scatter(x_mc, f(x_mc), alpha=0.5, color='orange', s=10)
    plt.title(f"Random Sampling (n={n})\nRMS: {val_mc:.4f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
