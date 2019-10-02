# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE 
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
def times1000(n):
    return n*1000
result = map(times1000, x)
print(result)

finalx = list(result)
print(finalx)

#newx = [n * 1000 for n in x]
#print(newx)