import tkinter as tk
import sys

class TextRedirector:
    def __init__(self, widget, tag):
        self.widget = widget
        self.tag = tag

    def write(self, str_):
        self.widget.configure(state="normal")
        self.widget.insert("end", str_, (self.tag,))
        self.widget.configure(state="disabled")

    def flush(self):
        pass


class TerminalApp:
    def __init__(self, master,shell,command):
        self.master = master
        self.master.title("Terminal")

        # Widget de salida para la terminal
        self.output_text = tk.Text(self.master, wrap='word', height=20, width=100,bg='black',fg='white')
        self.output_text.pack(padx=10, pady=10)

        # Redirigir sys.stdout al widget de texto
        sys.stdout = TextRedirector(self.output_text, "stdout")
        shell.exec(command)
        # Ejemplo: Imprimir algo en la terminal
        
"""
if __name__ == "__main__":
    root = tk.Tk()
    app = TerminalApp(root)
    print("¡Hola desde el programa!")
    root.mainloop()
"""