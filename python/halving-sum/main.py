

def halving_sum(n):
    r = 0
    while n > 0:
        r += n
        n //= 2
    return r


def example_tests():
    assert halving_sum(25) == 47
    assert halving_sum(127) == 247


if __name__ == '__main__':
    example_tests()

