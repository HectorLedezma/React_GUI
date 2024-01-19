import tkinter as tk
from subprocess import Popen, PIPE, STDOUT
from shell import Shell

class TerminalApp:
    def __init__(self, master, command):
        self.command = command
        self.master = master
        self.master.title("Terminal")
        self.Shell = Shell
        # Widget de salida para la terminal
        self.output_text = tk.Text(self.master, wrap='word', height=20, width=100,bg='black',fg='white')
        self.output_text.pack(padx=10, pady=10)
        self.execute_command()

    def execute_command(self, event=None):
        # Obtener el comando desde la entrada
        #print(f'ejecutando comando {self.command}')
        # Ejecutar el comando y obtener la salida
        output, _ = self.Shell.exec(self.command)

        # Mostrar la salida en el widget de texto
        self.output_text.insert(output.decode('utf-8'))
        self.output_text.insert(tk.END, '\n')
"""
if __name__ == "__main__":
    root = tk.Tk()
    app = TerminalApp(root,'ls')
    root.mainloop()
"""