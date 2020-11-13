cp=int(input("enter a cost price"))
sp=int(input("enter a selling price"))
if cp>sp:
    profit=sp-cp
    pp=cp-sp*100
    print("profi=",profit)
    print("profit%=",pp)
elif sp<cp:
    los=cp-sp
    ip=cp-sp/cp*100
    print("loss=",los)
    print("loss%=",lp)
else:
    print("no profit no loss")
# cp=int(input("enter a cost price"))
# sp=int(input("enter a selling price"))
# if cp>sp:
#     profit=sp-cp
#     temp=cp-sp*100
#     print("profit=",profit)
#     print("profit%=",temp)
# elif sp<cp:
#     loss=cp-sp
#     lp=sp-cp/cp*100
#     print("loss=",loss)
#     print("loss%=",lp)
# else:
#     print("no profit no loss")
# cp=int(input("enter a cost price"))
# sp=int(input("enter a selling price"))
# if cp>sp:
#     profit=sp-cp
#     pp=cp-sp*100
#     print("profit=",profit)
#     print("profit%=",pp)
# elif sp<cp:
#     loss=cp-sp
#     lp=sp-cp/cp*100
#     print("loss=",loss)
#     print("loss%=",lp)
# else:
#     print("no profit no loss")
