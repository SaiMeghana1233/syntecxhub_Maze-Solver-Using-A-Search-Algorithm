# 🧠 Maze Solver using A* Search Algorithm

## 📌 Project Overview
This project implements the A* (A-Star) Search Algorithm to find the shortest path in a grid-based maze environment. The maze consists of a start node (S), goal node (G), walls (#), and open paths (.).

The algorithm efficiently computes the optimal shortest path using heuristic-based cost evaluation.

---

## 🚀 Features
- Grid-based maze representation
- A* Search Algorithm implementation
- Manhattan and Euclidean heuristic support
- Shortest path computation
- Obstacle handling
- Unreachable case detection
- Console visualization of final path

---

## 🧮 Algorithm Explanation

A* uses the evaluation function:

f(n) = g(n) + h(n)

Where:
- g(n) → Actual cost from start to current node
- h(n) → Heuristic estimated cost from current node to goal
- f(n) → Total estimated cost

The algorithm selects the node with the lowest f(n) value using a priority queue to guarantee the shortest path (when heuristic is admissible).

---

## 🛠️ Technologies Used
- Python
- Heapq (Priority Queue)
- Basic Data Structures

---

## ▶️ How to Run the Project

1. Install Python (if not installed)
2. Open Command Prompt inside project folder
3. Run:
