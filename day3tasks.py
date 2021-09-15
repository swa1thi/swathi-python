#1)find out numbers which are divisible with 3 and 9 in a given range
n=int(input("enter ending value:"))
print("numbers divisible with 3 and 9")
for x in range(1,n):
  if((x%3==0)and(x%9==0)):
       print(x,end=" ")


output:
C:/Users/swathi/Desktop/day3task.py
enter ending value:50
numbers divisible with 3 and 9
9 18 27 36 45

#2)implement a logic to find a given year is leap or not
year=int(input("enter a year"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("given year is leap year")
       else:
             print("given year is not leap year")
   else:
         print("given year is leap year")
else:
     print("given year is not leap year")


output:
C:/Users/swathi/Desktop/day3task.py
enter a year1800
given year is not leap year

enter a year1988
given year is leap year


#3)print numbers in reverse order
for x in range(10,0,-1):
    print(x)

output:
C:/Users/swathi/Desktop/day3task.py
10
9
8
7
6
5
4
3
2
1
  

