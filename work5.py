import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("タイピングアプリ")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

str_list = ["昨日は雨", "今日はいい天気"]

label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)


def display_entry_text():
    entry_text = entry1.get()
    current_text = label1.cget("text")
    if entry_text == current_text:
        # 新しいテキストを設定
        new_text = random.choice(str_list)
        # 新しいテキストが現在のテキストと異なることを保証する
        while new_text == current_text:
            new_text = random.choice(str_list)
        label1.config(text=new_text)
        entry1.delete(0, tk.END)  # エントリフィールドをクリア


button = tk.Button(
    window, text="OK", command=display_entry_text, bg=bg_color, fg=fg_color
)
button.pack(pady=10)


random_text = random.choice(str_list)
label1.config(text=random_text)

window.mainloop()
