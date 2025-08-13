def floyd_warshall(n, graph):

     # Define infinity as maximum value for comparison

    INF = float('inf')

     # Create a matrix initialized with infinity for all pairs of vertices
    floyd_warshall_matrix = list(map(lambda _: [INF] * (n + 1), range(n + 1)))

    # Modify the matrix diagonals to be zero (if i equals j)

    floyd_warshall_matrix = [
        [0 if row == col else floyd_warshall_matrix[row][col] for col in range(len(floyd_warshall_matrix))]
        for row in range(len(floyd_warshall_matrix))
    ]
    

     # Update the matrix with edge weights from the given graph
    for u in range(1, n + 1):
        for edge in graph[u]:
            v, w = edge
            floyd_warshall_matrix[u][v] = w

    # Apply the Floyd-Warshall algorithm to find shortest paths
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):

                # Update the shortest path if a shorter path is found through intermediate vertex k

                floyd_warshall_matrix[i][j] = min(
                    floyd_warshall_matrix[i][j], floyd_warshall_matrix[i][k] + floyd_warshall_matrix[k][j]
                )

        # Retrieve the shortest path from vertex 1 to n if exists, otherwise return "INFINITY"
    result = floyd_warshall_matrix[1][n] if floyd_warshall_matrix[1][n] != INF else "INFINITY"
    return result



def floyd_warshall_main():

    # Take user input for number of vertices (n) and edges (m)

    user_input = input().split()[::]

    iter_data = map(str, user_input)

    n, m = map(int, (next(iter_data), next(iter_data)))

    # Create an empty graph represented as a dictionary

    graph_matrix = {}
    
    graph_matrix = {i: [] for i in range(1, n + 1)}
    count_graph = 0


    # Populate the graph with edges and their weights

    for _ in range(m):
        values = list(map(int, input().split()))
        q1, q2, q3 = values[0], values[1], values[2]

         # Check if a node is not already in the graph and add it with its respective edge

        if q1 not in graph_matrix:
            graph_matrix[q1] = []
        graph_matrix[q1].append((q2, q3))

        # Calculate and print the shortest path using Floyd-Warshall algorithm

    floyd_warshall_output = floyd_warshall(n, graph_matrix)
    print(floyd_warshall_output)

    # Execute the main function

floyd_warshall_main()



