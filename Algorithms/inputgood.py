import sys

def main():
    # generator of tuple of integers from the line in sys.stdin
    # each time it's called it returns a tuple of int numbers
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    # below is an example of usage
    n, capacity = next(reader)
    values_and_weights = list(reader)
    assert len(values_and_weights) == n

# next(sys.stdin)