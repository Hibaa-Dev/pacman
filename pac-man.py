import json
import sys
from src.parser import Parser


def main() -> None:
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python pac-man.py <config_file>")

        parser = Parser(sys.argv[1])
    except ValueError as e:
        print(e)

    except FileNotFoundError as e:
        print(e)

    except json.decoder.JSONDecodeError as e:
        print(e)

    except KeyboardInterrupt:
        print("Error: KeyboardInterrupt.")


if __name__ == "__main__":
    main()
