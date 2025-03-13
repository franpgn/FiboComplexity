import time

from fibonacci.Fib_I import interactive_fibonacci
from fibonacci.Fib_R import recursive_fibonacci

def recursive_fibonacci_performance(max_position):
    ## Compare the performance of the recursive_fibonacci function
    for i in range(1, max_position+1, 1):
        start_time = time.time()

        value = recursive_fibonacci(i)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f'Fibonacci value at position {i}: {value}')
        print(f'Elapsed time: {elapsed_time} seconds')

def interactive_fibonacci_performance(max_position):
    ## Compare the performance of the interactive_fibonacci function
    for i in range(1, max_position+1, 1):
        start_time = time.time()

        value = interactive_fibonacci(i)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f'Fibonacci value at position {i}: {value}')
        print(f'Elapsed time: {elapsed_time} seconds')

if __name__ == '__main__':
    max_position = 100
    #recursive_fibonacci_performance(max_position)
    interactive_fibonacci_performance(max_position)