# Importaciones
import random #Numeros randoms incorporados en python
import math #Para constantes como pi
import pyclip #Integracion del clipboard para copiar valores de las series
import tkinter # Parte del gui
import customtkinter #Parte del gui
import matplotlib.pyplot as plt


def graficar(frec,lista_intervalos):
    plt.close()
    plt.ioff()
    plt.title("Histograma de Frecuencias")
    rango = lista_intervalos[3][2] - lista_intervalos[3][1]
    plt.bar(lista_intervalos[3],frec,width=rango,color="lightgrey", ec="orange")
    plt.xticks(lista_intervalos[2])    
    plt.xlabel("Intervalos")
    plt.ylabel("Frecuencias")
    plt.show()
    #plt.savefig('plot.png') Guardar imagen x si acaso

def agregar_numeros(frame, lista, indice):
    #Tenemos un indice, un tiempo de espera y conjunto de datos a cargar
    #Debido a la alta carga para el procesador de colocar tantos elementos a la vez para n > 10.000, se utiliza cargas x lote de a 10
    for i in range(10):
        if indice < len(lista):
            #Se crea labels hasta cumplir el primer conjunto
            elemento = lista[indice]
            customtkinter.CTkLabel(frame, text=elemento).pack()
            indice += 1
        #Utilizamos "after", una funcion de tkinter que llama a una funcion con sus variables despues de un tiempo en milisegundos "100" 
    if indice < len(lista):
        #Si aun el indice es menor a la cantidad de datos, sigue activando la funcion hasta que termine, gracias a after TKINTER despues de un tiempo
        frame.after(100, agregar_numeros, frame, lista, indice)

def segmentacion(lista):
    #Devuelvo una lista conformada con otras listas asi -> [Num Intervalo,Valor Inf,Valor Sup,Marca Clase]
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
    # print("Lista de Intervalos:")
    # print(lista_intervalos)
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
    frec_acum = [0] * q_interv #Lista de frec Acumulada
    acum = 0 #acumulador
    #Reviso numero x numero
    for i in range(0,n):
        #Reviso Intervalo x intervalo
        for o in range(0,q_interv):
            #Si el valor es mayor al intervalo superior revisando, paso al otro intervalo, sino sumo uno en frecuencia
            if lista[i] < lista_intervalos[2][o]:
                frec[o] += 1
                break
    for i in range(0,len(frec)):
        acum += frec[i]
        frec_acum[i]= acum
    #Coloco en el frame de frecuencias, los valores obtenidos
    for i in range(0,q_interv):
        texto_intervalo = "[ " + str(lista_intervalos[1][i]) + "," + str(lista_intervalos[2][i]) + " )"
        customtkinter.CTkButton(frame_frecuencia, text=texto_intervalo,fg_color="#6f632d").grid(row=i,column=0,pady=5,padx=1)
        customtkinter.CTkButton(frame_frecuencia, text=frec[i],fg_color="#a68cd9").grid(row=i,column=1,pady=5,padx=1)
        customtkinter.CTkButton(frame_frecuencia, text=lista_intervalos[3][i],fg_color="#a68cd9").grid(row=i,column=2,pady=5,padx=1)
        customtkinter.CTkButton(frame_frecuencia, text=frec_acum[i],fg_color="#5f4758").grid(row=i,column=3,pady=5,padx=1)
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
    lista = []
    for i in range(0,n):
        rnd = random.uniform(0,1)
        x = rnd*(b - a) + a
        x = round(x,2)
        lista.append(x)
    agregar_numeros(frame_lista, lista,0)
    print("Lista generada: ")
    print(lista)
    #Copia al clipboard la lista generada 
    lista_a_copiar = "\n".join(map(str,lista))
    pyclip.copy(lista_a_copiar)
    frec , lista_intervalos = obtener_frecuencias(lista)
    #Como necesito una lista con valores de todos los intervalos, solo agrego el faltante de los inferiores o superiores al contrario y lo uso
    lista_intervalos[2].insert(0,lista_intervalos[1][0])
    graficar(frec,lista_intervalos)

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
        lista.append(x)
    agregar_numeros(frame_lista, lista,0)
    print("Lista generada:")
    print(lista)
    #Copia al clipboard la lista generada
    lista_a_copiar = "\n".join(map(str,lista))
    pyclip.copy(lista_a_copiar)
    frec , lista_intervalos = obtener_frecuencias(lista)
    #Como necesito una lista con valores de todos los intervalos, solo agrego el faltante de los inferiores o superiores al contrario y lo uso
    lista_intervalos[2].insert(0,lista_intervalos[1][0])
    graficar(frec,lista_intervalos)

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
        #Con extend agregamos mas de 1 elemento por vez
        lista.extend([z1, z2])    
    #Si N es impar, eliminamos el ultimo valor par obtenido
    if n % 2 != 0:
        #Se tuvo que acomodar ya que ahora al ser por lotes, el ultimo frame no esta creado hasta un buen tiempo
        #frame_lista.winfo_children()[-1].destroy() 
        lista.pop(-1) #Elimina el valor del indice -1
    agregar_numeros(frame_lista, lista,0)
    print("Lista generada: ")
    print(lista)
    #Copia al clipboard la lista generada
    lista_a_copiar = "\n".join(map(str,lista))
    pyclip.copy(lista_a_copiar)
    frec , lista_intervalos = obtener_frecuencias(lista)
    #Como necesito una lista con valores de todos los intervalos, solo agrego el faltante de los inferiores o superiores al contrario y lo uso
    lista_intervalos[2].insert(0,lista_intervalos[1][0])
    graficar(frec,lista_intervalos)

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

def rellenar_random():
    #Relleno los valores de los textos de forma rapida y aleatoria
    borrar()
    texto_semilla.insert(0,random.randint(0,10))
    texto_muestra.insert(0,random.randint(0,500))
    texto_a.insert(0,random.randint(0,100))
    texto_b.insert(0,random.randint(0,100))
    texto_media.insert(0,random.randint(1,100))
    texto_desv.insert(0,random.randint(1,100))
    texto_intervalos.insert(0,random.randint(1,20))


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
boton_borrar = customtkinter.CTkButton(master=app, text="Borrar",command=borrar,height=25,width=597,fg_color="gray",text_color="black")
boton_borrar.place(relx=0.651,rely=0.165,anchor=tkinter.CENTER)

boton_uniforme = customtkinter.CTkButton(master=app, text="Uniforme",command=generar_uniforme,height=40)
boton_uniforme.place(relx=0.509,rely=0.05,anchor=tkinter.NE)

boton_normal = customtkinter.CTkButton(master=app, text="Normal",command=generar_normal,height=40)
boton_normal.place(relx=0.655,rely=0.05,anchor=tkinter.NE)

boton_exponencial = customtkinter.CTkButton(master=app, text="Exponencial",command=generar_exponencial,height=40)
boton_exponencial.place(relx=0.805,rely=0.05,anchor=tkinter.NE)

boton_random = customtkinter.CTkButton(master=app, text="Random",command=rellenar_random,height=40,width=100,fg_color='gray')
boton_random.place(relx=0.920,rely=0.05,anchor=tkinter.NE)

#Textos
texto_semilla = customtkinter.CTkEntry(app,width=100,height=40,placeholder_text="Semilla...",text_color="green")
texto_semilla.place(relx=0.133,rely=0.05,anchor=tkinter.NE)

texto_muestra = customtkinter.CTkEntry(master=app, placeholder_text="N (Muestra)",text_color="green",height=40,width=160)
texto_muestra.place(relx=0.285,rely=0.05,anchor=tkinter.NE)

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
customtkinter.CTkLabel(frame_grafico, text="Frec Acum.").place(relx=0.915,rely=0.12,anchor=tkinter.NE)

#Labels de aclaracaion
customtkinter.CTkLabel(app, text="Uniforme: Intervalo a-b").place(relx=0.509,rely=0.93,anchor=tkinter.NE)
customtkinter.CTkLabel(app, text="Normal: Media y Desv Std.").place(relx=0.680,rely=0.93,anchor=tkinter.NE)
customtkinter.CTkLabel(app, text="Exponencial: Media").place(relx=0.805,rely=0.93,anchor=tkinter.NE)

app.mainloop() # Ejecuto loop visual
