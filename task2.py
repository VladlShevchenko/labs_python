import argparse


# create variables for operations
MULTIPLY = "multiply"
DIVIDE = "divide"
ADD = "add"
SUBSTRACT = "substract"

#declare method for choosing operation
def chooseOperation(firstN, op, secondN):
    result = "Wrong operation. Choose between: add, substract, multiply, divide"
    if op == MULTIPLY:
        result = firstN * secondN
    elif op == DIVIDE:
        result = firstN / secondN
    elif op == ADD:
        result = firstN + secondN
    elif op == SUBSTRACT:
        result = firstN - secondN
    return result

#create parser
parser = argparse.ArgumentParser()

# add operations to the parser
parser.add_argument('op', type=str, help='arithmetic operator')

parser.add_argument('firstN', type=int, help='first number') parser.add_argument('secondN', type=int, help='second number')
args = parser.parse_args()
print(chooseOperation(args.firstN, args.op, args.secondN))
