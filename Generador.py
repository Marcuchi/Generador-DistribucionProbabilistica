#Importaciones
import random #Numeros randoms incorporados en python
import math #Para constantes como pi
import pyclip  #Integracion del clipboard para copiar valores de las series
import tkinter # Parte del gui
import customtkinter #Parte del gui
import matplotlib.figure as Figure #Graficador de histogramas
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) #Integracion de matplot con tkinter

class Distro:

    def __init__(self,semilla):
        self.semilla = semilla
        random.seed(semilla)
        

    def uniforme(self,n,a,b):
        print("Distribucion Uniforme")
        for i in range(0,n):
            rnd = random.uniform(0,1)
            x = rnd*(b - a) + a
            print(round(x,2))

    def exponencial(self,n,media):
        print("Distribucion Exponencial")
        lamb = 1/media
        for i in range(0,n):
            rnd = random.uniform(0,1)
            x = (math.log(1-rnd))/(-lamb)
            print(round(x,2))

    def normal(self,n):
        print("Distribucion Normal")
        lista = list()
        for i in range(0,n):
            r1 = random.uniform(0,1)
            r2 = random.uniform(0,1)
            z1 = math.sqrt(-2*math.log(r1))*math.sin(2*math.pi*r2)
            z2 = math.sqrt(-2*math.log(r1))*math.cos(2*math.pi*r2)
            print(round(z1,2))
            print(round(z2,2))
            lista.extend([z1,z2])

        plt.title("Distribucion Normal")
        plt.hist(lista)
        plt.xlabel("Valores")
        plt.ylabel("Frecuencias")
        plt.show()

def graficar(lista):
    fig = Figure(figsize=(2.5,2.2))
    canvas = FigureCanvasTkAgg(figure=fig,master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.5,rely=0.5)

def generar_uniforme():
    #Destruye la lista generada anteriormente
    for widget in frame_lista.winfo_children():
       widget.destroy()
    #Obtengo los valores de cada celda de texto
    random.seed(int(texto_semilla.get()))
    n = int(texto_muestra.get())
    a = int(texto_a.get())
    b = int(texto_b.get())
    #Genero los numeros
    lista = []
    for i in range(0,n):
        rnd = random.uniform(0,1)
        x = rnd*(b - a) + a
        x = round(x,4)
        print(x)
        customtkinter.CTkButton(frame_lista,text=x).pack(pady=10)
        lista.append(x)
    print(lista)
    #Copia al clipboard la lista generada 
    pyclip.copy(str(lista))

def borrar():
    texto_semilla.delete(0,"end")
    texto_muestra.delete(0,"end")
    texto_a.delete(0,"end")
    texto_b.delete(0,"end")
    texto_media.delete(0,"end")


# generador = Distro(0)
# n = int(input("Cantidad de valores a generar: "))

# a = int(input("Desde: "))
# b = int(input("Hasta: "))
# generador.uniforme(n,a,b)

# media = int(input("Media: "))
# generador.exponencial(n,media)

# generador.normal(n)

#Gui 
customtkinter.set_appearance_mode("DARK")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk() #Creo ventana
app.title("Grupo 11 - Trabajo Práctico 1 'Generador de números'")
app.geometry("800x500") #Establezco dimensiones
app.resizable(0,0) #Deshabilita maximizar ventana


    
#Tomo las relaciones de los pixeles en x e y de la pantalla para posicionar
#Uso de "anclaje" el sector noroeste de la pantalla para fijar los botones


texto_semilla = customtkinter.CTkEntry(app,width=100,height=40,placeholder_text="Semilla...",text_color="green")
texto_semilla.place(relx=0.14,rely=0.1,anchor=tkinter.NE)

boton_borrar = customtkinter.CTkButton(master=app, text="Borrar",command=borrar,height=25,width=445,fg_color="gray",text_color="black")
boton_borrar.place(relx=0.625,rely=0.165,anchor=tkinter.CENTER)

boton_uniforme = customtkinter.CTkButton(master=app, text="Uniforme",command=generar_uniforme,height=40)
boton_uniforme.place(relx=0.525,rely=0.05,anchor=tkinter.NE)

boton_normal = customtkinter.CTkButton(master=app, text="Normal",command=generar_uniforme,height=40)
boton_normal.place(relx=0.715,rely=0.05,anchor=tkinter.NE)

boton_exponencial = customtkinter.CTkButton(master=app, text="Exponencial",command=generar_uniforme,height=40)
boton_exponencial.place(relx=0.905,rely=0.05,anchor=tkinter.NE)

texto_muestra = customtkinter.CTkEntry(master=app, placeholder_text="N (Muestra)",text_color="green",height=40,width=100)
texto_muestra.place(relx=0.28,rely=0.1,anchor=tkinter.NE)

frame_lista = customtkinter.CTkScrollableFrame(master=app,width=200,height=328,corner_radius=10)
frame_lista.place(relx=0.29, rely=0.2, anchor=tkinter.NE)

frame_grafico = customtkinter.CTkFrame(master=app,width=450,height=350,corner_radius=10)
frame_grafico.place(relx=0.91, rely=0.2, anchor=tkinter.NE)

texto_a = customtkinter.CTkEntry(frame_grafico,placeholder_text="Valor Inicial (a)",text_color="green")
texto_a.place(relx=0.31,rely=0.001,anchor=tkinter.NE)

texto_b = customtkinter.CTkEntry(frame_grafico,placeholder_text="Valor Final (b)",text_color="green")
texto_b.place(relx=0.640,rely=0.001,anchor=tkinter.NE)

texto_media = customtkinter.CTkEntry(frame_grafico,placeholder_text="Media",text_color="green")
texto_media.place(relx=0.98,rely=0.001,anchor=tkinter.NE)



app.mainloop() # Ejecuto loop visual
