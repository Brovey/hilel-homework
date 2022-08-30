#Taras Shevchenko*1814-03-09*1861-03-10
IncData = str(input("Введить данні:"))
TempData = IncData.split('*')
dob = TempData[1]
dod = TempData[2]
print("Name:", TempData[0])
print("Age:", int(dod[0:4]) - int(dob[0:4]),  "years")

