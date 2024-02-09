import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta 
apellido: Perez Medrano
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y 
        si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % 
        y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, 
        si es  “FelipeLamparas” se hace un descuento del 10 % 
        y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = int(self.combobox_cantidad.get())

        precio_lamparas = 800
        descuento = 0

        if cantidad >= 6:
            descuento = 0.50
        elif cantidad == 5 and marca == "ArgentinaLuz":
            descuento = 0.40
        elif cantidad == 5:
            descuento = 0.30
        elif cantidad == 4 and (marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
            descuento = 0.25
        elif cantidad == 4:
            descuento = 0.20
        elif cantidad == 3 and marca == "ArgentinaLuz":
            descuento = 0.15
        elif cantidad == 3 and marca == "FelipeLamparas":
            descuento = 0.10
        elif cantidad == 3:
            descuento = 0.05

        total = cantidad * precio_lamparas 
        total_con_descuento = total - (total * descuento)

        if total_con_descuento > 4000:
            total_con_descuento -= total * 0.05

        mensaje = alert(message=f"El total es de {total}\n El total con descuento es de {total_con_descuento}")
        if total_con_descuento > 4000:
            alert(message="Tiene descuento adicional del 5%")
        pass
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()