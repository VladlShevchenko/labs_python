import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('firstN', type=int, help='first number')
    parser.add_argument('op', type=str, help='arithmetic operator')
    parser.add_argument('secondN', type=int, help='second number')

    args = parser.parse_args()

    result = str(args.firstN) + args.op + str(args.secondN)
    print(eval(result))

if __name__ == '__main__':
    main()
