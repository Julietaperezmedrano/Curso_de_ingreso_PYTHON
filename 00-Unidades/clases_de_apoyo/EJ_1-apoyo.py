import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Perez Medrano
---
Enunciado:

Ingresar el valor del dólar oficial y el valor del dólar blue.
Mostrar la diferencia expresada en porcentaje entre una cotización y otra.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        valor_oficial = float(prompt(title="dolar oficial", prompt="Ingrese el valor del dolar oficial"))
        valor_blue = float(prompt(title="dolar blue", prompt="Ingrese el valor del dolar blue"))

        diferencia_valores = (valor_blue - valor_oficial) / valor_oficial * 100

        mensaje = alert(title="Respuesta", message=f"La diferencia entre el valor oficial y el valor blue es de: {diferencia_valores}%")
        pass
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()