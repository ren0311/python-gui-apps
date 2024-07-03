import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("マルバツゲ=ム")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

label1 = tk.Label(window, text="どこを◯×にしますか？", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ゲームの変数
current_player = "◯"
buttons = [[None for _ in range(3)] for _ in range(3)]


# 勝者や引き分けをチェックする関数
def check_winner():
    for i in range(3):
        # 行と列をチェック
        if (
            buttons[i][0]["text"]
            == buttons[i][1]["text"]
            == buttons[i][2]["text"]
            != ""
        ):
            return buttons[i][0]["text"]
        if (
            buttons[0][i]["text"]
            == buttons[1][i]["text"]
            == buttons[2][i]["text"]
            != ""
        ):
            return buttons[0][i]["text"]

    # 斜めをチェック
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]

    # 引き分けをチェック
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return None
    return "引き分け"


# ボタンクリックの処理関数
def on_button_click(x, y):
    global current_player
    if buttons[x][y]["text"] == "" and current_player == "◯":
        buttons[x][y]["text"] = current_player
        winner = check_winner()
        if winner:
            if winner == "引き分け":
                label1.config(text="引き分けです！")
            else:
                label1.config(text=f"{winner} の勝ち！")
            for row in buttons:
                for button in row:
                    button.config(state="disabled")
        else:
            current_player = "×"
            label1.config(text=f"次は {current_player} の番です")
            computer_move()


# コンピュータの動き
def computer_move():
    global current_player
    empty_spaces = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]["text"] == ""]
    if empty_spaces:
        x, y = random.choice(empty_spaces)
        buttons[x][y]["text"] = "×"
        winner = check_winner()
        if winner:
            if winner == "引き分け":
                label1.config(text="引き分けです！")
            else:
                label1.config(text=f"{winner} の勝ち！")
            for row in buttons:
                for button in row:
                    button.config(state="disabled")
        else:
            current_player = "◯"
            label1.config(text=f"次は {current_player} の番です")


# ゲームをリセットする関数
def reset_game():
    global current_player
    current_player = "◯"
    label1.config(text="どこを◯×にしますか？")
    for row in buttons:
        for button in row:
            button.config(text="", state="normal")


# 3x3のボタンを作成
frame = tk.Frame(window, bg=bg_color)
frame.pack()
for i in range(3):
    for j in range(3):
        button = tk.Button(
            frame,
            text="",
            font=("Arial", 24),
            width=5,
            height=2,
            command=lambda x=i, y=j: on_button_click(x, y),
        )
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = button

# リセットボタンを追加
reset_button = tk.Button(
    window, text="リセット", command=reset_game, bg=bg_color, fg=fg_color
)
reset_button.pack(pady=20)

# お約束のコード
window.mainloop()
# お約束のコード
