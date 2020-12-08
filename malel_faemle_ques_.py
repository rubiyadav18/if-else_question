sex=input("enter a sex")
age=int(input("enter a age"))
if sex=="female":
    print("she work only urban areas")
if sex=="male":
    if age>=20 and age<=40:
        print("he work anywhere")
if sex=="male":
    if age>=40 and age<=60:
        print("he work only urban areas")
else:
    print("nothing")