import tkinter as tk
import psutil
import time

class SystemMonitorWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Pop!_OS System Monitor")
        self.root.geometry("300x150")
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#2e2e2e")

        self.cpu_label = tk.Label(root, text="CPU Usage: --%", bg="#2e2e2e", fg="#00ff00", font=("Arial", 12))
        self.cpu_label.pack(pady=5)
        self.mem_label = tk.Label(root, text="Memory Usage: --%", bg="#2e2e2e", fg="#00ff00", font=("Arial", 12))
        self.mem_label.pack(pady=5)

        self.update_info()

    def update_info(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        self.cpu_label.config(text=f"CPU Usage: {cpu_percent:.1f}%")

        memory = psutil.virtual_memory()
        mem_percent = memory.percent
        self.mem_label.config(text=f"Memory Usage: {mem_percent:.1f}%")

        self.root.after(1000, self.update_info)

def main():
    root = tk.Tk()
    app = SystemMonitorWidget(root)
    root.mainloop()

if __name__ == "__main__":
    main()

