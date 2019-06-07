def last(n):
    return n[-1]

def sort_List(tuples):
    return sorted(tuples, key=last)

print(sort_List([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
