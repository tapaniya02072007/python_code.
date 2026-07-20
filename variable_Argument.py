def add(farg,*args): 
    print("Formal arguments = ",farg) 
    sum=0 
    for i in args: 
        sum+=i 
        print("sum of all numbers= ",(farg+sum)) 
add(5,10) 
add(15,20,25,30) 
