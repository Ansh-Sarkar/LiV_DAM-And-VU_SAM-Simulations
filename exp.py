# Experimental use of defined functions and Python Code for running Simulations
# Python3 implementation of the approach
import random

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

def printGraph(graph):
    for key in graph.keys():
        print(key, " : ", graph[key])

def expGraph(graph):
    for i in range(10):
        graph[i] = []
    graph[2] = [6]
    graph[6] = [3]
    graph[3] = [9]
    graph[9] = [4]
    graph[4] = [6]

def detectSelfCycle(graph, node1, node2):
    if (node1 in graph[node2]) and (node2 in graph[node1]):
        return True
    return False

userPrefMatrixOverVSP = [
    [1, 3, 2, 0, 4],
    [2, 3, 4, 0, 1],
    [1, 2, 0, 3, 4],
    [4, 1, 2, 3, 0],
    [0, 3, 1, 2, 4]
]

graph = {}
for i in range(10):
    graph[i] = []

# graph = [[] for i in range(5 * 2)]
# allocations[i] => ith user is allocated the allocations[i]th VSP
allocations = [i for i in range(5)]
random.shuffle(allocations)


# put these initial allocations in the graph
# pretty obvious that we will not be getting
# any sort of cycles during this step.
for i in range(5):
    graph[5 + allocations[i]].append(i)

nextPref = [0 for i in range(5)]
freeUsers = [i for i in range(5)]

# g.addedge(0, 1)
# g.addedge(0, 2)
# g.addedge(0, 3)
# g.addedge(1, 2)
# g.addedge(3, 4)

# findCycle(n, e, g)

# expGraph(graph)
# cycle = []
# detectCycle(2, -1, graph, cycle)
# print("detected cycle : ", cycle)

while freeUsers:
    user = freeUsers.pop()
    graph[user].append(5 + userPrefMatrixOverVSP[user][nextPref[user]])
    nextPref[user] += 1

    print(f"Added edge: {user} to {graph[user][-1]}")

    # check for cycle by calling dfs on user to
    # which edge was newly node
    cycle = []
    print(f"Calling detectCycle on {user}")
    detectCycle(user, -1, graph, cycle)

    expGraph(graph)
    printGraph(graph)

    print("Detecting cycle . . . ")
    print("Cycle : ", cycle)
    # cycle = cycle[:-1]
    print("Cycle mil gayaaaaa !")
    selfCycle = detectSelfCycle(graph, user, 5 + userPrefMatrixOverVSP[user][nextPref[user]])
    print("Self Cycle Detection : ", selfCycle)

    print("")
    break

for i in userPrefMatrixOverVSP:
    print(*i)

print(graph, allocations)