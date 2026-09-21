# Effective Value (RMS) via Grid vs. Monte Carlo Sampling 🎲⚡

A Python script exploring numerical approximation of Root Mean Square (RMS) values using deterministic grid spacing versus probabilistic random sampling (Monte Carlo).

---

## 📐 Mathematical Overview

The **effective value** (Root Mean Square, RMS) of a continuous function $f(x)$ over a range $[a, b]$ is defined as:

$$X_{\text{eff}} = \sqrt{\frac{1}{b - a} \int_{a}^{b} [f(x)]^2 \, dx}$$

Depending on how we sample the function, we can compute this numerically using two distinct approaches:

### 1. Equally Distributed Grid (Deterministic)
We divide the interval into $n$ evenly spaced points $x_i$ using a step size $\Delta x$:
$$X_{\text{eff, grid}} \approx \sqrt{\frac{1}{n} \sum_{i=1}^{n} [f(x_i)]^2}$$

### 2. Random Sampling (Monte Carlo)
Instead of a rigid grid, we sample $n$ points uniformly distributed at random across $[a, b]$:
$$X_{\text{eff, MC}} \approx \sqrt{\frac{1}{n} \sum_{i=1}^{n} [f(x_{\text{rand}, i})]^2}$$

---

## 📝 Analytical Derivations & Examples

### Example A: The Linear Function ($f(x) = x$)

For a linear ramp function over $[a, b]$:
1. Square the function: $f(x)^2 = x^2$
2. Integrate: $\int_{a}^{b} x^2 \, dx = \frac{b^3 - a^3}{3} = \frac{(b - a)(b^2 + ab + a^2)}{3}$
3. Apply the RMS formula and simplify:

$$X_{\text{eff}} = \sqrt{\frac{b^2 + ab + a^2}{3}}$$

*(Special case for interval $[0, b]$: $X_{\text{eff}} = \frac{b}{\sqrt{3}}$)*

---

### Example B: The Sinusoidal Function ($f(x) = \sin(x)$)

For a sine wave over a general range $[a, b]$:
1. Use the half-angle identity: $\sin^2(x) = \frac{1 - \cos(2x)}{2}$
2. Integrate over the interval:
$$\int_{a}^{b} \sin^2(x) \, dx = \left[ \frac{x}{2} - \frac{\sin(2x)}{4} \right]_{a}^{b}$$
3. General formula for any range $[a, b]$:

$$X_{\text{eff}} = \sqrt{\frac{1}{2} - \frac{\sin(2b) - \sin(2a)}{4(b - a)}}$$

*(Special case for a full wave cycle $[0, 2\pi]$ or half-cycle $[0, \pi]$: The sinusoidal fluctuation terms cancel out, leaving the standard AC root-mean-square multiplier $X_{\text{eff}} = \frac{1}{\sqrt{2}} \approx 0.707$)*

---

## 🛠️ Usage

Install dependencies:
```bash
pip install numpy matplotlib
