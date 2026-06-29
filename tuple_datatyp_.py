print("..............code.1")
tup=()
print(tup)
print(" ")

#string
tup=('jnis','tpny')
print(tup)
print(" ")

#list
li=[1,2,3,4,5]
print(tuple(li))
print(" ")

#built-in function
tup=tuple('tapaniya')
print(tup)
print(" ")

print("..............code.2")
t=(10,'tapaniya',10.30)
#t[0]=100 //array is not supported
for i in t:
    print(i)
print(" ")

print("..............code.3")
tup=tuple("jenish")
print(tup[0])
print(tup[1:4])
print(tup[3:])
print(" ")

print("..............code.4")
tup=tuple("kamani_science_collage_amreli")
print(tup[0])
print("---------------------")
print(tup[1:12:2])
print("---------------------")
print(tup[0:10:3])
print("---------------------")
print(tup[3:])
print("---------------------")
print(tup[1:15:6])
print("---------------------")
print(tup[10:0:-1])
print("---------------------")
print(tup[15:-2:])
print("---------------------")
print(" ")

print("..............code.5")
tup1=(2,4,6)
tup2=('abc','pqr','xyz')
tup3=tup1+tup2
print(tup3)


