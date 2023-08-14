#Define functions (+, -, *, /)
#print options to user to choose
#Ask for values
#loop to give the option to keep calculating or exit

#Define the functions
def add (a, b):
    return (a + b)
def sub (a, b):
    return (a - b)
def mul (a, b):
    return (a * b)
def div (a, b):
    return (a / b)

#Ask the Functon
function = (input("Choose a mathematical function (add, sub, mult or div)")) 

numbers = []

#Recieve the numbers from the user
for i in range(2):
    num = float(input(f"Enter number: "))
    numbers.append((num))

#perform the chosen operation
if function == 'add':
    result = add(*numbers)
elif function == 'sub':
    result = sub(*numbers)
elif function == 'mul':
    result = mul(*numbers)
elif function == 'div':
    result = div(*numbers)
else:
    print("Invalid function")
    exit()

print("Result", result)
