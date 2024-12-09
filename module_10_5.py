from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8', errors='ignore') as f:
        line = f.readline()
        while line:
            all_data.append(line)
            line = f.readline()
    # Возвращать список необязательно, но можно
    return all_data

if __name__ == '__main__':
    # Замените 'file {number}.txt' на реальные имена файлов, если они отличаются
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start = datetime.now()
    for name in filenames:
        read_info(name)
    end = datetime.now()
    print(end - start, "(линейный)")

    # Многопроцессный вызов
    # Закомментируйте предыдущий блок кода или этот, чтобы запускать их по отдельности
    start = datetime.now()
    with Pool() as pool:
        # map вернёт результат, но нам в принципе не обязательно его использовать
        results = pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start, "(многопроцессный)")