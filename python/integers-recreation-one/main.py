
# Codewars task url:
# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

# See:
# https://stackoverflow.com/questions/34891170/find-all-integers-between-m-and-n-whose-sum-of-squared-divisors-is-itself-a-squa
# https://projecteuler.net/problem=211#:~:text=Divisor%20Square%20Sum&text=For%20a%20positive%20integer%20n,%2B%2025%20%2B%20100%20%3D%20130.

def list_squared(m, n):
    result = []
    for i in range(m, n + 1):
        s = sum([1] + [j**2 for j in range(2, i + 1) if i % j == 0])
        if i == 1 or (s > 1 and (s**.5).is_integer()):
            result.append([i, s])
    return result

if __name__ == "__main__":
    assert list_squared(1, 250) == [[1, 1], [42, 2500], [246, 84100]]
    assert list_squared(42, 250) == [[42, 2500], [246, 84100]]
    assert list_squared(250, 500) == [[287, 84100]]
