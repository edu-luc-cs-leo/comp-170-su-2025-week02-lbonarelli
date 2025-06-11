# 1. Function to greet a person
def greet(name):
    return f"Hello {name}. How are you?"

print(greet("Luca"))  # Example usage

# 2. Greet a few friends
my_friends = ["Manuel", "Pier", "Gabriel"]
for name in my_friends:
    print(greet(name))

# 3. Solve a quadratic equation
import math

def solve_quadratic(a, b, c):
    print(f"{a}x^2 + {b}x + {c} = 0")

    equation = b**2 - 4*a*c

    if equation < 0:
        print("No real solutions")
    else:
        r1 = (-b - math.sqrt(equation)) / (2*a)
        r2 = (-b + math.sqrt(equation)) / (2*a)
        print(f"x1 = {r1}")
        print(f"x2 = {r2}")

# Example usage
solve_quadratic(1, 2, 3)
