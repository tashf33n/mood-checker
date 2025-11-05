import argparse
from calculator import add, subtract, multiply, divide

def main():
    parser = argparse.ArgumentParser(description="Simple Calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")

    args = parser.parse_args()

    result = None
    if args.operation == "add":
        result = add(args.num1, args.num2)
    elif args.operation == "subtract":
        result = subtract(args.num1, args.num2)
    elif args.operation == "multiply":
        result = multiply(args.num1, args.num2)
    elif args.operation == "divide":
        result = divide(args.num1, args.num2)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
