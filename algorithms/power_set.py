def power_set(input_set):
    print("CALLING POWER SET")
    if len(input_set) == 0:
        return [[]]
    final_subsets = []
    subsets = power_set(input_set[1:])
    print("BEFORE FINAL SUBSETS: ", final_subsets)
    print("SUBSETS: ", subsets)
    for subset in subsets:
        print("APPENDING: ", input_set[:1], " + ", subset)
        final_subsets.append(input_set[:1] + subset)
        final_subsets.append(subset)
    print("FINAL SUBSETS: ", final_subsets)
    return final_subsets


if __name__ == "__main__":
    print(power_set([1, 2]))
