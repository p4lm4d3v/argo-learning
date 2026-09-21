from math import sin
from typing import Callable


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
        return sin(x)

    # Initial params:
    # n - the number of rectangles (partitions of the interval)
    n: int = 100000
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


if __name__ == "__main__":
    main()
