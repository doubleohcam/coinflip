import numpy as np


class CoinFlipper:
    """CoinFlipper class to flip a coin given a probability."""

    def __init__(self, probability: float) -> None:
        """Initialize the CoinFlipper class."""
        self.probability = probability

    def flip(self) -> int:
        """Return a coin flip, given a probability."""
        # return binomial distribution with 1 trial and probability
        return np.random.binomial(1, self.probability)

    def flips(self, number_of_flips: int) -> None:
        """Return a list of coin flips, given a probability and number of flips."""
        results = np.arange(number_of_flips)
        for i in range(0, number_of_flips):
            results[i] = self.flip()
        return self._interpret_results(results)

    def _interpret_results(self, results: list[int]) -> None:
        """Print the results of the coin flips."""
        print(f"Probability is set to {self.probability*100}%")
        print("Tails = 0, Heads = 1")
        print("Results: [")
        print_string = " "
        for i, value in enumerate(results):
            if i % 10 == 0 and i != 0:
                print(print_string)
                print_string = " "
            print_string += f"{str(value)} "
            if i == len(results) - 1:
                print(print_string)

        print("]")
        print("Head Count: ", np.count_nonzero(results == 1))
        print("Tail Count: ", np.count_nonzero(results == 0))
