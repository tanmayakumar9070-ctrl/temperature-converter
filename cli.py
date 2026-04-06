import argparse
from converter import convert

def main():
    parser = argparse.ArgumentParser(
        description="Temperature Converter CLI"
    )
    parser.add_argument("value", type=float, help="Temperature value")
    parser.add_argument("from_unit", help="Input unit: C, F, or K")
    parser.add_argument("to_unit",   help="Output unit: C, F, or K")
    args = parser.parse_args()

    try:
        result = convert(args.value, args.from_unit, args.to_unit)
        print(f"{args.value}°{args.from_unit.upper()} = "
              f"{result:.2f}°{args.to_unit.upper()}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()