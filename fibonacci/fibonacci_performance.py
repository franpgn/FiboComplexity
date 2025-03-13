import time
import csv
from fibonacci.Fib_I import interactive_fibonacci
from fibonacci.Fib_R import recursive_fibonacci

def recursive_fibonacci_performance(max_position):
    ## Compare the performance of the recursive_fibonacci function
    data = []
    for i in range(1, max_position + 1):
        start_time = time.time()

        value = recursive_fibonacci(i)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f'Fibonacci value at position {i}: {value}')
        print(f'Elapsed time: {elapsed_time:.2f} seconds')

        data.append([i, value, elapsed_time])  # Collect data

    # Export to CSV
    export_to_csv(data, "recursive_fibonacci_performance.csv")

def interactive_fibonacci_performance(max_position):
    ## Compare the performance of the interactive_fibonacci function
    data = []
    for i in range(1, max_position + 1):
        start_time = time.time()

        value = interactive_fibonacci(i)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f'Fibonacci value at position {i}: {value}')
        print(f'Elapsed time: {elapsed_time:.2f} seconds')

        data.append([i, value, elapsed_time])  # Collect data

    # Export to CSV
    export_to_csv(data, "interactive_fibonacci_performance.csv")

def export_to_csv(data, filename):
    """ Helper function to export data to CSV """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Elemento na série", "Valor do elemento", "Tempo de cálculo (s)"])
        writer.writerows(data)

if __name__ == '__main__':
    max_position = 100
    #recursive_fibonacci_performance(max_position)
    interactive_fibonacci_performance(max_position)
