import tkinter as tk
from datetime import datetime

# === НАСТРОЙКИ ===
DURATION_SEC = 180  # время в секундах
DOT_RADIUS = 60  # радиус точки
LOG_FILE = "focus_on_point.log"

click_count = 0


def on_click(event):
    global click_count
    click_count += 1


def finish():
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} | duration={DURATION_SEC}s | clicks={click_count}\n")
    root.destroy()


root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="white")
root.bind("<Escape>", lambda e: root.destroy())
root.bind("<Button-1>", on_click)

canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
x, y = w // 2, h // 2

canvas.create_oval(x - DOT_RADIUS, y - DOT_RADIUS, x + DOT_RADIUS, y + DOT_RADIUS, fill="black", outline="")

root.after(DURATION_SEC * 1000, finish)
root.mainloop()
