import time
import tkinter as tk
import winsound

class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Countdown Timer")
        self.root.geometry("400x300")
        self.root.config(bg="#2b2b2b")

        self.hours = tk.StringVar()
        self.minutes = tk.StringVar()
        self.seconds = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Countdown Timer", font=("Arial", 24), bg="#2b2b2b", fg="#ffffff").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        tk.Label(self.root, text="Hours:", font=("Arial", 16), bg="#2b2b2b", fg="#ffffff").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.hours, font=("Arial", 16), width=5).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Minutes:", font=("Arial", 16), bg="#2b2b2b", fg="#ffffff").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.minutes, font=("Arial", 16), width=5).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Seconds:", font=("Arial", 16), bg="#2b2b2b", fg="#ffffff").grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.seconds, font=("Arial", 16), width=5).grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Start", command=self.start_timer, font=("Arial", 16), bg="#4CAF50", fg="#ffffff", width=10).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.time_label = tk.Label(self.root, text="", font=("Arial", 48), bg="#2b2b2b", fg="#ffffff")
        self.time_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def start_timer(self):
        try:
            hours = int(self.hours.get())
            minutes = int(self.minutes.get())
            seconds = int(self.seconds.get())
            total_seconds = hours * 3600 + minutes * 60 + seconds
            self.countdown(total_seconds)
        except ValueError:
            self.time_label.config(text="Invalid input")

    def countdown(self, total_seconds):
        while total_seconds > 0:
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.root.update()
            time.sleep(1)
            total_seconds -= 1
        self.time_label.config(text="Time's up!")
        winsound.Beep(2500, 1000)  # 2500 Hz frequency, 1000 ms duration

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    countdown_timer = CountdownTimer()
    countdown_timer.run()