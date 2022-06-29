# py_randlabel
## Generate a 'label string' of randomised letters and numbers

This is a python module that provides a function to generate a string of randomised characters and numbers.

The function should be fairly easy to use. Just import the module and then call the function, giving it an integer argument that sets the character length of the returned randomised string.

A sample program, *testcase.py* is included. It's source is shown below:

```
import randlabel

for _ in range(1, 10):
    print(randlabel.randlabel(16))
```
