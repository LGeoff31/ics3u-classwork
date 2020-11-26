10 QUESTIONS ON CODINGBAT

Greeting

name = input('Please enter your name: ')
print(f"Hello {name}")

Make abba

a = input("Please enter somethingL ")
b = input("Please enter something: ")
print(a + b + b + a)

Print last two letters

word = input("Please enter a word: ")
last_2_letters = word[len(word) -2:]
print(last_2_letters + last_2_letters + last_2_letters)

Print first two letters

word = input("Please enter a word: ")
first_2_letters = word[:2]
print(first_2_letters + first_2_letters + first_2_letters)

Print middle letters

word = input("Please enter a word: ")
middle_letters = word[1:len(word)-1]
print(middle_letters)

Combo string

a = input("Please enter something: ")
b = input("Please enter something: ")
if len(a)>len(b):
    print(b + a + b)
else:
    print(a + b + a)

non start

a = input("Please enter something: ")
b = input("Please enter something: ")
print(a[1:] + b[1:])

first half

word = input("Please enter something: ")
first_half = word[:int(len(word)/2)]
print(first_half)

Ends in ly

word = input('Please enter a word: ')
if word[len(word)-2:] == 'ly':
    print('true')
else:
    print('false')

at_first

word = input("Please enter a word: ")
first_2_letters = word[:2]
if len(word)>1:
    print(first_2_letters)
else:
    print(word + '@')




WORKBOOK 10 QUESTIONS if questions 34-44 !!!!


34 Even or odd?

integer = int(input('Please enter a integer: '))
if integer % 2 == 0:
    print('It is even!')
else:
    print('It is odd!')

35 Dog years

human_years = int(input('Please enter human years: '))
if human_years == 1:
    print('10.5')
elif human_years == 2:
    print('21')
else:
    print(21 + (human_years-2) * 4)

36 Vowel or consonant

letter = input('Please enter a letter: ')
if letter in ['a', 'e', 'i', 'o', 'u']:
    print('The letter is a vowel!')
elif letter == 'y':
    print('y is sometimes a vowel and sometimes a consonant')
else:
    print('The letter is a consonant!')

37 Name that shape

sides = int(input('Please enter the amount of sides: '))
if sides == 3:
    print('Wow, thats a triangle!')
elif sides == 4:
    print('That can a square, rectangle, rhombus, kite or pallaogram!')
elif sides == 5:
    print('Thats a pentagon! Fantastic!')
elif sides == 6:
    print('Hexagon, my favorite!')
elif sides == 7:
    print('Thats a heptagon, very unknown in this world')
elif sides == 8:
    print('Thats a octogon, think of it as a octupus!')
elif sides == 9:
    print('Nonagon, bit unusal')
elif sides == 10:
    print('Decagon, sounds like a monster!')
else:
    print('Shape is wayyy to large or an unexsisting shape')

38 Month name to number of days

month = input('Please enter the month: ').lower()
if month == 'january':
    print('31!')
elif month == 'february':
    print('That can be 28 or 29 depending on the year')
elif month == 'march':
    print('31!')
elif month == 'april':
    print('30!')
elif month == 'may':
    print('31!')
elif month == 'june':
    print('30!')
elif month == 'july':
    print('31!')
elif month == 'august':
    print('31!')
elif month == 'september':
    print('30!')
elif month == 'october':
    print('31!')
elif month == 'november':
    print('30!')
elif month == 'december':
    print('31!')
else: 
    print('That is not a month sir/maam')


39 Sound levels

db = int(input('Please enter the decibel level of the noise: '))
if db == 130:
    print('Jackhammer')
elif db == 106:
    print('Gas lawnmower')
elif db == 70:
    print('Alarm clock')
elif db == 40:
    print('Quiet room')
elif 40 < db < 70:
    print('Your noise is between a queit room and an alarm clock!')
elif 70 < db < 106:
    print('Your noise is between a alarm clock and a gas lawnmower!')
elif 106 < db < 130:
    print('Your noise is between a gas lawnmower and a jackhammer!')
elif db < 40:
    print('The noise is almost unhearable!')
else:
    print("THATS SO LOUD, YOU'RE DISTURBING YOUR NEIGHBOARDS, TURN IT DOWN!")

40 Name that triangle

triangle_side_1 = float(input('Please enter the triangles first side lenth in cm: '))
triangle_side_2 = float(input('Please enter the triangles secound side lenth in cm: '))
triangle_side_3 = float(input('Please enter the triangles third side lenth in cm: '))

if triangle_side_1 == triangle_side_2 and triangle_side_2 != triangle_side_3 or triangle_side_2 == triangle_side_3 and triangle_side_3 != triangle_side_1 or triangle_side_3 == triangle_side_1 and triangle_side_1 != triangle_side_2:
    print('The traignle is isoscles!')
elif triangle_side_1 == triangle_side_2 == triangle_side_3:
    print('It is a equalateral!')
else: 
    print('It is a scalene!')

41 Note to frequency

note = input('Please enter your note: ')
if note == 'C4':
    print("The note's frequency is 261.63!")
elif note == 'D4':
    print("The note's frequency is 293.66!")
elif note == 'E4':
    print("The note's frequency is 329.63!")
elif note == 'F4':
    print("The note's frequency is 349.23!")
elif note == 'G4':
    print("The note's frequency is 392.00!")
elif note == 'A4':
    print("The note's frequency is 440.00!")
elif note == 'B4':
    print("The note's frequency is 493.88!")


43 Faces on money

money_value = int(input('Please enter the value of the banknote in $: '))
if money_value == 1:
    print('George Washinton is on that coin!')
elif money_value == 2:
    print('Thomas Jefferson is on that coin!')
elif money_value == 5:
    print('Abraham Lincoin is on that bill!')
elif money_value == 10:
    print('Alexander Hamilton is on that bill!')
elif money_value == 20:
    print('Andrew jackson is on that bill!')
elif money_value == 50:
    print('Ulysses S. Grant is on that bill!')
elif money_value == 100:
    print('Benjamin Franklin is on that bill!')
else: 
    print('No such note exists, where do you live?')

44 Date to the holiday name

month = input('Please enter the month: ').lower()
day = int(input('Please enter the day: '))
if month == 'january' and day == 1:
    print("Thats New Year's Day!")
elif month == 'july' and day == 1:
    print("Thats Canada's Day!")
elif month == 'december' and day == 25:
    print("That's Chrismas day!")
else:
    print('The date does not correspond to a fixed-date holiday')

