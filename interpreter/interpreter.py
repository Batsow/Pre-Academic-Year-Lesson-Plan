#option 1
'''
expression = input("Expression: ")
x,y,z = expression.split(" ")
x = int(x)
z = int(z)

if y == "+":
    print(float(x+z))
elif y == "-":
    print(float(x-z))
elif y == "/":
    print(float(x/z))
elif y == "*":
    print(float(x*z))
'''

#option 2
expression = input("Expression: ")
x,y,z = expression.split()
x, z = int(x), int(z)

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z

print(float(result))
