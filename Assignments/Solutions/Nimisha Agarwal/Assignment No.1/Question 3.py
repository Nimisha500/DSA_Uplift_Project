"""
Question3.
1
2 3
4 5 6
7 8 9 10

"""

a=1
for i in range(4):
    for j in range(0,i+1):
        print(a,end=" ")
        a=a+1
    print(end="\n")
