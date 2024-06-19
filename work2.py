import tkinter as tk

window = tk.Tk()
window.title("西暦 / 和暦変換アプリ")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)


def date():
    num = int(entry1.get())
    if num >= 1868 and num <= 1911:
        if ((num - 1867) == 1):
            label1.config(text=f"西暦{num}年は明治元年")
        else:
            label1.config(text=f"西暦{num}年は明治{num - 1867}年")
    elif num >= 1912 and num <= 1925:
        if ((num - 1911) == 1):
            label1.config(text=f"西暦{num}年は大正元年")
        else:
            label1.config(text=f"西暦{num}年は大正{num - 1911}年")
    elif num >= 1926 and num <= 1988:
        if ((num - 1925) == 1):
            label1.config(text=f"西暦{num}年は昭和元年")
        else:
            label1.config(text=f"西暦{num}年は昭和{num - 1925}年")
    elif num >= 1989 and num <= 2018:
        if ((num - 1988) == 1):
            label1.config(text=f"西暦{num}年は平成元年")
        else:
            label1.config(text=f"西暦{num}年は平成{num - 1988}年")
    elif num >= 2019 and num <= 2050:
        if ((num - 2018) == 1):
            label1.config(text=f"西暦{num}年は令和元年")
        else:
            label1.config(text=f"西暦{num}年は令和{num - 2018}年")
    else:
        label1.config(text=f"西暦{num}年は対応していません。")

# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="変換", command=date)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)


window.mainloop()
