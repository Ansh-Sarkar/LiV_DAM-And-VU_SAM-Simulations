# Used to create graphs between all the different attributes / variables
# and saves them to dedicated image files
import sys
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from modular_double_sided_matching import DoubleSidedMatching
from modular_single_sided_matching import SingleSidedMatching

if __name__ == '__main__':

    N = int(sys.argv[1])
    singleSidedAllocation = SingleSidedMatching(N)
    doubleSidedAllocation = DoubleSidedMatching(N)

    singleAllocationFreqRandom = [0 for _ in range(N)]
    for allocation in singleSidedAllocation[0]:
        singleAllocationFreqRandom[singleSidedAllocation[0][allocation]] += 1
    singleAllocationFreqAlloc = [0 for _ in range(N)]
    for allocation in singleSidedAllocation[1]:
        singleAllocationFreqAlloc[singleSidedAllocation[1][allocation]] += 1

    doubleAllocationFreqRandom = [0 for _ in range(N)]
    for allocation in doubleSidedAllocation[0]:
        doubleAllocationFreqRandom[doubleSidedAllocation[0][allocation]] += 1
    doubleAllocationFreqAlloc = [0 for _ in range(N)]
    for allocation in doubleSidedAllocation[1]:
        doubleAllocationFreqAlloc[doubleSidedAllocation[1][allocation]] += 1
    
    # doubleAllocationFreq = [0 for _ in range(N)]
    # for allocation in doubleSidedAllocation[0]:
    #     doubleAllocationFreq[allocation] += 1

    # figSingleSidedAllocation = plt.figure()
    # axSingleSidedAllocation = plt.axes(projection='3d')
    # # axSingleSidedAllocation.plot_surface(
    # #     singleSidedAllocation[0], singleSidedAllocation[1], np.array(singleSidedAllocation[2]), 
    # #     rstride = 1, cstride = 1, cmap = 'viridis', edgecolor = 'none')
    # axSingleSidedAllocation.scatter(
    #     singleSidedAllocation[0], 
    #     singleAllocationFreqRandom,
    #     singleSidedAllocation[1],
    #     cmap = 'viridis', 
    #     linewidth = 0.5
    # );
    # axSingleSidedAllocation.set_xlabel('actual allocation')
    # axSingleSidedAllocation.set_ylabel('count of preferences')
    # axSingleSidedAllocation.set_zlabel('random allocation');
    # plt.show()

    # figDoubleSidedAllocation = plt.figure()
    # axDoubleSidedAllocation = plt.axes(projection='3d')
    # axDoubleSidedAllocation.scatter(
    #     doubleSidedAllocation[0],  
    #     doubleAllocationFreq,
    #     doubleSidedAllocation[1],
    #     cmap = 'viridis', 
    #     linewidth = 0.5
    # );
    # axDoubleSidedAllocation.set_xlabel('actual allocation')
    # axDoubleSidedAllocation.set_ylabel('count of preferences')
    # axDoubleSidedAllocation.set_zlabel('random allocation');
    # plt.show()

    singleSidedRandom = []
    for i in range(N):
        singleSidedRandom.append([i, singleAllocationFreqRandom[singleSidedAllocation[0][i]], singleSidedAllocation[0][i]])
    print("Single Sided Random :", singleSidedAllocation[0])

    singleSidedAlloc = []
    for i in range(N):
        singleSidedAlloc.append([i, singleAllocationFreqAlloc[singleSidedAllocation[1][i]], singleSidedAllocation[1][i]])
    print("Single Sided Allocation :", singleSidedAllocation[1])

    doubleSidedRandom = []
    for i in range(N):
        doubleSidedRandom.append([i, doubleAllocationFreqRandom[doubleSidedAllocation[0][i]], doubleSidedAllocation[0][i]])
    print("Double Sided Random :", doubleSidedAllocation[0])

    doubleSidedAlloc = []
    for i in range(N):
        doubleSidedAlloc.append([i, doubleAllocationFreqAlloc[doubleSidedAllocation[1][i]], doubleSidedAllocation[1][i]])
    print("Double Sided Allocation :", doubleSidedAllocation[1])


    # print("\n\n\nTotal Single Sided Allocation Data Result")
    # print(singleSidedAllocation)

    # print("Single Sided Non Random : ", singleSidedAllocation[0])
    # print("Allocation Preference Matrix : ", singleAllocationFreqRandom)
    # print("Coordinates :")
    # for coordinate in singleSidedRandom:
    #     print(coordinate)

    xSingleRandom = [singleSidedRandom[i][0] for i in range(len(singleSidedRandom))]
    ySingleRandom = [singleSidedRandom[i][1] for i in range(len(singleSidedRandom))]
    zSingleRandom = [singleSidedRandom[i][2] for i in range(len(singleSidedRandom))]
    xSingleAlloc = [singleSidedAlloc[i][0] for i in range(len(singleSidedAlloc))]
    ySingleAlloc = [singleSidedAlloc[i][1] for i in range(len(singleSidedAlloc))]
    zSingleAlloc = [singleSidedAlloc[i][2] for i in range(len(singleSidedAlloc))]

    xDoubleRandom = [doubleSidedRandom[i][0] for i in range(len(doubleSidedRandom))]
    yDoubleRandom = [doubleSidedRandom[i][1] for i in range(len(doubleSidedRandom))]
    zDoubleRandom = [doubleSidedRandom[i][2] for i in range(len(doubleSidedRandom))]
    xDoubleAlloc = [doubleSidedAlloc[i][0] for i in range(len(doubleSidedAlloc))]
    yDoubleAlloc = [doubleSidedAlloc[i][1] for i in range(len(doubleSidedAlloc))]
    zDoubleAlloc = [doubleSidedAlloc[i][2] for i in range(len(doubleSidedAlloc))]

    figSingleSidedAllocation = plt.figure()
    axSingleSidedAllocation = plt.axes(projection='3d')
    # axSingleSidedAllocation.plot_surface(
    #     singleSidedAllocation[0], singleSidedAllocation[1], np.array(singleSidedAllocation[2]), 
    #     rstride = 1, cstride = 1, cmap = 'viridis', edgecolor = 'none')
    axSingleSidedAllocation.scatter3D(xSingleRandom, ySingleRandom, zSingleRandom, marker = "H", color = "green");
    axSingleSidedAllocation.scatter3D(xSingleAlloc, ySingleAlloc, zSingleAlloc, marker = "D", color = "hotpink")
    axSingleSidedAllocation.set_xlabel('User Number')
    axSingleSidedAllocation.set_ylabel('Count of Preferences')
    axSingleSidedAllocation.set_zlabel('Preference Index');
    plt.show()
    plt.savefig("3d_single_alloc.png")

    figDoubleSidedAllocation = plt.figure()
    axDoubleSidedAllocation = plt.axes(projection='3d')
    # axSingleSidedAllocation.plot_surface(
    #     singleSidedAllocation[0], singleSidedAllocation[1], np.array(singleSidedAllocation[2]), 
    #     rstride = 1, cstride = 1, cmap = 'viridis', edgecolor = 'none')
    axDoubleSidedAllocation.scatter3D(xDoubleRandom, yDoubleRandom, zDoubleRandom, color = "purple", marker = "p");
    axDoubleSidedAllocation.scatter3D(xDoubleAlloc, yDoubleAlloc, zDoubleAlloc, color = "orange", marker = "*")
    axDoubleSidedAllocation.set_xlabel('LiDAR Number')
    axDoubleSidedAllocation.set_ylabel('Count of Preferences')
    axDoubleSidedAllocation.set_zlabel('Preference Index');
    plt.show()
    plt.savefig("3d_double_alloc.png")

