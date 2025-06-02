def super_digit(n, k):
    def get_super_digit(x):
        if len(x) == 1:
            return int(x)
        return get_super_digit(str(sum(int(digit) for digit in x)))
    
    initial_sum = sum(int(digit) for digit in n) * k
    return get_super_digit(str(initial_sum))
