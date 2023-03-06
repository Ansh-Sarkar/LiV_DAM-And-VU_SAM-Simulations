# Modular / function wise implementation of the Double Sided Matching Algorithm
import os
import sys
import random
import numpy as np
import matplotlib.pyplot as plt

# *
# * shuffle to create random order.
#
def createRandomPrefs(v):
    # Create a vector with the values 0, 1, 2, ...
    # i = 0
    # while i < len(v):
    # 	v[i] = i
    # 	i += 1
    # Create a random permutation of this vector.
    random.shuffle(v)


# here we are taking the preference lists of every man and woman and just
# randomly shuffling them so as to create a random preference profile
def StableMarriage(n, manPref, womanPref):
    for i in range(int(n)):
        createRandomPrefs(manPref[i])
        createRandomPrefs(womanPref[i])
        # random.shuffle(manPref[i])
        # random.shuffle(womanPref[i])


# *
# * Prints the matrix v.
#
def printMatrix(v):
    if v == None:
        print("<null>")
        return
    i = 0
    while i < len(v):
        sys.stdout.write("  " + str(i) + "  |")
        j = 0
        while j < len(v[i]):
            sys.stdout.write(" " + str(v[i][j]) + " ")
            j += 1
        print(" ")
        i += 1


# As the name suggests, this function is used to print the
# preference matrix. Uses a helper function to do so.
def printPrefTables(manPref, womanPref):

    print("\n  Man Preferences")
    print("--------------------------")
    printMatrix(manPref)
    print("\n  Woman Preferences")
    print("--------------------------")
    printMatrix(womanPref)


# *
# * Returns true iff w prefers x to y.
#
def prefers(w, x, y, womanPref, n):
    for i in range(int(n)):
        pref = womanPref[w][i]
        if pref == x:
            return True
        if pref == y:
            return False
    # This should never happen.
    print("Error in womanPref list " + w)
    return False


# *
# * Returns a stable marriage in the form an int array current,
# * where current[i] is the man married to woman i.
#
def stable(manPref, manPrefIndex, womanPref, n):
    # Indicates that woman i is currently engaged to
    # the man current[i].
    current = []
    NOT_ENGAGED = -1
    for i in range(int(n)):
        current.append(NOT_ENGAGED)

    # List of men that are not currently engaged.
    freeMen = []
    # since initially no man is engaged, we add all of them to the
    # list of free men
    for i in range(int(n)):
        freeMen.append(i)

    # next[i] is the next woman to whom i has not yet proposed.
    next = []
    for i in range(int(n)):
        next.append(0)

    # computeRanking
    # while there exist free men
    while freeMen:

        # we take out the next man from the list of free men
        m = freeMen.pop()

        # the woman to whom this man would like to propose is the next
        # one in his preference list. this is why initially all the values
        # in the next list is set to 0 which points towards the first
        # value in the manPref list of the mth man which in turn denotes
        # his most preferred choice of woman.
        w = manPref[m][next[m]]

        # so once this is done, we store this new preference for the man.
        manPrefIndex[m] = next[m]  # Store index of preference for man

        # we then increment the next index by 1 which means that the next
        # time the man tries to propose, it would be to the next woman in
        # his preference list
        next[m] += 1

        # once we have our woman selected, we check if she is engaged or
        # if she is not engaged then she marries the current man
        if current[w] == NOT_ENGAGED:
            current[w] = m
        else:
            # if she is already engaged, then we check who that man is to
            # whom she is already engaged
            m1 = current[w]

            # we ask the woman whom she prefers and if she prefers the
            # current man over the man she was previously engaged to,
            # she is engaged to the current man and the previous man is
            # added back to the free men list, waiting to propose the
            # next woman in his preference list
            if prefers(w, m, m1, womanPref, n):
                current[w] = m
                freeMen.append(m1)
            else:
                # in case, the woman still prefers the same man, over
                # the current man, then the current man is sent back
                # into the free men list where he waits in order to
                # propose to his next most preferred woman in the profile
                freeMen.append(m)

    # once the entire allocation is done, and no free man exists, it would
    # mean that no free woman or unengaged woman also exists as there are n
    # of each gender and stable one to one mapping is guaranteed by Galey-Shapley
    # thereby meaning that all engagements have been made.
    return current


def printMarriage(m):
    print("\nAllocated Pairs (LiDAR, VSP): ")
    print("------------------------------")
    i = 0
    while i < len(m):
        print("(" + str(i) + ", " + str(m[i]) + ")")
        i += 1
    print("")


# Creates a Random marriage of size n
def createRandomMarriage(randomMarriage):
    # Create a vector with the values 0, 1, 2, ...
    i = 0
    while i < len(randomMarriage):
        randomMarriage[i] = i
        i += 1
    # Create a random permutation of this vector.
    random.shuffle(randomMarriage)


def findRandomMarriagePrefIndex(randomMarriage, manPref, manPrefIndexRandom, n):
    for i in range(int(n)):
        m = randomMarriage[i]
        for j in range(int(n)):
            if manPref[m][j] == i:
                manPrefIndexRandom[m] = j


def plotGraph(manPrefIndex, manPrefIndexRandom, n):
    # Plotting Man Number Vs Woman Allocation Preference Index
    x = np.arange(int(n))

    # plt.plot(x,manPrefIndex,'b-',x,manPrefIndexRandom,'g--')
    plt.plot(x, manPrefIndex, "bo", color = "purple", marker = "p", label="LiDAR-VSP Matching")
    plt.plot(x, manPrefIndexRandom, "r^", color = "orange", marker = "*", label="Random Matching")

    plt.legend()
    plt.title("Random Matching Vs LiV-DAM Matching")

    plt.ylabel(
        "Preference Index of Allocated VSP\n(High pref --> Low pref)"
    )
    plt.xlabel("LiDAR Number")
    plt.savefig("LiV-DAM_" + str(n) + ".png")
    # plt.show()


def DoubleSidedMatching(n):
    print("\nLiV-DAM Matching Allocation Algorithm Execution\n")

    # we need to pass the arguments, or number of entities on
    # both sides (n) as well via the terminal
    # if len(sys.argv) == 2:
    #     n = sys.argv[1]
    # else:
    #     print(f"Usage: python {__file__.split('/')[-1]} <n> \n")
    #     exit()

    # preference of man
    manPrefIndex = []
    # for every man we create a new preference list
    for i in range(int(n)):
        manPrefIndex.append([])

    # we are creating men, and also corresponding lists and then appending
    # all possible women, from 0 to n - 1 to this list. Initially this list seems
    # ordered but as we move further, we shuffle the orders to form a random
    # preference list
    manPref = []
    for i in range(int(n)):
        # appending an empty preference list for every man
        manPref.append([])
        for j in range(int(n)):
            # appending all women from 0 to n - 1 in the list
            manPref[i].append(j)

    # we are creating women, and also corresponding lists and then appending
    # all possible men, from 0 to n - 1 to this list. Initially this list seems
    # ordered but as we move further, we shuffle the orders to form a random
    # preference list
    womanPref = []
    for i in range(int(n)):
        # appending an empty preference list for every women
        womanPref.append([])
        for j in range(int(n)):
            # appending all women from 0 to n - 1 in the list
            womanPref[i].append(j)

    # * Calling StableMarriage()
    StableMarriage(n, manPref, womanPref)

    print("Random Preference Tables : ")
    printPrefTables(manPref, womanPref)

    marriage = []
    marriage = stable(manPref, manPrefIndex, womanPref, n)
    printMarriage(marriage)

    print("LiDAR Preference Index In LiDAR-VSP Allocation : ", manPrefIndex)

    # * *******************************************
    # * Create Arbitrary Marriage Problem of size n
    # * *******************************************
    randomMarriage = []
    for i in range(int(n)):
        randomMarriage.append(i)
    createRandomMarriage(randomMarriage)

    # *
    # * FIND PREF INDEX OF RANDOM MARRIAGE
    # *
    manPrefIndexRandom = []
    for i in range(int(n)):
        manPrefIndexRandom.append(i)

    print("\n*******************************************************")
    print("\nExecuting LiDAR-VSP Matching Algorithm                 ")

    printMarriage(randomMarriage)
    findRandomMarriagePrefIndex(randomMarriage, manPref, manPrefIndexRandom, n)
    print("Random Allocation Preference Index : ", manPrefIndexRandom)

    plotGraph(manPrefIndex, manPrefIndexRandom, n)
    return (manPrefIndexRandom, manPrefIndex, womanPref)

if __name__ == '__main__':
    print(DoubleSidedMatching(20))