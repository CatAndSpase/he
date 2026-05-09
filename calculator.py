import tkinter as tk

BG        = "#1e1e2e"
BG_DISP   = "#11111b"
FG        = "#cdd6f4"
FG_SUB    = "#6c7086"
BTN_NUM   = "#313244"
BTN_OP    = "#45475a"
BTN_EQ    = "#cba6f7"
BTN_CLEAR = "#f38ba8"
BTN_HOVER = "#585b70"
FONT_DISP = ("SF Pro Display", 36, "bold")
FONT_SUB  = ("SF Pro Display", 16)
FONT_BTN  = ("SF Pro Display", 20, "bold")


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор")
        self.resizable(False, False)
        self.configure(bg=BG)

        self._expr = ""
        self._result_shown = False

        self._build_display()
        self._build_buttons()
        self.bind("<Key>", self._on_key)

    def _build_display(self):
        frame = tk.Frame(self, bg=BG_DISP, padx=20, pady=16)
        frame.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=(12, 6))

        self._sub_var = tk.StringVar(value="")
        tk.Label(frame, textvariable=self._sub_var, bg=BG_DISP, fg=FG_SUB,
                 font=FONT_SUB, anchor="e").pack(fill="x")

        self._disp_var = tk.StringVar(value="0")
        tk.Label(frame, textvariable=self._disp_var, bg=BG_DISP, fg=FG,
                 font=FONT_DISP, anchor="e").pack(fill="x")

    def _btn(self, parent, text, row, col, cmd, color=BTN_NUM, colspan=1):
        btn = tk.Button(
            parent, text=text, command=cmd,
            bg=color, fg=FG, activebackground=BTN_HOVER, activeforeground=FG,
            font=FONT_BTN, relief="flat", bd=0, cursor="hand2",
            width=4 if colspan == 1 else 9,
        )
        btn.grid(row=row, column=col, columnspan=colspan,
                 padx=5, pady=5, ipady=14, sticky="nsew")
        btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))

    def _build_buttons(self):
        frame = tk.Frame(self, bg=BG)
        frame.grid(row=1, column=0, padx=12, pady=(0, 12))

        layout = [
            [("C", BTN_CLEAR, self._clear),   ("⌫", BTN_OP, self._back),
             ("%", BTN_OP, lambda: self._append("%")), ("÷", BTN_OP, lambda: self._append("/"))],
            [("7", BTN_NUM, lambda: self._append("7")), ("8", BTN_NUM, lambda: self._append("8")),
             ("9", BTN_NUM, lambda: self._append("9")), ("×", BTN_OP, lambda: self._append("*"))],
            [("4", BTN_NUM, lambda: self._append("4")), ("5", BTN_NUM, lambda: self._append("5")),
             ("6", BTN_NUM, lambda: self._append("6")), ("−", BTN_OP, lambda: self._append("-"))],
            [("1", BTN_NUM, lambda: self._append("1")), ("2", BTN_NUM, lambda: self._append("2")),
             ("3", BTN_NUM, lambda: self._append("3")), ("+", BTN_OP, lambda: self._append("+"))],
        ]

        for r, row in enumerate(layout):
            for c, (text, color, cmd) in enumerate(row):
                self._btn(frame, text, r, c, cmd, color)

        self._btn(frame, "0",  4, 0, lambda: self._append("0"), BTN_NUM, colspan=2)
        self._btn(frame, ".",  4, 2, lambda: self._append("."), BTN_NUM)
        self._btn(frame, "=",  4, 3, self._evaluate, BTN_EQ)

    def _append(self, char):
        if self._result_shown and char not in "+-*/":
            self._expr = ""
        self._result_shown = False

        ops = {"/": "÷", "*": "×", "-": "−"}
        if char in ops:
            if self._expr and self._expr[-1] in "+-*/":
                self._expr = self._expr[:-1]
            self._expr += char
        elif char == "%" and self._expr:
            try:
                self._expr = str(eval(self._expr) / 100)
            except Exception:
                pass
        else:
            self._expr += char

        display = self._expr.replace("/", "÷").replace("*", "×").replace("-", "−")
        self._disp_var.set(display or "0")

    def _evaluate(self):
        if not self._expr:
            return
        self._sub_var.set(self._expr.replace("/", "÷").replace("*", "×").replace("-", "−") + " =")
        try:
            result = eval(self._expr)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self._disp_var.set(f"{result:,}".replace(",", " "))
            self._expr = str(result)
        except ZeroDivisionError:
            self._disp_var.set("Деление на 0")
            self._expr = ""
        except Exception:
            self._disp_var.set("Ошибка")
            self._expr = ""
        self._result_shown = True

    def _clear(self):
        self._expr = ""
        self._result_shown = False
        self._disp_var.set("0")
        self._sub_var.set("")

    def _back(self):
        if self._result_shown:
            self._clear()
            return
        self._expr = self._expr[:-1]
        display = self._expr.replace("/", "÷").replace("*", "×").replace("-", "−")
        self._disp_var.set(display or "0")

    def _on_key(self, event):
        key = event.char
        if key in "0123456789.+-*/":
            self._append(key)
        elif key in ("\r", "="):
            self._evaluate()
        elif event.keysym == "BackSpace":
            self._back()
        elif event.keysym == "Escape":
            self._clear()


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
