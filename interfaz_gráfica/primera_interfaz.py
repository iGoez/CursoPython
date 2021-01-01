from tkinter import *

# Por convensión se llama raíz
# el mainloop es para ejecutar las interfaces gráficas, es un loop infinito que pemite mostrar las ventanas.
raiz= Tk()
raiz.title("Ventana de pruebas")

# Pemite que la ventana no se puede ajustar
# Los parametros son valores lógicos, sirven tanto el 1,0 como el True,False
#raiz.resizable(0,0)
# Permite cambiar el icono de tkinter por defecto de nuestro programa
#raiz.iconbitmap("nombreImagen.co")

# Permite camibar el tamaño de la ventana
# La raíz se ajustará automaticamente al tamaño del frame que contiene.
# raiz.geometry("650x350")

# El config permite cambiar muchas cosas, entre ellas, el color de fondo
raiz.config(bg="gray", bd=10, relief="sunken", cursor="pirate")

# Creamos el Frame y debemos empaquetarlo en nuestra raíz
miFrame = Frame()

# Si le colocamos el argumento side="" se anclará donde le digamos
# anchor permite ubicar el frame donde queramos porque maneja puntos cardinales
#miFrame.pack(side="left", anchor="s")

# fill permite rellenar la coordenada especifica
#miFrame.pack(fill="x")
# En el caso de Y se debe hacer lo siguiente
miFrame.pack(fill="y",expand=True)

# Para expandir ambos se necesita el both y el expand
#miFrame.pack(fill="both",expand=True)

# Ahora vamos a modificar el frame
# Primero se debe darle un tamaño y la raíz debe ajustar a ese tamaño automaticamente.
# El relief sirve para cambiar las características del borde
# También, debemos colocar bd para cambiar el ancho de los bordes porque por defecto es 0
# También podemos cambiar el cursor cuando éste pasa por el Frame con cursor
miFrame.config(bg="Red",width=650,height=350, bd=10, relief="sunken", cursor="hand2")

raiz.mainloop()
