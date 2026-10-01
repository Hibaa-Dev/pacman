import json
import sys
from src.config.loader import load_config
from src.game import Game


def main() -> None:
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python pac-man.py <config_file>")

        data = load_config('config.json')
        run = Game()
        run.run()
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
