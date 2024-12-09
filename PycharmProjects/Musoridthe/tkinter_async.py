import multiprocessing
import threading
import time
import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()  # Инициализируем базовый класс tk.Tk
        self.title("Naming")  # Устанавливаем заголовок окна
        self.geometry("1100x580")  # Задаём размеры окна

        # Создаём кнопки
        self.create_widgets()

    def create_widgets(self):
        # Кнопка 1
        button1 = tk.Button(self, text="Кнопка 1", command=self.start_button1_process)
        button1.pack(pady=10)  # Размещаем кнопку с отступом

        # Кнопка 2
        button2 = tk.Button(self, text="Кнопка 2", command=self.on_button2_click)
        button2.pack(pady=10)  # Размещаем кнопку с отступом

    def start_button1_process(self):
        """Запуск процесса для кнопки 1"""
        process = threading.Thread(target=self.on_button1_click)
        process.start()

    def on_button1_click(self):
        """Функция, выполняемая в отдельном процессе"""
        time.sleep(2)
        print("Кнопка 1 нажата!")

    def on_button2_click(self):
        """Обработчик для кнопки 2"""
        print("Кнопка 2 нажата!")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
