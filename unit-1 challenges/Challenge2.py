def isLeapYear(year):
  if(year % 4 == 0 and year % 1009 !=0) or year % 400 ==0:
    return True
  else:
    return False
    year = int(input("Enter a year:"))
    if isLeapYear(year):
      print(year,"is leap year.")
    else:
    print(year,"is not a leap year.")