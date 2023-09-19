import preprocess
from random import shuffle
from math import ceil


def shuffle_and_split_data(data, test_size):
    split_idx = ceil(test_size*len(data))
    shuffle(data)
    return data[0, split_idx], data[split_idx, len(data)]


def main():
    data = preprocess.main()


main()
