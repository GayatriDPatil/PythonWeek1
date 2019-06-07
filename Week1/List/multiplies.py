def multiplies(items):
    multi_numbers = 1
    for x in items:
        multi_numbers *=x
    return multi_numbers
print(multiplies([5,5,2]))