# Riemann Sum Integration 📊

A simple Python implementation and mathematical exploration of numerical integration using rectangular Riemann sums (Left, Right, and Midpoint methods).

---

## 📐 Mathematical Overview

### 1. Partitioning the Interval
Given a continuous function $f(x)$ on a closed interval $[a, b]$, our goal is to approximate the net area under the curve. We divide the interval into $n$ subintervals of equal width $\Delta x$, defined as:

$$\Delta x = \frac{b - a}{n}$$

The endpoints of these subintervals form a partition:
$x_0, x_1, x_2, \dots, x_n$
where $x_0 = a$, $x_n = b$, and any general point is given by $x_i = a + i \Delta x$.

### 2. The General Riemann Sum Formula
To approximate the total area, we approximate the area of the curve over each subinterval $[x_{i-1}, x_i]$ as a rectangle. The height of each rectangle is determined by evaluating the function at a chosen sample point $x_i^*$ within that subinterval.

The general Riemann sum is expressed as:

$$S_n = \sum_{i=1}^{n} f(x_i^*) \Delta x$$

### 3. Choosing Sample Points ($x_i^*$)
Depending on how we pick the sample point $x_i^*$ inside each subinterval, we get different approximation methods:

* **Left Riemann Sum:** Evaluates the function at the left endpoint of each subinterval ($x_i^* = x_{i-1}$).
  $$S_{\text{left}} = \sum_{i=1}^{n} f(x_{i-1}) \Delta x$$

* **Right Riemann Sum:** Evaluates the function at the right endpoint of each subinterval ($x_i^* = x_i$).
  $$S_{\text{right}} = \sum_{i=1}^{n} f(x_i) \Delta x$$

* **Midpoint Riemann Sum:** Evaluates the function at the exact middle of each subinterval ($x_i^* = \frac{x_{i-1} + x_i}{2}$). This method generally yields higher accuracy for a given $n$:
  $$S_{\text{mid}} = \sum_{i=1}^{n} f\left(\frac{x_{i-1} + x_i}{2}\right) \Delta x$$

### 4. Convergence to the Definite Integral
As the number of rectangles approaches infinity ($n \to \infty$), the width $\Delta x$ approaches zero, and the limit of the Riemann sum yields the exact definite integral:

$$\int_{a}^{b} f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x$$

---

## 🛠️ Usage

Run the script to see the calculated approximation:
```bash
python riemann.py
```

---

## 🤖 Robotics Context
In embedded systems and robotics, we rarely deal with continuous analytical functions. Instead, we deal with discrete-time sensor data (sampled at fixed time steps $\Delta t$).

If you want to find the distance traveled ($s$) by integrating a robot's velocity profile ($v(t)$) over time, the discrete Riemann sum becomes a numerical integration scheme (such as **Euler's Method**):

$$s \approx \sum_{k=1}^{n} v(t_k) \Delta t$$
