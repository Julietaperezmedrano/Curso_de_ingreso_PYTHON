import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Les paso 2 consignas para que practiquen para el examen del viernes. Cualquier cosa consulten. 

Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

-Nombre
-Edad (debe ser mayor a 12)
-Altura (no debe ser negativa)
-Días que asiste a la semana (1, 3, 5)
-Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

No sabemos cuántos clientes serán consultados.
Se debe informar al usuario:
A) El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.--
B) El porcentaje de clientes que asiste solo 1 día a la semana. --
C) Nombre y edad del cliente con más altura. --
D) Determinar si los clientes eligen más ir 1, 3 o 5 días --
E) Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        acumulador_kilos_tres_dias = 0
        contador_kilos_tres_dias = 0

        total_clientes = 0

        clientes_un_dia = 0
        clientes_tres_dias = 0
        clientes_cinco_dias = 0

        flag_altura = True
        cliente_mas_altura = 0
        nombre_mas_altura = ""
        edad_mas_altura = 0

        mas_joven_cinco = 100
        nombre_joven_cinco = ""
        kilos_joven_cinco = 0

        while True:
            nombre = prompt("Ingreso", "ingrese su nombre")

            edad = prompt("Ingreso", "ingrese su edad")
            edad = int(edad)
            while edad < 12:
                edad = prompt("Error", "Reingrese su edad")
                edad = int(edad)

            altura = prompt("ingreso", "Ingrese su altura")
            altura = float(altura)
            while altura < 1:
                altura = prompt("Error", "Reingrese la altura")
                altura = float(altura)

            dias = prompt("Ingreso", "ingrese los dias que asiste(1, 3 o 5)")
            while dias != "1" and dias != "3" and dias != "5":
                dias = prompt("Error", "Reingrese la cantidad de dias(1/3/5)")
            
            kilos_peso_muerto = prompt("Ingreso", "ingrese la cantidad de kilos que carga en peso muerto")
            kilos_peso_muerto = int(kilos_peso_muerto)
            while kilos_peso_muerto == 0 or kilos_peso_muerto < 1:
                kilos_peso_muerto = prompt("Error", "Reingrese la cantidad de kilos")
                kilos_peso_muerto = int(kilos_peso_muerto)

            match dias:
                case "1":
                    clientes_un_dia += 1
                case "3":
                    acumulador_kilos_tres_dias += kilos_peso_muerto
                    contador_kilos_tres_dias += 1
                    clientes_tres_dias += 1
                case "5":
                    clientes_cinco_dias += 1
                    if edad < mas_joven_cinco:
                        mas_joven_cinco = edad
                        nombre_joven_cinco = nombre
                        kilos_joven_cinco = kilos_peso_muerto


            if altura > cliente_mas_altura or flag_altura == True:
                cliente_mas_altura = altura
                nombre_mas_altura = nombre
                edad_mas_altura = edad
                flag_altura = False

            if clientes_un_dia > clientes_tres_dias and clientes_un_dia > clientes_cinco_dias:
                mas_elegido = "Clientes - 1 dia"
            elif clientes_tres_dias > clientes_cinco_dias:
                mas_elegido = "Clientes - 3 dias"
            else:
                mas_elegido = "Clientes - 5 dias"


            total_clientes += 1

            pregunta = question(message="Desea continuar?")
            if pregunta == False:
                break
   

        promedio_kilos_tres_dias = acumulador_kilos_tres_dias / contador_kilos_tres_dias

        porcentaje_un_dia = clientes_un_dia * 100 / total_clientes

        alert(message=f"El promedio de los kilos de las personas que van tres veces por semana es: {promedio_kilos_tres_dias}")
        alert(message=f"El procentaje de clientes que asiste una vez a la semana es de: {porcentaje_un_dia}%")
        alert(message=f"El cliente con más altura es {nombre_mas_altura} con la edad de {edad_mas_altura} y una altura de {cliente_mas_altura}")
        alert(message=f"Los clientes eligen más: {mas_elegido}")
        alert(message=f"La persona más joven que asiste 5 dias a la semana es {nombre_joven_cinco}, que levanta {kilos_joven_cinco} y su edad es de {mas_joven_cinco}")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()