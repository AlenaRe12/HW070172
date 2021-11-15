Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Chapter 3

=============== RESTART: C:/Users/rehde/Desktop/python/change.py ===============
Change Counter

Please enter the count of each coin type.
Quarters: 6
Dimes: 7
Nickels: 12
Pennies: 3

The total value of your change is 2.83
type(3)
<class 'int'>
type(3.12)
<class 'float'>

= RESTART: C:/Users/rehde/AppData/Local/Programs/Python/Python310/quadratic.py =
This program finds the real solutions to a quadratic

Please enter the coefficients (a, b, c): 
Traceback (most recent call last):
  File "C:/Users/rehde/AppData/Local/Programs/Python/Python310/quadratic.py", line 19, in <module>
    main()
  File "C:/Users/rehde/AppData/Local/Programs/Python/Python310/quadratic.py", line 10, in main
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
  File "<string>", line 0
    
SyntaxError: unexpected EOF while parsing
main()
This program finds the real solutions to a quadratic

Please enter the coefficients (a, b, c): (3, 4, -2)

The solutions are: 0.38742588672279316 -1.7207592200561266
main()
This program finds the real solutions to a quadratic

Please enter the coefficients (a, b, c): (1, 2, 3)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    main()
  File "C:/Users/rehde/AppData/Local/Programs/Python/Python310/quadratic.py", line 12, in main
    discRoot = math.sqrt(b * b - 4 * a * c)
ValueError: math domain error
#Homework Chapter 3

=== RESTART: C:/Users/rehde/AppData/Local/Programs/Python/Python310/sphere.py ==
Given radius, this program will calculate the volume and
 surface area of a sphere
Input a value for the radius: 5
A sphere with radius 5 has volume 523.599 and surface area 314.159 .

================ RESTART: C:/Users/rehde/Desktop/python/pizza.py ===============
Please enter the cost of the Pizza, and how big it was: 12, 20
The price per square inch is 0.04
# Exercise 3

============== RESTART: C:/Users/rehde/Desktop/python/molecular.py =============
Enter the number of Hydrogen, Carbon, and Oxygen atoms separated by commas: 2, 4, 7
The molecular weight of the hydrocarbon is 162.0556 g/mol

================ RESTART: C:/Users/rehde/Desktop/python/flash.py ===============
How long was the time elapsed between flash and the sound of thunder? 2
Lightning struck 0.4166666666666667 miles away.
# Exercise 4
main()
How long was the time elapsed between flash and the sound of thunder? 2
Lightning struck 0.4166666666666667 miles away.
# Exercise 5

=============== RESTART: C:/Users/rehde/Desktop/python/coffee.py ===============
How many pounds of coffee is in the order? 12
Your order will cost a total of $ 137.82
# Exercise 6

================ RESTART: C:/Users/rehde/Desktop/python/slope.py ===============
Enter the first point values of x,y: 13, 25
Enter the second point values of x,y: 66. 87
Traceback (most recent call last):
  File "C:/Users/rehde/Desktop/python/slope.py", line 6, in <module>
    main()
  File "C:/Users/rehde/Desktop/python/slope.py", line 3, in main
    x2, y2 = eval(input("Enter the second point values of x,y: "))
  File "<string>", line 1
    66. 87
    ^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
main()
Enter the first point values of x,y: 13, 25
Enter the second point values of x,y: 66, 87
The slope of the line is 1.169811320754717
# Exercise 7

============== RESTART: C:/Users/rehde/Desktop/python/distance.py ==============
Enter the first point values of x,y: 22, 2349
Enter the second point values of x,y: 798, 3555
The distance between these two points is 1434.0892580310335
# Exercise 8

============== RESTART: C:/Users/rehde/Desktop/python/Georgian.py ==============
Input the 4 digit year 2021
the Gregorian Epact value is 16
# Chapter 5

============= RESTART: C:/Users/rehde/Desktop/python/dateconvert.py ============
Enter a date (mm/dd/yyy): 
============= RESTART: C:/Users/rehde/Desktop/python/dateconvert.py ============
Enter a date (mm/dd/yyyy): 10/12/2021
The converted date is: October 12, 2021
# Exercise 1

================ RESTART: C:/Users/rehde/Desktop/python/date2.py ===============
Enter a day, month, and year in numbers: 01, 02, 1998
Traceback (most recent call last):
  File "C:/Users/rehde/Desktop/python/date2.py", line 13, in <module>
    main()
  File "C:/Users/rehde/Desktop/python/date2.py", line 3, in main
    day, month, year = eval(input("Enter a day, month, and year in numbers: "))
  File "<string>", line 1
    01, 02, 1998
    ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
main()
Enter a day, month, and year in numbers: 10032021
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    main()
  File "C:/Users/rehde/Desktop/python/date2.py", line 3, in main
    day, month, year = eval(input("Enter a day, month, and year in numbers: "))
TypeError: cannot unpack non-iterable int object
main()
Enter a day, month, and year in numbers: 10/12/2021
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    main()
  File "C:/Users/rehde/Desktop/python/date2.py", line 3, in main
    day, month, year = eval(input("Enter a day, month, and year in numbers: "))
TypeError: cannot unpack non-iterable float object
main()
Enter a day, month, and year in numbers: 10.02.2012
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    main()
  File "C:/Users/rehde/Desktop/python/date2.py", line 3, in main
    day, month, year = eval(input("Enter a day, month, and year in numbers: "))
  File "<string>", line 1
    10.02.2012
    ^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
# Exercise 2

================ RESTART: C:/Users/rehde/Desktop/python/grade.py ===============
Enter a grade with no separation. 3
C

=============== RESTART: C:/Users/rehde/Desktop/python/grade2.py ===============
Enter a number grade: 3
F
Enter a number grade: 4
F
Enter a number grade: 2
F
Enter a number grade: 34
F
Enter a number grade: 55
F
Enter a number grade: 80
B
Enter a number grade: 90
A
Enter a number grade: 100
A
Enter a number grade: 99
A
Enter a number grade: 34
F
#Exercise 3
main()
Enter a number grade: 23
F
Enter a number grade: 44
F
Enter a number grade: 55
F
Enter a number grade: 66
D
Enter a number grade: 77
C
Enter a number grade: 88
B
Enter a number grade: 99
A
Enter a number grade: 100
A
Enter a number grade: 79
C
Enter a number grade: 65
D
# Exercise 4

=============== RESTART: C:/Users/rehde/Desktop/python/acronym.py ==============
This program creates acronyms from user input.
What would you like acronymized? 
random
R
# Exercise 5

================ RESTART: C:/Users/rehde/Desktop/python/name.py ================
What is your name? 
Alena
The numeric value of your name is 33.
# Exercise 6

============== RESTART: C:/Users/rehde/Desktop/python/fullname.py ==============
What is your name? 
Alena Maria Julia Rehder
The numeric value of your name is 186.
# Exercise 7

=============== RESTART: C:/Users/rehde/Desktop/python/caesar.py ===============
Enter the message you'd like encrypted.
End of the homework
What's the key? : 3
Your encoded message is Hqg#ri#wkh#krphzrun.
