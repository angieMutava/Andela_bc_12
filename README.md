# Andela_bc_12
<hr>
##Prime numbers generator
<hr>
This is a simple command line program that generates list of prime numbers from zero to the number passed in the function.
For example passing a value like 10 to the method it should return the given result.
<hr>

```
print prime_generator(10)
[2, 3, 5, 7]
```
<hr>

##Guide
</hr>
######Clone the repository 
*$ git clone https://github.com/angieMutava/Andela_bc_12.git*
Then run the app using the command *python primegenerator.py* while  in the  directory.
<hr>
##Tests
To demonstrate TDD using Python's unittest the tests.py file  has some testcases that the prime_generator method must pass.
For example the test below checks whether the number passed is negative and gives the given message.
```
 def test_negative_numbers(self):
        self.assertEqual(testcases.prime_generator(-5), "Negative numbers not allowed.")
``` 

#tasks not accomplished within the reporting period

Improving the efficiency of the program in the cases where the number passed is huge.For example 1000000.