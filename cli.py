"""
cli.py — Command-line interface for the temperature converter.

Usage:
    python cli.py <value> <from_unit> <to_unit>
    python cli.py 100 C F
    python cli.py --all 100 C          # show conversion to all units
    python cli.py --interactive         # enter interactive mode

Design note: This file contains ONLY I/O logic.
All maths lives in converter.py so it can be imported anywhere
(Flask, Streamlit, tests) without dragging in CLI concerns.
"""

import argparse
import sys
from converter import convert, all_conversions

UNIT_SYMBOLS = {"C": "°C", "F": "°F", "K": "K"}


def format_result(value, unit):
    return f"{value:.2f} {UNIT_SYMBOLS[unit.upper()]}"


def run_interactive():
    """Loop: ask for input, print result, repeat until Ctrl-C or 'q'."""
    print("Temperature Converter — Interactive Mode")
    print("Type  q  or press Ctrl-C to exit.\n")

    while True:
        try:
            raw = input("Enter  <value> <from> <to>  (e.g. 100 C F): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if raw.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        parts = raw.split()
        if len(parts) != 3:
            print("  ✗  Please enter exactly three values: value, from_unit, to_unit\n")
            continue

        try:
            value = float(parts[0])
            result = convert(value, parts[1], parts[2])
            from_sym = UNIT_SYMBOLS[parts[1].upper()]
            to_sym   = UNIT_SYMBOLS[parts[2].upper()]
            print(f"  ✓  {value} {from_sym} = {format_result(result, parts[2])}\n")
        except ValueError as e:
            print(f"  ✗  {e}\n")


def build_parser():
    parser = argparse.ArgumentParser(
        prog="cli.py",
        description="Convert temperatures between Celsius, Fahrenheit, and Kelvin.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python cli.py 100 C F          → 100.00 °C = 212.00 °F
  python cli.py 32 F C           → 32.00 °F  = 0.00 °C
  python cli.py 0 K C            → 0.00 K    = -273.15 °C
  python cli.py --all 100 C      → show all three conversions
  python cli.py --interactive    → enter interactive mode
        """,
    )

    parser.add_argument(
        "value",
        nargs="?",
        type=float,
        help="Temperature value to convert (e.g. 100 or -40.5)",
    )
    parser.add_argument(
        "from_unit",
        nargs="?",
        help="Unit to convert FROM: C, F, or K",
    )
    parser.add_argument(
        "to_unit",
        nargs="?",
        help="Unit to convert TO: C, F, or K (omit when using --all)",
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        dest="show_all",
        help="Show conversion to all three units at once",
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Enter interactive (REPL) mode",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    # ── Interactive mode ──────────────────────────────────────────────
    if args.interactive:
        run_interactive()
        return

    # ── Validate that required positional args are present ───────────
    if args.value is None or args.from_unit is None:
        parser.print_help()
        sys.exit(1)

    # ── Show-all mode ─────────────────────────────────────────────────
    if args.show_all:
        try:
            results = all_conversions(args.value, args.from_unit)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

        from_sym = UNIT_SYMBOLS[args.from_unit.upper()]
        print(f"\n  {args.value} {from_sym} equals:\n")
        for unit, val in results.items():
            print(f"    {UNIT_SYMBOLS[unit]:>3}  →  {val:>10.2f}")
        print()
        return

    # ── Single conversion ─────────────────────────────────────────────
    if args.to_unit is None:
        print("Error: to_unit is required (or use --all to show all conversions).",
              file=sys.stderr)
        sys.exit(1)

    try:
        result = convert(args.value, args.from_unit, args.to_unit)
        from_sym = UNIT_SYMBOLS[args.from_unit.upper()]
        print(f"{args.value} {from_sym} = {format_result(result, args.to_unit)}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
