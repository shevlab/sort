#_*_ coding : utf-8 _*_
'''
У цьому прикладі використовується рекурсивний підхід, де обробка папок вкладається одна в одну. 
Кожен підкаталог обробляється в окремому потоці за допомогою ThreadPoolExecutor, що дозволяє паралельно виконувати обробку папок та файлів. 
Перенесення файлів відбувається за допомогою функції shutil.move, яка також може працювати в окремому потоці або пулі потоків для збільшення швидкості.
'''
import os
import shutil
from concurrent.futures import ThreadPoolExecutor

while True:
    def sort_files(folder_path):
        # Отримуємо список файлів та папок в заданій папці
        files = []
        subfolders = []
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                files.append(item_path)
            else:
                subfolders.append(item_path)
        
        # Сортуємо файли за розширеннями
        for file_path in files:
            _, ext = os.path.splitext(file_path)
            ext = ext[1:]  # Видаляємо крапку з початку розширення
            ext_folder = os.path.join(folder_path, ext)
            os.makedirs(ext_folder, exist_ok=True)  # Створюємо папку за розширенням, якщо не існує
            shutil.move(file_path, ext_folder)  # Переміщуємо файл у відповідну папку за розширенням

        # Обробляємо підкаталоги рекурсивно в окремих потоках
        with ThreadPoolExecutor() as executor:
            executor.map(sort_files, subfolders)
        print('задача Ок !')
    # Виклик функції для обробки папки "Мотлох"
    folder_path = input('Шлях до вашого Мотлоху : ')
    sort_files(folder_path)
