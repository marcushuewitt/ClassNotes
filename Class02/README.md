
[TOC levels=1,2,3 numbered]: # "Class02"

# Class02
- [Class02](#class02)
- [Objectives:](#objectives)
- [Agenda](#agenda)
- [C2, Ex01 (the assignment formally known as Assignment01, Part04)](#c2-ex01-the-assignment-formally-known-as-assignment01-part04)
- [C2, Ex02](#c2-ex02)
- [C3, Ex03](#c3-ex03)
- [Installation of Python and VSCode](#installation-of-python-and-vscode)
  - [The two major version of Python](#the-two-major-version-of-python)
- [Introduction to VSCode](#introduction-to-vscode)
- [Introduction to Markdown](#introduction-to-markdown)
- [Writing your first program](#writing-your-first-program)
- [More on the version control system Git and GitHub](#more-on-the-version-control-system-git-and-github)
- [From here on will be content for Class03](#from-here-on-will-be-content-for-class03)
- [Topics](#topics)
  - [Learning to "code"](#learning-to-%22code%22)
  - [Values, Variables, Statements and Expressions](#values-variables-statements-and-expressions)
    - [Statement](#statement)
    - [Values and data types](#values-and-data-types)
    - [Variables](#variables)
    - [String interlude](#string-interlude)
    - [Variables naming and keywords](#variables-naming-and-keywords)
  - [Statements](#statements)
    - [Expressions](#expressions)
- [rotate patrick clockwise by 1/6th of a full rotation](#rotate-patrick-clockwise-by-16th-of-a-full-rotation)
- [then move forward by 25 pixels](#then-move-forward-by-25-pixels)
- [rotate patrick clockwise by 2/6th of a full rotation](#rotate-patrick-clockwise-by-26th-of-a-full-rotation)
- [then move forward by 25 pixels](#then-move-forward-by-25-pixels-1)
- [rotate patrick clockwise by 3/6th of a full rotation](#rotate-patrick-clockwise-by-36th-of-a-full-rotation)
- [then move forward by 25 pixels](#then-move-forward-by-25-pixels-2)
- [rotate patrick clockwise by 4/6th of a full rotation](#rotate-patrick-clockwise-by-46th-of-a-full-rotation)
- [then move forward by 25 pixels](#then-move-forward-by-25-pixels-3)
- [rotate patrick clockwise by 5/6th of a full rotation](#rotate-patrick-clockwise-by-56th-of-a-full-rotation)
- [then move forward by 25 pixels](#then-move-forward-by-25-pixels-4)
- [rotate patrick clockwise by 6/6th of a full rotation](#rotate-patrick-clockwise-by-66th-of-a-full-rotation)
- [then move forward by 25 pixels](#then-move-forward-by-25-pixels-5)
- [run the program](#run-the-program)
    - [Exercise02](#exercise02)
      - [Using user input to initialize turtle graphics](#using-user-input-to-initialize-turtle-graphics)
    - [Exercise03](#exercise03)
      - [Drawing using turtle.](#drawing-using-turtle)
  - [Assignment02](#assignment02)

# Objectives:
* Review last class, and get more practice with Git
* Install Python and VSCode
* Understand basic navigation and use of VSCode 
* Understand how to create documentation using Markdown
* Write your first program

# Agenda
* Review and discuss Assignment01 from last Class.
* Complete Assignment01 part 4 as an exercise
* Complete two additional exercises:
  * Create a local repo, then push it to GitHub
  * Pull request changes to a class repo
* Discuss programming/coding learning "journey" (and how frustration is most likely a necessary part of the process)
* Install Anaconda Python and VSCode
* Write and run your first program
* Setup VSCode as default editor for git
  
# C2, Ex01 (the assignment formally known as Assignment01, Part04)

# C2, Ex02

So far, you've primarly been creating repos on GitHub, then cloning these to your local harddrive. Though this is probably the most common approach, there are times where you may want to create the local repo (by local, I mean on your machine) first, and then push the repo up to GitHub (or other repo servers).

Here are the steps:

# C3, Ex03

# Installation of Python and VSCode

## The two major version of Python

There are two versions of Python, the 2.x series, and the 3.x series. Unlike most languages that retain backward compatibility, version 3.x python shed some of the old ways of working in python. This was necessary to clean up and refresh the language (other languages, such as Java, have retained backward compatibility, but it also creates a lot of complexity as new layers of ways of doing things are plastered on top of old ways. With Python's clean break from the past, there were free to make changes and not increase the complexity of working in the language by having to retain old ways of doing things. There was a downside to this approach though, and that is that early Python programs needed to be "ported" (a computer programming term for rewriting the program) for the new Python 3.x language. Also, programmers had to learn the new syntax and concepts, and many were reluctant. It has taken many years, but much of the Python codebase has been ported to version 3.x, and most programmers now use the new version.


Download and install the Anaconda Python distribution (https://anaconda.org/tcsmith314/dashboard)

NOTE: See [here](anaconda_install.md) for detailed steps.

Anaconda has the option to install VSCode. 

# Introduction to VSCode 

VSCode is an open-source project supported by Microsoft. When programming, programmers needs special tools to create, edit, run, and debug their code. The most basic of these tools is a Text Editor (for instance, MS Windows has a built in text editor, Notepad. Though you could use Notepad for your development, but there are better options.)



# Introduction to Markdown


# Writing your first program


# More on the version control system Git and GitHub



# From here on will be content for Class03

* 
* Understand and use Variables, Expressions and Statements

* Converting variable type (aka type casting)

* Getting user input from command line

* Introduce 'turtle graphics'

* Complete exercises and assignment02.


# Topics

## Learning to "code"

https://coes.latech.edu/wp-content/uploads/sites/7/2018/07/130-student.pdf


## Values, Variables, Statements and Expressions

### Statement

A statement is an instruction that the Python interpreter can execute, but a value is not calculated or assignable.

>If you can print it, or assign it to a variable, it’s an expression. If you can’t, it’s a statement.

Examples (of statements):

```python
if CONDITION:
elif CONDITION:
else:
for VARIABLE in SEQUENCE:
while CONDITION:
try:
except EXCEPTION as e:
class MYCLASS:
def MYFUNCTION():
return SOMETHING
raise SOMETHING
with SOMETHING:
```

The distinction is nothing we should get too caught up on. What we will focus on for much of today's lecture is expressions (that's that are, or return a value)

Examples (of expressions):

```python
2 + 2
3 * 7
1 + 2 + 3 * (8 ** 9) - sqrt(4.0)
min(2, 22)
max(3, 94)
round(81.5)
"foo"
"bar"
"foo" + "bar"
None
True
False
2
3
4.0
```

### Values and data types

We can include values within our programming code. Within any programming language, values have a classification of type.

* Numbers are either whole numbers (which we call integers) or fractional/decimal numbers which we called floating point numbers (float for short)

* True of false values are called boolean.

* Text that is a series of any character, is called a string.

Let's open a Python console and test these ideas:

```
>>> 10
10
>>> type(10)
<class 'int'>
```

```
>>> 12.2
12.2
>>> type(12.2)
<class 'float'>
```

```
>>> True
True
>>> type(True)
<class 'bool'>
```

```
>>> False
False
>>> type(False)
<class 'bool'>
```

```
>>> "Hello, this is a string"
'Hello, this is a string'
>>> type("Hello, this is a string")
<class 'str'>
>>>
```

Each of these are examples of using "literal" values (often called "literals"). As we can see by using the type() command, each value is assigned a type -- in this case, int, float, bool, or str (for for integer, floating point, boolean, and string).


### Variables

Often we want to store values into memory. To do this we use variables.

Open a Python Console and try the following:

```
>>> x = 10
>>> type(x)
<class 'int'>
```

```
>>> y = 12.2
>>> type(y)
<class 'float'>
```

```
>>> z = True
>>> type(z)
<class 'bool'>
```

```
>>> s = "This is a string"
>>> type(s)
<class 'str'>
```

Python is known as a **dynamically typed" language. Many languages, such as C, C++, Java, etc. are what is called **strongly typed** or **statically typed**. In statically typed languages, when a variable is created we must **declare** it's type. This is useful for large programing projects that involve many programmers, as it forces programmers to be very explicit and carful about the variables they are using. But, statically types languages can often be much more verbose and involve more coding than a dynamically typed languages.

Since Python is a dynamically types language, Python will do two very useful things.
1. It will infer the type of variable you need/are asking for.
2. It will allow a variable to later be set to another value type.

To illustrate this, let's try duplicating the setting of variables that we did previously, but this time we'll use the same variable name.

```
>>> x = 10
>>> type(x)
<class 'int'>
```

```
>>> x = 12.2
>>> type(x)
<class 'float'>
```

```
>>> x = True
>>> type(x)
<class 'bool'>
```

```
>>> x = "This is a string"
>>> type(x)
<class 'str'>
```

By contrast to Python's dynamic typing, in a language like Java, we'd need to set the variable x to be a specific type and x will remain this type for the rest of the program (when in scope -- scope is something that we will be covering in greater detail later). In Java, if we declared x to be an integer, then if we later tried to store a floating point value, it would cause an error.

### String interlude

You'll use string types often in your programming. Python is unique from languages like C and Java, in that you can use either double or single quotes to indicate the start and end of a string.

```
>>> x = "Cannot"
>>> x = 'Cannot'
```

This feature comes in handy when we need to embed quotes within the string.
```
>>> x = 'Can't'
  File "<stdin>", line 1
    x = 'Can't'
             ^
SyntaxError: invalid syntax
>>> x = "Can't"
```

But, remember that once your choose either single of double quotes, both start and end quotes must be of the same type.

```
>>> x = 'Cannot"
  File "<stdin>", line 1
    x = 'Cannot"
               ^
SyntaxError: EOL while scanning string literal
```

Also note (and this will be covered in greater detail in a later class) strings can also be considered program documentation -- in python, called "DocStrings". When we place a multi-line string at the very beginning of a Python file, it is considered a DocString for the module (for the file). Full documentation on DocStrings can be found [here](https://www.python.org/dev/peps/pep-0257/), but for this class, we will use DocStrings only to document something about our program -- what we will consider "header" information:

```
"""
Author:         Tim Smith
Description:    Class01 program that simply displays the phrase "Hello World" to the screen.
"""

print("Hello World")
```




### Variables naming and keywords

We can call variables any name we want, as long as the name follows a few simple rules:

* Variable names can contain only letters, numbers, and underscores.
* Variable names can start with a letter or an underscore, but not with a number.
* Spaces are not allowed in variable names (use underscores to separate words in variable names).


Also, despite the freedom that these rules afford us, there are some conventions that we follow when choosing names:

* Though it's allowed syntactically, don't use Python keywords and function names as variable names:


|       |       |       |           |       |       |
|:---:  | :---: | :---: | :---:     | :---: | :---: |
|and    | as	| assert| break	    | class	| continue|
|def	| del	| elif	| else	    | except| exec  |
|finally| for	| from	| global	| if	| import|
|in	    | is	| lambda| nonlocal	| not	| or    |
|pass	| raise	| return| try	    | while	| with  |
|yield	| True	| False	| None      |       |       |


* Variable names should be short but descriptive enough to convey meaning. For example, volume is better than v, circle_area is better than c_a, and circle_area is better than area_of_a_circle.

* NOTE: Lowercase letter l and the uppercase letter O can be confused with the numbers 1 and 0. Avoid using these if there is any risk of the context not clearly indicating which interpretation we should have.

In Python it tends to be convention to avoid using uppercase letters in names of variables. Just remember that Python is case sensitive. Therefore X is not the same variable as x, nor is Volume the same variables as volume. Stick with lowercase and you'll be less likely to make such mistakes.

Though we can use underscore characters anywhere in a variable, there are some cases where an underscore may have special meaning. When starting out, it's a good practice to start all names with a letter.


```
# The professor will demonstrate variable naming.
```

## Statements

Statements are single line Python instructions. Python executes statements and an action is taken, but statements do not produce any result.

```
>>> x = 10
```

Notice that assignment is a statement. It results in Python storing a value at a memory location indicated by the variable name, but also doesn't produce a result - nothing is displayed to the screen.


### Expressions

We've see the assignment statement - but it would be boring if we could only assign values. This is where expressions come in. Expressions are a collection of values, variables, operators and functions

We've seen values and variables, but what about operators and functions?

Well, from our grade school days, you should have been expossed to many operators and functions. Operators include addition, subtraction, mulitiplication, and power. Functions can be thought of as maps a given set of inputs to outputs (often calculated).

 Here are how we use the basic operators in python.

 ```
 >>> x = 2 + 3
>>> y = y * 2
>>> y = x * 2
>>> x
5
>>> y
10
>>> y = y/2
>>> y
5.0
>>> y = y - x
>>> y
0.0
>>> 3**3
27
```

What's the difference between operators and operands? Operators are special tokens that represent computations like addition, multiplication, division and power (as we see in the examples above, these are respectively + , - , * , / and **). The values the operator uses are called operands.

### Integer division and the modulo operator (and integer division)

In python, and many programming languages, we have two forms of division. The first form is the one we're most used to seeing, and it the one demonstrated above - and that is real division.

```
>>> 1/4
0.25
```

But, let's say we're given a number of minutes, and we need to display these in a format that shows number of hours and minutes. For example, showing 90 minutes as 1 hour and 30 minutes. How would we do this?

If we use "real division" this is what we'd get

```
>>> 90/60
1.5
```

What we really want though, is a way to get the whole number of hours, and the remainder that would be the minutes. We can do this in Python using the integer division operators (//) and the modulo operator (

```
>>> minutes = 90
>>> hours = 90 // 60
>>> hours
1
>>> minutes = 90 % 60
>>> minutes
30
>>> print("Total hours is " + str(hours) + " and total minutes is " + str(minutes))
Total hours is 1 and total minutes is 30
```

NOTE: Notice how we displayed hours and minutes using the print statements. Print statements are a function and accepts a value - in this case, the value is the result from an expression that contatenates are string. We will explain this more in a section below.

### Order of operations

Expressions consist of many operators. To determine the result calculated from an expression, we therefore need to know the order of evaluation. Order of evaluation depends on the rules of precedence. Python follows the same precedence rules for its mathematical operators that mathematics does. The acronym PEMDAS is a useful way to remember the order of operations:

Parentheses have the highest precedence. This allows you to force an expression to evaluate in any order your want.

Exponents have the next highest precedence.

Multiplication and Division operators have the same precedence, and these are evaluated before Addition and Subtraction.

Addition and substraction have the same precedence, and are the lowest precedence.

Any operators with the same precedence are evaluated in a left to right order. We first handle any exponents (powers), then multiplication and devision, and then addition and subtraction.

```
>>> 2*2**4
32
>>> 2*3**3+3
57
>>> (2*3)**3+3
219
>>> 2+3+4*2
13
>>> 24/2*4
48.0
```

### Type conversion

It is often the case that we wish to translate a value of one type to a value of another type. This is often referred to as "casting", and within python there exists a number of type converter functions that help us do this.

int() converts a given value to an integer.

```
>>> type(3.14)
<class 'float'>
>>> 3.14
3.14
>>> int(3.14)
3
>>> type(int(3.14))
<class 'int'>
```

float() converts a given value to a floating point value.

```
>>> 3
3
>>> type(3)
<class 'int'>
>>> float(3)
3.0
>>> type(float(3))
<class 'float'>
```

str() converts a given value to a string.

```
>>> 3.14
3.14
>>> type(3.14)
<class 'float'>
>>> str(3.14)
'3.14'
>>> type(str(3.14))
<class 'str'>
```

### Operations on Strings

Now remember back to a previous example:

```
>>> print("Total hours is " + str(hours) + " and total minutes is " + str(minutes))
Total hours is 1 and total minutes is 30
```

What you see in this code is the use of conversion plus something called "concatenation".

As we saw previously, str(hours) and str(minutes) are examples of converting a value to a string. The addition operator here, though, is not doing mathematical addition, but rather it is functioning as a 'concatenation' operator. Concatenation is just a fancy word that means to append one string to another.

### Other operators in Python

We've covered a small subset of the many operators you can find in Python. For a full list see this this [link](http://www.tutorialspoint.com/python/python_basic_operators.htm) you will not be required to learn all of these, but just keep this link for future reference. We will see more operators later.


## Getting user input

We can use the input() function to ask a user for input data.

```
>>> name = input("Please enter your name: ")
Please enter your name: Tim
>>> age = input("Please enter your age: ")
Please enter your age: 20
>>> type(name)
<class 'str'>
>>> type(age)
<class 'str'>
>>> age + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> int(age)+1
21
>>>
```

Notice from the above code, input always returns a string value. It it therefore up to the programmer to convert the input to whatever variable type is required.

## Composition

Let's look how we can combine statements, expressions, variables, conversion, print and input functions.

First, let's look at how we could calculate the volume of a cube

```python
print("Welcome to Cube Calculator: The greatest Cube Volume calculator there is")
print()
side_length = float(input("Please enter the length of one side of the cube: "))
volume = side_length**3
print("The volume of a cub e of " + str(side_length) + " is " + str(volume))
```

Now, what if you were to calculate the volume of a box?

```python
print("Welcome to Box Calculator: The greatest Box Volume calculator there is")
print()
length = float(input("Please enter the length of the box: "))
width = float(input("Please enter the width of the box: "))
height = float(input("Please enter the height of the box: "))
volume = length * width * height
print("The volume of a box with length " + str(length) +
      ", width " + str(width) + " and height " + str(height) + 
      " is " + str(volume))
```

What about the length of a hypotenuse of a given right traingle?

```python
print("Welcome to Hyp Calc: The greatest Hypotenuse calculator there is")
print()
side_a = float(input("Please enter the length of side a: "))
side_b = float(input("Please enter the length of side b: "))
hypotenuse = (side_a**2 + side_b**2)**(1/2)
print("The length of the hypotenuse of a right triangle with length side a = " + str(side_a) +
      " and length side b = " + str(side_b) + " is " + str(hypotenuse))

```

*Now, move to the bottom of the screen and do [Exercise01](#exercise01)

## Using Multi-Line Statements

In Python, we do not need to add a semicolon at the end of statements. As we write a new line, the terminal is implied.

```
>>> a = 1
>>> b = 1
>>> c = 1
>>> a
1
>>> b
1
>>> c
1
>>> d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>>
```

The only time we need to end our statements with a semicolon are when we need to write multiple statements per line

```
>>> a = 1; b = 1; c = 1;
>>> a
1
>>> b
1
>>> c
1
>>>
```

We can also have instances where a statement can space multiple lines. There are two general situations where this occurs: 1) implicit line continuation, and 2) explicit line continuation.

### Explicit line continuation

We use the backslash to signal that our statement continues to the next line

```
>>> a = 1 + 2 \
... + 3 + 4 \
... + 5
>>> a
15
>>>

```

### Implicit line continuation

Often though, there are an implied continuation of the statement on the next line. This occurs within blocks indicates by () [] and  {} (these indicate tuples, lists and dictionaries ... data structures which we will cover later)

```
>>> a = (1 + 2 +
... 3 + 4)
>>> a
10
>>> b = (1 + 2, 3
... + 4)
>>> b
(3, 7)
>>> names = ['Jill',
... 'Bill',
... 'Julie']
>>> names
['Jill', 'Bill', 'Julie']
>>>

```

## Working with 'The Turtle'

When working in any programming languages, we often utilize libraries of preexisting code. Python has many 'modules' of existing code that you can include and use within your program.

One such model is the "turtle" module.

In this section, we'll use the turtle model to help us further develop your computational thinking.

### A basic turtle program

Turtle graphics were developed to help students learn programming. It helps students by providing a graphical, and thus visual, representation of the instructions the programmer provides the "turtle". (NOTE: Turtle graphics was originally part of the Logo programming language developed by Wally Feurzig and Seymour Papert in 1966.)

A turtle is an example of an object. Python is considered an object oriented language, in that is supports concepts of objects, classes, instance variables and methods. This is a topic that we will cover in much greater depth later, but for now, understand that Turtle is a `class` that we `instantiate` into an `object` using the command Turtle() (also known as `constructing the object`). Each turtle object has it's own state (a location, a drawing mode, etc.) and a set of actions (methods that we can call in order to have the turtle respond and change it's state in some way).

Here is a simple turtle program:

```python
import turtle               # This allows this program to use turtle objects

sandbox = turtle.Screen()   # This creates the area in which out turtles will move

patrick = turtle.Turtle()   # Create a turtle and call is patick
david = turtle.Turtle()     # '                         ' david
emily = turtle.Turtle()     # '                         ' emily
marty = turtle.Turtle()     #
jordyn = turtle.Turtle()    #
regina = turtle.Turtle()    #

# rotate patrick clockwise by 1/6th of a full rotation
# then move forward by 25 pixels
patrick.right(360/6*1)      
patrick.forward(25*1)


# rotate patrick clockwise by 2/6th of a full rotation
# then move forward by 25 pixels
david.right(360/6*2)
david.forward(25*2)


# rotate patrick clockwise by 3/6th of a full rotation
# then move forward by 25 pixels
emily.right(360/6*3)
emily.forward(25*3)


# rotate patrick clockwise by 4/6th of a full rotation
# then move forward by 25 pixels
marty.right(360/6*4)
marty.forward(25*4)

# rotate patrick clockwise by 5/6th of a full rotation
# then move forward by 25 pixels
jordyn.right(360/6*5)
jordyn.forward(25*5)

# rotate patrick clockwise by 6/6th of a full rotation
# then move forward by 25 pixels
regina.right(360/6*6)
regina.forward(25*6)

# run the program
sandbox.mainloop()

```

Turtles start at (0,0) in the x, y plan. Sending a message to a turtle to move forward by 50 pixels would be written in python as `<turtle name>.forward(50)` (where `<turtle name>` is replaced with the instance name of the specific turtle you want to send the message to). To turn a given turtle, we specific the degrees we wish to rotate it. We can either message the turtle to turn left or right. To turn a turtle around we could write our code four different ways and acheive the same result `<turtle name>.right(180)` , `<turtle name>.right(-180)` , `<turtle name>.left(180)` , `<turtle name>.left(-180)`


NOTE: We will note be covering every method and operation you can do with Turtle graphics. For a full description of all the available features found in the turtle module, see the official documentation [here](https://docs.python.org/3.7/library/turtle.html?highlight=turtle)

Now, move to the bottom of the screen and do [Exercise02](#exercise02) and [Exercise03](#exercise03)

# Class work

## Exercises

Exercises are not marked. They are an opportunity for you to practice the material from class while getting support from the professor and peers.

>NOTE1: If you get stuck, you can reach out to fellow students and the professor. You will benefit most from this exercise is you first try on your own before seeking help. Trying to work through issues is how you develop your problem solving skills.

>NOTE2: I will be looking for evidence that you've completed the exercises when determining your final class participation grade and repository management grade.


### Exercise01

#### Write four investment calculators

Simple interest calculations involve four values - future value of investment, a present value of investment, expected rate of return per term, and the number of terms being invested.

The following equations demonstrate hot to calculate any of these values given the other three.

![financial_formulas_01](images/financial_formulas_01.png)

Write for programs to calculate each of the four values. They should be named as followed:
* FutureValueCalc.py
* PresentValueCalc.py
* RateOfReturnCalc.py
* TermOfDeposit.py

>NOTE1: Remember from you "math days" that inverse power is the root, that is, if you are looking for the cube root of 64, then just take this to the power 1/3 (the square root woul be by 64**(1/2), the cube root would be 64**(1/3), the quad root would be 64**(1/4) etc.). The parentheses are important, so don't leave them out!

>NOTE2: We will learn how to better format output later. For now, expect some results to have an excessively large number of decimal places (i.e. 12.000000000002)

**In each of these programs (and all following programs), you must include a header with the following format**:

```python
"""
Author:         <your first and last name>
Description:    <a description of the program/module>
"""
```


### Exercise02

#### Using user input to initialize turtle graphics

Write a program called TurtleColor that asks a user for a color and sets the color of a turtle to this value. Then, write the code necessary to draw a circle with a radius of 100 pixels.

> NOTE1: You will need to review the [official Python documentation on turtle graphics](https://docs.python.org/3.7/library/turtle.html?highlight=turtle) to find which methods to use to set the turtle color.

> NOTE2: You may notice that improper input will result in generating an exception (for instance, try entering XGFSSD for the color). Later in the course, we'll be covering how to "catch" such exceptions to better handle these situations.

### Exercise03

#### Drawing using turtle.

Write three programs to draw each of the three pictures using turtle graphics.

In the first two examples, you only need to use forward and left methods.

![TurtleGraphic_01](images/TurtleGraphic_01.png)

![TurtleGraphic_02](images/TurtleGraphic_02.png)

In this last example, you will need to use penup, pendown, and hideturtle methods.


![TurtleGraphic_03](images/TurtleGraphic_03.png)

## Assignment02

See Assignments repos for Assignment02. This must be submitted by end of class (11 pm).








