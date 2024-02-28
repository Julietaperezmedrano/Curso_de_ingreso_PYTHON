import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Simulacro Turno Mañana

Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.

Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:

Nombre del votante

Edad del votante (debe ser mayor a 13)

Género del votante (Masculino, Femenino, Otro)

El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:
Simulacro Turno Mañana

Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.

Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:

Nombre del votante

Edad del votante (debe ser mayor a 13)

Género del votante (Masculino, Femenino, Otro)

El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:

El promedio de edad de las votantes de género Femenino 

Del votante más viejo, su nombre.

Nombre del votante más joven qué votó a Gianni.

Nombre de cada participante y porcentaje de los votos qué recibió.

El nombre del participante que debe dejar la casa (El que tiene más votos)

Del votante más viejo, su nombre.

Nombre del votante más joven qué votó a Gianni.

Nombre de cada participante y porcentaje de los votos qué recibió.

El nombre del participante que debe dejar la casa (El que tiene más votos)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad_femenino = 0
        contador_edad_femenino = 0

        edad_mas_viejo = 0
        nombre_mas_viejo = ""

        joven_gianni = 1000
        nombre_joven_gianni = ""

        votantes_general = 0
        votantes_esteban = 0
        votantes_gianni = 0
        votantes_giovanni = 0
        
        while True:
            nombre = prompt("Ingreso", "Ingrese su nombre")

            edad = prompt("Ingreso", "Ingrese su edad")
            edad = int(edad)
            if edad < 13:
                edad = prompt("Error", "Su edad debe ser mayor a 13 años")
                edad = int(edad)                  

            genero = prompt("Ingreso", "Ingrese su genero")
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = prompt("Error", "Reingrese el genero")

            participante = prompt("Ingreso", "Ingrese el nombre del participante")
            while participante != "Giovanni" and participante != "Gianni" and participante != "Esteban":
                if participante == "Matias" or participante == "Renato":
                    alert(message="No se encuentra en placa")
                    participante = prompt("Error", "Reingrese el participante")
                else: 
                    participante = prompt("Error", "Reingrese el participante")


            #Del votante más viejo, su nombre.

            if edad > edad_mas_viejo:
                edad_mas_viejo = edad
                nombre_mas_viejo = nombre

                        
            if genero == "Femenino":
                edad_femenino += edad
                contador_edad_femenino += 1


            #Nombre del votante más joven qué votó a Gianni.
            if participante == "Gianni":
                if edad < joven_gianni:
                    joven_gianni = edad
                    nombre_joven_gianni = nombre

            
            #Nombre de cada participante y porcentaje de los votos qué recibió.
            match participante:
                case "Esteban":
                    votantes_esteban += 1
                case "Gianni":
                    votantes_gianni += 1
                case "Giovanni":
                    votantes_giovanni += 1
                    


            votantes_general += 1

            pregunta = question("pregunta", "Desea continuar?")
            if pregunta == False:
                break

        promedio_femenino = edad_femenino / contador_edad_femenino


        porcentaje_esteban = votantes_esteban * 100 / votantes_general
        porcentaje_gianni = votantes_gianni * 100 / votantes_general
        porcentaje_giovanni = votantes_giovanni * 100 / votantes_general

        #El nombre del participante que debe dejar la casa (El que tiene más votos)
        if votantes_esteban > votantes_gianni and votantes_esteban > votantes_giovanni:
            mas_votado = "Esteban"
        elif votantes_gianni > votantes_giovanni:
            mas_votado = "Gianni"
        else: 
            mas_votado = "Giovanni"

        alert(message=f"El votante más joven que votó a Gianni fue {nombre_joven_gianni} con {joven_gianni} años de edad")
        alert(message=f"El votante más viejo es: {nombre_mas_viejo} y su edad es de {edad_mas_viejo}")
        alert(message=f"El promedio de edad es: {promedio_femenino}")
        alert(message=f"Pariticipantes\n\t Esteban: {porcentaje_esteban}% \nGianni: {porcentaje_gianni}% \nGiovanni: {porcentaje_giovanni}%")
        alert(message=f"El participante más votado y que deja la casa fue {mas_votado}")



            

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()