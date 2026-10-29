"""The same demo with no server: one customer's chance of default, reason and error costs, printed.

Run it from the repository's top folder:

    python app/no_server.py
    python app/no_server.py --row 12 --miss-cost 20
"""
import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))  # so this file can import src
from src import data, score, train  # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description="Score one customer of the test book.")
    parser.add_argument("--row", type=int, default=0, help="a row of the test book, counted from 0")
    parser.add_argument("--miss-cost", type=float, default=train.MISS_COST, help="cost of a missed default")
    parser.add_argument("--wasted-cost", type=float, default=train.WASTED_COST, help="cost of a wasted call")
    args = parser.parse_args(argv)

    try:
        learn, book = train.split_book(data.load_cards())
        if not 0 <= args.row < len(book):
            parser.error(f"--row must be from 0 to {len(book) - 1}")
        probability, reason = score.score(book.iloc[args.row])
    except (NotImplementedError, FileNotFoundError) as not_ready:
        print(f"Not ready yet: {not_ready}")
        return 1

    print(f"Customer {args.row} of the test book")
    print(f"Chance of default in October: {probability:.0%}")
    print(f"Main reason: {reason}")
    print(f"If Kalpa calls and the customer would have paid: a wasted call costing {args.wasted_cost:g}, "
          f"chance times cost {(1 - probability) * args.wasted_cost:.2f}")
    print(f"If Kalpa skips and the customer defaults: a missed default costing {args.miss_cost:g}, "
          f"chance times cost {probability * args.miss_cost:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Test inputs and expected outcomes
# ---------------------------------
# python app/no_server.py, in a new copy of the repository
#     Not ready yet: load_cards in src/data.py is still a __TODO__ for your group (exit code 1)
# python app/no_server.py, with src/ written but section 4 of the notebook never run
#     Not ready yet: No saved model at .../models/model.joblib: run section 4 ... (exit code 1)
# python app/no_server.py, with everything written
#     Five lines for row 0: its chance, its reason, then the two mistakes priced at 1 and 5.
# python app/no_server.py --row 12 --miss-cost 20
#     Row 12's chance and reason; the missed-default line uses 20, four times its value at 5.
# python app/no_server.py --row 9000
#     error: --row must be from 0 to 8999 (exit code 2)
