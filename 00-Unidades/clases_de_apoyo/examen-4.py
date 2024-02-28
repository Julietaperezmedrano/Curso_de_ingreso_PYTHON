import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:
Nombre
-Importe ganado (mayor o igual $1000)
-Género (“Femenino”, “Masculino”, “Otro”)
-Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:
A) Nombre y género de la persona que más ganó. --
B) Promedio de dinero ganado en Ruleta. --
C) Porcentaje de personas que jugaron en el Tragamonedas. --
D) Cuál es el juego menos elegido por los ganadores. --
E) Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000 -- 
F) Porcentaje de dinero en función de cada juego. --
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
            mas_ganador = 0
            nombre_mas_ganador = ""
            genero_mas_ganador = ""
            bandera = True

            acumulador_ruleta = 0
            contador_ruleta = 0

            total_personas = 0
            personas_tragamonedas = 0
            personas_poker = 0

            contador_no_poker = 0
            acumulador_no_poker = 0

            dinero_ruleta = 0
            dinero_poker = 0
            dinero_tragamonedas = 0
            dinero_total = 0


            while True:
                nombre = prompt("ingreso", "ingrese su nombre")

                importe_ganado = prompt("ingreso", "ingrese el importe ganado")
                importe_ganado = float(importe_ganado)
                while importe_ganado < 1000:
                    importe_ganado = prompt("Error", "Reingrese el importe ganado")
                    importe_ganado = float(importe_ganado)

                genero = prompt("ingreso", "ingrese su genero(Femenino, Masculino u Otro)")
                while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                    genero = prompt("Error", "Reingrese un genero válido")

                juego = prompt("Ingreso", "Ingrese el juego ganador")
                while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                    juego = prompt("Error", "Reingrese el juego")

                if importe_ganado > mas_ganador or bandera == True:
                    mas_ganador = importe_ganado
                    nombre_mas_ganador = nombre
                    genero_mas_ganador = genero
                    bandera = False

                match juego:
                    case "Ruleta":
                        acumulador_ruleta += importe_ganado
                        contador_ruleta += 1
                        dinero_ruleta += importe_ganado
                    case "Poker":
                        personas_poker += 1
                        dinero_poker += importe_ganado
                    case "Tragamonedas":
                        personas_tragamonedas += 1
                        dinero_tragamonedas += importe_ganado

                if contador_ruleta < personas_poker and contador_ruleta < personas_tragamonedas:
                    menos_elegido = "Ruleta"
                elif personas_poker < personas_tragamonedas:
                    menos_elegido = "Poker"
                else:
                    menos_elegido = "Tragamonedas"

                if (not juego == "Poker" )and importe_ganado > 15000:
                    acumulador_no_poker += importe_ganado
                    contador_no_poker += 1

                total_personas += 1
                dinero_total += importe_ganado

                pregunta = question(message="Desea continuar?")
                if pregunta == False:
                    break

            promedio_ruleta = acumulador_ruleta / contador_ruleta

            porcentaje_tragamonedas = personas_tragamonedas * 100 / total_personas


            promedio_importe_no_poker = acumulador_no_poker / contador_no_poker

            porcentaje_ruleta = dinero_ruleta * 100 / dinero_total
            porcentaje_poker = dinero_poker * 100 / dinero_total
            porcentaje_tragamonedas_dinero = dinero_tragamonedas * 100 / dinero_total

            alert(message=f"El que más ganó fue {nombre_mas_ganador} de genero {genero_mas_ganador} con ganancias de {mas_ganador}")
            alert(message=f"El promedio de dinero ganado en la ruleta fue de {promedio_ruleta}")
            alert(message=f"El porcentaje de personas que jugaron en el Tragamonedas fue de {porcentaje_tragamonedas}%")
            alert(message=f"El juego menos elegido fue el: {menos_elegido}")
            alert(message=f"El promedio de importe de personas que no jugaron poker y su importe es mayor a 15000 es de: {promedio_importe_no_poker}")
            alert(message=f"Porcentajes\n RULETA: {porcentaje_ruleta}%\n POKER: {porcentaje_poker}%\n TRAGAMONEDAS: {porcentaje_tragamonedas_dinero}%")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()