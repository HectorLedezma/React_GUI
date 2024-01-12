import tkinter as tk
from itertools import cycle
from PIL import ImageTk, Image
import numpy as np


class LoadingAnimation:
    def __init__(self, master,message):
        
        
        self.master = master
        self.message = message
        

        self.canvas = tk.Canvas(self.master, width=750, height=40)
        self.loading_images = [ImageTk.PhotoImage(Image.open(fp=f"./Images/Loading/f{i}.png")) for i in range(100)]
        self.loading_animation = cycle(self.loading_images)
        self.loading_image = self.canvas.create_image(100, 100, image=next(self.loading_animation))
        
        
        self.end = False
        self.iterator = 0
        #self.master.after(100, self.animate)

    
    def start_animation(self):
        self.canvas.pack()
        self.message.config(text="Cargando...",fg="black")
        self.master.after(40, self.animate)
    
    def animate(self):
        if(not self.end):
            self.canvas.itemconfig(self.loading_image, image=next(self.loading_animation))
            
            #self.message.config(text=str(self.iterator),fg="black")
            #self.iterator += 1
            
            self.master.after(40, self.animate)
        #else:
            

    
    
    def stop_animation(self):
        self.master.after_cancel(self.animate)
        self.end = True
        self.message.config(text="!Listo¡",fg="green")
        
