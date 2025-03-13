def recursive_fibonacci(position):
    if position <= 1:
        return 0
    elif position == 2:
        return 1
    else:
        return recursive_fibonacci(position - 1) + recursive_fibonacci(position - 2)