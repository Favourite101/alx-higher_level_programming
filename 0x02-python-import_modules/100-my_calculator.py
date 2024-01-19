#!/usr/bin/python3

if  __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv)
    if argc < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
