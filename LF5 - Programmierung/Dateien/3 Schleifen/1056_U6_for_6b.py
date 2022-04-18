#6b.a
j=1

for i in range(6):
    print("X"*j)
    j+=1


#6b.b
n=" "
for i in range(6):
    print(n+"X")
    n = " " + n


#6b.c
for y in range(6,0,-1):
    x = " "*(y-1) +"X"
    print(x)


#6b.d
#nur mit 6 als zahl
i=6
for y in range(i):
    if(y<i/2):
        print(" "*y + "X" +" "*(i-y*2-2)+"X"+" "*y )
    elif (y>=i/2):
        print(" "*(i-y-1)+"X"+" "*(y*2-i)+"X"+" "*(i-y-1))


#6b.d
#nur mit variabler zahl
i=11
for y in range(i):
    if(i%2==1): 
        if(y<i//2):
            print(" "*y + "X" +" "*(i-y*2-2)+"X"+" "*y )
        elif (y==i//2):
            print(" "*y+"X"+" ")
        elif (y>i/2):
            print(" "*(i-y-1)+"X"+" "*(y*2-i)+"X"+" "*(i-y-1))
    
    else:
        if(y<i/2):
            print(" "*y + "X" +" "*(i-y*2-2)+"X"+" "*y )
        elif (y>=i/2):
            print(" "*(i-y-1)+"X"+" "*(y*2-i)+"X"+" "*(i-y-1))
    