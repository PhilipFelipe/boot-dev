# This function is an example of "slow to solve, fast to verify" problem.
def get_num_guesses(length):
    total_guesses = 0
    for i in range(1, length + 1):
        total_guesses += 26**i
    return total_guesses


if __name__ == "__main__":
    print(get_num_guesses(3))
