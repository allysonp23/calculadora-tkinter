import tkinter as tk
from typing import List

# Definindo a classe da calculadora e cetando as configurações para não trabalhar diretamente na factories
class Calculator:
    def __init__(
        self, 
        root: tk.Tk, 
        label: tk.Label, 
        display: tk.Entry, 
        buttons: List[List[tk.Button]]
    ):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons


# Função para iniciar a calculadora visual no tkinter        
    def start(self):
        self._config_buttons()
        self._config_display()
        self.root.mainloop()
        
        
        
# 2 Configurando os botões do display 

# 2.a Bindando C para clear.
        
    def _config_buttons(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text = button['text']
                
                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)
   

    
    def _config_display(self):
        ...
        
    def clear (self, event=None):
        self.display.delete(0, 'end')
        
        