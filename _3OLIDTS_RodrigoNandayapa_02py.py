import tkinter as ttk #importamos la libreria tkinter que nos servira para crear objetos y ventana
                       #tomando en cuenta que python no tiene una seccion visual como C#    
                       #asi que se tendra que hacer a código todo los componentes

ventana = ttk.Tk() #Generamos nuestra ventana
ventana.title("Practica 02 Python") #Le ponemos nombre a esa venta como:
ventana.geometry("520x480")
Etiqueta1= ttk.Label(ventana,text="Ingrese su nombre:") #creamos una etiqueta (Label)
Etiqueta1.place(x=120, y=100) #configuramos el tamaño
entrada = ttk.Entry() #creamos una caja de texto (textbox)
entrada.place(x=120, y=160, width=200)
btnAceptar= ttk.Button(text="Aceptar") #Creamos un boton
btnAceptar.place(x= 120, y=183) #le asignamos la posicion
btnCancelar= ttk.Button(text="Cancelar") #Creamos un segundo boton
btnCancelar.place(x= 250, y=183) #le asignamos la posicion
ventana.mainloop()
