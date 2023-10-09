from multiprocessing import Pool, cpu_count

def factorize_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    results = []
    for number in numbers:
        factors = factorize_number(number)
        results.append(factors)
    return results

def parallel_factorize_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def parallel_factorize(*numbers):
    with Pool(cpu_count()) as pool:
        results = pool.map(parallel_factorize_number, numbers)
    return results

if __name__ == "__main__":
    import time

    start_time_sync = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end_time_sync = time.time()
    print("Synchronous version: {:.4f} ".format(end_time_sync - start_time_sync))

    start_time_parallel = time.time()
    a_parallel, b_parallel, c_parallel, d_parallel = parallel_factorize(128, 255, 99999, 10651060)
    end_time_parallel = time.time()
    print("Parallel version: {:.4f} s".format(end_time_parallel - start_time_parallel))

