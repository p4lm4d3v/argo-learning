from math import sin
import math
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np


def riemman_left(
    function: Callable[[float], float], n: int, a: float, b: float
) -> float:
    """Approximation of the integral of the [function] over the [a,b] interval, with n partition of it, using the Left Riemman Sum Approximation."""

    # Defining the sum and the "differentialy" small dx
    sum: float = 0
    dx: float = (b - a) / n

    # Calculating the rectangle areas and summing the up
    # using the left riemman sum approach
    for i in range(1, n + 1):
        leftx: float = get_xi(i - 1, a, dx)
        result: float = function(leftx)

        sum += result * dx

    return sum


def riemman_mid(
    function: Callable[[float], float], n: int, a: float, b: float
) -> float:
    """Approximation of the integral of the [function] over the [a,b] interval, with n partition of it, using the Midpoint Riemman Sum Approximation."""

    # Defining the sum and the "differentialy" small dx
    sum: float = 0
    dx: float = (b - a) / n

    # Calculating the rectangle areas and summing the up
    # using the midpoint riemman sum approach
    for i in range(1, n + 1):
        leftx: float = get_xi(i - 1, a, dx)
        rightx: float = get_xi(i, a, dx)
        midx: float = (leftx + rightx) / 2
        result: float = function(midx)

        sum += result * dx

    return sum


def riemman_right(
    function: Callable[[float], float], n: int, a: float, b: float
) -> float:
    """Approximation of the integral of the [function] over the [a,b] interval, with n partition of it, using the Right Riemman Sum Approximation."""

    # Defining the sum and the "differentialy" small dx
    sum: float = 0
    dx: float = (b - a) / n

    # Calculating the rectangle areas and summing the up
    # using the right riemman sum approach
    for i in range(1, n + 1):
        rightx: float = get_xi(i, a, dx)
        result: float = function(rightx)

        sum += result * dx

    return sum


def get_xi(i: int, a: float, dx: float) -> float:
    return a + i * dx


def main() -> None:
    # Defining the function to be integrated
    def f(x: float):
        return math.cos(x)

    # Initial params:
    # n - the number of rectangles (partitions of the interval)
    n: int = 100
    # a, b - the interval over which the integration is approximated
    a, b = 5, 50

    # Calculating the integral approximation
    # using the left, right, and midpoint riemman sum approaches
    sum_left: float = riemman_left(f, n, a, b)
    sum_mid: float = riemman_mid(f, n, a, b)
    sum_right: float = riemman_right(f, n, a, b)

    print(f"Left Riemman Sum: {sum_left}")
    print(f"Midpoint Riemman Sum: {sum_mid}")
    print(f"Right Riemman Sum: {sum_right}")

    # --- Updated Visualization (3-Panel Subplot) ---
    # Using a smaller partition count for clear visual rendering of rectangles
    n_plot: int = 15
    dx_plot = (b - a) / n_plot
    x_curve = np.linspace(a, b, 500)
    y_curve = [f(x) for x in x_curve]

    fig, axs = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    fig.suptitle(f"Riemann Sum Approximations for f(x) on [{a}, {b}]", fontsize=14)

    # 1. Left Riemann Plot
    x_left_rects = [get_xi(i, a, dx_plot) for i in range(n_plot)]
    y_left_rects = [f(x) for x in x_left_rects]
    axs[0].plot(x_curve, y_curve, 'b-', label='True f(x)')
    axs[0].bar(x_left_rects, y_left_rects, width=dx_plot, align='edge', alpha=0.4, color='red', edgecolor='black')
    axs[0].set_title(f"Left Riemann Sum: {sum_left:.4f}")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("f(x)")
    axs[0].grid(True, linestyle='--', alpha=0.7)
    axs[0].legend()

    # 2. Midpoint Riemann Plot
    x_mid_rects = [get_xi(i, a, dx_plot) + dx_plot / 2 for i in range(n_plot)]
    y_mid_rects = [f(x) for x in x_mid_rects]
    axs[1].plot(x_curve, y_curve, 'b-', label='True f(x)')
    axs[1].bar(x_mid_rects, y_mid_rects, width=dx_plot, align='center', alpha=0.4, color='orange', edgecolor='black')
    axs[1].set_title(f"Midpoint Riemann Sum: {sum_mid:.4f}")
    axs[1].set_xlabel("x")
    axs[1].grid(True, linestyle='--', alpha=0.7)
    axs[1].legend()

    # 3. Right Riemann Plot
    x_right_rects = [get_xi(i + 1, a, dx_plot) for i in range(n_plot)]
    # Alternatively using edge alignment starting from a + dx_plot
    x_right_bars = [get_xi(i, a, dx_plot) for i in range(1, n_plot + 1)]
    y_right_rects = [f(x) for x in x_right_bars]
    axs[2].plot(x_curve, y_curve, 'b-', label='True f(x)')
    axs[2].bar(x_right_bars, y_right_rects, width=-dx_plot, align='edge', alpha=0.4, color='green', edgecolor='black')
    axs[2].set_title(f"Right Riemann Sum: {sum_right:.4f}")
    axs[2].set_xlabel("x")
    axs[2].grid(True, linestyle='--', alpha=0.7)
    axs[2].legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    main()
