"""
Question 2.

* * * * *  * * * * *
* * * *      * * * *
* * *          * * *
* *              * *
*                  *
*                  *
* *              * *
* * *          * * *
* * * *      * * * *
* * * * *  * * * * *

"""
for i in range(1,6):
    for j in range(6,i,-1):
        print("*",end=" ")
    for k in range(1,(4*i)-2,+1):
        print(" ",end="")
    for l in range(6,i,-1):
        print("*",end=" ")
    print(end="\n")

for i in range(5,0,-1):
    for j in range(6,i,-1):
        print("*",end=" ")
    for k in range((4*i)-2,1,-1):
        print(" ",end="")
    for l in range(6,i,-1):
        print("*",end=" ")
    print(end="\n")
