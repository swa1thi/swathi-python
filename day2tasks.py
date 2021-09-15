#1)you have to implement a logic to perform all arithmetic operations
a=int(input("enter a value:"))
b=int(input("enter b value:"))
s=a+b
print('addition:',s)
sb=a-b
print('subtraction:',sb)
mul=a*b
print('multiplication:',mul)
div=a/b
print('division:',div)
mod=a%b
print('module:',mod)
fdiv=a//b
print('floordivision:',fdiv)
exp=a**b
print('exponent:',exp)


output:
C:/Users/swathi/Desktop/day2tasks.py
enter a value:5
enter b value:3
addition: 8
subtraction: 2
multiplication: 15
division: 1.6666666666666667
module: 2
floordivision: 1
exponent: 125

#2)Biggest of two numbers
n1=int(input("enter n1 value"))
n2=int(input("enter n2 value"))
if(n1>n2):
    print(" n1 is biggest number")
else:
    print(" n2 is biggest number")


output:
C:/Users/swathi/Desktop/day2tasks.py
enter n1 value10
enter n2 value25
 n2 is biggest number


#3)Biggest of three numbers
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if (a>b)and(a>c):
    print( "a is biggest number")
elif (b>a)and(b>c):
    print("b is biggest number")
else:
    print("c is bigest number")


output:
C:/Users/swathi/Desktop/day2tasks.py
enter a value:5
enter b value:10
enter c value:4
b is biggest number


#4)write a program to generate numbers in given range
start=int(input("enter starting value:"))
end=int(input("enter ending value:"))
for i in range(start,end):
    print(i)


output:
C:/Users/swathi/Desktop/day2tasks.py
enter starting value:5
enter ending value:20
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19



#5)printing even and odd numbers
print("even numbers",end=" ")
for i in range(2,50,2):
       print(i,end=" ")
print("odd numbers",end="\n")
for j in range(1,50,2):
       print(j,end=" ")

output:
C:/Users/swathi/Desktop/day2tasks.py
even numbers 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48
odd numbers 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49


#6)printing 5th table
num=int(input("enter a value:"))
for i in range(1,21):
    print(num,'x',i,"=", num*i)


output:
C:/Users/swathi/Desktop/day2tasks.py
enter a value:5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
5 x 11 = 55
5 x 12 = 60
5 x 13 = 65
5 x 14 = 70
5 x 15 = 75
5 x 16 = 80
5 x 17 = 85
5 x 18 = 90
5 x 19 = 95
5 x 20 = 100

   
