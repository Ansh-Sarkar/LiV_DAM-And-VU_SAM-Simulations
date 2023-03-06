# Modular / function wise implementation of the Single Sided Matching Algorithm
import sys
import random
import numpy as np
import matplotlib.pyplot as plt

def helper(node, par, graph, visited, parent, cycle):
    if not visited[node]:
        cycle.append(node)
        parent[node] = par
        visited[node] = True
        for neighbour in graph[node]:
            point = helper(neighbour, node, graph, visited, parent, cycle)
            if point != -1:
                return point
        cycle.pop()
        return -1
    else:
        if parent[node] != par:
            return node

def detectCycle(node, par, graph):
    cycle = []
    visited = [False for _ in range(len(graph))]
    parent = [-1 for i in range(len(graph))]
    cyclicPoint = helper(node, par, graph, visited, parent, cycle)
    if cyclicPoint == -1: return []
    print("Lets see where the error is : ", cycle)
    try:
        return cycle[cycle.index(cyclicPoint):]
    except Exception as error:
        print("Error :", error)
        return []

def printGraph(graph):
    for key in graph.keys():
        print(key, " : ", graph[key])

def reassignEntities(graph, cycle, n, freeUsers, allocations):
    for i in range(0, len(cycle), 2):
        user, vsp = cycle[i], cycle[i + 1]
        print(f"user: {user}, vsp: {vsp}")
        try:
            allocations[user] = vsp
        except Exception as error:
            print("Error :", error)
            return
        graph[user] = []
        graph[vsp] = []

        for user in range(n):
            temp = []
            for v in graph[user]:
                if v != vsp:
                    temp.append(v)
            graph[user] = temp
        
        try: freeUsers.pop(freeUsers.index(user))
        except Exception as error: print(f"Expected error occurred : {error}")

def plotGraph(manPrefIndex, manPrefIndexRandom, n):
    # Plotting Man Number Vs Woman Allocation Preference Index
    x = np.arange(int(n))

    # plt.plot(x,manPrefIndex,'b-',x,manPrefIndexRandom,'g--')
    plt.plot(x, manPrefIndex, "bo", color = "hotpink", marker = "D", label="VSP-User Matching")
    plt.plot(x, manPrefIndexRandom, "r^", color = "green", marker = "H", label="Random Matching")

    plt.legend()
    plt.title("Random Matching Vs VSP-User Matching")

    plt.ylabel(
        "Preference Index of Allocated VSP\n(High pref --> Low pref)"
    )
    plt.xlabel("User Number")
    plt.savefig(str(str(n) + ".png"))
    # plt.plot()

# userPrefMatrixOverVSP = [
#     [1, 3, 2, 0, 4],
#     [2, 3, 4, 0, 1],
#     [1, 2, 0, 3, 4],
#     [4, 1, 2, 3, 0],
#     [0, 3, 1, 2, 4]
# ]

def SingleSidedMatching(n):
    userPrefMatrixOverVSP = []
    for _ in range(n):
        pref = [i for i in range(n)]
        random.shuffle(pref)
        userPrefMatrixOverVSP.append(pref)

    while True:
        graph = {}
        for i in range(2 * n):
            graph[i] = []

        # graph = [[] for i in range(n * 2)]
        # allocations[i] => ith user is allocated the allocations[i]th VSP
        allocations = [i for i in range(n)]
        random.shuffle(allocations)

        # put these initial allocations in the graph
        # pretty obvious that we will not be getting
        # any sort of cycles during this step.
        for i in range(n):
            graph[n + allocations[i]].append(i)

        nextPref = [0 for i in range(n)]
        freeUsers = [i for i in range(n)]

        print(allocations)

        counter = 0

        while freeUsers:
            for user in freeUsers:
                graph[user].append(n + userPrefMatrixOverVSP[user][nextPref[user]])

                nextPref[user] += 1
                counter += 1
                
                if nextPref[user] >= n:
                    try: 
                        freeUsers.pop(freeUsers.index(user))
                        continue
                    except Exception as error: print(f"Expected error occurred : {error}")

                print(f"Added edge: {user} to {graph[user][-1]}")

                # check for cycle by calling dfs on user to
                # which edge was newly node
                print(f"Calling detectCycle on {user}")
                cycle = detectCycle(user, -1, graph)

                if cycle != []:
                    if len(cycle) % 2 == 0:
                        reassignEntities(graph, cycle, n, freeUsers, allocations)

        for i in userPrefMatrixOverVSP:
            print(*i)

        print(graph)
        flag = True
        for allocation in allocations:
            if allocation < n:
                flag = False
                break
        if flag:
            allocations = [userPrefMatrixOverVSP[user].index(allocations[user] - n) for user in range(n)]
            print("VSP-User Allocation : ", allocations)
            randomAllocations = [i for i in range(n)]
            random.shuffle(randomAllocations)
            print("Random Allocation :", randomAllocations)
            print("Plotting Graph : ")
            plotGraph(allocations, randomAllocations, len(allocations))
            return (randomAllocations, allocations, userPrefMatrixOverVSP)

# # allocations = [x - n for x in allocations]
# print("allocations :", allocations)

# randomAllocations = [i for i in range(n)]
# random.shuffle(randomAllocations)
# print("randomAllocations :", randomAllocations)

if __name__ == '__main__':
    print(SingleSidedMatching(20))