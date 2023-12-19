import tkinter

ventana = tkinter.Tk()

nombre_var = tkinter.StringVar()

def cambio_nombre():
    hola_nombre.configure(text="Hola " + nombre_var.get())

hola_nombre = tkinter.Label(ventana,text="Hola Nombre",font=("Arial",18),padx=20,pady=10)
hola_nombre.pack()

nombre = tkinter.Entry(ventana,font=("Arial",16),textvariable=nombre_var)
nombre.pack(padx=20,pady=10)

boton_cambio = tkinter.Button(ventana,text=("Cambio"),font=("Arial",16),command=cambio_nombre)
boton_cambio.pack(padx=20,pady=10)

ventana.mainloop()
