# Function for Depth-First Search (DFS)
def dfs(graph, start, visited):
    # Mark the current node as visited
    visited[start] = True
    print(start, end=' ')  # Print the current node
    
    # Recur for all the vertices adjacent to this vertex
    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited)

# Main function
if __name__ == "__main__":
    # Example graph represented by adjacency list
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2]
    }
    
    # Number of vertices
    num_vertices = 6
    
    # Array to keep track of visited nodes
    visited = [False] * num_vertices
    
    # Calling DFS from the starting node 0
    print("Depth-First Search starting from node 0:")
    dfs(graph, 0, visited)
