import datetime
now=datetime.datetime.now()
month=now.month
if 3<=month<=5:
    print("spring")
elif 6<=month<=8:
    print("summer")
elif 9<=month<=11:
    print("fall")
else :
    print("winter")
