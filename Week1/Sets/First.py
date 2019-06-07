thisset = {"Apple", "Bannana", "Mango"}
#thisset.clear()
print(thisset)

# iterate
loopset = {"Gayatri","Digvijay","Patil"}
for x in loopset:
    print(x)

# Add member
addset = {1,2,3}
addset.add(4)
addset.remove(2)
print(3 in addset)

# check present then remove
rmvset = {"1","2","3","4","5"}
rmvset.discard(3)
print(rmvset)

#Intersection set
setx = {"Gayatri","Digvijay","Patil"}
sety = {"Gayatri","Gajanan","Jadhav"}
#setz = setx.intersection(sety)
#setz = setx.union(sety)
#setz = sety.difference(setx)
setz = setx.symmetric_difference(sety)
print(setz)