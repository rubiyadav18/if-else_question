# name=input("enter a paasword")
# if len(name)>=6 or len(name)<=16:
#     if name>="A" or name<="Z":
#         if name>="@" or name<="#":
#             print("stron password")
#     else:
#          print("week password")
name=input("enter a password")
if len(name)>=6 or len(name)<=16:
    if "A" in name or "Z" in name:
        if "#" in name and "@" in name:
            print("strog password")
    else:
            print("week paasword")
# if "6" in name or "16" in name:
#     if "A" in name or "Z" in name:
#         if "#" in name or "@" in name:
#             print("strong pasword")
#     else:
#             print("week paasword")
name=int(input("enter a paasword"))
if "6" in name or "16" in name:
    if "A" in name or "Z" in name:
        if "#" in name or "$" in name:
            print("strong paasword")
    else:
        print("week paasword")
    