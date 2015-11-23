# -*- coding: utf-8 -*-
import math


def sigmoid(x, para=None):
    buffer = 1/(1 + math.exp(-x))
    return buffer


if __name__ == "__main__":
    test = [0, 0.000001, 0.00002, 0.3, 0.45, 0.7]
    for value in test:
        print(sigmoid(value))