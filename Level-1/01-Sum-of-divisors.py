

import math


def solution(n: int) -> int:
    """ 
    Takes an integer n as input, and returns the sum of all divisors of n.
    Args:
        n (int)
    Constraints:
        0 <= n <= 3000
    Questions:
        What if the case of n = 0?
        constraints of n should be modified to 1 <= n <= 3000, because n cannot be zero.
    Returns:
        result (int): Sum of all divisors of n
    """
    assert type(n) == int and 0 <= n <= 3000, 'Invalid input!'

    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    result = sum(divisors)
    return result


def get_divisors_faster(n: int) -> list[int]:
    """ 
    For a natural number n (greater than or equal to 1),
    returns a list of all divisors of n.
    (Square root method: check only from 1 to sqrt n)
    Args:
        n (int)
    Constraints:
        0 <= n <= 3000
    Returns:
        result (list[int]): List of all divisors of n
    """
    divisors = []
    limit = math.isqrt(n) # Return sqrt of n as an integer (after Python 3.8)

    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


if __name__ == '__main__':
    
    # Test
    examples = [
        (12, 28),
        (5, 6),
    ]
    for example in examples:
        n, result = example
        pred = solution(n=n)
        if pred == result:
            print('Success! => n: {}, result: {}'.format(n, result))
        else:
            raise Exception('Failure!')

    print(get_divisors_faster(12))
    print(get_divisors_faster(24))
    print(get_divisors_faster(36))