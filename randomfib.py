from random import random
import matplotlib.pyplot as plt


def random_fibonacci(a, b):
    """Returns a 'random Fibonacci' number.

    Essentially, there is an equal random chance that the number 
    returned will be either F_(n) + F_(n-1) or F_(n) - F_(n-1).
    """
    return (a + b) if random() >= 0.5 else (a - b)


def main():
    numbers_to_add = 10
    number_of_trials = 10
    trials = []
    numbers = [0, 1]  # Start with first two Fibonacci numbers.

    for i in range(number_of_trials):
        for j in range(1, numbers_to_add + 1):
            next_number = random_fibonacci(numbers[j], numbers[j-1])
            numbers.append(next_number)
            print(f"{next_number:,}")
        trials.append(numbers)
        numbers = [0, 1]

    # All trials are plotted.
    plt.title("Random Fibonacci numbers")
    for i in range(number_of_trials):
        plt.plot(list(range(numbers_to_add + 2)), trials[i])
    plt.show()


if __name__ == "__main__":
    main()
