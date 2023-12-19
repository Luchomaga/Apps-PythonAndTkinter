import tkinter
"""
texto = "Hola mundo"
texto_binario = ""


for letra in texto:
    texto_binario += bin(ord(letra))[2:]

print(texto_binario)"""


ventana = tkinter.Tk()

def a_binario():
    text = texto.get("1.0",tkinter.END)
    texto_binario = ""
    for letra in text:
        texto_binario += bin(ord(letra))[2:]

    texto.delete("1.0",tkinter.END)
    texto.insert("1.0",texto_binario)

label_texto = tkinter.Label(ventana, text="Texto",font=("Arial",18)).pack(padx=20,pady=10)
texto = tkinter.Text(ventana,width=40,height=15)
texto.pack(padx=20,pady=10)
boton_cambio = tkinter.Button(ventana,text="A Binario",font=("Arial",18),command=a_binario).pack(padx=20,pady=10)
ventana.mainloop()
