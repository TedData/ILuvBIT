def geometric(start, ratio, length=None) :
    pos = 0
    value = start
    while length is None or pos < length :
        yield value
        value *= ratio
        pos += 1


if __name__ == "__main__" :
    powers_two = geometric(1, 2)
    print(next(powers_two), next(powers_two), next(powers_two))

    print(list(geometric(2, 3, 6)))
