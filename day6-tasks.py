#1>Python Program to Replace all Occurrences of ‘a’ with $ in a String
name=input("Enter Name:")
print(name)
name=name.replace("a","$")
print(name)

output:
PS C:\Users\swathi\Desktop> python day6-tasks.py
Enter Name:swathi
swathi
sw$thi

#2>Python Program to Detect if Two Strings are Anagrams

s1=input("enter String1:")
s2=input("enter string2:")
status=0
if len(s1)==len(s2):
    for ch in s1:
        if ch in s2:
            status+=1
            continue

        else:
          print("its not a anagram")
else:
    print("its not a anagram")


if status==len(s1):
    print("its is a anagram")

output:
PS C:\Users\swathi\Desktop> python day6-tasks.py
enter String1:listen
enter string2:silent
its is a anagram

#3)Python Program to Form a New String where the First Character and the Last Character have been Exchanged

string=input("enter a string")
pos=string[0]
end=string[-1]
sub=string[1:6]
r=end+sub+pos
print(r)

output:
enter a string :conzura
aonzurc


#4>Python Program to Count the Number of Vowels in a String

x=input("enter a string")
count=0
y=x.lower()
for ch in y:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count+=1
print(count)

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter a string:mounika
4

#5>Python Program to Take in a String and Replace Every Blank Space with Hyphen
n=input("enter a string")
print("before replacing:",n)
n1=n.replace(" ","-")
print("after replacing:",n1)

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter a stringswa thi
before replacing: swa thi
after replacing: swa-thi


#6>Python Program to Calculate the Length of a String Without Using a Library Function
n=input("enter a string:")
count=0
for i in n:
    count+=1
print("length of string:",count)


output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter a string:vizag institute of technology
length of string: 29


#7> Python Program to Calculate the Number of Words and the Number of Characters Present in a String
sen=input("enter the string")
sen1=sen.split()
count=0
wcount=0
for i in sen:
    count+=1
for j in sen1:
    wcount+=1
print("no of characters in a string:",count)
print("no of words in a string:",wcount)

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter the string"hi this is swathi"
no of characters in a string: 19
no of words in a string: 4





#8>Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

s1=input("enter a string1:")
s2=input("enter a string2:")

count1=0
count2=0
for i in s1:
    count1+=1
for j in s2:
    count2+=1

if(count1>count2):
    print("string1 is bigger", count1)
else:
    print("string2 is bigger", count2)

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter a string1:"pratice"
enter a string2:"learning"
string2 is bigger 10


#9>Python Program to Count Number of Lowercase Characters in a String
string=input("enter a string:")
count=0
for i in string:
    if i.islower()==True:
        count+=1
print("no of lower case characters:",count)

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter a string:hi this is swathi
no of lower case characters: 14



#10>Python Program to Check if a String is a Palindrome or Not

x=input("enter a string")
y=x[::-1]
if (x==y):
    print(x,"is a palindrome")
else:
    print(x,"is not a palindrome")

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter a string:sms
sms is  a palindrome

#11>Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String

string=input("enter a string:")
lcount=0
rcount=0
for i in string:
    if i.islower()==True:
        lcount+=1
for j in string:
    if j.isupper()==True:
        rcount+=1
print("no of lower case letters:",lcount)
print("no of upper case letters:",rcount)

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter a string:SwaThi
no of lower case letters: 4
no of upper case letters: 2

#12>Python Program to Calculate the Number of Digits and Letters in a String


s=input("enter a string:")
dcount=0
lcount=0
for ch in s:
    if ch.isdigit():
        dcount+=1
    elif ch.isalpha():
        lcount+=1
    else:
        pass
print("digits count is:",dcount)
print("chars count is:",lcount)

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py

enter a string:abc123
digits count is: 3
chars count is: 3


#13>Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String
x=input("enter a string")
y=x[0:2]
z=x[-2:]
print(y+z)

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter a string:swathi
swhi


#14>Python Program to Count the Occurrences of Each Word in a Given String Sentence
x="this is swathi is"
z=x.split()
a=[]
for i in z:
    if (i not in a):
        a.append(i)
for i in range(0,len(a)):
    print("occurences of",a[i],"is:",z.count(a[i]))

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
occurences of this is: 1
occurences of is is: 2
occurences of swathi is: 1


#15>Python Program to Check if a Substring is Present in a Given String
x=input("enter a substring")
z="hi hello"
if(x in z):
    print(x,"is a substring")
else:
    print(x,"not a substring")

output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter a substring hy
hy not a substring

#16>python program to print sum of digits in given string
x=input("enter a value:")
sum=0
for ch in x:
    if ch.isdigit():
        sum+=int(ch)
print(sum)


output:
pS C:\Users\swathi\Desktop> python day6-tasks.py
enter a value:swathi234
9
