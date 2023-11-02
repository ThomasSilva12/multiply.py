### Thomas Silva
### ENGR 103 Project 5a.

def multiply(a, b):
    if a == 0 or b == 0:
        return 0

    return a + multiply(a, b - 1)


num1 = 5
num2 = 5
result = multiply(num1, num2)
print(f"{num1} * {num2} = {result}")

