
#DICTIONARIES
===================
>>> d1={"name":"abdul","age":26.3,"branch":"cse"}
>>> d1
{'name': 'abdul', 'age': 26.3, 'branch': 'cse'}
>>> d1["age"]
26.3
>>> d1["name"]
'abdul'
>>> d1.get("branch")
'cse'
>>> d1["rollno"]=123
>>> d1
{'name': 'abdul', 'age': 26.3, 'branch': 'cse', 'rollno': 123}
>>> d1["rollno"]=27
>>> d1
{'name': 'abdul', 'age': 26.3, 'branch': 'cse', 'rollno': 27}
>>> dir(d1)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d1.keys()
dict_keys(['name', 'age', 'branch', 'rollno'])
>>> d1.values()
dict_values(['abdul', 26.3, 'cse', 27])
>>> d1.items()
dict_items([('name', 'abdul'), ('age', 26.3), ('branch', 'cse'), ('rollno', 27)])
>>> d1.pop("age")
26.3
>>> d1
{'name': 'abdul', 'branch': 'cse', 'rollno': 27}
>>> d1.popitem()
('rollno', 27)
>>> d1.update({"phno":"9493456789"})
>>> d1
{'name': 'abdul', 'branch': 'cse', 'phno': '9493456789'}
marks={}.fromkeys(["c","cpp","python","java"],35)
>>> marks
{'c': 35, 'cpp': 35, 'python': 35, 'java': 35}
>>> marks["python"]=80
>>> marks
{'c': 35, 'cpp': 35, 'python': 80, 'java': 35}
>>> d1.setdefault("email":"123@")
SyntaxError: invalid syntax
>>> d1.setdefault("email","123@")
'123@'
>>> d1
{'name': 'abdul', 'branch': 'ece', 'phno': '9493456789', 'email': '123@'}

#Tasks
#1)write a program to add a key-value pair to the dicitionary

details={}
n=int(input("enter range"))
for i in range(n):
    k=input("enter the key")
    v=input("enter the value")

    details[k]=v
print(details)

output:
C:/Users/swathi/Desktop/day11tasks.py
enter range4
enter the keyname
enter the valueswathi
enter the keyage
enter the value21
enter the keybranch
enter the valuecse
enter the keyid
enter the value519
{'name': 'swathi', 'age': '21', 'branch': 'cse', 'id': '519'}


#2)write a program to concatenate two dictionaries into one
x={"name":"swathi","age":21,"branch":"cse"}
y={"rollno":"519","result":"pass"}
x.update(y)
print(x)

output:
C:/Users/swathi/Desktop/day11tasks.py
{'name': 'swathi', 'age': 21, 'branch': 'cse', 'rollno': '519', 'result': 'pass'}


#3)write a program to check if a given key exists in a dictionary or not
dict1={}
n=int(input("enter range value"))

for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    dict1.update({key:value})

gkey=input("enter key to check:")
if gkey in dict1:
     print("key exits")
else:
    print("key does not exists")

print(dict1)


output:
C:/Users/swathi/Desktop/day11tasks.py
enter range value4
enter key:lang
enter value:java
enter key:idle
enter value:ecllipse
enter key:platform
enter value:independent
enter key:oops
enter value:yes
enter key to check:platform
key exits
{'lang': 'java', 'idle': 'ecllipse', 'platform': 'independent', 'oops': 'yes'}

#4)write a program to generate a dictionary that contains numbers (between 1 and n)in the form(x,x*x)
edict={}
n=int(input())
for i in range(1,n+1):
    edict.setdefault(i,i*i)
print(edict)


output:
C:/Users/swathi/Desktop/day11tasks.py
5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#5)write a program to sum all the items in  a dicitionary
dict1={}
n=int(input("enter range value"))

for i in range(n):
    key=input("enter key:")
    value=int(input("enter value:"))
    dict1[key]=value
print(dict1)
print(sum(dict1.values()))



output:
C:/Users/swathi/Desktop/day11tasks.py
enter range value4
enter key:physics
enter value:50
enter key:chemistry
enter value:45
enter key:maths
enter value:55
enter key:biology
enter value:60
{'physics': 50, 'chemistry': 45, 'maths': 55, 'biology': 60}
210


#6)write a program to multiply all the items in  a dicitionary
dict1={}
n=int(input("enter range value"))

for i in range(n):
    key=input("enter key:")
    value=int(input("enter value:"))
    dict1[key]=value
print(dict1)

def mul(a):
    for i in a:
        z=i*i
    print(z)   

mul(dict1.values())

output:
C:/Users/swathi/Desktop/day11tasks.py
enter range value3
enter key:emp1
enter value:1000
enter key:emp2
enter value:2000
enter key:emp3
enter value:3000
{'emp1': 1000, 'emp2': 2000, 'emp3': 3000}
9000000


#7)write a program to remove the given key from a dicitionary
dict1={"ename":"xyz","designation":"analyst","salary":"40,000","eid":"2304"}
key=input("enter key to remove:")
dict1.pop(key)
print(dict1)


output:
C:/Users/swathi/Desktop/day11tasks.py
enter key to remove:eid
{'ename': 'xyz', 'designation': 'analyst', 'salary': '40,000'}


#8)python program to map two lists into a dicitionary
list1=[5,6,7,8]
list2=[25,36,49,64]
z=dict(zip(list1,list2))
print(z)

output:
C:/Users/swathi/Desktop/day11tasks.py
{5: 25, 6: 36, 7: 49, 8: 64}



#9)python program to count the frequency of words appering in a string using dicitionary
words=input("enter a sentence:").split()
wordsCount={}
print(len(words))
for word in words:
    wordsCount[word]=words.count(word)
print(wordsCount)


output:
C:/Users/swathi/Desktop/day11tasks.py
enter a sentence:i am abdul and i am from kadapa and i am working in css
14
{'i': 3, 'am': 3, 'abdul': 1, 'and': 2, 'from': 1, 'kadapa': 1, 'working': 1, 'in': 1, 'css': 1}

#to reduce the iterations
words=input("enter a sentence").split()
wordsCount={}
uniqueword=list(set(words))
print(len(uniqueword))
for word in uniqueword:
    wordsCount[word]=words.count(word)
print(wordsCount)


output:
C:/Users/swathi/Desktop/day11tasks.py
enter a sentencei am abdul and i am from kadapa and i am working in css
9
{'from': 1, 'i': 3, 'abdul': 1, 'kadapa': 1, 'working': 1, 'in': 1, 'and': 2, 'css': 1, 'am': 3}




#10)python program to create a dictionary with key as first character and value as words starting with that characters

string=input("enter string:")
word=string.split()
dict1={}

for str in word:
    ch=str[0]
    if ch not in dict1:
        dict1[ch]=[]
        dict1[ch].append(str)
    else:
       dict1[ch].append(str)
print(dict1)

for k,v in dict1.items():
    print(k,":",v)


output:
C:/Users/swathi/Desktop/day11tasks.py
enter string:apple apricort produces fiber antioxidants vitamins
{'a': ['apple', 'apricort', 'antioxidants'], 'p': ['produces'], 'f': ['fiber'], 'v': ['vitamins']}
a : ['apple', 'apricort', 'antioxidants']
p : ['produces']
f : ['fiber']
v : ['vitamins']
