import tkinter as tk
from Client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Catalogo')
    ##root.icontbitmap('')#agregamos icono
    root.resizable(1,1)#Podemos estirar de los lados, asignando "1"
    barra_menu(root)
   
    app = Frame(root = root)
   # frame = tk.Frame(root)#frame, es el conteneror de los elementos
    #frame.pack()
    #frame.config(width = 480, height = 320, bg ='green')#Tamaño de inicio de ventana#
    app.mainloop()

if __name__ == '__main__':
    main()