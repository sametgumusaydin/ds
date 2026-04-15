class Graph:
    """
    Graph implementation using a Python dictionary as an adjacency list.
    Each key in graphdict represents a node, and its value is a list of
    (neighbor, weight) tuples.

    Supports:
    - Directed / Undirected graphs
    - Weighted edges
    """

    def __init__(self, directed=False, weighted=False):
        self.directed = directed
        self.weighted = weighted
        self.graphdict = {}     # { node_name : [(neighbor, weight), ...] }

    # ------------------------------------------------------------
    # Add a new node to the graph
    # ------------------------------------------------------------
    def add_node(self, node):
        """
        Add a new node to the graph.
        If the node already exists, return a warning message.
        """
        if node not in self.graphdict:
            self.graphdict[node] = []
        else:
            return "Node already exists"

    # ------------------------------------------------------------
    # Add an edge between node1 and node2
    # ------------------------------------------------------------
    def add_edge(self, node1, node2, weight=1):
        """
        Add an edge between node1 and node2.
        For undirected graphs, add edges in both directions.
        Each edge is stored as (neighbor, weight).

        Returns node name if it does not exist in graph.
        """
        if node1 not in self.graphdict:
            return f"Node '{node1}' does not exist"
        if node2 not in self.graphdict:
            return f"Node '{node2}' does not exist"

        # Add edge node1 -> node2
        self.graphdict[node1].append((node2, weight))

        # If graph is undirected, also add edge node2 -> node1
        if not self.directed:
            self.graphdict[node2].append((node1, weight))

    # ------------------------------------------------------------
    # Print the graph (adjacency list)
    # ------------------------------------------------------------
    def print_graph(self):
        """
        Print the adjacency list of the graph.
        Shows neighbors along with weight values.
        """
        for node in self.graphdict:
            print(f"{node} -> {self.graphdict[node]}")

    # ------------------------------------------------------------
    # Breadth-First Search (BFS)
    # ------------------------------------------------------------
    def bfs(self, start):
        """
        Perform Breadth-First Search starting from 'start' node.
        Returns the visitation order.

        BFS uses a queue and explores the graph level by level.
        """
        if start not in self.graphdict:
            return "Start node does not exist"

        visited = set()
        queue = []
        order = []

        visited.add(start)
        queue.append(start)

        while queue:
            current = queue.pop(0)
            order.append(current)

            for (neighbor, _) in self.graphdict[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    # ------------------------------------------------------------
    # Depth-First Search (DFS) - Recursive
    # ------------------------------------------------------------
    def dfs_recursive(self, start):
        """
        Perform Depth-First Search using recursion.
        Returns visitation order.
        """
        if start not in self.graphdict:
            return "Start node does not exist"

        visited = set()
        order = []

        def dfs(node):
            visited.add(node)
            order.append(node)
            for (neighbor, _) in self.graphdict[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return order

    # ------------------------------------------------------------
    # Depth-First Search (DFS) - Iterative
    # ------------------------------------------------------------
    def dfs_iterative(self, start):
        """
        Perform DFS using an explicit stack.
        """
        if start not in self.graphdict:
            return "Start node does not exist"

        visited = set()
        stack = [start]
        order = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                order.append(current)

                # Reverse to mimic recursive DFS order
                neighbors = [n for (n, _) in self.graphdict[current]]
                for n in reversed(neighbors):
                    if n not in visited:
                        stack.append(n)

        return order

    # ------------------------------------------------------------
    # Shortest Path (Unweighted Graph) - BFS
    # ------------------------------------------------------------
    def shortest_path_unweighted(self, start, target):
        """
        Compute shortest path in UNWEIGHTED graph using BFS.
        Returns the list of nodes from start to target.
        """
        if start not in self.graphdict:
            return "Start node does not exist"
        if target not in self.graphdict:
            return "Target node does not exist"

        visited = set()
        prev = {node: None for node in self.graphdict}
        queue = []

        visited.add(start)
        queue.append(start)

        while queue:
            current = queue.pop(0)
            if current == target:
                break

            for (neighbor, _) in self.graphdict[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    prev[neighbor] = current
                    queue.append(neighbor)

        # No path?
        if prev[target] is None and start != target:
            return None

        # Reconstruct path
        path = []
        at = target
        while at is not None:
            path.append(at)
            at = prev[at]

        path.reverse()
        return path

    # ------------------------------------------------------------
    # Dijkstra Algorithm (Weighted Graph, Non-negative weights)
    # ------------------------------------------------------------
    def dijkstra(self, start):
        """
        Compute shortest distances from 'start' to all nodes
        using Dijkstra's algorithm.

        Requires all weights to be NON-NEGATIVE.
        """
        import heapq

        if start not in self.graphdict:
            return "Start node does not exist"

        # Distance dictionary
        dist = {node: float("inf") for node in self.graphdict}
        dist[start] = 0

        # Min-heap priority queue
        pq = [(0, start)]

        while pq:
            current_dist, node = heapq.heappop(pq)

            # Ignore outdated entries
            if current_dist > dist[node]:
                continue

            # Explore neighbors
            for (neighbor, weight) in self.graphdict[node]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return dist



g2=Graph(True,True)
g2.add_node('A')
g2.add_node('B')
g2.add_node('C')
g2.add_node('D')
g2.add_node('E')

g2.add_edge('A','B',6)
g2.add_edge('A','D',1)
g2.add_edge('B','C',5)
g2.add_edge('B','E',4)
g2.add_edge('C','E',5)
g2.add_edge('D','B',2)
g2.add_edge('D','E',1)
g2.add_edge('E','B',2)

for key,value in g2.graphdict.items():
    print(key+ ' ->', end=(' '))
    for i in value:
        print(str(i[0])+ ':'+'weight :'+str(i[1]),end=(' '))
    print(' ')

g2.dijkstra('A')
g2.dfs_recursive('A')
