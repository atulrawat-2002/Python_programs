def maxOfSubarrays(arr, k):
    n = len(arr)

    res = []

    for i in range(0, n - k + 1):

        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        res.append(max)

    return res