# Linear Algebra Applications

This repository is my personal sandbox for exploring and implementing **Linear Algebra** algorithms completely from scratch as part of my computer engineering / software engineering coursework.

> **Current Update Note:** Refactoring legacy Turkish code into English, improving time/space complexity ($O(n)$ bounds), and adding deep structural matrix operations.

---

## Project Philosophy & Motto

- **Learn by Implementing:** I avoid using pre-built high-level linear algebra libraries for core logic. My primary goal is to write everything from basic primitives to understand what happens under the hood—focusing heavily on algorithmic cost, memory management, and time complexity.
- **Weekly Learning Loop:** Whenever I learn a new theoretical topic in class, I sit down and convert it into code. If a topic isn't directly suitable for strict computer logic, I take the concepts and build creative experiments around them just for fun!
- **Purely for Fun & Mastery:** This repository grows with my knowledge. Expect continuous refactoring, optimization passes, and low-level matrix experiments.

---

## Key Features & Progress

- **Determinant Calculator (`CalcDeterminant`)**:
  - Direct branch paths for small matrices ($1\times1$, $2\times2$, and $3\times3$ Sarrus Rule).
  - Row reduction / **Gaussian Elimination** for general $N \times N$ matrices to maintain optimal time complexity.
- **Matrix Property Analyzer**:
  - Deterministic checks for Symmetry (`is_symmetrical`), Anti-symmetry (`anti_symetrical`), Orthogonality (`is_orthogonal`), and Periodicity (`is_periodic`).
- **Custom Mathematical Exception Handling**:
  - Strict shape and type validation (e.g., enforcing square matrix requirements before determinant or trace calculation).
- **Work in Progress**:
  - Zero-count optimization (`CountZeros`) for high-efficiency **Laplace Expansion**.

---

## Tech Stack & Requirements

- **Python 3.x**
- Minimal dependencies (NumPy used only as a lightweight array container during refactoring passes).

---

*I'm doing this to challenge myself, understand low-level execution efficiency, and enjoy the math. Hope you find it interesting!*
