import json
import time
import psutil
import os
import sympy


def sieve_of_eratosthenes(n):
    return list(sympy.primerange(0, n + 1))


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return round(process.memory_info().rss / (1024 * 1024), 2)


def get_cpu_usage():
    return psutil.cpu_percent(interval=None)


def benchmark_primes_py(repetitions, n):
    total_time = 0
    total_memory = 0
    total_cpu = 0

    start_total = time.time()

    for _ in range(repetitions):
        start_memory = get_memory_usage()
        start = time.time()

        cpu_before = get_cpu_usage()
        primes = sieve_of_eratosthenes(n)
        cpu_after = get_cpu_usage()

        end = time.time()
        memory_usage = get_memory_usage() - start_memory

        total_time += (end - start) * 1000
        total_memory += memory_usage
        total_cpu += cpu_after

    # ET (Execution Time)

    end_total = time.time()
    total_exec_time = round((end_total - start_total) * 1000, 2)
    avg_time = round(total_time / repetitions, 2)

    # RAM

    avg_memory = round(total_memory / repetitions, 2)

    # CPU

    avg_cpu = round(total_cpu / repetitions, 2)

    return {
        'total_time': f"Total ET (1000x): {total_exec_time} ms",
        'av_time': f"ET av (1000x): {avg_time} ms",
        'cpu_usage': f"CPU av (1000x): {avg_cpu} %",
        'memory_usage': f"RAM av (1000x): {avg_memory} MB"
    }


def main():
    result = benchmark_primes_py(1000, 10_000)
    response = {
        'type': None,
        'data': result
    }
    print(json.dumps(response))


if __name__ == '__main__':
    main()
