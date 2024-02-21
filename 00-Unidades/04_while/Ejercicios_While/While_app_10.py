import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’,
 solicitar mediante prompt todos los números que el usuario quiera 
 hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_negativos = 0
        cantidad_positivos = 0

        suma_positivos = 0
        cantidad_negativos = 0

        cantidad_ceros = 0
        
        while True:
            numero = prompt("Ingreso", "Ingrese un numero")

            if numero == None:
                break

            numero = float(numero)

            if numero < 0:
                suma_negativos += numero
                cantidad_negativos += 1
            elif numero > 0:
                suma_positivos += numero
                cantidad_positivos += 1
            else:
                cantidad_ceros += 1
        
        diferencia = cantidad_positivos - cantidad_negativos

        alert(message=f"La suma acumulada de los negativos es: {suma_negativos}\n La suma acumulada de los positivos es {suma_positivos}\n La cantidad de numeros positivos ingresados es {cantidad_positivos}\n La cantidad de numeros negativos ingresados es {cantidad_negativos}\n La cantidad de ceros es: {cantidad_ceros} \n La diferencia entre positivos y negativos es de {diferencia}")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
