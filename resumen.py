from tkinter import *

class Resumen:
    
    def __init__(self, juegoClass):
        self.juego = juegoClass
        self.window = juegoClass.window
        self.puntos = juegoClass.puntos
        self.title = juegoClass.interrogante
    
    def reintentar(self):
        print("reintentando..")
        self.ocultarPantalla()
        self.juego.mostrarPantalla()
        
    def regresar_inicio(self):
        print("regresando")
        self.ocultarPantalla()
        self.juego.main.showWinMain()
        
    def salir(self):
        self.window.destroy()
    
    def ocultarPantalla(self):
        self.label_puntos.place(x=1000, y=1000) #ocultaer
        #self.btn_again.place(x=1000, y=1000)
        self.btn_inicio.place(x=1000, y=1000)
        self.btn_salir.place(x=1000, y=1000)
    
    def mostrarPantalla(self):
        self.label_puntos.place(x=250, y=150) #ocultaer
        #self.btn_again.place(x=100, y=300)
        self.btn_inicio.place(x=250, y=300)
        self.btn_salir.place(x=400, y=300)    
    
    def cargarPantalla(self):
        self.title.config(text="Resumen")
        
        self.label_puntos = Label(self.window, text=f"Puntaje:\n {self.puntos}")
        self.label_puntos.config(
            font=("Cambria", 25),
        )
        self.label_puntos.place(x=250, y=150)
        
        def al_entrar(bind):
            self.window.config(cursor="hand2")
        def al_salir(bind):
            self.window.config(cursor="arrow")
        
        """
        self.btn_again = Button(self.window, text="Reintentar")
        self.btn_again.config(
            background="#85CCB7",
            fg = "#3462E5",
            font=("Cambria", 12),
            width=10,
            height=2,
            command=lambda:self.reintentar()
        )
        self.btn_again.place(x=100, y=300)
        
        self.btn_again.bind("<Enter>", al_entrar)
        self.btn_again.bind("<Leave>", al_salir)
        """

        self.btn_inicio = Button(self.window, text="Inicio")
        self.btn_inicio.config(
            background="#85CCB7",
            fg = "#3462E5",
            font=("Cambria", 12),
            width=10,
            height=2,
            command=lambda:self.regresar_inicio()
        )
        self.btn_inicio.place(x=100, y=300)
        self.btn_inicio.bind("<Enter>", al_entrar)
        self.btn_inicio.bind("<Leave>", al_salir)        
        
        self.btn_salir = Button(self.window, text="Salir")
        self.btn_salir.config(
            background="#85CCB7",
            fg = "#3462E5",
            font=("Cambria", 12),
            width=10,
            height=2,
            command=lambda:self.salir()
        )
        self.btn_salir.place(x=400, y=300)
        self.btn_salir.bind("<Enter>", al_entrar)
        self.btn_salir.bind("<Leave>", al_salir)