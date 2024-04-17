#Importaciones
import random #Numeros randoms incorporados en python
import math #Para constantes como pi
import pyclip #Integracion del clipboard para copiar valores de las series
import tkinter # Parte del gui
import customtkinter #Parte del gui
import matplotlib.pyplot as plt

        # plt.title("Distribucion Normal")
        # plt.hist(lista)
        # plt.xlabel("Valores")
        # plt.ylabel("Frecuencias")
        # plt.show()

def graficar(lista_intervalos,frec):
    fig, ax = plt.subplots()
    plt.title("Histograma de Frecuencias")
    plt.hist(x=lista_intervalos[3],weights=frec)
    plt.xlabel("Marca Clase")
    plt.ylabel("Frecuencias")
    plt.show()

def segmentacion(lista):
    #Devuelvo una lista conformada asi [Num Intervalo,Valor Inf,Valor Sup,Marca Clase]
    n = int(texto_muestra.get())
    intervalos = int(texto_intervalos.get())
    n_max = max(lista)
    n_min = min(lista)
    print("Numero max:",n_max)
    print("Numero min:",n_min)
    rango = round((n_max - n_min)/intervalos,2) + 0.01
    print("Rango:",rango)
    lista_intervalos = [[],[],[],[]]
    for i in range(0, intervalos):
        val_sup = round(n_min + rango,2)
        lista_intervalos[0].append(i + 1)
        lista_intervalos[1].append(round(n_min,2))
        lista_intervalos[2].append(val_sup)
        lista_intervalos[3].append(round((val_sup+n_min)/2,2))
        n_min += round(rango,2)
    print("Lista de Intervalos:")
    print(lista_intervalos)
    return lista_intervalos

def obtener_frecuencias(lista):
    for widget in frame_frecuencia.winfo_children():
        widget.destroy()
    lista_intervalos = segmentacion(lista)
    q_interv = int(texto_intervalos.get()) 
    print("Cantidad de intervalos:",q_interv)
    n = int(texto_muestra.get())
    #Creo una lista vacia de valores de frecuencia, 1 x cada intervalo
    frec = [0] * q_interv
    for i in range(0,n):
        for o in range(0,q_interv):
            if lista[i] < lista_intervalos[2][o]:
                frec[o] += 1
                break
    #Coloco en el frame de frecuencias, los valores obtenidos
    for i in range(0,q_interv):
        texto_intervalo = "[ " + str(lista_intervalos[1][i]) + "," + str(lista_intervalos[2][i]) + " )"
        customtkinter.CTkButton(frame_frecuencia, text=texto_intervalo,fg_color="#6f632d").grid(row=i,column=0,pady=5,padx=1)
        customtkinter.CTkButton(frame_frecuencia, text=frec[i],fg_color="#a68cd9").grid(row=i,column=1,pady=5,padx=1)
        customtkinter.CTkButton(frame_frecuencia, text=lista_intervalos[3][i],fg_color="#a68cd9").grid(row=i,column=2,pady=5,padx=1)
    return frec,lista_intervalos
      
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
    print("Valores generados: ")
    lista = []
    for i in range(0,n):
        rnd = random.uniform(0,1)
        x = rnd*(b - a) + a
        x = round(x,2)
        print(x)
        customtkinter.CTkLabel(frame_lista,text=x).pack(pady=2)
        lista.append(x)
    print("Lista generada: ")
    print(lista)
    #Copia al clipboard la lista generada 
    pyclip.copy(str(lista))
    frec, lista_intervalos = obtener_frecuencias(lista)
    graficar(lista_intervalos,frec)

def generar_exponencial():
    #Destruye la lista generada anteriormente
    for widget in frame_lista.winfo_children():
       widget.destroy()
    #Obtengo los valores de cada celda de texto
    random.seed(int(texto_semilla.get()))
    n = int(texto_muestra.get())
    media = int(texto_media.get())
    lamb = 1/media
    #Genero los numeros
    lista = []
    for i in range(0, n):
        rnd = random.uniform(0, 1)
        x = (math.log(1 - rnd)) / (-lamb)
        x = round(x,2)
        print(x)
        customtkinter.CTkLabel(frame_lista,text=x).pack(pady=10)
        lista.append(x)
    print(lista)
    #Copia al clipboard la lista generada
    pyclip.copy(str(lista))
    frec, lista_intervalos = obtener_frecuencias(lista)
    graficar(lista_intervalos,frec)

def generar_normal(): #Metodo Box-Muller
    #Destruye la lista generada anteriormente
    for widget in frame_lista.winfo_children():
       widget.destroy()
    #Obtengo los valores de cada celda de texto
    random.seed(int(texto_semilla.get()))
    n = int(texto_muestra.get())
    media = int(texto_media.get())
    desv = float(texto_desv.get())
    #Genero los numeros
    lista = []
    #Realizo por pares en forma decreciente hasta obtener los n numeros (cada iteracion hace dos, por lo que cuando termina el loop, resto 2 en n)
    for i in range(n,0,-2):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        z1 = (math.sqrt(-2 * math.log(r1)) * math.sin(2 * math.pi * r2)) * desv + media
        z2 = math.sqrt(-2 * math.log(r1)) * math.cos(2 * math.pi * r2) * desv + media
        
        z1 = round(z1,2)
        z2 = round(z2,2)
        
        print("Valor de z",i,":",z1)
        print("Valor de z",i+1,":",z2)
        customtkinter.CTkLabel(frame_lista,text=z1).pack(pady=10)
        customtkinter.CTkLabel(frame_lista,text=z2).pack(pady=10)
        #Con extend agregamos mas de 1 elemento por vez
        lista.extend([z1, z2])
    #Si N es impar, eliminamos el ultimo valor par obtenido
    if n % 2 != 0:
        frame_lista.winfo_children()[-1].destroy()
        lista.pop(-1) #Elimina el valor del indice -1
    print("Lista generada: ")
    print(lista)
    #Copia al clipboard la lista generada
    pyclip.copy(str(lista))
    frec, lista_intervalos = obtener_frecuencias(lista)
    graficar(lista_intervalos,frec)

def borrar():
    texto_semilla.delete(0,"end")
    texto_muestra.delete(0,"end")
    texto_a.delete(0,"end")
    texto_b.delete(0,"end")
    texto_media.delete(0,"end")
    texto_intervalos.delete(0,"end")
    texto_desv.delete(0,"end")
    for widget in frame_lista.winfo_children():
       widget.destroy()
    for widget in frame_frecuencia.winfo_children():
       widget.destroy()

#Gui 
customtkinter.set_appearance_mode("DARK")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk() #Creo ventana
app.title("Grupo 11 - Trabajo Práctico 1 'Generador de números'")
app.geometry("1100x500")  #Establezco dimensiones
app.resizable(0,0)  #Deshabilita maximizar ventana

#Tomo las relaciones de los pixeles en x e y de la pantalla para posicionar
#Uso de "anclaje" el sector noroeste de la pantalla para fijar los botones

frame_lista = customtkinter.CTkScrollableFrame(master=app,width=250,height=328,corner_radius=10)
frame_lista.place(relx=0.293, rely=0.2, anchor=tkinter.NE)

frame_grafico = customtkinter.CTkFrame(master=app,width=600,height=350,corner_radius=10)
frame_grafico.place(relx=0.925, rely=0.2, anchor=tkinter.NE)

frame_frecuencia = customtkinter.CTkScrollableFrame(master=frame_grafico,width=550,height=250,corner_radius=10)
frame_frecuencia.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

#Botones
boton_borrar = customtkinter.CTkButton(master=app, text="Borrar",command=borrar,height=25,width=590,fg_color="gray",text_color="black")
boton_borrar.place(relx=0.653,rely=0.165,anchor=tkinter.CENTER)

boton_uniforme = customtkinter.CTkButton(master=app, text="Uniforme",command=generar_uniforme,height=40)
boton_uniforme.place(relx=0.525,rely=0.05,anchor=tkinter.NE)

boton_normal = customtkinter.CTkButton(master=app, text="Normal",command=generar_normal,height=40)
boton_normal.place(relx=0.715,rely=0.05,anchor=tkinter.NE)

boton_exponencial = customtkinter.CTkButton(master=app, text="Exponencial",command=generar_exponencial,height=40)
boton_exponencial.place(relx=0.905,rely=0.05,anchor=tkinter.NE)

#Textos
texto_semilla = customtkinter.CTkEntry(app,width=100,height=40,placeholder_text="Semilla...",text_color="green")
texto_semilla.place(relx=0.133,rely=0.05,anchor=tkinter.NE)

texto_muestra = customtkinter.CTkEntry(master=app, placeholder_text="N (Muestra)",text_color="green",height=40,width=100)
texto_muestra.place(relx=0.28,rely=0.05,anchor=tkinter.NE)

texto_a = customtkinter.CTkEntry(frame_grafico,placeholder_text="Valor Inicial (a)",text_color="green")
texto_a.place(relx=0.24,rely=0.015,anchor=tkinter.NE)

texto_b = customtkinter.CTkEntry(frame_grafico,placeholder_text="Valor Final (b)",text_color="green")
texto_b.place(relx=0.500,rely=0.015,anchor=tkinter.NE)

texto_media = customtkinter.CTkEntry(frame_grafico,placeholder_text="Media",text_color="green")
texto_media.place(relx=0.75,rely=0.015,anchor=tkinter.NE)

texto_desv = customtkinter.CTkEntry(frame_grafico,placeholder_text="Desviacion estandar",text_color="green")
texto_desv.place(relx=0.995,rely=0.015,anchor=tkinter.NE)

texto_intervalos = customtkinter.CTkEntry(app,width=270,placeholder_text="Cantidad Intervalos (Enteros)",text_color="green")
texto_intervalos.place(relx=0.2871,rely=0.14,anchor=tkinter.NE)

#Labels de texto
customtkinter.CTkLabel(frame_grafico, text="Intervalo").place(relx=0.18,rely=0.12,anchor=tkinter.NE)
customtkinter.CTkLabel(frame_grafico, text="Frecuencia Obs.").place(relx=0.45,rely=0.12,anchor=tkinter.NE)
customtkinter.CTkLabel(frame_grafico, text="Marca Clase.").place(relx=0.67,rely=0.12,anchor=tkinter.NE)

app.mainloop() # Ejecuto loop visual
