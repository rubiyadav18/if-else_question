unit=int(input("enter a unit bil"))
if unit>=50 and unit <100:
    print(0.50*unit+0.2)
if unit>=100 and unit<=200:
    print(0.75*unit+0.2)
if unit>=100 and unit<=200:
    print(1.20*unit+0.2)
elif unit==250:
    print(1.50*250+0.2)
elif unit<=40:
    print(1*unit)
else:
    print("no charges")


