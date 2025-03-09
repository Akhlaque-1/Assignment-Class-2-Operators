# Arithmetic Operators
# Addition
x = 5
y = 4
print(x + y) #9

# Subtraction
x = 5
y = 4
print(x - y) #1

# Multiplication
x = 5
y = 4
print(x * y)  #20

	# Division
x = 5
y = 4
print(x / y) # 1.25

# Modulus
x = 5
y = 4
print(x % y) #1

# Exponentiation
x = 5
y = 4
print(x ** y) #625

# Floor division
x = 5
y = 4
print(x // y) #1


# Assignment Operators
x = 5
print(x) #5



x = 5
x += 3 
print(x) #8

x = 5
x -= 3 
print(x) #2

x = 5
x *= 3 
print(x) #15

x = 5
x /= 3 
print(x) #1.25

x = 5
x %= 3 
print(x) #2

x = 5
x //= 3 
print(x) #1

x = 5
x **= 3 
print(x) #125

x = 5
x &= 3 
print(x) #1


x = 5
x |= 3 
print(x) #7

x = 5
x ^= 3 
print(x) #6

x = 5
x >>= 3 
print(x) #0

x = 5
x <<= 3 
print(x) #40


x = 5
x = 3 
print(x := 3) #3

# Comparison Operators
x = 5
y = 3
print(x == y) #False

x = 5
y = 3
print(x != y) #True

x = 5
y = 3
print(x > y) #True

x = 5
y = 3
print(x < y) #False

x = 5
y = 3
print(x >= y) #True

x = 5
y = 3
print(x <= y) #False

# Logical Operators
x = 5
print(x > 3 and x < 10) #True

x = 5
print(x > 3 or x < 4)  #True

x = 5
print(not(x > 3 and x < 10)) #False

# Identity Operators
x = 5
y = 3
print(x is y) #False

x = 5
y = 3
print(x != y) #True

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z) #False
print(x is not y) #True
print(x != y) #False


# Membership Operators
x = ["apple", "banana"]
print("banana" in x) #True

x = ["apple", "banana"]
print("pineapple" not in x) #True

# Bitwise Operators
print(6 & 3) #2

print(6 | 3) #7

print(6 ^ 3) #5

print(~3)  #-4

print(3 << 2) #12

print(8 >> 2) #2
