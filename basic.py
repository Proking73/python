numDays = int(input("Enter the number of days: "));
#print(numDays, "days");
days_to_sec = numDays*60*60*24;
if numDays==1:
  print(numDays,"day is equal to",days_to_sec,"seconds");
else:
  print(numDays,"days are equal to",days_to_sec,"seconds");