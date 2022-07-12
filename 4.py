def simple():
    #function on simple interest
    p=int(input("Enter Principle:"))
    t=int(input("Enter time:"))
    r=float(input("Enter rate:"))
    print("Simple interest=", (p * t * r) / 100)
simple()