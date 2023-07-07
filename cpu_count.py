import time
from multiprocessing import Pool, cpu_count

def factorize_single(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    start_time = time.time()
    
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize_single, numbers)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return results, execution_time

if __name__ == '__main__':
    try:
        
        # Перевірка результатів та вимірювання часу
        numbers = (128, 255, 99999, 10651060)
        result, execution_time = factorize(*numbers)

        a, b, c, d = result

        assert a == [1, 2, 4, 8, 16, 32, 64, 128]
        assert b == [1, 3, 5, 15, 17, 51, 85, 255]
        assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
        assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
        print('Data (a, b, c, d) % == 0', '(OK)')
        print("Час виконання:", execution_time)
        num_processors = cpu_count()
        print("Кількість процесорів:", num_processors)
        
    except:
        print('!!!!!AssertionError!!!!!') # assert a == [1, 2, 23, 8, 16, 32, 64, 128] Видасть помилку AssertionError
       




