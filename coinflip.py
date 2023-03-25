import sys
from coinflipper import CoinFlipper


def get_probability(probability: str) -> float:
    """Return a probability as a float."""
    try:
        if "/" in probability:
            numerator, denominator = probability.split("/")
            probability = int(numerator) / int(denominator)
        else:
            probability = float(probability)
    except ValueError:
        err_msg = "Probability input must take form of a float (0.005) or fraction (1/1000)."
        raise ValueError(err_msg)
    
    if probability > 1 or probability < 0:
        err_msg = "Probability must be a value between 0 and 1"
        raise ValueError(err_msg)
    return probability

def get_number_of_flips(number_of_flips: str) -> int:
    """Return number of flips as an int."""
    try:
        number_of_flips = int(number_of_flips)
    except ValueError:
        err_msg = "Number of flips must be an integer."
        raise ValueError(err_msg)
    return number_of_flips

def get_inputs() -> tuple[float, int]:
    """Return probability and number of flips as floats."""
    try:
        if len(sys.argv) < 2:
            raise ValueError("Too few inputs.")
        elif len(sys.argv) > 3:
            raise ValueError("Too many inputs.")
        elif len(sys.argv) == 2:
            sys.argv.append("1")
        probability = get_probability(sys.argv[1])
        number_of_flips = get_number_of_flips(sys.argv[2])
    except Exception as e:
        print("Unable to parse inputs:")
        print(f"-  {e}")
        print("")
        print("Usage: \"python coinflip.py <probability> <number of flips (optional, defaults to 1)>\"")
        print("> Example: \"python coinflip.py 0.5 100\"")
        print("> Example: \"python coinflip.py 1/2\"")
        sys.exit(1)
    return probability, number_of_flips

def main() -> None:
    probability, number_of_flips = get_inputs()
    if number_of_flips == 1:
        print("Heads" if CoinFlipper(probability).flip() else "Tails")
    else:
        CoinFlipper(probability).flips(number_of_flips)

if __name__ == "__main__":
    main()