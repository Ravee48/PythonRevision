import argparse
from random import choice, choices

parser = argparse.ArgumentParser(description="Simple Parser for calcualtion :")

parser.add_argument("num1", type=float, help="Provide frist number for operation" )
parser.add_argument("num2", type=float, help="Provide frist number for operation" )
parser.add_argument("operation", choices=['sum', 'sub', 'mul', 'div'], help="Provide operation to perform")

arg = parser.parse_args()

print(arg)

if arg.operation == 'sum':
    print(f"Sum of the two numbers are : {arg.num1 + arg.num2}")
elif arg.operation == 'sub':
    print(f"Substraction of the two numbers are : {arg.num1 - arg.num2}")
elif arg.operation == 'div':
    print(f"Division of the two numbers are : {arg.num1 / arg.num2}")
elif arg.operation == 'mul':
    print(f"Multiplication of the two numbers are : {arg.num1 * arg.num2}")
else:
    print(f"Something wrong has occured, please check the numbers and operations provided")

