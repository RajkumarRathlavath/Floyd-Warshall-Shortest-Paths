# Floyd–Warshall Shortest Paths

This project contains a simple Python implementation of the **Floyd–Warshall algorithm** for finding the shortest paths between all pairs of vertices in a weighted graph.

---

## Features
- Works with **directed** and **undirected** graphs  
- Handles **positive** and **negative** edge weights (no negative cycles)  
- Produces a **distance matrix** showing shortest path costs  

---

## File Structure
- **`main.py`** – Contains the Floyd–Warshall implementation and a sample run  

---

## Example Usage
```bash
python main.py

Example input (distance matrix):
[
    [0, 5, 999, 10],
    [999, 0, 3, 999],
    [999, 999, 0, 1],
    [999, 999, 999, 0]
]

Example output:
Shortest distance matrix:
[0, 5, 8, 9]
[999, 0, 3, 4]
[999, 999, 0, 1]
[999, 999, 999, 0]


The algorithm updates distances between all vertex pairs by checking if passing through an intermediate vertex offers a shorter path.
It runs in O(n³) time, where n is the number of vertices.
