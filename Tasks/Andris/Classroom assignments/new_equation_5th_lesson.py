equation = input('Indicate your equation: ').replace(' ', '')  # Remove all spaces after input.

# The put the string in a separate variable, split it by the "equal" sign, we get 2 indices: [zero and first].
equation1 = equation.split('=')

# The put the contents of the first index into a new variable, then also split it by the "x" sign.
# We get 2 indices from the first: [zero and first].
equation2 = equation1[1].split('x')

# The translate both indices of the new variable to an int.
k = int(equation2[0])
b = int(equation2[1])
x = int(input('Indicate a value for "x": '))

print('y=', k * x + b, sep='')
