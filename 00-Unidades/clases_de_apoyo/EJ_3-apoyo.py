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

La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

COMETA: 
AB = Diámetro mayor
DC = diámetro menor
BD y BC = lados menores
AD y AC = lados mayores

Todos los datos se ingresan por prompt. Pueden usar el mismo html del ejercicio 01 de E/S

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.

COMETA BICOLOR
Ahora necesitamos saber cuánto papel de cada color necesitamos. Las entradas son las mismas.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        AB = prompt(title="ingreso AB", prompt="Ingrese el diámetro AB (en cm)")
        AB = float(AB)

        DC = prompt(title="ingreso DC", prompt="Ingrese el diámetro DC (en cm)")
        DC = float(DC)

        lados_menores = prompt(title="ingreso lados menores", prompt="Ingrese los lados menores (BD Y BC) en cm")
        lados_menores = float(lados_menores)

        lados_mayores = prompt(title="ingreso lados mayores", prompt="Ingrese los lados mayores (AD Y AC) en cm")
        lados_mayores = float(lados_mayores)

        perimetro = lados_menores + lados_mayores
        varillas = perimetro / 100

        area_rectangulo = lados_menores * lados_mayores
        area_triangulo = (AB * DC) / 2
        area_cuerpo = area_rectangulo - area_triangulo
        area_total = area_cuerpo * (10 / 9)  
        papel_cuerpo = area_total / 10000
        papel_cuerpo_prim = papel_cuerpo * 10

        alert(message=f"Varillas necesarias para 10 cometas: {papel_cuerpo_prim}")

        pass
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()