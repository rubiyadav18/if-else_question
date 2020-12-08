print("welcome")
print("state bank of india")
print("insert your card")
language=input("enter a language")
if language==1:
    pass
pin=int(input("enter a 4 digit pin"))
if pin==1234:
   pass
transaction=int(input("enter a transaction"))
if transaction==1:
       pass
select=int(input("please choose your account type press\n,"))
if select==1:
       pass
amount=int(input("enter a amount"))
if amount<=20000:
       print("please wait your transaction is being process")
else:
       print("you dont have safficeant balance please try later")
if transaction==2:
    pass
deposite=int(input("enter how much amount you want to deposite"))
if deposite<=20000:
        print("your transaction is being process")
else:
        print("you amount is more than deposite limit")
if transaction==3:
    print(balance+money,"its your total balance in your account")
else:
    print("thank you visiting you card")