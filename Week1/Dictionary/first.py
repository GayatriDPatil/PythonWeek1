y={
    1:2,3:4,4:3,2:1,0:0
  } 
                                         
l=list(y.items())   #convet the given dict. into list
#In Python Dictionary, items() method is used to return the list
l.sort()   
print('Ascending order is',l)

l=list(y.items())
l.sort(reverse=True) #sort in reverse order
print('Descending order is',l)

dict=dict(l) # convert the list in dictionary 

print("Dictionary",dict) #the desired output is this sorted dictionary
