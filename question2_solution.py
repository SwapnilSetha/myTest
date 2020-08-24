def countPairsWithDiffK(arr, n, k):
    count = []
    for i in range(0, n):
        for j in range(i+1, n):
            if abs(arr[i] - arr[j]) == abs(k):
                count.append((arr[i], arr[j]))

    return count
