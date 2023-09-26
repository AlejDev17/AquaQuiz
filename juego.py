from tkinter import *
from PIL import Image, ImageTk
import random
import resumen

class Funciones:
    
    def __init__(self, main,  window):
        self.main = main
        self.window = window
        self.interrogante = main.titleLabel
        self.contador = 1
        self.puntos = 0
    
    def definirValores(self):
        self.pregunta1 = ["./images/gotita.png", "Para cuidar el agua debemos:", "Cerrar los caños", "Tomar poca agua", "Regar mucho", "Dejar pasar fugas"]
        self.pregunta2 = ["./images/tierra.png", "Cantidad de agua que hay en el planeta:", "70%", "50%", "100%", "25%"]
        self.pregunta3 = ["./images/desierto.png", "¿Que pasa si el agua se acaba?", "Acaba la vida en la tierra", "Nada", "Nos da sed", "Será mejor"]
        self.pregunta4 = ["./images/agua-contaminada.jpg", "Si el agua se contamina:", "No se puede tomar", "Estaría mejor", "Se toma", "Aumenta su cantidad"]
        self.cargarPantalla()
        self.nuevosValores()
    
    def cargarPantalla(self):
        print("aij")
        
        def al_entrar(bind):
            self.window.config(cursor="hand2")
        def al_salir(bind):
            self.window.config(cursor="arrow")
        
        self.puntosLabel = Label(self.window, text=f"Puntos: {self.puntos}")
        self.puntosLabel.config(background="blue", 
                        fg="white", 
                        font=("Cambria", 20)),

        self.puntosLabel.place(x=0, y=150)
        
        self.label_imagen = Label(self.window)
        self.label_imagen.place(x=150, y=100)
        
        self.rpta_1 = Button(self.window, text="ijsn")
        self.rpta_1.config(
            background="#85CCB7",
            fg = "#3462E5",
            font=("Cambria", 12),
            padx=20,
            width=15
        )
        self.rpta_1.place(x=100, y=350)
        
        self.rpta_1.bind("<Enter>", al_entrar)
        self.rpta_1.bind("<Leave>", al_salir)

        self.rpta_2 = Button(self.window, text="smsd")
        self.rpta_2.config(
            background="#85CCB7",
            fg = "#3462E5",
            font=("Cambria", 12),
            padx=20,
            width=15

        )
        self.rpta_2.place(x=300, y=350)
        self.rpta_2.bind("<Enter>", al_entrar)
        self.rpta_2.bind("<Leave>", al_salir)        

        self.rpta_3 = Button(self.window, text="hoaa")
        self.rpta_3.config(
            background="#85CCB7",
            fg = "#3462E5",
            font=("Cambria", 12),
            padx=20,
            width=15
        )
        self.rpta_3.place(x=100, y=400)
        self.rpta_3.bind("<Enter>", al_entrar)
        self.rpta_3.bind("<Leave>", al_salir)
        
        self.rpta_4 = Button(self.window, text="oa")
        self.rpta_4.config(
            background="#85CCB7",
            fg = "#3462E5",
            font=("Cambria", 12),
            padx=20,
            width=15
        )
        self.rpta_4.place(x=300, y=400)
        self.rpta_4.bind("<Enter>", al_entrar)
        self.rpta_4.bind("<Leave>", al_salir)
        
    def nuevosValores(self):
        if self.contador == 1:
            self.actualizarValores(self.pregunta1)
        if self.contador == 2:
            self.actualizarValores(self.pregunta2)
        if self.contador == 3:
            self.actualizarValores(self.pregunta3)
        if self.contador == 4:
            self.actualizarValores(self.pregunta4)
        elif self.contador > 4:
            #if self.objectR:
                #self.objectR.mostrarPantalla()
            #else:
            print("puntos"+str(self.puntos))
            print("contador" +str(self.contador))
            self.ocultarPantalla()
            self.objectR = resumen.Resumen(self)
            self.objectR.cargarPantalla()                
            
    def actualizarValores(self, pregunta):
        if len(pregunta) == 6:
            imagen = Image.open(pregunta[0])  # Reemplaza "ejemplo.png" con la ruta de tu imagen
            nuevo_tamano = (300, 300)  # Especifica el nuevo tamaño en píxeles (ancho x alto)
            imagen.thumbnail(nuevo_tamano)
            # Convertir la imagen en un formato compatible con tkinter
            imagen_tk = ImageTk.PhotoImage(imagen)

            # Actualizar el Label con la nueva imagen
            self.label_imagen.config(image=imagen_tk)
            self.label_imagen.image = imagen_tk
            
            self.puntosLabel.config(text=f"Puntos: {self.puntos}")
            
            del pregunta[0] 

            #Setear el título
            self.interrogante.config(text=pregunta[0], width=7, anchor=CENTER, justify=CENTER)
            del pregunta[0]
            print(pregunta)
        
        else:
            pass
        
        #Setear respuesta correcta
        respuestaOk = pregunta[0]
        print(respuestaOk)
        
        #Barajear la lista
        print(pregunta)
        respuestasBaraja = random.sample(pregunta, 4)
        print(respuestasBaraja)
        
        #Modificar botones
        
        self.rpta_1.config(
            text=respuestasBaraja[0],
            command=lambda:self.nota(respuestaOk, respuestasBaraja[0]),
        )
        
        self.rpta_2.config(
            text=respuestasBaraja[1],
            command=lambda:self.nota(respuestaOk, respuestasBaraja[1]),
        )
        
        self.rpta_3.config(
            text=respuestasBaraja[2],
            command=lambda:self.nota(respuestaOk, respuestasBaraja[2]),
        )
        
        self.rpta_4.config(
            text=respuestasBaraja[3],
            command=lambda:self.nota(respuestaOk, respuestasBaraja[3]),
        )
        

        
    def nota(self, correcta, seleccion):
        if correcta == seleccion:
            self.puntos += 1
        else:
            self.puntos += -1
        print(self.puntos)
        
        self.contador += 1
        self.nuevosValores()
    
    def ocultarPantalla(self):
        self.label_imagen.place(x=1000, y=1000)
        self.rpta_1.place(x=1000, y=1000)
        self.rpta_2.place(x=1000, y=1000)
        self.rpta_3.place(x=1000, y=1000)
        self.rpta_4.place(x=1000, y=1000)
        self.puntosLabel.place(x=1000, y=1000)
    
    def mostrarPantalla(self):
        self.label_imagen.place(x=150, y=100)
        self.rpta_1.place(x=100, y=350)
        self.rpta_2.place(x=300, y=350)
        self.rpta_3.place(x=100, y=400)
        self.rpta_4.place(x=300, y=400)
        self.puntosLabel.place(x=0, y=150)
        self.contador = 1
        self.nuevosValores()
        