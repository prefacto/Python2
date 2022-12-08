distancetravelled=float(input("Enter distance covered=",))
totalfare=0
if distancetravelled>0 and distancetravelled<50:
    totalfare=distancetravelled*2
else:
        totalfare=49*2
distancetravelled=distancetravelled-49
if distancetravelled>0 and distancetravelled<50:
    totalfare=totalfare+distancetravelled*4
else:
        totalfare=totalfare+(distancetravelled*4)
if distancetravelled>0 and distancetravelled<50:
    totalfare=totalfare+((distancetravelled-50))*4
    distancetravelled=distancetravelled-50
    totalfare=totalfare+(distancetravelled*5)

print("You should pay",totalfare,"Rs.")
