# Temporary code that is used for the detecting cycles in the graph
def helper(node, par, visited, graph, cycle):
    visited[node] = True
    print(f"{node} ", end = "")
    cycle.append(node)
    for neighbour in graph[node]:
        if not visited[neighbour]:
            if helper(neighbour, node, visited, graph, cycle):
                return True
        elif par != neighbour:
            cycle.append(neighbour)
            return True
    cycle.pop()
    return False

def detectCycle(node, par, graph, cycle):
    visited = [False for i in range(len(graph))]
    helper(node, par, visited, graph, cycle)
    print("Cycle form inside detectCycle : ", cycle)
    return cycle

graph = [[] for i in range(5 * 2)]
graph[2] = [6]
graph[6] = [2]

cycle = []
print(detectCycle(2, -1, graph, cycle))
print("Cycle :", cycle)