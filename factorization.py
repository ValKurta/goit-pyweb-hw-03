import time
import multiprocessing as mp


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize_sync(numbers):
    return [factorize(number) for number in numbers]


def factorize_parallel(numbers):
    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    return results


if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    results_sync = factorize_sync(numbers)
    end_time = time.time()
    print("the results from simple func:", results_sync)
    print("the runtime from simple func:", end_time - start_time, "sec")

    start_time = time.time()
    results_parallel = factorize_parallel(numbers)
    end_time = time.time()
    print("the results from parallel func:", results_parallel)
    print("the runtime from parallel func:", end_time - start_time, "sec")
