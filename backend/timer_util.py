import time
from datetime import timedelta


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record end time

        elapsed_time = timedelta(seconds=end_time - start_time)  # Compute elapsed time
        print(f"Execution time of {func.__name__}: {str(elapsed_time)}")
        return result
    return wrapper
