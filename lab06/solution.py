def count_items(values):
    ans = {}
    for i in values:
        ans[i] = ans.get(i, 0)+1
    return ans


def unique_sorted(values):
    return sorted(set(values))

def common(first, second):
    return sorted(set(first) & set(second))

def only_in_first(first, second):
    return sorted(set(first) - set(second))
