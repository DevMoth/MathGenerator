# Math Generator
## Description 
**MathGenerator** is an app, designed for generating simple math problems (1st to 2nd grade level) in configurable amounts to test your (or your children's) skills.
## How to use
To use the program you'll have to install a Python interpreter. 
After that simply launch the "*app.py*" file and input the count of rounds (a single equation) you want to have.
Equation parameters (such as range of numbers or allowed operations) can be configured before launch in the "*config.txt*" file.
## Configuration
Here are all of the equation parameters that can be configured:
- *oper_count_range* <2 numbers> - Configures the count of operators allowed in a single "line" (expression, consisting of numbers and operators without braces).
First number is the minimal count of operators and the second is the maximum. Increasing the upper limit leads to more complex equations.
- *num_range* <2 numbers> - Configures the range of numbers that can be added into the equation.
First number is the minimum and the second is the maximum. Increasing the range will make the equation harder to caclulate by hand.
- *allowed_opers* <list of operators> - Sets the operators that will appear in the equations.
Currently, only addition (+), subtraction (-) and multiplication (*) are implemented.
- *brace_count_range* <2 numbers> - Configures the count of braces that can appear in the equation.
First number is the minimum count of braces and the second is the maximum.
- *max_brace_depth* <1 number> - Configures the max depth of nested braces. Increasing the number will lead to exponential growth in complexity.
- *max_brace_opers* <1 number> - Configures the max count of operators in expressions inside braces.
- *allow_negative* <True/False> - Configures whether negative numbers can appear in the answers to expressions.
To allow negative numbers to be a part of the initial equation see *num_range*.
