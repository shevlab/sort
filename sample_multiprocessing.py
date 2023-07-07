from multiprocessing import Pool, cpu_count

def process_data(data):
    # обробка даних
    pass
if __name__ == '__main__':
    num_processes = cpu_count()
    data = [...]  # дані для обробки

    with Pool(num_processes) as pool:
        pool.map(process_data, data)
