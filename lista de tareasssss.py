import tkinter

ventana = tkinter.Tk()

tareas = ["Levantarse 6 AM","Estudiar","Desayunar"]

for tarea in tareas:
    tkinter.Checkbutton(ventana,text=tarea,font=("Arial",18)).pack(padx=20,pady=10)

ventana.mainloop()
