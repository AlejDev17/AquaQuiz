from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import juego

class Main:
    
    def __init__(self, window):
        self.window = window
        self.prueba= "prueba"
    
    def loadWinMain(self):  

        self.titleLabel = Label(self.window, text="Aqua Quiz")
        self.titleLabel.config(background="#85CCB7", 
                          fg="#3462E5", 
                          padx=250, 
                          pady=30,
                          font=("Cambria", 20))
        self.titleLabel.place(x=0, y=0)
        
        self.btn_jugar = Button(self.window, text="Jugar", command=self.irJuego)
        self.btn_jugar.config(padx=20, pady=20, width=15, font=("Arial", 10), background="#85CCB7")
        self.btn_jugar.place(x=230, y=350)
        
        """self.btn_crear = Button(self.window, text="Crear", command=self.crear)
        self.btn_crear.config(padx=20, pady=20, font=("Arial", 10), background="#85CCB7")
        self.btn_crear.place(x=300, y=350)"""
        
    def hideWinMain(self):
        self.btn_jugar.place(x=1000, y=1000)
        #self.btn_crear.place(x=1000, y=1000)
    
    def showWinMain(self):
        self.btn_jugar.place(x=230, y=350)
        #self.label_imagen1.place(x=150, y=100)
        #self.btn_crear.place(x=300, y=350)
    
    def irJuego(self):
        self.hideWinMain()
        juegoClass = juego.Funciones(self, self.window)
        load = juegoClass.definirValores()
        
    def crear(self):
        pass 

window = Tk()
window.resizable(0,0)
window.geometry("600x500")
#window.config(
    #background = "#BCEEED"
#)

bg = PhotoImage(file = ".\images\preguntas2.png")
  
# Create Canvas
canvas1 = Canvas(window, width = 400,
                 height = 400)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

Main = Main(window)
Main.loadWinMain()

window.mainloop()
