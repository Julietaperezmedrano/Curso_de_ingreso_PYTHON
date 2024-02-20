import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Perez Medrano
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre,
la edad (mayor 25) 
y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        mayor_votos = 0
        nombre_mayor_votos = ""
        menor_votos = 100
        nombre_menor_votos = 0
        edad_menor_votos = 0
        edades = 0
        cantidades_votos = 0
        cantidad_candidatos = 0
        
        while True:
            nombre = prompt("Ingreso", "Ingrese su nombre")
            if nombre == None:
                break

            edad = prompt("Ingreso", "Ingrese su edad")
            edad = int(edad)
            while edad < 25:
                edad = int(prompt("Error", "Ingrese una edad válida"))

            cantidad_votos = prompt("Ingreso", "Ingrese la cantidad de votos")
            cantidad_votos = int(cantidad_votos)
            while cantidad_votos < 0:
                cantidad_votos = int(prompt("Error", "Ingrese una cantidad de votos válida"))

            if cantidad_votos > mayor_votos:
                mayor_votos = cantidad_votos
                nombre_mayor_votos = nombre

            if cantidad_votos < menor_votos:
                menor_votos = cantidad_votos
                nombre_menor_votos = nombre
                edad_menor_votos = edad

            edades += edad
            cantidades_votos += cantidad_votos
            cantidad_candidatos += 1

        promedio = edades / cantidad_candidatos

        alert(message=f"El candidato con más votos es {nombre_mayor_votos}\n con una cantidad total de {mayor_votos} votos")
        alert(message=f"El nombre del candidato con menos votos es: {nombre_menor_votos}\n Su edad es {edad_menor_votos} y la cantidad de votos fue {menor_votos}")
        alert(message=f"El promedio de las edades de los candidatos fue de {promedio}")
        alert(message=f"El total de votos emitidos fue de {cantidades_votos}")



            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
