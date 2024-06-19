# TSP = Traveling Salesman Problem
# Given a list of cities, the distances between each pair of cities, and a total distance,
# is there a path through all the cities that is less than the distance given?
def tsp(cities, path, dist):
    permuts = permutations(cities)
    for permutation in permuts:
        distance_sum = 0
        for i in range(1, len(permutation)):
            distance_sum += path[permutation[i - 1]][permutation[i]]
        if distance_sum <= dist:
            return True
    return False


# don't touch below this line
def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res


# This function verifies the actual_path instead of search for the shortest
# That is why TSP is in NP, cause we can also verifiy a solution much faster.
def verify_tsp(paths, dist, actual_path):
    dist_sum = 0
    for i in range(1, len(actual_path)):
        dist_sum += paths[actual_path[i - 1]][actual_path[i]]
    if dist_sum > dist:
        return False
    return True
