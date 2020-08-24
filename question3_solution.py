
def compare_tuple(tup1, tup2):
    if tup1[0] == tup2[0] or tup1[1] == tup2[1] or tup1[2] == tup2[2]:
        return True
    else:
        return False


def get_indices(arr):
    matched_result = []
    noMatch = []
    for i in range(len(arr)):
        ismatch = False
        for j in range(i+1, len(arr)):
            if compare_tuple(arr[i], arr[j]):
                ismatch = True
                if i not in matched_result:
                    matched_result.append(i)
                matched_result.append(j)
        if not ismatch and i not in matched_result:
            noMatch.append(i)

    return [matched_result, noMatch]
