# Andela_bc_12

##Prime numbers generator

This is a simple command line program that generates list of prime numbers from zero to the number passed in the function.
For example passing a value like 10 to the method it should return the given result.


```
print prime_generator(10)
[2, 3, 5, 7]
```
##Guide

######Clone the repository 
*$ git clone https://github.com/angieMutava/Andela_bc_12.git*
Then run the app using the command *python primegenerator.py* while  in the  directory.

##Tests
To demonstrate TDD using Python's unittest the tests.py file  has some testcases that the prime_generator method must pass.
For example the test below checks whether the number passed is negative and gives the given message.
```
 def test_negative_numbers(self):
        self.assertEqual(testcases.prime_generator(-5), "Negative numbers not allowed.")
``` 

##Asymptotic Analysis
This is a simple description of the prime_generator method in regard to Big O-notation in terms of the time taken to execute it.From my analysis the method is executing at a constant average time of a few seconds.Proper analysis is to be conducted for worst cases.

##Tasks not accomplished.

Improving the efficiency of the program in cases where the number passed is huge.For example 1,000,000.Still analysing the program to check for better ways to achieve the same with minimum resource usage in the worst case.