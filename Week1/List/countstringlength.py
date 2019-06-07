def count_string(words):
    strng = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            strng +=1
    return strng
print(count_string(['abc', 'xyz', 'aba', '1221']))