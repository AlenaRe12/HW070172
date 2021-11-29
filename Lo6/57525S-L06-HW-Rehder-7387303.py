Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Homework Lesson 6
Chapter 8
SyntaxError: invalid syntax. Perhaps you forgot a comma?
#Chapter 8
# Exercise 1

============== RESTART: C:\Users\rehde\Desktop\python\fibonacci.py =============
What number in the Fibonnaci sequence would you like to see?: 8
21
# Exercise 2

============== RESTART: C:\Users\rehde\Desktop\python\Windchill.py =============
        -20    -10      0     10     20     30     40     50

 0      0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0
 5    -34.0  -22.3  -10.5    1.2   13.0   24.7   36.5   48.2
10    -40.7  -28.3  -15.9   -3.5    8.9   21.2   33.6   46.0
15    -45.0  -32.2  -19.4   -6.6    6.2   19.0   31.8   44.6
20    -48.2  -35.1  -22.0   -8.9    4.2   17.4   30.5   43.6
25    -50.8  -37.5  -24.1  -10.7    2.6   16.0   29.4   42.8
30    -53.0  -39.4  -25.9  -12.3    1.3   14.9   28.5   42.0
35    -54.9  -41.2  -27.4  -13.6    0.1   13.9   27.7   41.4
40    -56.6  -42.7  -28.8  -14.8   -0.9   13.0   26.9   40.9
45    -58.1  -44.1  -30.0  -15.9   -1.8   12.2   26.3   40.4
50    -59.5  -45.3  -31.1  -16.9   -2.7   11.5   25.7   39.9
# Exercise 3

=== RESTART: C:\Users\rehde\AppData\Local\Programs\Python\Python310\years.py ===
What is the annualized interest rate? .1
What is the initial principal? 100
200.10123573304637
694
# Exercise 4

============== RESTART: C:\Users\rehde\Desktop\python\syracuse.py ==============
Input a natural number: 80
80
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
1.0
# Exercise 5

=== RESTART: C:\Users\rehde\AppData\Local\Programs\Python\Python310\prime2.py ==
Input a positive whole number: 9
The number is prime.
# Exercise 6

=============== RESTART: C:/Users/rehde/Desktop/python/prime3.py ===============
Input a positive whole number: 99
1
2
3
5
7
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
53
59
61
67
71
73
79
83
89
97
# Exercise 7

============== RESTART: C:/Users/rehde/Desktop/python/Goldbach.py ==============
Input a positive whole number: 80
79 + 1 = 80
73 + 7 = 80
67 + 13 = 80
61 + 19 = 80
43 + 37 = 80
37 + 43 = 80
19 + 61 = 80
13 + 67 = 80
7 + 73 = 80
1 + 79 = 80
# Exercise 8

================= RESTART: C:/Users/rehde/Desktop/python/gcd.py ================
Please enter 2 numbers, separated by a comma: 80, 55
The GCD is 5
# Chapter 11
# Exercise 1

=============== RESTART: C:/Users/rehde/Desktop/python/stats2.py ===============
Enter a series of numbers, separated by commas: 23, 44, 56, 79
This program is capable of calculating the mean(Avg), median,(Med)
and standard deviation(Std) of a set of values.
Type "Avg", "Med", "Std", or "AvgStd" (<Enter> to exit)>>>  Avg
50.5
Type "Avg", "Med", "Std", or "AvgStd" (<Enter> to exit)>>>  Med
50.0
Type "Avg", "Med", "Std", or "AvgStd" (<Enter> to exit)>>>  AvgStd
(50.5, 23.388031127053)
Type "Avg", "Med", "Std", or "AvgStd" (<Enter> to exit)>>>  
# Exercise 2

================= RESTART: C:/Users/rehde/Desktop/python/gpa.py ================
Enter the name of the grade file: A
Traceback (most recent call last):
  File "C:/Users/rehde/Desktop/python/gpa.py", line 51, in <module>
    main()
  File "C:/Users/rehde/Desktop/python/gpa.py", line 31, in main
    infile = open(filename, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'A'

================ RESTART: C:/Users/rehde/Desktop/python/gpa2.py ================
This program sorts student grade information by GPA, name, or credits.
Traceback (most recent call last):
  File "C:/Users/rehde/Desktop/python/gpa2.py", line 52, in <module>
    if __name__ == '__main__': main()
  File "C:/Users/rehde/Desktop/python/gpa2.py", line 28, in main
    data = readStudents(filename)
  File "C:/Users/rehde/Desktop/python/gpa2.py", line 10, in readStudents
    infile = open(filename, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'gpa1.txt'
main()
This program sorts student grade information by GPA, name, or credits.
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    main()
  File "C:/Users/rehde/Desktop/python/gpa2.py", line 28, in main
    data = readStudents(filename)
  File "C:/Users/rehde/Desktop/python/gpa2.py", line 10, in readStudents
    infile = open(filename, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'gpa1.txt'
main()
This program sorts student grade information by GPA, name, or credits.
Type "GPA", "name", or "credits" >>>  name
The data has been written to gpa_(name).py
GPA
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    GPA
NameError: name 'GPA' is not defined
main()
This program sorts student grade information by GPA, name, or credits.
Type "GPA", "name", or "credits" >>>  GPA
The data has been written to gpa_(GPA).py
main()
This program sorts student grade information by GPA, name, or credits.
Type "GPA", "name", or "credits" >>>  credits
The data has been written to gpa_(credits).py
# Exercise 3

================ RESTART: C:/Users/rehde/Desktop/python/gpa3.py ================
This program sorts student grade information by GPA, name, or credits.
Type "GPA", "name", or "credits" >>>  name
Type "A" for ascending, "D" for descending.D
The data has been written to gpa_(name).py
# Exercise 4

================ RESTART: C:/Users/rehde/Desktop/python/gpa4.py ================
Traceback (most recent call last):
  File "C:/Users/rehde/Desktop/python/gpa4.py", line 2, in <module>
    from graphics import *
ModuleNotFoundError: No module named 'graphics'
# Exercise 5

=============== RESTART: C:/Users/rehde/Desktop/python/mylist.py ===============
Count of x:  3
X in myList:  True
Index of x:  4
Reverse list:  [9, 0, 3, 5, 7, 6, 8, 9, 0, 3, 5, 7, 6, 8, 9, 0, 3, 5, 7, 6, 8]
Sort List:  [0, 0, 0, 3, 3, 3, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
# Exercise 7

============== RESTART: C:/Users/rehde/Desktop/python/Exercise7.py =============
Enter first list: 4, 5, 7, 9, 
Enter second list: 2, 5, 6, 7
The inner product is:  138
# Exercise 8

============== RESTART: C:/Users/rehde/Desktop/python/exercise8.py =============
# Exercise 9

============== RESTART: C:/Users/rehde/Desktop/python/exercise9.py =============
This program sorts student grade information by GPA
Enter the name of the data file: gpa1.txt
Enter a name for the output file: gpa2.txt
The data has been written to gpa2.txt
#Exercise 10

============ RESTART: C:/Users/rehde/Desktop/python/Eratosthenes.py ============
Sieve of Eratosthenes

Enter upper limit: 99
2
3
5
7
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
53
59
61
67
71
73
79
83
89
97
# Exercise 11

=============== RESTART: C:/Users/rehde/Desktop/python/censor.py ===============
Enter file to censor: gpa1.txt
Enter file for censored output: gpa3.txt
Censored file written to gpa3.txt
