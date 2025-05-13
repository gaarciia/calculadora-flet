import tkinter as tk

def on_click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

root = tk.Tk()
root.title("Calculadora")

# configurações da janela principal
root.geometry("400x600")
root.config(bg="#3a3a3a")

# tela de entrada
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#2f2f2f", fg="#ffffff")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# estilo dos botões
button_style = {
    'width': 5,
    'height': 2,
    'font': ("Arial", 18),
    'bd': 2,
    'relief': 'solid'
}

# botões
buttons = [
    ('C', 1, 0), ('%', 1, 1), ('/', 1, 2), ('*', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('+', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('=', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('(', 5, 2), (')', 5, 3)
]

# botões na interface
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, **button_style, command=lambda text=text: on_click(text) if text != "=" else calculate())
    button.grid(row=row, column=col, padx=10, pady=10)

# botão "Limpar"
clear_button = tk.Button(root, text="C", **button_style, command=clear, bg="#ff6347", fg="#ffffff")
clear_button.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
