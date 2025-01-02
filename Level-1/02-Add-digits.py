

def solution(n: int) -> int:
    """ 
    Calculate the sum of each digit of a natural number n
    Args:
        n (int)
    Constraints:
        n is a natural number
        n <= 100,000,000
    Returns:
        result (int): Sum of each digit of a natural number n
    """
    assert type(n) == int and 1 <= n <= 100000000, 'Invalid input!'
    n = str(n)
    result = 0
    for k in n:
        result += int(k)
    return result

if __name__ == '__main__':
    
    # Test
    examples = [
        (123, 6),
        (987, 24),
    ]
    for example in examples:
        n, result = example
        pred = solution(n=n)
        if pred == result:
            print('Success! => n: {}, result: {}'.format(n, result))
        else:
            raise Exception('Failure!')