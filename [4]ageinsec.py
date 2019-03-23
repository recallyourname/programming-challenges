ageYears = int(input())
lY = ageYears // 4
cY = ageYears - lY
#cY stands for common years and lY for leap years
ageSecs = (lY*366 + cY*365)*24*60*60
print(ageSecs)