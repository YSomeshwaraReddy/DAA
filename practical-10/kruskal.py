def kruskal(edges, vertices):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    parent = {v: v for v in vertices}
    mst = []
    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for u, v, weight in edges:
        root_u = find(u)
        root_v = find(v)
        # Check if adding edge creates a cycle
        if root_u != root_v:
            mst.append((u, v, weight))
            parent[root_u] = root_v
    return mst
# Vertices
vertices = ['A', 'B', 'C', 'D']
# Edges: (vertex1, vertex2, weight)
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 2),
    ('B', 'D', 4),
    ('C', 'D', 5)
]
# Find MST
mst = kruskal(edges, vertices)
print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(u, "-", v, "=", weight)