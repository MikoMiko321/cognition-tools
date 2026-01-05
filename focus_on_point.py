import tkinter as tk

# === НАСТРОЙКИ ===
DURATION_SEC = 180  # время в секундах
DOT_RADIUS = 60  # радиус точки

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="white")
root.bind("<Escape>", lambda e: root.destroy())

canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
x, y = w // 2, h // 2

canvas.create_oval(x - DOT_RADIUS, y - DOT_RADIUS, x + DOT_RADIUS, y + DOT_RADIUS, fill="black", outline="")

root.after(DURATION_SEC * 1000, root.destroy)
root.mainloop()
