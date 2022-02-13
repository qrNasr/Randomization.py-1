import random

# Create random ontegers numbers using .random(a,b)
random_integer = random.randint(1, 10)
print(random_integer)

# Create random float numbers using .random()
random_float = random.random()
print(random_float)

print(random_float * 5)

# Head or tail game

FlipSide= random.randint(0,1)

if FlipSide ==1:
  print("Head")
else:
  print("Tail")
