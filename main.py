year = int(input('Input year:'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):#ebuchi visokosny god, vse chto nize 100 ne dolzno bit kratnim 100 po etomy ispol'zuem 100 != 0
    print(year, 'is leap')
else:
    print(year, 'is not leap')