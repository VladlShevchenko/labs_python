import argparse


def main():

# create parser
parser = argparse.ArgumentParser()
parser.add_argument('formula', help='String with formula', type=str) args = parser.parse_args()

numbers = "0123456789"
signs = "+-"

isStatementCorrect = True
result = ''

# check formula size and first symb.
if len(args.formula) > 0 and args.formula[0] in numbers:
    for index, symb in enumerate(args.formula):

# check formula
  if symb in numbers or (symb in signs and not args.formula[index + 1]
      result += symb
  else:
       result = None
       isStatementCorrect = False
       break

   if isStatementCorrect:
       print(f'result = ({isStatementCorrect}, {eval(result)})')
   else:
       print(f'result = ({isStatementCorrect}, None)')
else:
        print(f'result = ({False}, None)')

if __name__ == '__main__':
    main()
