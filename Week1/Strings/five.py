def longestword(wrdlist):
    word_length = []
    for n in wrdlist:
        word_length.append((len(n), n))
    word_length.sort()
    return word_length[-1][1]

print (longestword(["Gayatri","Divya","Digvijay"]))