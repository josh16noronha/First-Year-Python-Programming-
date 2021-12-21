"""
ECOR 1041 Lab 6 Solution Template

Author and Student Number: Joshua Noronha, 101194076

This file is to be used in conjunction with the detailed lab description for Lab 6
Use this file to enter your answers to the series of exercises you will complete.

==========

Exercise 1: Single or Double Quotes - Does it matter?

Example, "haven't" or '"Spam, spam, spam," he said.'

>>> type('Hello')
# Type what you see: <class 'str'>


>>> type("goodbye")
# Type what you see: <class 'str'>


>>> 'Hello'
# Type what you see: 'Hello'

>>> ""     (An empty string - type two quotes with no spaces between them.)
# Type what you see: '' (The double quotes outputs a single pair of quotes)

>>> '"Spam, spam, spam," he said.'
# Type what you see: '"Spam, spam, spam," he said.' (Nested quotations)

>>> "I haven't a clue" 
# Type what you see: "I haven't a clue" (Nested apostrophe)

>>> 'I haven't a clue' 
# Type what you see: 

Traceback (most recent call last):
  Python Shell, prompt 12, line 1
Syntax Error: invalid syntax: <string>, line 1, pos 10
 
(Nested apostrophe)

Concluding Questions: Generally, either double or single quotes works well but can you give a scenario where one is better than the other?

# The example that I am using is ("I haven't a clue") in this case it is best to apply the double quotes surrounding the text because python interprets the apostrophe in (haven't) as an incomplete string and the output is an error, unless the double quotes are used to surround the text. 
==================

Exercise 2: What operations are permitted with values of type str?

When used with strings, + is the concatenation operator. 

>>> 'Hello, ' + 'world!'
# Type what you see: 'Hello, world!'

When used with strings, * is the replication operator.

>>> "Spam" * 3
# Type what you see: 'SpamSpamSpam'

>>> 3 * "Spam"
# Type what you see: 'SpamSpamSpam'  (Reflect: What does this say about order of operators?)
	# This shows that the order of the operator does not matter if it is "Spam" * 3 or 3 * "Spam" the output is the same 'SpamSpamSpam' 
>>> "Spam" * 0
# Type what you see: ''

>>> "Spam" * -3
# Type what you see: ''


There are other operators to try now: - and /

>>> "Hello" - "He"
# Type what you see: 

Traceback (most recent call last):
  Python Shell, prompt 7, line 1
builtins.TypeError: unsupported operand type(s) for -: 'str' and 'str'


>>> 'Spam' / 3
# Type what you see: 

Traceback (most recent call last):
  Python Shell, prompt 8, line 1
builtins.TypeError: unsupported operand type(s) for /: 'str' and 'int'


Concluding Questions: What operators work with strings?  Does the order of operands matter?

# The only operator that works with strings and does not give '' as an output is the multiplication operator. The order of the multiplication operator does not matter as the output is the same in both these cases above 

=======================

Exercise 3 : Understand the string representation

Is  the string '123' the same as the integer 123? 

>>> '123' + 456
# Type what you see: 

Traceback (most recent call last):
  Python Shell, prompt 9, line 1
builtins.TypeError: can only concatenate str (not "int") to str

>>> '123' + '456'
# Type what you see: '123456'

Concluding Question: When a string looks like a number, is it a number or a string?

# It is a string which cannot be used to do any calculations but can be used to add two strings together such as this example '123' + '456'

=========
Last edited: October 27, 2020
"""

# Lab Number: 16A

# Name and Student Number: Joshua Noronha, 101194076

# Functions below this line:
def repeat(s: str, n: int) -> str:
 """ Return s repeated n times; if n is negative, return the
 empty string.
 >>> repeat('yes', 4)
 'yesyesyesyes'
 >>> repeat('no', 0)
 ''
 >>> repeat('no', -2)
 ''
 >>> repeat('yesnomaybe', 3)
 'yesnomaybeyesnomaybeyesnomaybe'
 """
 return s*n

def total_length(s1: str, s2: str) -> int:
 """ Return the sum of the lengths of s1 and s2.
 >>> total_length('yes', 'no')
 5
 >>> total_length('yes', '')
 3
 >>> total_length('YES!!!!', 'Noooooo')
 14
 """
 return len(s1+s2)

def replicate(st:str)->str:
 """Returns s1 which is repeated based on the length of the string's characters
 >>> replicate ('a')
 a
 >>> replicate ('abc')
 abcabcabc
 >>> replicate ('')
 ''
 >>> replicate ('12345')
 1234512345123451234512345
 """
 return len(st) * st

# Main Script below this line:

# Exercise 4
print ("\n Exercise 4 Outputs: \n") 

result = repeat('yes', 4)
print(result)
result = repeat('no', 0)
print(result )
result  = repeat('no', -2)
print(result )
result  = repeat('yesnomaybe', 3)
print(result )

# Exercise 5
print ("\n Exercise 5 Outputs: \n")

result = total_length('yes', 'no')
print(result)
result = total_length('yes', '')
print(result)
result = total_length('YES!!!!', 'Noooooo')
print(result)

# Exercise 6
print ("\n Exercise 6 Outputs: \n")

Input = replicate ('a')
print(Input)
Input = replicate ('abc')
print(Input)
Input = replicate ('')
print(Input)
Input = replicate ('12345')
print(Input)

# No code below this line
print("\nEnd of file reached successfully")