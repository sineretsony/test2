import time
import json
import tkinter as tk
import threading
from datetime import datetime, timedelta

def checker():
    JSON_FILE = r"M:\setup_action_folder\orders.json"

    def load_orders():
        try:
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_orders(updated_order_number, updated_order_data):
        orders = load_orders()
        if updated_order_number in orders:
            orders[updated_order_number].update(updated_order_data)
        else:
            orders[updated_order_number] = updated_order_data
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(orders, f, ensure_ascii=False, indent=4)

    def create_notification(order_number, date, y_offset):
        root = tk.Tk()
        root.title("Notification")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        window_width = 300
        window_height = 150
        x_position = screen_width - window_width - 10
        y_position = screen_height - window_height - y_offset

        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        root.attributes("-topmost", True)
        root.overrideredirect(True)

        label = tk.Label(root, text=f"№: {order_number}\nДата: {date}", font=("Arial", 20))
        label.pack(pady=10)

        def on_done():
            updated_order_data = {"date": date, "status": "processed"}
            save_orders(order_number, updated_order_data)
            root.destroy()

        def on_not_found():
            updated_order_data = {"date": date, "status": "not_tc"}
            save_orders(order_number, updated_order_data)
            root.destroy()

        def auto_close():
            root.after(10000, root.destroy)

        button_done = tk.Button(root, text="Готово", command=on_done, bg="green", fg="white", font=("Arial", 12))
        button_done.pack(side="left", padx=20, pady=10)

        button_not_found = tk.Button(root, text="Немає ТК", command=on_not_found, bg="red", fg="white", font=("Arial", 12))
        button_not_found.pack(side="right", padx=20, pady=10)

        # Запускаем автоматическое закрытие окна через 10 секунд
        auto_close()

        root.mainloop()

    def parse_date(date_str):
        for fmt in ("%d.%m", "%Y-%m-%d"):
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue
        raise ValueError(f"Unknown date format: {date_str}")

    def format_date(date):
        return date.strftime("%d.%m")

    def delete_yesterday_orders():
        orders = load_orders()
        yesterday = (datetime.now() - timedelta(days=1)).date()

        to_delete = [order_number for order_number, details in orders.items()
                     if parse_date(details["date"]) == yesterday]

        for order_number in to_delete:
            del orders[order_number]

        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(orders, f, ensure_ascii=False, indent=4)

    def check_orders():
        while True:
            delete_yesterday_orders()

            orders = load_orders()
            for order_number, details in orders.items():
                if (details["status"] == "new" or details["status"] == "not_tc") and details.get("file") == 'only_file':
                    create_notification(order_number, details["date"], 100)

            time.sleep(1)

    check_orders()

if __name__ == "__main__":
    while True:
        try:
            checker()
        except Exception as f:
            print(f'reload...{f}')
            time.sleep(10)  # Ожидание перед повторной попыткой
