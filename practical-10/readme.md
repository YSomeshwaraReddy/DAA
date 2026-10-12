## Overall Summary
This project implements **Kruskal’s Algorithm** in Python to find the **Minimum Spanning Tree (MST)** of a weighted, undirected graph. The algorithm sorts all edges in ascending order of their weights and selects the minimum-weight edges one by one, ensuring that no cycle is formed.
The implementation uses a `find()` function to identify the connected components of vertices and a parent dictionary to manage connections between them. By adding an edge only when its two endpoints belong to different components, the algorithm avoids cycles and constructs a Minimum Spanning Tree with the minimum possible total edge weight.
The example graph contains four vertices (`A`, `B`, `C`, and `D`) and five weighted edges. The algorithm selects the edges `A-B`, `B-C`, and `B-D`, producing a Minimum Spanning Tree with a total weight of **7**.
### Key Features
- Sorts edges by weight in ascending order.
- Selects minimum-weight edges to construct the MST.
- Prevents cycles using a `find()` function and a parent dictionary.
- Demonstrates graph representation using vertices and weighted edges.
- Displays the selected MST edges along with their weights.
## Overall Conclusion
Kruskal’s Algorithm provides an efficient and systematic way to find a Minimum Spanning Tree in a connected, weighted, undirected graph. This implementation demonstrates the fundamental concepts of greedy algorithms, graph traversal concepts, cycle prevention, and minimum-cost network construction.
For the given example, the algorithm produces a Minimum Spanning Tree containing three edges with a total weight of **7**, connecting all four vertices without forming any cycles.
This project helps build a practical understanding of graph algorithms and their applications in network design, communication systems, and cost-efficient infrastructure planning. It also provides a foundation for exploring more optimized implementations using the Disjoint Set Union (DSU) data structure with path compression and union by rank.
Overall, the project demonstrates how Kruskal’s Algorithm can be implemented in Python to solve the Minimum Spanning Tree problem using a greedy approach.