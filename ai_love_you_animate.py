import tkinter as tk
import random
import time

# Buat jendela utama
root = tk.Tk()
root.title("🤖 AI Love You 💕")
root.geometry("400x500")
root.config(bg="pink")

canvas = tk.Canvas(root, width=400, height=500, bg="pink", highlightthickness=0)
canvas.pack()

# Tampilkan pesan utama
canvas.create_text(200, 50, text="🤖 AI Love You 💖", font=("Arial", 24, "bold"), fill="red")

# Fungsi untuk membuat hati
def buat_hati():
    x = random.randint(50, 350)
    y = 480
    ukuran = random.randint(10, 20)
    hati = canvas.create_text(x, y, text="❤️", font=("Arial", ukuran))
    return hati

hati_list = []

# Fungsi animasi
def animasi():
    # Tambahkan hati baru
    if random.random() < 0.2:
        hati_list.append(buat_hati())
    # Gerakkan hati
    for hati in hati_list[:]:
        canvas.move(hati, 0, -3)
        x, y = canvas.coords(hati)
        if y < -20:
            canvas.delete(hati)
            hati_list.remove(hati)
    root.after(50, animasi)

# Jalankan animasi
animasi()

root.mainloop()
