#1)find evens in between range along with count and sum
start=int(input("enter starting value:"))
end=int(input("enter ending value:"))
def even(num):
        if num%2==0:
            return True
        else:
            return False

count=sum=0
for i in range(start,end+1):
      if even(i):
         print(i,end=" ")
         count+=1
         sum+=i
print("count of even numbers:",count)
print("sum of even numbers:",sum)

output:
C:/Users/swathi/Desktop/day3task.py
enter starting value:15
enter ending value:30
16 18 20 22 24 26 28 30
count of even numbers: 8
sum of even numbers: 184


#2)find a given number is prime or not
n=int(input("enter a value:"))
def prime(a):
    for num in range(2,a):
        if (a%num)==0:
           return False
        return True

#if it is prime it's returns true otherwise it's returns false       
print(prime(n))


output:
C:/Users/swathi/Desktop/day3task.py
enter a value:5
True


#3)print primes in given range then print count
ran=int(input("enter value:"))
def isPrime(a):
   for i in range(2,a):
     if (a%i)==0:
        return False
   return True
print("prime numbers:")

count=0
for j in range(2,ran):
    if j>1:
      if isPrime(j):
        print(j,end=" ")
        count+=1
print("count of numbers:",count)


output:
C:/Users/swathi/Desktop/day3task.py
enter value:19
prime numbers:
2 3 5 7 11 13 17
count of numbers: 7


#4)print primes in between range with count
start=int(input("enter a starting value:"))
end=int(input("enter a ending value:"))
def prime(a):
    for num in range(2,a):
        if (a%num)==0:
            return False
    return True

count=0
print("prime numbers is:")
for i in range(start,end):
    if i>1:
       if prime(i):
          print(i,end="\n")
          count+=1
print("count of numbers:",count)


output:
C:/Users/swathi/Desktop/day3task.py
enter a starting value:10
enter a ending value:50
prime numbers is:
11
13
17
19
23
29
31
37
41
43
47
count of numbers: 11




#5)write a function to print the 5 multiples of given range
def multiples():
    for i in range(1,n+1):
       if i%5==0:
          print(i)
       
    
n=int(input("enter a range"))
multiples()


output:
C:/Users/swathi/Desktop/day4task.py
enter a range 25
5
10
15
20
25


