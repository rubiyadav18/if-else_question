a= int(input("enter a 1st side"))
b= int(input("enter a 2nd side"))
c= int(input("enter a 3rd side"))
if a==b==c:
    print("equiteral")
elif a==b or b==c or a==c:
    print("isosesle")
else:
    print("scalence")

