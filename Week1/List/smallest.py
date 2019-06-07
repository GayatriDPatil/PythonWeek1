#def small_num(items):
 #   smallest_number = 0
#print("smallest number is :", min([5,3,2]))

def smallest_num(items):
    multi_numbers = items[0]
    for x in items:
       if x < multi_numbers:
           multi_numbers = x
    return multi_numbers
print(smallest_num([5,5,2,-9]))