Dijkstra algorithm for uninformed search.
A* algorithm for informed search.
Manhattan distance is used for heuristic computing in A*.

Performance comparsion: A* is 20% faster than dijkstra on average.

Common functions:
getnums(filename): get number of vertices and number of edges.
readfile(filename): read data file into vertex and edge structure.
extract_min(vertices, g): g==Ture, return the vertex with minimum distance(g(n))
		      g==False, return the vertex with minimum heuristic(h(n))
reconstruct_path(previous,end): return path
edges: 2D array, the distance between vertex I and vertex j is edges[i][j] if edges[i][j]!=0

