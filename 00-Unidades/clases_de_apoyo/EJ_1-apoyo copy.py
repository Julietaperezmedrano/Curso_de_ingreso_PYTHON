import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        cantidad_masculinos = 0

        votantes_ia = 0
        votantes_rvra = 0
        votantes_iot = 0

        total_generos = 0

        while True:
            nombre = prompt("Ingreso", "Ingrese su nombre")

            edad = prompt("Ingreso", "Ingrese su edad")
            edad = int(edad)
            if edad < 18:
                edad = prompt("Error", "Reingrese la edad")

            genero = prompt("Ingreso", "Ingrese su genero")
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = prompt("Error", "Reingrese el genero")

            tecnologia = prompt("Ingreso", "Ingrese la tecnologia")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = prompt("Error", "Reingrese la tecnologia")

            pregunta = question("Pregunta", "Desea continuar?")
            if pregunta == False:
                break

            #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
            #!X 3) - Porcentaje de empleados por cada genero

            match genero:
                case "Masculino":
                    if (tecnologia == "IOT" or tecnologia == "IA") and (edad > 24 and edad < 51):
                        cantidad_masculinos += 1
                        total_generos += 1
                        porcentaje_masculino = porcentaje_masculino * 100 / total_generos
                case "Femenino":
                    total_generos += 1
                case "Otro":
                    total_generos += 1

            alert(message=porcentaje_masculino)
                    

            #!X 2) - Tecnología que mas se votó.
                        
            match tecnologia:
                case "IA":
                    votantes_ia += 1
                case "RV/RA":
                    votantes_rvra += 1
                case "IOT":
                    votantes_iot += 1

            if votantes_ia > votantes_rvra and votantes_ia > votantes_iot:
                mas_votado = votantes_ia
            elif votantes_rvra > votantes_iot:
                mas_votado = votantes_rvra
            else:
                mas_votado = votantes_iot

                    

            

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()