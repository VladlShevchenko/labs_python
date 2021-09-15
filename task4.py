import argparse
import ast

def getMaxWeight(items, capacity):
    size = len(items)
    # create matrix
    list = [[0 for a in range(capacity + 1)] for i in range(size + 1)]

    # loop which fill the memorization table
    for i in range(size + 1):
    for a in range(capacity + 1):
            if i == 0 or a == 0:
                list[i][a] = 0
            elif items[i - 1] <= a:
                list[i][a] = max(items[i - 1] + list[i - 1][a - items[i - 1]], list[i - 1][a])
            else:
                list[i][a] = list[i - 1][a]

    return list[size][capacity]


def main():

    # create parser
    parser = argparse.ArgumentParser()
    parser.add_argument("capacity", help="Bag capacity W", type=int)
    parser.add_argument("weights", help="List of weights of each gold bar", nargs='*')
    args = parser.parse_args()

    # call function
    maxWeight = getMaxWeight([ast.literal_eval(weight) for weight in args.weights], args.capacity)
    print(f"Maximum weight of gold that fits into a knapsack is {maxWeight} with capacity of {args.capacity}")

if __name__ == "__main__":
    main()
