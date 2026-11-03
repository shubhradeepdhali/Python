# Introduction to Matplotlib (sdhali.signingIN)

Matplotlib is one of the most widely used data visualization libraries in Python. It provides a flexible and powerful way to create plots, graphs, and charts to uncover patterns, trends, and insights in data.

## Key Points

* **Library Type**: Low-level plotting library
* **Core Idea**: Gives full control over every element of a figure (titles, axes, labels, colors, styles)
* **Origin**: Inspired by MATLAB’s plotting system
* **Flexibility**: Creates everything from simple line plots to customized multi-plot figures
* **Integration**: Works seamlessly with NumPy, Pandas, and SciPy

## Uses of Matplotlib

* Visualizing data effectively before analysis and modeling
* Creating publication-quality figures
* Customizing every detail of plots (size, colors, fonts, legends, grids)
* Serving as the foundation for higher-level libraries like Seaborn and Pandas `.plot()`

## Anatomy of a Matplotlib Figure

1. **Figure**: The overall window or canvas that contains everything
2. **Axes**: The actual coordinate area where data is plotted (x-axis, y-axis)
3. **Axis**: The scales, limits, and ticks for x and y directions
4. **Plot Elements**: Titles, labels, legends, lines, bars, and markers

## Typical Workflow & Setup

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from warnings import filterwarnings

filterwarnings("ignore")
```

## Markers & Color Reference

### 1. Standard Marker Symbols

Single-character shortcuts used inside format strings (e.g., `'ro'` for red circles) or passed to the `marker` parameter:

| Symbol | Description | Symbol | Description |
| :--- | :--- | :--- | :--- |
| `.` | Point marker | `p` | Pentagon marker |
| `,` | Pixel marker | `P` | Plus (filled) marker |
| `o` | Circle marker | `*` | Star marker |
| `v` | Triangle-down marker | `h` | Hexagon-1 marker |
| `^` | Triangle-up marker | `H` | Hexagon-2 marker |
| `<` | Triangle-left marker | `+` | Plus marker |
| `>` | Triangle-right marker | `x` | X marker |
| `1` | Tri-down marker | `X` | X (filled) marker |
| `2` | Tri-up marker | `D` | Diamond marker |
| `3` | Tri-left marker | `d` | Thin diamond marker |
| `4` | Tri-right marker | `\|` | Vertical line marker |
| `8` | Octagon marker | `_` | Horizontal line marker |
| `s` | Square marker | | |

### 2. Advanced & STIX Math Markers

Pass TeX/STIX math strings wrapped in `$` signs to the `marker` parameter:

* `'$\alpha$'`: Alpha Greek symbol (α)
* `'$\beta$'`: Beta Greek symbol (β)
* `'$\sum$'`: Summation symbol (∑)
* `'$\infty$'`: Infinity symbol (∞)
* `'$\clubsuit$'`: Club card symbol (♣)
* `'$\heartsuit$'`: Heart card symbol (♡)

### 3. Colors

* **Base Colors (Single-Letter Shorthand)**: `b` (Blue), `g` (Green), `r` (Red), `c` (Cyan), `m` (Magenta), `y` (Yellow), `k` (Black), `w` (White)
* **Tableau Palette (Default Sequential Colors)**: `tab:blue`, `tab:orange`, `tab:green`, `tab:red`, `tab:purple`, `tab:brown`, `tab:pink`, `tab:gray`, `tab:olive`, `tab:cyan`
* **CSS / HTML Named Colors**:
  * **Blues/Cyans**: `navy`, `darkblue`, `blue`, `skyblue`, `teal`, `cyan`, `turquoise`
  * **Greens**: `darkgreen`, `green`, `forestgreen`, `lime`, `olive`, `lightgreen`
  * **Reds/Pinks**: `maroon`, `darkred`, `red`, `crimson`, `tomato`, `pink`, `hotpink`
  * **Oranges/Yellows**: `darkorange`, `orange`, `gold`, `yellow`, `khaki`
  * **Purples**: `indigo`, `purple`, `darkmagenta`, `violet`, `plum`, `lavender`
  * **Greys**: `black`, `dimgray`, `gray`, `silver`, `lightgray`, `white`

## Basic Canvas & Line Plot

```python
# Two simple arrays
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Canvas creation
plt.figure(figsize=(5, 5))

# Plot with format string (yellow line, star marker)
plt.plot(x, y, "y-*")

# Plot labels and title
plt.xlabel("number of items")
plt.ylabel("price of items")
plt.title("Price chart")

# Render plot
plt.show()
```

## Subplots (Multiple Plots on One Canvas)

Use `plt.subplot(rows, columns, index)` to divide a canvas into a grid:

```python
from matplotlib.lines import lineMarkers

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

plt.figure(figsize=(8, 8))

# Subplot 1
plt.subplot(1, 3, 1)
plt.plot(x, y1, color='red', marker="h", markerfacecolor='blue')

# Subplot 2
plt.subplot(1, 3, 2)
plt.plot(x, y2, color='navy', marker=r'$\clubsuit$', markerfacecolor='lime')

# Subplot 3
plt.subplot(1, 3, 3)
plt.plot(x, y1, color='red', marker="h", markerfacecolor='blue')

plt.show()
```

## Figure Size, Aspect Ratio & DPI

* **Figure Size (`figsize`)**: Width × Height of the canvas in inches
* **Aspect Ratio**: Relationship between width and height
* **DPI (Dots Per Inch)**: Resolution (pixels per inch)

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure with custom size (8x4 inches) & resolution (120 DPI)
plt.figure(figsize=(8, 4), dpi=120)

plt.plot(x, y, color="teal", marker="o")
plt.title("Custom Figure Size & DPI")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
```

## Legends, Labels & Multi-Line Plots

Assign a `label` inside each `plt.plot()` call and invoke `plt.legend()` to display the key:

```python
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.figure(figsize=(7, 4))

# Plot first and second lines
plt.plot(x, y1, color="blue", marker="o", label="Squares")
plt.plot(x, y2, color="red", marker="s", label="Line")

# Add labels, title, legend, and grid
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Example: Legends, Labels & Title")
plt.legend(loc="upper left")
plt.grid(True)
plt.show()
```

## Inset Plot & Axis Limits (Object-Oriented vs. Pyplot)

Demonstrates how to set explicit coordinate boundaries (`xlim`, `ylim`) using both standard `pyplot` syntax and the Object-Oriented (OO) API with an embedded inset axis.

* **Pyplot Approach**: Uses `plt.xlim([-5, 10])` and `plt.ylim([-5, 5])` on the active figure.
* **Object-Oriented Approach**:
  * `fig, ax = plt.subplots()`: Initializes the parent `Figure` (`fig`) and primary `Axes` (`ax`).
  * `fig.add_axes([left, bottom, width, height])`: Adds a secondary inset axis (`ax2`) using normalized coordinates (`0.0` to `1.0`).
  * `set_xlim` / `set_ylim`: Supports one-sided boundaries by passing `None` to leave the opposite bound auto-scaled.

```python
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# 1. Pyplot Approach (Functional)
plt.figure(figsize=(8, 4))
plt.xlim([-5, 10])
plt.ylim([-5, 5])
plt.show()

# 2. Object-Oriented Approach (Figures & Axes)
fig, ax = plt.subplots(figsize=(8, 5), dpi=120)
ax.plot(x, y, color='teal', marker='o', label='Growth')
ax.set(title="Hello", xlabel="X", ylabel="Y")

# Inset axis: [left, bottom, width, height]
ax2 = fig.add_axes([0.2, 0.6, 0.3, 0.2])
ax2.set_xlim(left=-5, right=None)
ax2.set_ylim(top=None, ymin=9)

ax.legend(loc='upper left')
plt.show()
```

## Pyplot vs. Object-Oriented API Reference

| Action | Pyplot (`plt`) | Object-Oriented (`ax`) |
| :--- | :--- | :--- |
| Create Canvas | `plt.figure(figsize=(8, 4))` | `fig, ax = plt.subplots(figsize=(8, 4))` |
| Plot Data | `plt.plot(x, y)` | `ax.plot(x, y)` |
| Title & Labels | `plt.title()`, `plt.xlabel()` | `ax.set(title=..., xlabel=..., ylabel=...)` |
| Axis Limits | `plt.xlim([min, max])` | `ax.set_xlim(left=min, right=max)` |
| Show Legend | `plt.legend(loc="upper left")` | `ax.legend(loc="upper left")` |
| Inset Axis | Not directly supported | `fig.add_axes([left, bottom, width, height])` |
