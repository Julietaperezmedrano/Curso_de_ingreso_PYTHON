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

para saber el costo de un viaje necesitamos el siguiente algoritmo,
sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMPT
los datos a solicitar de dos personas son,
nombre, edad y peso
se pide  armar el siguiente mensaje
"hola german y marina , sus pesos son 80 kilos y 60 kilos respectivamente
, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos  

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        kilo_por_pasajero = 1000

        nombre = prompt(title="nombre", prompt="Ingrese su nombre")
        edad = int(prompt(title="edad", prompt="Ingrese su edad"))
        peso = float(prompt(title="peso", prompt="Ingrese su peso"))

        nombre_secundario = prompt(title="nombre", prompt="Ingrese su nombre")
        edad_secundaria = int(prompt(title="edad", prompt="Ingrese su edad"))
        peso_secundario = float(prompt(title="peso", prompt="Ingrese su peso"))

        total_peso = peso + peso_secundario
        promedio_edad = (edad + edad_secundaria) / 2

        valor_viaje = total_peso * kilo_por_pasajero

        mensaje = alert(message=f"Hola {nombre} y {nombre_secundario}, sus pesos son {peso} y {peso_secundario} respectivamente, sumados da {total_peso} kilos, el promedio de edad es {promedio_edad} y su viaje vale {valor_viaje} pesos")
        pass
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()