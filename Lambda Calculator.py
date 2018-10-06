num1 = float(input("First number: "))
num2 = float(input("Second number: "))
nums = (num1, num2)
calculations = input('What would you like to use?')

operations = (
    (('+', 'add', 'addition'), lambda n: n[0] + n[1]),
    (('-', 'subtract', 'subtraction'), lambda n: n[0] - n[1]),
    (('*', 'multiply', 'multiplication'), lambda n: n[0] * n[1]),
    (('/', 'divide', 'division'), lambda n: n[0] / n[1])
)

for op in operations:
    if calculations in op[0]:
        print(op[1](nums))