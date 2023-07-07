'''Цей код демонструє використання модуля multiprocessing для створення пула процесів та виконання функції get_value у кожному процесі з використанням методу map.
Основні етапи коду:
import multiprocessing: Імпортуємо модуль multiprocessing, який надає функції та класи для мультипроцесингу.
def get_value(value): Оголошуємо функцію get_value, яка приймає значення value як аргумент і виводить його разом з ім'ям поточного процесу.
if __name__ == '__main__':: Перевіряємо, чи код виконується в головному модулі.
with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
multiprocessing.cpu_count(): Визначаємо кількість доступних процесорів на системі.
multiprocessing.Pool: Створюємо пул процесів, вказуючи кількість процесів, яку потрібно використовувати.
as p: Зберігаємо пул процесів у змінну p.
p.map(get_value, [1,2,3,4,5]): Викликаємо метод map пула процесів p і передаємо йому функцію get_value та список значень [1,2,3,4,5]. Кожен процес у пулі викликатиме функцію get_value зі своїм власним значенням зі списку.
Після запуску коду кожен процес в пулі виконуватиме функцію get_value для відповідного значення зі списку. Результатом будуть виведення значень разом з іменами процесів, що виконують цю функцію.
'''
import multiprocessing

def get_value(value):
    name = multiprocessing.current_process().name
    print(f'[{name}] value: {value}')

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.map(get_value, [1,2,3,4,5])    