#1)write a program to find the largest number in the list
def large():
    big=max(list1)
    print("largest number in the list:",big)

list1=[12,85,90,105,8,92]
large()

output:
C:/Users/swathi/Desktop/day8-tasks.py
largest number in the list: 105



#2)write a program to find the second largest number in a list

def secondlargest():
            list1.sort()
            print("second largest number:",list1[-2])

list1=[100,200,400,300,500]
secondlargest()


output:
C:/Users/swathi/Desktop/day8-tasks.py
second largest number: 400


#3)write a program to put even and odd elements in  a list into two different lists
li=[1,2,3,4,5,6,7,8,9,10]
eli=[]
oli=[]
for i in li:
    if i%2==0:
        eli.append(i)
    else:
        oli.append(i)
print("even elements in the list:",eli)
print("odd elements in the list:",oli)



output:
C:/Users/swathi/Desktop/day8-tasks.py
even elements in the list: [2, 4, 6, 8, 10]
odd elements in the list: [1, 3, 5, 7, 9]


#4)write a program to remove the duplicates items from a list
li=[1,2,4,5,6,8,2,2,3,4,9,10]
print(" before removing the duplicates:",li)
print("after removing duplicates:",list(set(li)))


output:
C:/Users/swathi/Desktop/day8-tasks.py
before removing the duplicates: [1, 2, 4, 5, 6, 8, 2, 2, 3, 4, 9, 10]
after removing duplicates: [1, 2, 3, 4, 5, 6, 8, 9, 10]



#5)write a program to read a list of words and return the length of longest one

def longest(a):
    length= len(a[0])
    temp=a[0]
    for i in a:
        if(len(i) > length):
                length=len(i)
                temp = i
 
    print("The word with the longest length is:",temp)
 
 
a=['abdul','mohammed','rassol','lokesh','ganesh']
longest(a)


output:
C:/Users/swathi/Desktop/day8-tasks.py
The word with the longest length is: mohammed


#7)write a program to find all numbers in a range which are perfect squares and sum of all digits in the numbers is less than 10


num=int(input("enter starting number:"))
num1=int(input("enter last number:"))
print("perfect squraes:")
while num<=num1:
    for i in range(1,num):
        if i*i==num:
            print(num)
    num=num+1

output:
C:/Users/swathi/Desktop/day8-tasks.py
enter a value:1
enter a value:10
1 4 9 

