__author__ = 'A. Sangha'
"""
Date: February 2, 2022
File Name: Graphing_Tool
Description: Displays a graph of the desired inputted function from the x values of -10 to 10
"""

# Import to graph
import matplotlib.pyplot as plt

# Create x coordinates
x = []
count = (-5)

while count <= 5:
    x.append(count)
    count += 1

# Empty y value list
y_values = []

# Checks the function
def function_check():

    # Create global variable for the function to call it anytime
    global func

    check = True
    while check:
        try:

            # Turn function into string to evaluate
            func = input('Please enter function to graph (requires spaces, x must be lowercase): ')
            func = "'" + func + "'"
            func = eval(func)

        except TypeError:
            print('Function not understood.')
        else:
            return func

# Solves the function to find y values
def solver(func):

    # Turn the input into a a list
    count = 0
    func = func.split()

    # Look for where the x is located
    try:
        x_value_index = func.index('x')
    except ValueError:
        print('Function not understood.')

    # Inputs each x value into the function
    for i in range(11):
        # replace x in eval with each item in x list
        x_values = x[count]
        func[x_value_index] = x_values

        # Turn the list into a string to use "eval()"
        X_Str = ' '.join(map(str, func))
        y_values.append(eval(X_Str))
        count += 1

# Main method
def main():

    function_check()
    solver(func)
    try:

        # If function entered is a quadratic:
        if func.index('**'):
            Real_y =  [abs(item) for item in y_values]
            plt.plot(x,Real_y)
            plt.show()

    # If function entered is linear
    except ValueError:
        plt.plot(x,y_values)
        plt.show()

# Run program
if __name__ == '__main__':
    main()
