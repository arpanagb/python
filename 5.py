def fact(n):
    f=1
    if n<0:
        print("Factorial cannot be computed!")
    elif n==0:
        print("Factorial of",n,"is 1")
    else:
        for i in range (1,n+1):
            f=f * i
        print ("Factorial of",n," is", f)
fact(9)