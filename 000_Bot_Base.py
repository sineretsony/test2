import tkinter as tk
import time
import threading

class TimedMessageWindow:
    def __init__(self, message, countdown_seconds):
        self.message = message
        self.countdown = countdown_seconds
        self.root = tk.Tk()
        self.root.title("Внимание")
        self.root.attributes("-alpha", 0.70)  # полупрозрачность
        self.root.attributes("-topmost", True)
        self.root.geometry("400x200")

        self.label = tk.Label(self.root, text=message, font=("Arial", 14), wraplength=380)
        self.label.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="", font=("Arial", 12), fg="red")
        self.timer_label.pack()

        self.button = tk.Button(self.root, text="Выполнено", state="disabled", command=self.on_done)
        self.button.pack(pady=20)

        threading.Thread(target=self.start_timer, daemon=True).start()
        self.root.mainloop()

    def start_timer(self):
        while self.countdown > 0:
            mins, secs = divmod(self.countdown, 60)
            timer_text = f"{mins:02}:{secs:02}"
            self.timer_label.config(text=timer_text)
            time.sleep(1)
            self.countdown -= 1

        self.timer_label.config(text="00:01")
        self.button.config(state="normal")

    def on_done(self):
        print("Пользователь подтвердил выполнение.")
        self.root.destroy()

# Пример использования
TimedMessageWindow("Размер с ТК и макет", 10)
TimedMessageWindow("Шрифты в документе", 10)
TimedMessageWindow("CMYK или нет?", 10)
TimedMessageWindow("Разрешение если растр, нужно 300", 10)

