"""
Question4.
     *
    * *
   * * *
    * *
     *


"""
a=5
for i in range(1,4):
    for k in range(1,a-i,+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print(end="\n")

for i in range(3,1,-1):
    for k in range(1,a-i+1,+1):
        print(end=" ")
    for j in range(1,i):
        print("*",end=" ")
    print(end="\n") 
