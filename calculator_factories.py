import tkinter as tk

def make_root() -> tk.Tk:
    root = tk.Tk() 
    root.title('Calculator')
    root.config(padx=10, pady= 10, background='#fff')
    root.resizable(False, False)
    return root

def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text='Sem conta ainda',
        anchor='e', justify='right', background='#fff'
        )
    