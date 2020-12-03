#Adding three numbers

def add(a:int, b:int, c:int) -> int:
    return a+b+c

result = add(3,5,8)
print(result)

#Name and age

def person(name:str, age:int):
    return str(name) + ', ' + str(age)
    

string = person('Geoffrey', 4)
print(f"This next person is {string} is his age?")

#Average of 2 numbers

def average(a:int, b:int) -> int:
    return (a + b)/2

result = average(5,7)
print(result)

#Largest of 3 numbers

def largest(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

result = largest(3,11,9)
print(result)

def two_letters(word:str) -> str:
    return word[:2]

result = two_letters('Hippo')
print(result)
