#Taras Shevchenko*1814-03-09*1861-03-10
inc_data = str(input("Введить данні:"))
temp_data = inc_data.split('*')
dob = temp_data[1]
dod = temp_data[2]
print("Name:", temp_data[0])
print("Age:", int(dod[0:4]) - int(dob[0:4]),  "years")

