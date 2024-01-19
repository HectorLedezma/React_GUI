import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from shell import Shell
from Gui.Loading import LoadingAnimation
from Gui.Terminal1 import TerminalApp
from threading import Thread
import time
from tqdm import tqdm



class Frame:
    def __init__(self):
        self.ventana = tk.Tk()
        directorio_personal = os.path.expanduser("~")
        self.directorio_documentos = os.path.join(directorio_personal, "Documentos")
        self.mensaje = tk.Label(self.ventana, text="",font=("Helvetica", 20,"bold"))
        #self.load = LoadingAnimation(self.ventana,self.mensaje)
        
    def show(self):
        def obtener_texto():
            texto_ingresado = cuadro_texto.get()
            print(texto_ingresado)
            #etiqueta.config(text="Texto ingresado: " + texto_ingresado)
        
        def funcion():
            print('Cargando.')
            print('cargando..')
            print('cargando...')
            loop = tqdm(total=50000,position=0,leave=False)
            for i in range(50000):
                loop.set_description('Loading...'.format(i))
                loop.update(1)
            loop.close()
            print('Listo')
            #app.stop_animation()
            #for i in range(l):
            #    print(i,end='\r')
            #    time.sleep(1)
            
        
        def noSpace(route):
            print(route)
            indexes = []
            for i in range(len(route)):
                if route[i] == chr(32):
                    indexes.append(i)
                
            charList = list(route)
            iPos = 0
            for pos in indexes:
                charList.insert(pos+iPos,chr(92))
                iPos += 1
            newString = ''.join(charList)
            return newString
        
        def seleccionar_directorio():
            # Construimos la ruta completa al directorio "Documentos"
            texto_ingresado = cuadro_texto.get()
            self.directorio_documentos = filedialog.askdirectory(initialdir=self.directorio_documentos)
            
            comando = "cd "+noSpace(str(self.directorio_documentos))+"\nnpx create-react-app "+texto_ingresado
            #print(comando)
            if validaInput(texto_ingresado) == 0:
                self.mensaje.config(text="Creando proyecto "+texto_ingresado+"\nPor favor espere...",fg='black')
                Shell.exec(comando)
                self.mensaje.config(text="Proyecto "+texto_ingresado+"\ncreado exitodamente",fg='green')
                #self.load.start_animation()
                #print(noSpace(self.directorio_documentos))
                #TerminalApp(self.ventana,comando)
                #
                
                #self.ventana.after(10,funcion)
                #(self.load)
                
                
                #self.load.stop_animation()
                
                #self.ventana.after(0,lambda:funcion(10,self.load))
                
                
                #animation_thread = Thread(target=self.load.start_animation,name="animation")
                #animation_thread.start()
                
                #funcion(10)
                
                #self.load.stop_animation()
                
                #animation_thread.join()
                #
                #
                #print(load.loading_image)
                #Shell.exec(comando)
                #error.config(text="El Proyecto "+texto_ingresado+" fue creado con exito en\n"+str(self.directorio_documentos),fg="green")
                #load.end = True
                #
            elif validaInput(texto_ingresado) == 1:
                self.mensaje.config(text="Error: El nombre no debe contener caracteres en mayusculas",fg="red")
            elif validaInput(texto_ingresado) == 2:
                self.mensaje.config(text="Error: El nombre del proyecto no esta ingresado",fg="red")

        def validaInput(txt):
            ok = 0
            #print('txt:',txt)
            if txt == "" or txt == None:
                ok = 2
            else:
                for i in txt:
                    if ord(i) >= 65 and ord(i) <=90:
                        ok = 1
                        break
            #print('Estado:',ok)
            return ok
        
        self.ventana.title("Nuevo proyecto")
        
        ancho_pantalla = self.ventana.winfo_screenwidth() #método para obtener Ancho
        alto_pantalla = self.ventana.winfo_screenheight() #método para obtener Alto
        # Calcular las coordenadas para centrar la ventana
        ancho_ventana = 900
        alto_ventana = 600
        posicion_x = (ancho_pantalla - ancho_ventana) // 2 
        posicion_y = (alto_pantalla - alto_ventana) // 2

        # Establecer el tamaño y la posición de la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

        imagen = Image.open("Images/ReactLogo2.png")
        nuevo_tamano = (115, 100)  # Especifica el nuevo tamaño deseado
        imagen = imagen.resize(nuevo_tamano)

        imagen_tk = ImageTk.PhotoImage(imagen)#""",width=10,height=10"""
        
        etiqueta = tk.Label(self.ventana,text="logo", image=imagen_tk)
        proyecto = tk.Label(self.ventana,text="¿Como se llamará el proyecto?")
        cuadro_texto = tk.Entry(self.ventana, width=30)
        
        #error = tk.Label(self.ventana, text="",fg="red",font=("Helvetica", 20,"bold"))
        
        boton1 = tk.Button(self.ventana, text="Guardar",command=seleccionar_directorio)
        
        etiqueta.pack(pady=50)
        proyecto.pack()
        cuadro_texto.pack()
        boton1.pack(pady=40)
        self.mensaje.pack()
        
        
        #ventana.geometry("900x600")#+<posición_x>+<posición_y>
        self.ventana.mainloop()
    
    