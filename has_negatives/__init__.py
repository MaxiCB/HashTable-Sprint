def has_negatives(a):
    cache = {}
    numbers_with_negatives = []

    for number in a:

        cache[number] = 1

        if number != 0 and -number in cache:
            numbers_with_negatives.append(abs(number))

    return numbers_with_negatives


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
